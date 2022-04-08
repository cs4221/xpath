import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker, InputStream
from .compilerv1 import XPathLexer, XPathParser
# from mongoconverter import PyMongoElement
from .queryconstructor import MongoQuery


'''
Produces a parse tree with the root of the tree for the xpath query labelled
xpath
'''


class XPath:
    def __init__(self, pymongo=None) -> None:
        self.treeWalker = ParseTreeWalker()
        self.result = []
        self.listener = MongoQuery(self.result, pymongo)
        pass

    def fromQueryString(self, expr: str):
        input = InputStream(expr)
        lexer = XPathLexer(input)
        stream = CommonTokenStream(lexer)
        self.parser = XPathParser(stream)
        self.parseTree = self.parser.xpath()
        self.treeWalker.walk(self.listener, self.parseTree)
        return self

    def fromQueryFile(self, xpath_file: str):
        input = FileStream(xpath_file)
        lexer = XPathLexer(input)
        stream = CommonTokenStream(lexer)
        self.parser = XPathParser(stream)
        self.parseTree = self.parser.xpath()
        self.treeWalker.walk(self.listener, self.parseTree)
        return self

    def get(self):
        return self.result

    def toDebugString(self) -> str:
        return self.parseTree.toStringTree(recog=self.parser)
    pass


if __name__ == "__main__":
    input = FileStream(sys.argv[1])
    lexer = XPathLexer(input)
    stream = CommonTokenStream(lexer)
    parser = XPathParser(stream)
    parseTree = parser.xpath()
    walker = ParseTreeWalker()
    listerner = MongoQuery()
    print(parseTree.toStringTree(recog=parser))
    walker.walk(listerner, parseTree)
    pass
