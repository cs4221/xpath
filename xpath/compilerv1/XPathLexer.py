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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01ed\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u0098\n\3\3\4\3\4\7\4\u009c\n\4\f\4\16")
        buf.write("\4\u009f\13\4\3\5\6\5\u00a2\n\5\r\5\16\5\u00a3\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u00ac\n\6\3\7\3\7\3\7\3\7\5\7\u00b2")
        buf.write("\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\38\38\38\38\38\39\39\39\39")
        buf.write("\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3=\3")
        buf.write("=\3=\3=\3=\3>\3>\3?\3?\3?\7?\u01cc\n?\f?\16?\u01cf\13")
        buf.write("?\3?\3?\3?\3?\7?\u01d5\n?\f?\16?\u01d8\13?\3?\5?\u01db")
        buf.write("\n?\3@\3@\3@\3A\3A\3B\6B\u01e3\nB\rB\16B\u01e4\3C\6C\u01e8")
        buf.write("\nC\rC\16C\u01e9\3C\3C\4\u01cd\u01d6\2D\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177\2\u0081")
        buf.write("\2\u0083\2\u0085A\3\2\b\5\2C\\aac|\7\2/\60\62;C\\aac|")
        buf.write("\4\2$$``\3\2))\3\2\62;\5\2\13\f\16\17\"\"\2\u0205\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\u0085\3\2\2\2\3\u0087\3\2\2\2\5")
        buf.write("\u0097\3\2\2\2\7\u0099\3\2\2\2\t\u00a1\3\2\2\2\13\u00ab")
        buf.write("\3\2\2\2\r\u00b1\3\2\2\2\17\u00b3\3\2\2\2\21\u00b5\3\2")
        buf.write("\2\2\23\u00b7\3\2\2\2\25\u00b9\3\2\2\2\27\u00bb\3\2\2")
        buf.write("\2\31\u00be\3\2\2\2\33\u00c0\3\2\2\2\35\u00c3\3\2\2\2")
        buf.write("\37\u00c5\3\2\2\2!\u00c7\3\2\2\2#\u00ca\3\2\2\2%\u00cc")
        buf.write("\3\2\2\2\'\u00cf\3\2\2\2)\u00d1\3\2\2\2+\u00d4\3\2\2\2")
        buf.write("-\u00d6\3\2\2\2/\u00d9\3\2\2\2\61\u00dc\3\2\2\2\63\u00de")
        buf.write("\3\2\2\2\65\u00e1\3\2\2\2\67\u00e4\3\2\2\29\u00e6\3\2")
        buf.write("\2\2;\u00e8\3\2\2\2=\u00eb\3\2\2\2?\u00ed\3\2\2\2A\u00ef")
        buf.write("\3\2\2\2C\u00f1\3\2\2\2E\u00f3\3\2\2\2G\u00f5\3\2\2\2")
        buf.write("I\u00f7\3\2\2\2K\u00fa\3\2\2\2M\u00fc\3\2\2\2O\u00ff\3")
        buf.write("\2\2\2Q\u0101\3\2\2\2S\u0104\3\2\2\2U\u0106\3\2\2\2W\u010f")
        buf.write("\3\2\2\2Y\u0120\3\2\2\2[\u0124\3\2\2\2]\u012e\3\2\2\2")
        buf.write("_\u0134\3\2\2\2a\u013c\3\2\2\2c\u0147\3\2\2\2e\u015a\3")
        buf.write("\2\2\2g\u0164\3\2\2\2i\u0176\3\2\2\2k\u017b\3\2\2\2m\u017f")
        buf.write("\3\2\2\2o\u0182\3\2\2\2q\u0189\3\2\2\2s\u0193\3\2\2\2")
        buf.write("u\u01a5\3\2\2\2w\u01bc\3\2\2\2y\u01c1\3\2\2\2{\u01c6\3")
        buf.write("\2\2\2}\u01da\3\2\2\2\177\u01dc\3\2\2\2\u0081\u01df\3")
        buf.write("\2\2\2\u0083\u01e2\3\2\2\2\u0085\u01e7\3\2\2\2\u0087\u0088")
        buf.write("\7f\2\2\u0088\u0089\7q\2\2\u0089\u008a\7e\2\2\u008a\4")
        buf.write("\3\2\2\2\u008b\u0098\5U+\2\u008c\u0098\5W,\2\u008d\u0098")
        buf.write("\5[.\2\u008e\u0098\5]/\2\u008f\u0098\5a\61\2\u0090\u0098")
        buf.write("\5c\62\2\u0091\u0098\5e\63\2\u0092\u0098\5g\64\2\u0093")
        buf.write("\u0098\5o8\2\u0094\u0098\5q9\2\u0095\u0098\5s:\2\u0096")
        buf.write("\u0098\5w<\2\u0097\u008b\3\2\2\2\u0097\u008c\3\2\2\2\u0097")
        buf.write("\u008d\3\2\2\2\u0097\u008e\3\2\2\2\u0097\u008f\3\2\2\2")
        buf.write("\u0097\u0090\3\2\2\2\u0097\u0091\3\2\2\2\u0097\u0092\3")
        buf.write("\2\2\2\u0097\u0093\3\2\2\2\u0097\u0094\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0097\u0096\3\2\2\2\u0098\6\3\2\2\2\u0099\u009d")
        buf.write("\t\2\2\2\u009a\u009c\t\3\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\b\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a2\t\3\2")
        buf.write("\2\u00a1\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\n\3\2\2\2\u00a5\u00ac")
        buf.write("\5+\26\2\u00a6\u00ac\5\67\34\2\u00a7\u00ac\5\61\31\2\u00a8")
        buf.write("\u00ac\5\63\32\2\u00a9\u00ac\5-\27\2\u00aa\u00ac\5;\36")
        buf.write("\2\u00ab\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7")
        buf.write("\3\2\2\2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\f\3\2\2\2\u00ad\u00b2\5m\67\2\u00ae")
        buf.write("\u00b2\5Y-\2\u00af\u00b2\5k\66\2\u00b0\u00b2\5C\"\2\u00b1")
        buf.write("\u00ad\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b0\3\2\2\2\u00b2\16\3\2\2\2\u00b3\u00b4\7B\2")
        buf.write("\2\u00b4\20\3\2\2\2\u00b5\u00b6\7#\2\2\u00b6\22\3\2\2")
        buf.write("\2\u00b7\u00b8\7_\2\2\u00b8\24\3\2\2\2\u00b9\u00ba\7\177")
        buf.write("\2\2\u00ba\26\3\2\2\2\u00bb\u00bc\7<\2\2\u00bc\u00bd\7")
        buf.write("?\2\2\u00bd\30\3\2\2\2\u00be\u00bf\7<\2\2\u00bf\32\3\2")
        buf.write("\2\2\u00c0\u00c1\7<\2\2\u00c1\u00c2\7<\2\2\u00c2\34\3")
        buf.write("\2\2\2\u00c3\u00c4\7.\2\2\u00c4\36\3\2\2\2\u00c5\u00c6")
        buf.write("\7+\2\2\u00c6 \3\2\2\2\u00c7\u00c8\7<\2\2\u00c8\u00c9")
        buf.write("\7,\2\2\u00c9\"\3\2\2\2\u00ca\u00cb\7\60\2\2\u00cb$\3")
        buf.write("\2\2\2\u00cc\u00cd\7\60\2\2\u00cd\u00ce\7\60\2\2\u00ce")
        buf.write("&\3\2\2\2\u00cf\u00d0\7&\2\2\u00d0(\3\2\2\2\u00d1\u00d2")
        buf.write("\7?\2\2\u00d2\u00d3\7@\2\2\u00d3*\3\2\2\2\u00d4\u00d5")
        buf.write("\7?\2\2\u00d5,\3\2\2\2\u00d6\u00d7\7@\2\2\u00d7\u00d8")
        buf.write("\7?\2\2\u00d8.\3\2\2\2\u00d9\u00da\7@\2\2\u00da\u00db")
        buf.write("\7@\2\2\u00db\60\3\2\2\2\u00dc\u00dd\7@\2\2\u00dd\62\3")
        buf.write("\2\2\2\u00de\u00df\7>\2\2\u00df\u00e0\7?\2\2\u00e0\64")
        buf.write("\3\2\2\2\u00e1\u00e2\7>\2\2\u00e2\u00e3\7>\2\2\u00e3\66")
        buf.write("\3\2\2\2\u00e4\u00e5\7>\2\2\u00e58\3\2\2\2\u00e6\u00e7")
        buf.write("\7/\2\2\u00e7:\3\2\2\2\u00e8\u00e9\7#\2\2\u00e9\u00ea")
        buf.write("\7?\2\2\u00ea<\3\2\2\2\u00eb\u00ec\7]\2\2\u00ec>\3\2\2")
        buf.write("\2\u00ed\u00ee\7}\2\2\u00ee@\3\2\2\2\u00ef\u00f0\7*\2")
        buf.write("\2\u00f0B\3\2\2\2\u00f1\u00f2\7~\2\2\u00f2D\3\2\2\2\u00f3")
        buf.write("\u00f4\7-\2\2\u00f4F\3\2\2\2\u00f5\u00f6\7%\2\2\u00f6")
        buf.write("H\3\2\2\2\u00f7\u00f8\7~\2\2\u00f8\u00f9\7~\2\2\u00f9")
        buf.write("J\3\2\2\2\u00fa\u00fb\7A\2\2\u00fbL\3\2\2\2\u00fc\u00fd")
        buf.write("\7,\2\2\u00fd\u00fe\7<\2\2\u00feN\3\2\2\2\u00ff\u0100")
        buf.write("\7\61\2\2\u0100P\3\2\2\2\u0101\u0102\7\61\2\2\u0102\u0103")
        buf.write("\7\61\2\2\u0103R\3\2\2\2\u0104\u0105\7,\2\2\u0105T\3\2")
        buf.write("\2\2\u0106\u0107\7c\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7e\2\2\u0109\u010a\7g\2\2\u010a\u010b\7u\2\2\u010b\u010c")
        buf.write("\7v\2\2\u010c\u010d\7q\2\2\u010d\u010e\7t\2\2\u010eV\3")
        buf.write("\2\2\2\u010f\u0110\7c\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7e\2\2\u0112\u0113\7g\2\2\u0113\u0114\7u\2\2\u0114\u0115")
        buf.write("\7v\2\2\u0115\u0116\7q\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7/\2\2\u0118\u0119\7q\2\2\u0119\u011a\7t\2\2\u011a\u011b")
        buf.write("\7/\2\2\u011b\u011c\7u\2\2\u011c\u011d\7g\2\2\u011d\u011e")
        buf.write("\7n\2\2\u011e\u011f\7h\2\2\u011fX\3\2\2\2\u0120\u0121")
        buf.write("\7c\2\2\u0121\u0122\7p\2\2\u0122\u0123\7f\2\2\u0123Z\3")
        buf.write("\2\2\2\u0124\u0125\7c\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7v\2\2\u0127\u0128\7t\2\2\u0128\u0129\7k\2\2\u0129\u012a")
        buf.write("\7d\2\2\u012a\u012b\7w\2\2\u012b\u012c\7v\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\\\3\2\2\2\u012e\u012f\7e\2\2\u012f\u0130")
        buf.write("\7j\2\2\u0130\u0131\7k\2\2\u0131\u0132\7n\2\2\u0132\u0133")
        buf.write("\7f\2\2\u0133^\3\2\2\2\u0134\u0135\7e\2\2\u0135\u0136")
        buf.write("\7q\2\2\u0136\u0137\7o\2\2\u0137\u0138\7o\2\2\u0138\u0139")
        buf.write("\7g\2\2\u0139\u013a\7p\2\2\u013a\u013b\7v\2\2\u013b`\3")
        buf.write("\2\2\2\u013c\u013d\7f\2\2\u013d\u013e\7g\2\2\u013e\u013f")
        buf.write("\7u\2\2\u013f\u0140\7e\2\2\u0140\u0141\7g\2\2\u0141\u0142")
        buf.write("\7p\2\2\u0142\u0143\7f\2\2\u0143\u0144\7c\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7v\2\2\u0146b\3\2\2\2\u0147\u0148")
        buf.write("\7f\2\2\u0148\u0149\7g\2\2\u0149\u014a\7u\2\2\u014a\u014b")
        buf.write("\7e\2\2\u014b\u014c\7g\2\2\u014c\u014d\7p\2\2\u014d\u014e")
        buf.write("\7f\2\2\u014e\u014f\7c\2\2\u014f\u0150\7p\2\2\u0150\u0151")
        buf.write("\7v\2\2\u0151\u0152\7/\2\2\u0152\u0153\7q\2\2\u0153\u0154")
        buf.write("\7t\2\2\u0154\u0155\7/\2\2\u0155\u0156\7u\2\2\u0156\u0157")
        buf.write("\7g\2\2\u0157\u0158\7n\2\2\u0158\u0159\7h\2\2\u0159d\3")
        buf.write("\2\2\2\u015a\u015b\7h\2\2\u015b\u015c\7q\2\2\u015c\u015d")
        buf.write("\7n\2\2\u015d\u015e\7n\2\2\u015e\u015f\7q\2\2\u015f\u0160")
        buf.write("\7y\2\2\u0160\u0161\7k\2\2\u0161\u0162\7p\2\2\u0162\u0163")
        buf.write("\7i\2\2\u0163f\3\2\2\2\u0164\u0165\7h\2\2\u0165\u0166")
        buf.write("\7q\2\2\u0166\u0167\7n\2\2\u0167\u0168\7n\2\2\u0168\u0169")
        buf.write("\7q\2\2\u0169\u016a\7y\2\2\u016a\u016b\7k\2\2\u016b\u016c")
        buf.write("\7p\2\2\u016c\u016d\7i\2\2\u016d\u016e\7/\2\2\u016e\u016f")
        buf.write("\7u\2\2\u016f\u0170\7k\2\2\u0170\u0171\7d\2\2\u0171\u0172")
        buf.write("\7n\2\2\u0172\u0173\7k\2\2\u0173\u0174\7p\2\2\u0174\u0175")
        buf.write("\7i\2\2\u0175h\3\2\2\2\u0176\u0177\7p\2\2\u0177\u0178")
        buf.write("\7q\2\2\u0178\u0179\7f\2\2\u0179\u017a\7g\2\2\u017aj\3")
        buf.write("\2\2\2\u017b\u017c\7p\2\2\u017c\u017d\7q\2\2\u017d\u017e")
        buf.write("\7v\2\2\u017el\3\2\2\2\u017f\u0180\7q\2\2\u0180\u0181")
        buf.write("\7t\2\2\u0181n\3\2\2\2\u0182\u0183\7r\2\2\u0183\u0184")
        buf.write("\7c\2\2\u0184\u0185\7t\2\2\u0185\u0186\7g\2\2\u0186\u0187")
        buf.write("\7p\2\2\u0187\u0188\7v\2\2\u0188p\3\2\2\2\u0189\u018a")
        buf.write("\7r\2\2\u018a\u018b\7t\2\2\u018b\u018c\7g\2\2\u018c\u018d")
        buf.write("\7e\2\2\u018d\u018e\7g\2\2\u018e\u018f\7f\2\2\u018f\u0190")
        buf.write("\7k\2\2\u0190\u0191\7p\2\2\u0191\u0192\7i\2\2\u0192r\3")
        buf.write("\2\2\2\u0193\u0194\7r\2\2\u0194\u0195\7t\2\2\u0195\u0196")
        buf.write("\7g\2\2\u0196\u0197\7e\2\2\u0197\u0198\7g\2\2\u0198\u0199")
        buf.write("\7f\2\2\u0199\u019a\7k\2\2\u019a\u019b\7p\2\2\u019b\u019c")
        buf.write("\7i\2\2\u019c\u019d\7/\2\2\u019d\u019e\7u\2\2\u019e\u019f")
        buf.write("\7k\2\2\u019f\u01a0\7d\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2")
        buf.write("\7k\2\2\u01a2\u01a3\7p\2\2\u01a3\u01a4\7i\2\2\u01a4t\3")
        buf.write("\2\2\2\u01a5\u01a6\7r\2\2\u01a6\u01a7\7t\2\2\u01a7\u01a8")
        buf.write("\7q\2\2\u01a8\u01a9\7e\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab")
        buf.write("\7u\2\2\u01ab\u01ac\7u\2\2\u01ac\u01ad\7k\2\2\u01ad\u01ae")
        buf.write("\7p\2\2\u01ae\u01af\7i\2\2\u01af\u01b0\7/\2\2\u01b0\u01b1")
        buf.write("\7k\2\2\u01b1\u01b2\7p\2\2\u01b2\u01b3\7u\2\2\u01b3\u01b4")
        buf.write("\7v\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6\7w\2\2\u01b6\u01b7")
        buf.write("\7e\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9\7k\2\2\u01b9\u01ba")
        buf.write("\7q\2\2\u01ba\u01bb\7p\2\2\u01bbv\3\2\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd\u01be\7g\2\2\u01be\u01bf\7n\2\2\u01bf\u01c0")
        buf.write("\7h\2\2\u01c0x\3\2\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3")
        buf.write("\7g\2\2\u01c3\u01c4\7z\2\2\u01c4\u01c5\7v\2\2\u01c5z\3")
        buf.write("\2\2\2\u01c6\u01c7\5\u0083B\2\u01c7|\3\2\2\2\u01c8\u01cd")
        buf.write("\7$\2\2\u01c9\u01cc\5\177@\2\u01ca\u01cc\n\4\2\2\u01cb")
        buf.write("\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc\u01cf\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01d0\3")
        buf.write("\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01db\7$\2\2\u01d1\u01d6")
        buf.write("\7)\2\2\u01d2\u01d5\5\u0081A\2\u01d3\u01d5\n\5\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d8\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d9\3")
        buf.write("\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db\7)\2\2\u01da\u01c8")
        buf.write("\3\2\2\2\u01da\u01d1\3\2\2\2\u01db~\3\2\2\2\u01dc\u01dd")
        buf.write("\7$\2\2\u01dd\u01de\7$\2\2\u01de\u0080\3\2\2\2\u01df\u01e0")
        buf.write("\7)\2\2\u01e0\u0082\3\2\2\2\u01e1\u01e3\t\6\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e2\3\2\2\2")
        buf.write("\u01e4\u01e5\3\2\2\2\u01e5\u0084\3\2\2\2\u01e6\u01e8\t")
        buf.write("\7\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb")
        buf.write("\u01ec\bC\2\2\u01ec\u0086\3\2\2\2\17\2\u0097\u009d\u00a3")
        buf.write("\u00ab\u00b1\u01cb\u01cd\u01d4\u01d6\u01da\u01e4\u01e9")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class XPathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    AXES = 2
    NODE_NAME = 3
    DOCUMENT_NAME = 4
    PREDICATE_OPERATOR = 5
    PREDICATE_CONNECTIVES = 6
    AT = 7
    BANG = 8
    CB = 9
    CC = 10
    CEQ = 11
    COLON = 12
    COLONCOLON = 13
    COMMA = 14
    CP = 15
    CS = 16
    D = 17
    DD = 18
    DOLLAR = 19
    EG = 20
    EQ = 21
    GE = 22
    GG = 23
    GT = 24
    LE = 25
    LL = 26
    LT = 27
    MINUS = 28
    NE = 29
    OB = 30
    OC = 31
    OP = 32
    P = 33
    PLUS = 34
    POUND = 35
    PP = 36
    QM = 37
    SC = 38
    SLASH = 39
    SS = 40
    STAR = 41
    KW_ANCESTOR = 42
    KW_ANCESTOR_OR_SELF = 43
    KW_AND = 44
    KW_ATTRIBUTE = 45
    KW_CHILD = 46
    KW_COMMENT = 47
    KW_DESCENDANT = 48
    KW_DESCENDANT_OR_SELF = 49
    KW_FOLLOWING = 50
    KW_FOLLOWING_SIBLING = 51
    KW_NODE = 52
    KW_NOT = 53
    KW_OR = 54
    KW_PARENT = 55
    KW_PRECEDING = 56
    KW_PRECEDING_SIBLING = 57
    KW_PROCESSING_INSTRUCTION = 58
    KW_SELF = 59
    KW_TEXT = 60
    IntegerLiteral = 61
    StringLiteral = 62
    WS = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'doc'", "'@'", "'!'", "']'", "'}'", "':='", "':'", "'::'", 
            "','", "')'", "':*'", "'.'", "'..'", "'$'", "'=>'", "'='", "'>='", 
            "'>>'", "'>'", "'<='", "'<<'", "'<'", "'-'", "'!='", "'['", 
            "'{'", "'('", "'|'", "'+'", "'#'", "'||'", "'?'", "'*:'", "'/'", 
            "'//'", "'*'", "'ancestor'", "'ancestor-or-self'", "'and'", 
            "'attribute'", "'child'", "'comment'", "'descendant'", "'descendant-or-self'", 
            "'following'", "'following-sibling'", "'node'", "'not'", "'or'", 
            "'parent'", "'preceding'", "'preceding-sibling'", "'processing-instruction'", 
            "'self'", "'text'" ]

    symbolicNames = [ "<INVALID>",
            "AXES", "NODE_NAME", "DOCUMENT_NAME", "PREDICATE_OPERATOR", 
            "PREDICATE_CONNECTIVES", "AT", "BANG", "CB", "CC", "CEQ", "COLON", 
            "COLONCOLON", "COMMA", "CP", "CS", "D", "DD", "DOLLAR", "EG", 
            "EQ", "GE", "GG", "GT", "LE", "LL", "LT", "MINUS", "NE", "OB", 
            "OC", "OP", "P", "PLUS", "POUND", "PP", "QM", "SC", "SLASH", 
            "SS", "STAR", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", "KW_AND", 
            "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", 
            "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", "KW_NODE", "KW_NOT", 
            "KW_OR", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
            "KW_PROCESSING_INSTRUCTION", "KW_SELF", "KW_TEXT", "IntegerLiteral", 
            "StringLiteral", "WS" ]

    ruleNames = [ "T__0", "AXES", "NODE_NAME", "DOCUMENT_NAME", "PREDICATE_OPERATOR", 
                  "PREDICATE_CONNECTIVES", "AT", "BANG", "CB", "CC", "CEQ", 
                  "COLON", "COLONCOLON", "COMMA", "CP", "CS", "D", "DD", 
                  "DOLLAR", "EG", "EQ", "GE", "GG", "GT", "LE", "LL", "LT", 
                  "MINUS", "NE", "OB", "OC", "OP", "P", "PLUS", "POUND", 
                  "PP", "QM", "SC", "SLASH", "SS", "STAR", "KW_ANCESTOR", 
                  "KW_ANCESTOR_OR_SELF", "KW_AND", "KW_ATTRIBUTE", "KW_CHILD", 
                  "KW_COMMENT", "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", 
                  "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", "KW_NODE", "KW_NOT", 
                  "KW_OR", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                  "KW_PROCESSING_INSTRUCTION", "KW_SELF", "KW_TEXT", "IntegerLiteral", 
                  "StringLiteral", "FragEscapeQuot", "FragEscapeApos", "FragDigits", 
                  "WS" ]

    grammarFileName = "XPath.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


