from .compilerv1 import XPathListener

class MongoQuery(XPathListener):
    '''
    This class extends the listener. It defines only significant methods that
    are of interest, i.e. entering and exiting a nodetest.

    It ignores nodes of no interests such as xpath, expr or other grouping rule
    for the parser which would not help us in our construction of the query.

    Example:

    doc('library')/books/book -> will set the mongoroot database_name='library'
    and collection_name='books'

    doc('library')/players/player[surname='Wehn']/position:
    The XPath listener will ignore the immediate node following the collection
    name. It will assume each document in players collection is a player and
    try to find a document (player) with the attribute surname: 'Wehn'.
    '''

    def __init__(self, result=[], pymongo=None) -> None:
        self.database = None
        self.collection_name = None
        self.mongoroot = pymongo
        self.result = result
        self.mongodb = None
        self.mongocollection = None
        self.locationflag = False
        self.pred = False
        self.document_name = None
        self.predicate_field = None
        self.predicate_val = None
        self.document_field = None
        pass

    def enterDocument(self, ctx):
        if self.database is None:
            self.database = ctx.StringLiteral().getText()
            print(f"Enter document rule and set Database to: {self.database}")
        if self.mongoroot:
            self.mongodb = self.mongoroot.find(f"./database[@database_name={self.database}]")
            pass
        pass

    def exitDocument(self, ctx):
        print(f"Exit document rule: Database {self.database}")
        pass

    def enterNodeselector(self, ctx):
        # Once document name is discovered, we can start querying the
        # sollection to find a document we want
        if not self.inpredicate() and self.document_name:
            print("Getting document field")
            self.document_field = ctx.NODE_NAME().getText()
            pass
        elif self.document_name and self.inpredicate():
            self.predicate_field = ctx.NODE_NAME().getText()
            print(f"Set predicate field to {self.predicate_field}")
            pass
        elif self.mongocollection is not None and self.document_name is None:
            self.document_name = ctx.NODE_NAME().getText()
            print(f"Set document name in {self.collection_name} to {self.document_name}")
        elif self.collection_name is None:
            self.collection_name = ctx.NODE_NAME().getText()
            print(f"Enter nodeselector rule and set Collection to: {self.collection_name}")
            if self.mongodb:
                self.mongocollection = self.mongodb.find(f"./collection[@collection_name='{self.collection_name}']")
            pass
        pass

    def exitNodeselector(self, ctx):
        print(f"Exit nodeselector: {ctx.NODE_NAME().getText()}")
        pass

    def enterPred(self, ctx):
        print("Enter predicate")
        self.pred = True
        pass

    def exitPred(self, ctx):
        print("Exit predicate")
        self.pred = False
        pass

    def enterPath(self, ctx):
        print("Enter path")
        pass

    def exitPath(self, ctx):
        print("Exit path")
        pass

    def enterLocationstepexpr(self, ctx):
        print("Enter location step")
        self.locationflag = True
        pass

    def exitLocationstepexpr(self, ctx):
        print("Exit location step")
        self.locationflag = False
        pass

    def enterLiteral(self, ctx):
        print(f"Enter literal: {ctx.IntegerLiteral()}; {ctx.StringLiteral()}")
        if ctx.IntegerLiteral():
            self.predicate_val = ctx.IntegerLiteral().getText()
            print(f"Set predicate value to {self.predicate_val}")
            pass
        elif ctx.StringLiteral():
            self.predicate_val = ctx.StringLiteral().getText()
            print(f"Set predicate value to {self.predicate_val}")
        pass

    def inpredicate(self):
        return self.pred

    def exitXpath(self, ctx):
        r = self.mongocollection.find(f"./document[{self.predicate_field}={self.predicate_val}]")
        if self.document_field:
            r = r.find(f"./{self.document_field}")
        self.result.append(r)
        print("Exit XPath")
        pass

    pass
