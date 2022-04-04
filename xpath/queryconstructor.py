from compilerv1 import XPathListener

class MongoQuery(XPathListener):
    '''
    This class extends the listener. It defines only significant methods that
    are of interest, i.e. entering and exiting a nodetest.

    It ignores nodes of no interests such as xpath, expr or other grouping rule
    for the parser which would not help us in our construction of the query.

    Important:
    Collection name must be explicitly specified in the XPath i.e.
    '''

    def __init__(self) -> None:
        self.collection = None
        pass

    def enterNodeselector(self, ctx):
        if self.collection is None:
            self.collection = ctx.NODE_NAME().getText()
        pass

    def exitNodeselector(self, ctx):
        pass

    pass
