from msilib.schema import File
import sys
from antlr4 import CommonTokenStream, FileStream
from compiler import XPathLexer, XPathParser


class XPath:
    def __init__(self, xpath_file: str) -> None:
        self.input = FileStream(xpath_file)
        self.lexer = XPathLexer(self.input)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = XPathParser(self.stream)
        self.parse_tree = self.parser.xpath()
        pass

    def toDebugString(self) -> str:
        return self.parse_tree.toStringTree(recog=self.parser)
    pass


if __name__ == "__main__":
    file_name = sys.argv[1]
    xpath = XPath(file_name)
    print(xpath.toDebugString())
    pass
