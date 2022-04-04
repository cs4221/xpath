import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from compiler import XPathLexer, XPathParser, XPathListener


'''
Produces a parse tree with the root of the tree for the xpath query labelled
xpath
'''


class XPath:
    def __init__(self, xpath_file: str) -> None:
        self.input = FileStream(xpath_file)
        self.lexer = XPathLexer(self.input)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = XPathParser(self.stream)
        self.parseTree = self.parser.xpath()
        self.treeWalker = ParseTreeWalker()
        self.listener = XPathListener()
        pass

    def constructMongoQuery(self):
        self.treeWalker.walk(self.listener, self.parseTree)
        pass

    def toDebugString(self) -> str:
        return self.parseTree.toStringTree(recog=self.parser)
    pass


if __name__ == "__main__":
    file_name = sys.argv[1]
    xpath = XPath(file_name)
    print(xpath.toDebugString())
    pass
