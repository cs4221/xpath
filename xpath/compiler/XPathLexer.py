# Generated from .\xpath\xpathgrammer\XPath.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u0127\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("K\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\be")
        buf.write("\n\b\3\t\6\th\n\t\r\t\16\ti\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\32\6\32\u0122\n\32\r")
        buf.write("\32\16\32\u0123\3\32\3\32\2\2\33\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\3\2\5\5")
        buf.write("\2,-//~~\4\2C\\c|\5\2\13\f\16\17\"\"\2\u013d\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\3\65\3\2\2\2\5\67\3\2\2\2\7")
        buf.write("9\3\2\2\2\t;\3\2\2\2\13J\3\2\2\2\rL\3\2\2\2\17d\3\2\2")
        buf.write("\2\21g\3\2\2\2\23k\3\2\2\2\25t\3\2\2\2\27\u0085\3\2\2")
        buf.write("\2\31\u008f\3\2\2\2\33\u0095\3\2\2\2\35\u009d\3\2\2\2")
        buf.write("\37\u00a8\3\2\2\2!\u00bb\3\2\2\2#\u00c5\3\2\2\2%\u00d7")
        buf.write("\3\2\2\2\'\u00dc\3\2\2\2)\u00e3\3\2\2\2+\u00ed\3\2\2\2")
        buf.write("-\u00ff\3\2\2\2/\u0116\3\2\2\2\61\u011b\3\2\2\2\63\u0121")
        buf.write("\3\2\2\2\65\66\7\61\2\2\66\4\3\2\2\2\678\7]\2\28\6\3\2")
        buf.write("\2\29:\7_\2\2:\b\3\2\2\2;<\7<\2\2<=\7<\2\2=\n\3\2\2\2")
        buf.write(">K\5\23\n\2?K\5\25\13\2@K\5\27\f\2AK\5\31\r\2BK\5\35\17")
        buf.write("\2CK\5\37\20\2DK\5!\21\2EK\5#\22\2FK\5\'\24\2GK\5)\25")
        buf.write("\2HK\5+\26\2IK\5/\30\2J>\3\2\2\2J?\3\2\2\2J@\3\2\2\2J")
        buf.write("A\3\2\2\2JB\3\2\2\2JC\3\2\2\2JD\3\2\2\2JE\3\2\2\2JF\3")
        buf.write("\2\2\2JG\3\2\2\2JH\3\2\2\2JI\3\2\2\2K\f\3\2\2\2LM\7*\2")
        buf.write("\2MN\7+\2\2N\16\3\2\2\2Oe\t\2\2\2PQ\7f\2\2QR\7k\2\2Re")
        buf.write("\7x\2\2Se\7?\2\2TU\7#\2\2Ue\7?\2\2Ve\7>\2\2WX\7>\2\2X")
        buf.write("e\7?\2\2Ye\7@\2\2Z[\7@\2\2[e\7?\2\2\\]\7q\2\2]e\7t\2\2")
        buf.write("^_\7c\2\2_`\7p\2\2`e\7f\2\2ab\7o\2\2bc\7q\2\2ce\7f\2\2")
        buf.write("dO\3\2\2\2dP\3\2\2\2dS\3\2\2\2dT\3\2\2\2dV\3\2\2\2dW\3")
        buf.write("\2\2\2dY\3\2\2\2dZ\3\2\2\2d\\\3\2\2\2d^\3\2\2\2da\3\2")
        buf.write("\2\2e\20\3\2\2\2fh\t\3\2\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2")
        buf.write("\2ij\3\2\2\2j\22\3\2\2\2kl\7c\2\2lm\7p\2\2mn\7e\2\2no")
        buf.write("\7g\2\2op\7u\2\2pq\7v\2\2qr\7q\2\2rs\7t\2\2s\24\3\2\2")
        buf.write("\2tu\7c\2\2uv\7p\2\2vw\7e\2\2wx\7g\2\2xy\7u\2\2yz\7v\2")
        buf.write("\2z{\7q\2\2{|\7t\2\2|}\7/\2\2}~\7q\2\2~\177\7t\2\2\177")
        buf.write("\u0080\7/\2\2\u0080\u0081\7u\2\2\u0081\u0082\7g\2\2\u0082")
        buf.write("\u0083\7n\2\2\u0083\u0084\7h\2\2\u0084\26\3\2\2\2\u0085")
        buf.write("\u0086\7c\2\2\u0086\u0087\7v\2\2\u0087\u0088\7v\2\2\u0088")
        buf.write("\u0089\7t\2\2\u0089\u008a\7k\2\2\u008a\u008b\7d\2\2\u008b")
        buf.write("\u008c\7w\2\2\u008c\u008d\7v\2\2\u008d\u008e\7g\2\2\u008e")
        buf.write("\30\3\2\2\2\u008f\u0090\7e\2\2\u0090\u0091\7j\2\2\u0091")
        buf.write("\u0092\7k\2\2\u0092\u0093\7n\2\2\u0093\u0094\7f\2\2\u0094")
        buf.write("\32\3\2\2\2\u0095\u0096\7e\2\2\u0096\u0097\7q\2\2\u0097")
        buf.write("\u0098\7o\2\2\u0098\u0099\7o\2\2\u0099\u009a\7g\2\2\u009a")
        buf.write("\u009b\7p\2\2\u009b\u009c\7v\2\2\u009c\34\3\2\2\2\u009d")
        buf.write("\u009e\7f\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7u\2\2\u00a0")
        buf.write("\u00a1\7e\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7p\2\2\u00a3")
        buf.write("\u00a4\7f\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7p\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\36\3\2\2\2\u00a8\u00a9\7f\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7e\2\2\u00ac")
        buf.write("\u00ad\7g\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7f\2\2\u00af")
        buf.write("\u00b0\7c\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write("\u00b3\7/\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\u00b6\7/\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7g\2\2\u00b8")
        buf.write("\u00b9\7n\2\2\u00b9\u00ba\7h\2\2\u00ba \3\2\2\2\u00bb")
        buf.write("\u00bc\7h\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be\7n\2\2\u00be")
        buf.write("\u00bf\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7y\2\2\u00c1")
        buf.write("\u00c2\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7i\2\2\u00c4")
        buf.write("\"\3\2\2\2\u00c5\u00c6\7h\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7q\2\2\u00ca")
        buf.write("\u00cb\7y\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd")
        buf.write("\u00ce\7i\2\2\u00ce\u00cf\7/\2\2\u00cf\u00d0\7u\2\2\u00d0")
        buf.write("\u00d1\7k\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3\7n\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6\7i\2\2\u00d6")
        buf.write("$\3\2\2\2\u00d7\u00d8\7p\2\2\u00d8\u00d9\7q\2\2\u00d9")
        buf.write("\u00da\7f\2\2\u00da\u00db\7g\2\2\u00db&\3\2\2\2\u00dc")
        buf.write("\u00dd\7r\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7t\2\2\u00df")
        buf.write("\u00e0\7g\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7v\2\2\u00e2")
        buf.write("(\3\2\2\2\u00e3\u00e4\7r\2\2\u00e4\u00e5\7t\2\2\u00e5")
        buf.write("\u00e6\7g\2\2\u00e6\u00e7\7e\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7f\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb")
        buf.write("\u00ec\7i\2\2\u00ec*\3\2\2\2\u00ed\u00ee\7r\2\2\u00ee")
        buf.write("\u00ef\7t\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7e\2\2\u00f1")
        buf.write("\u00f2\7g\2\2\u00f2\u00f3\7f\2\2\u00f3\u00f4\7k\2\2\u00f4")
        buf.write("\u00f5\7p\2\2\u00f5\u00f6\7i\2\2\u00f6\u00f7\7/\2\2\u00f7")
        buf.write("\u00f8\7u\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7d\2\2\u00fa")
        buf.write("\u00fb\7n\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7p\2\2\u00fd")
        buf.write("\u00fe\7i\2\2\u00fe,\3\2\2\2\u00ff\u0100\7r\2\2\u0100")
        buf.write("\u0101\7t\2\2\u0101\u0102\7q\2\2\u0102\u0103\7e\2\2\u0103")
        buf.write("\u0104\7g\2\2\u0104\u0105\7u\2\2\u0105\u0106\7u\2\2\u0106")
        buf.write("\u0107\7k\2\2\u0107\u0108\7p\2\2\u0108\u0109\7i\2\2\u0109")
        buf.write("\u010a\7/\2\2\u010a\u010b\7k\2\2\u010b\u010c\7p\2\2\u010c")
        buf.write("\u010d\7u\2\2\u010d\u010e\7v\2\2\u010e\u010f\7t\2\2\u010f")
        buf.write("\u0110\7w\2\2\u0110\u0111\7e\2\2\u0111\u0112\7v\2\2\u0112")
        buf.write("\u0113\7k\2\2\u0113\u0114\7q\2\2\u0114\u0115\7p\2\2\u0115")
        buf.write(".\3\2\2\2\u0116\u0117\7u\2\2\u0117\u0118\7g\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7h\2\2\u011a\60\3\2\2\2\u011b")
        buf.write("\u011c\7v\2\2\u011c\u011d\7g\2\2\u011d\u011e\7z\2\2\u011e")
        buf.write("\u011f\7v\2\2\u011f\62\3\2\2\2\u0120\u0122\t\4\2\2\u0121")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0121\3\2\2\2")
        buf.write("\u0123\u0124\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\b")
        buf.write("\32\2\2\u0126\64\3\2\2\2\7\2Jdi\u0123\3\b\2\2")
        return buf.getvalue()


class XPathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    AXES = 5
    FUNCTION_CALL = 6
    OPERATOR = 7
    NODE_NAME = 8
    KW_ANCESTOR = 9
    KW_ANCESTOR_OR_SELF = 10
    KW_ATTRIBUTE = 11
    KW_CHILD = 12
    KW_COMMENT = 13
    KW_DESCENDANT = 14
    KW_DESCENDANT_OR_SELF = 15
    KW_FOLLOWING = 16
    KW_FOLLOWING_SIBLING = 17
    KW_NODE = 18
    KW_PARENT = 19
    KW_PRECEDING = 20
    KW_PRECEDING_SIBLING = 21
    KW_PROCESSING_INSTRUCTION = 22
    KW_SELF = 23
    KW_TEXT = 24
    WS = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'/'", "'['", "']'", "'::'", "'()'", "'ancestor'", "'ancestor-or-self'", 
            "'attribute'", "'child'", "'comment'", "'descendant'", "'descendant-or-self'", 
            "'following'", "'following-sibling'", "'node'", "'parent'", 
            "'preceding'", "'preceding-sibling'", "'processing-instruction'", 
            "'self'", "'text'" ]

    symbolicNames = [ "<INVALID>",
            "AXES", "FUNCTION_CALL", "OPERATOR", "NODE_NAME", "KW_ANCESTOR", 
            "KW_ANCESTOR_OR_SELF", "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", 
            "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
            "KW_NODE", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
            "KW_PROCESSING_INSTRUCTION", "KW_SELF", "KW_TEXT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "AXES", "FUNCTION_CALL", 
                  "OPERATOR", "NODE_NAME", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", 
                  "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", "KW_DESCENDANT", 
                  "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
                  "KW_NODE", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                  "KW_PROCESSING_INSTRUCTION", "KW_SELF", "KW_TEXT", "WS" ]

    grammarFileName = "XPath.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


