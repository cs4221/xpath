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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01e0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u0090\n\2\3\3")
        buf.write("\3\3\7\3\u0094\n\3\f\3\16\3\u0097\13\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u009f\n\4\3\5\3\5\3\5\3\5\5\5\u00a5\n\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38\38\38\38\3")
        buf.write("8\38\38\38\39\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write(";\3<\3<\3=\3=\3=\7=\u01bf\n=\f=\16=\u01c2\13=\3=\3=\3")
        buf.write("=\3=\7=\u01c8\n=\f=\16=\u01cb\13=\3=\5=\u01ce\n=\3>\3")
        buf.write(">\3>\3?\3?\3@\6@\u01d6\n@\r@\16@\u01d7\3A\6A\u01db\nA")
        buf.write("\rA\16A\u01dc\3A\3A\4\u01c0\u01c9\2B\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{\2}\2\177\2")
        buf.write("\u0081?\3\2\b\5\2C\\aac|\7\2/\60\62;C\\aac|\4\2$$``\3")
        buf.write("\2))\3\2\62;\5\2\13\f\16\17\"\"\2\u01f7\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\3\u008f\3\2\2\2\5\u0091\3\2\2\2\7\u009e\3\2\2\2\t\u00a4")
        buf.write("\3\2\2\2\13\u00a6\3\2\2\2\r\u00a8\3\2\2\2\17\u00aa\3\2")
        buf.write("\2\2\21\u00ac\3\2\2\2\23\u00ae\3\2\2\2\25\u00b1\3\2\2")
        buf.write("\2\27\u00b3\3\2\2\2\31\u00b6\3\2\2\2\33\u00b8\3\2\2\2")
        buf.write("\35\u00ba\3\2\2\2\37\u00bd\3\2\2\2!\u00bf\3\2\2\2#\u00c2")
        buf.write("\3\2\2\2%\u00c4\3\2\2\2\'\u00c7\3\2\2\2)\u00c9\3\2\2\2")
        buf.write("+\u00cc\3\2\2\2-\u00cf\3\2\2\2/\u00d1\3\2\2\2\61\u00d4")
        buf.write("\3\2\2\2\63\u00d7\3\2\2\2\65\u00d9\3\2\2\2\67\u00db\3")
        buf.write("\2\2\29\u00de\3\2\2\2;\u00e0\3\2\2\2=\u00e2\3\2\2\2?\u00e4")
        buf.write("\3\2\2\2A\u00e6\3\2\2\2C\u00e8\3\2\2\2E\u00ea\3\2\2\2")
        buf.write("G\u00ed\3\2\2\2I\u00ef\3\2\2\2K\u00f2\3\2\2\2M\u00f4\3")
        buf.write("\2\2\2O\u00f7\3\2\2\2Q\u00f9\3\2\2\2S\u0102\3\2\2\2U\u0113")
        buf.write("\3\2\2\2W\u0117\3\2\2\2Y\u0121\3\2\2\2[\u0127\3\2\2\2")
        buf.write("]\u012f\3\2\2\2_\u013a\3\2\2\2a\u014d\3\2\2\2c\u0157\3")
        buf.write("\2\2\2e\u0169\3\2\2\2g\u016e\3\2\2\2i\u0172\3\2\2\2k\u0175")
        buf.write("\3\2\2\2m\u017c\3\2\2\2o\u0186\3\2\2\2q\u0198\3\2\2\2")
        buf.write("s\u01af\3\2\2\2u\u01b4\3\2\2\2w\u01b9\3\2\2\2y\u01cd\3")
        buf.write("\2\2\2{\u01cf\3\2\2\2}\u01d2\3\2\2\2\177\u01d5\3\2\2\2")
        buf.write("\u0081\u01da\3\2\2\2\u0083\u0090\5Q)\2\u0084\u0090\5S")
        buf.write("*\2\u0085\u0090\5W,\2\u0086\u0090\5Y-\2\u0087\u0090\5")
        buf.write("]/\2\u0088\u0090\5_\60\2\u0089\u0090\5a\61\2\u008a\u0090")
        buf.write("\5c\62\2\u008b\u0090\5k\66\2\u008c\u0090\5m\67\2\u008d")
        buf.write("\u0090\5o8\2\u008e\u0090\5s:\2\u008f\u0083\3\2\2\2\u008f")
        buf.write("\u0084\3\2\2\2\u008f\u0085\3\2\2\2\u008f\u0086\3\2\2\2")
        buf.write("\u008f\u0087\3\2\2\2\u008f\u0088\3\2\2\2\u008f\u0089\3")
        buf.write("\2\2\2\u008f\u008a\3\2\2\2\u008f\u008b\3\2\2\2\u008f\u008c")
        buf.write("\3\2\2\2\u008f\u008d\3\2\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\4\3\2\2\2\u0091\u0095\t\2\2\2\u0092\u0094\t\3\2\2\u0093")
        buf.write("\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\6\3\2\2\2\u0097\u0095\3\2\2")
        buf.write("\2\u0098\u009f\5\'\24\2\u0099\u009f\5\63\32\2\u009a\u009f")
        buf.write("\5-\27\2\u009b\u009f\5/\30\2\u009c\u009f\5)\25\2\u009d")
        buf.write("\u009f\5\67\34\2\u009e\u0098\3\2\2\2\u009e\u0099\3\2\2")
        buf.write("\2\u009e\u009a\3\2\2\2\u009e\u009b\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009e\u009d\3\2\2\2\u009f\b\3\2\2\2\u00a0\u00a5")
        buf.write("\5i\65\2\u00a1\u00a5\5U+\2\u00a2\u00a5\5g\64\2\u00a3\u00a5")
        buf.write("\5? \2\u00a4\u00a0\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\n\3\2\2\2\u00a6\u00a7")
        buf.write("\7B\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7#\2\2\u00a9\16\3")
        buf.write("\2\2\2\u00aa\u00ab\7_\2\2\u00ab\20\3\2\2\2\u00ac\u00ad")
        buf.write("\7\177\2\2\u00ad\22\3\2\2\2\u00ae\u00af\7<\2\2\u00af\u00b0")
        buf.write("\7?\2\2\u00b0\24\3\2\2\2\u00b1\u00b2\7<\2\2\u00b2\26\3")
        buf.write("\2\2\2\u00b3\u00b4\7<\2\2\u00b4\u00b5\7<\2\2\u00b5\30")
        buf.write("\3\2\2\2\u00b6\u00b7\7.\2\2\u00b7\32\3\2\2\2\u00b8\u00b9")
        buf.write("\7+\2\2\u00b9\34\3\2\2\2\u00ba\u00bb\7<\2\2\u00bb\u00bc")
        buf.write("\7,\2\2\u00bc\36\3\2\2\2\u00bd\u00be\7\60\2\2\u00be \3")
        buf.write("\2\2\2\u00bf\u00c0\7\60\2\2\u00c0\u00c1\7\60\2\2\u00c1")
        buf.write("\"\3\2\2\2\u00c2\u00c3\7&\2\2\u00c3$\3\2\2\2\u00c4\u00c5")
        buf.write("\7?\2\2\u00c5\u00c6\7@\2\2\u00c6&\3\2\2\2\u00c7\u00c8")
        buf.write("\7?\2\2\u00c8(\3\2\2\2\u00c9\u00ca\7@\2\2\u00ca\u00cb")
        buf.write("\7?\2\2\u00cb*\3\2\2\2\u00cc\u00cd\7@\2\2\u00cd\u00ce")
        buf.write("\7@\2\2\u00ce,\3\2\2\2\u00cf\u00d0\7@\2\2\u00d0.\3\2\2")
        buf.write("\2\u00d1\u00d2\7>\2\2\u00d2\u00d3\7?\2\2\u00d3\60\3\2")
        buf.write("\2\2\u00d4\u00d5\7>\2\2\u00d5\u00d6\7>\2\2\u00d6\62\3")
        buf.write("\2\2\2\u00d7\u00d8\7>\2\2\u00d8\64\3\2\2\2\u00d9\u00da")
        buf.write("\7/\2\2\u00da\66\3\2\2\2\u00db\u00dc\7#\2\2\u00dc\u00dd")
        buf.write("\7?\2\2\u00dd8\3\2\2\2\u00de\u00df\7]\2\2\u00df:\3\2\2")
        buf.write("\2\u00e0\u00e1\7}\2\2\u00e1<\3\2\2\2\u00e2\u00e3\7*\2")
        buf.write("\2\u00e3>\3\2\2\2\u00e4\u00e5\7~\2\2\u00e5@\3\2\2\2\u00e6")
        buf.write("\u00e7\7-\2\2\u00e7B\3\2\2\2\u00e8\u00e9\7%\2\2\u00e9")
        buf.write("D\3\2\2\2\u00ea\u00eb\7~\2\2\u00eb\u00ec\7~\2\2\u00ec")
        buf.write("F\3\2\2\2\u00ed\u00ee\7A\2\2\u00eeH\3\2\2\2\u00ef\u00f0")
        buf.write("\7,\2\2\u00f0\u00f1\7<\2\2\u00f1J\3\2\2\2\u00f2\u00f3")
        buf.write("\7\61\2\2\u00f3L\3\2\2\2\u00f4\u00f5\7\61\2\2\u00f5\u00f6")
        buf.write("\7\61\2\2\u00f6N\3\2\2\2\u00f7\u00f8\7,\2\2\u00f8P\3\2")
        buf.write("\2\2\u00f9\u00fa\7c\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc")
        buf.write("\7e\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7t\2\2\u0101R\3")
        buf.write("\2\2\2\u0102\u0103\7c\2\2\u0103\u0104\7p\2\2\u0104\u0105")
        buf.write("\7e\2\2\u0105\u0106\7g\2\2\u0106\u0107\7u\2\2\u0107\u0108")
        buf.write("\7v\2\2\u0108\u0109\7q\2\2\u0109\u010a\7t\2\2\u010a\u010b")
        buf.write("\7/\2\2\u010b\u010c\7q\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7/\2\2\u010e\u010f\7u\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7n\2\2\u0111\u0112\7h\2\2\u0112T\3\2\2\2\u0113\u0114")
        buf.write("\7c\2\2\u0114\u0115\7p\2\2\u0115\u0116\7f\2\2\u0116V\3")
        buf.write("\2\2\2\u0117\u0118\7c\2\2\u0118\u0119\7v\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\u011b\7t\2\2\u011b\u011c\7k\2\2\u011c\u011d")
        buf.write("\7d\2\2\u011d\u011e\7w\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120X\3\2\2\2\u0121\u0122\7e\2\2\u0122\u0123")
        buf.write("\7j\2\2\u0123\u0124\7k\2\2\u0124\u0125\7n\2\2\u0125\u0126")
        buf.write("\7f\2\2\u0126Z\3\2\2\2\u0127\u0128\7e\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7o\2\2\u012a\u012b\7o\2\2\u012b\u012c")
        buf.write("\7g\2\2\u012c\u012d\7p\2\2\u012d\u012e\7v\2\2\u012e\\")
        buf.write("\3\2\2\2\u012f\u0130\7f\2\2\u0130\u0131\7g\2\2\u0131\u0132")
        buf.write("\7u\2\2\u0132\u0133\7e\2\2\u0133\u0134\7g\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7f\2\2\u0136\u0137\7c\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138\u0139\7v\2\2\u0139^\3\2\2\2\u013a\u013b")
        buf.write("\7f\2\2\u013b\u013c\7g\2\2\u013c\u013d\7u\2\2\u013d\u013e")
        buf.write("\7e\2\2\u013e\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140\u0141")
        buf.write("\7f\2\2\u0141\u0142\7c\2\2\u0142\u0143\7p\2\2\u0143\u0144")
        buf.write("\7v\2\2\u0144\u0145\7/\2\2\u0145\u0146\7q\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7/\2\2\u0148\u0149\7u\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a\u014b\7n\2\2\u014b\u014c\7h\2\2\u014c`\3")
        buf.write("\2\2\2\u014d\u014e\7h\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7n\2\2\u0150\u0151\7n\2\2\u0151\u0152\7q\2\2\u0152\u0153")
        buf.write("\7y\2\2\u0153\u0154\7k\2\2\u0154\u0155\7p\2\2\u0155\u0156")
        buf.write("\7i\2\2\u0156b\3\2\2\2\u0157\u0158\7h\2\2\u0158\u0159")
        buf.write("\7q\2\2\u0159\u015a\7n\2\2\u015a\u015b\7n\2\2\u015b\u015c")
        buf.write("\7q\2\2\u015c\u015d\7y\2\2\u015d\u015e\7k\2\2\u015e\u015f")
        buf.write("\7p\2\2\u015f\u0160\7i\2\2\u0160\u0161\7/\2\2\u0161\u0162")
        buf.write("\7u\2\2\u0162\u0163\7k\2\2\u0163\u0164\7d\2\2\u0164\u0165")
        buf.write("\7n\2\2\u0165\u0166\7k\2\2\u0166\u0167\7p\2\2\u0167\u0168")
        buf.write("\7i\2\2\u0168d\3\2\2\2\u0169\u016a\7p\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7f\2\2\u016c\u016d\7g\2\2\u016df\3")
        buf.write("\2\2\2\u016e\u016f\7p\2\2\u016f\u0170\7q\2\2\u0170\u0171")
        buf.write("\7v\2\2\u0171h\3\2\2\2\u0172\u0173\7q\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174j\3\2\2\2\u0175\u0176\7r\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7t\2\2\u0178\u0179\7g\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a\u017b\7v\2\2\u017bl\3\2\2\2\u017c\u017d")
        buf.write("\7r\2\2\u017d\u017e\7t\2\2\u017e\u017f\7g\2\2\u017f\u0180")
        buf.write("\7e\2\2\u0180\u0181\7g\2\2\u0181\u0182\7f\2\2\u0182\u0183")
        buf.write("\7k\2\2\u0183\u0184\7p\2\2\u0184\u0185\7i\2\2\u0185n\3")
        buf.write("\2\2\2\u0186\u0187\7r\2\2\u0187\u0188\7t\2\2\u0188\u0189")
        buf.write("\7g\2\2\u0189\u018a\7e\2\2\u018a\u018b\7g\2\2\u018b\u018c")
        buf.write("\7f\2\2\u018c\u018d\7k\2\2\u018d\u018e\7p\2\2\u018e\u018f")
        buf.write("\7i\2\2\u018f\u0190\7/\2\2\u0190\u0191\7u\2\2\u0191\u0192")
        buf.write("\7k\2\2\u0192\u0193\7d\2\2\u0193\u0194\7n\2\2\u0194\u0195")
        buf.write("\7k\2\2\u0195\u0196\7p\2\2\u0196\u0197\7i\2\2\u0197p\3")
        buf.write("\2\2\2\u0198\u0199\7r\2\2\u0199\u019a\7t\2\2\u019a\u019b")
        buf.write("\7q\2\2\u019b\u019c\7e\2\2\u019c\u019d\7g\2\2\u019d\u019e")
        buf.write("\7u\2\2\u019e\u019f\7u\2\2\u019f\u01a0\7k\2\2\u01a0\u01a1")
        buf.write("\7p\2\2\u01a1\u01a2\7i\2\2\u01a2\u01a3\7/\2\2\u01a3\u01a4")
        buf.write("\7k\2\2\u01a4\u01a5\7p\2\2\u01a5\u01a6\7u\2\2\u01a6\u01a7")
        buf.write("\7v\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa")
        buf.write("\7e\2\2\u01aa\u01ab\7v\2\2\u01ab\u01ac\7k\2\2\u01ac\u01ad")
        buf.write("\7q\2\2\u01ad\u01ae\7p\2\2\u01aer\3\2\2\2\u01af\u01b0")
        buf.write("\7u\2\2\u01b0\u01b1\7g\2\2\u01b1\u01b2\7n\2\2\u01b2\u01b3")
        buf.write("\7h\2\2\u01b3t\3\2\2\2\u01b4\u01b5\7v\2\2\u01b5\u01b6")
        buf.write("\7g\2\2\u01b6\u01b7\7z\2\2\u01b7\u01b8\7v\2\2\u01b8v\3")
        buf.write("\2\2\2\u01b9\u01ba\5\177@\2\u01bax\3\2\2\2\u01bb\u01c0")
        buf.write("\7$\2\2\u01bc\u01bf\5{>\2\u01bd\u01bf\n\4\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c3\3\2\2\2")
        buf.write("\u01c2\u01c0\3\2\2\2\u01c3\u01ce\7$\2\2\u01c4\u01c9\7")
        buf.write(")\2\2\u01c5\u01c8\5}?\2\u01c6\u01c8\n\5\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cc\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01ce\7)\2\2\u01cd\u01bb\3")
        buf.write("\2\2\2\u01cd\u01c4\3\2\2\2\u01cez\3\2\2\2\u01cf\u01d0")
        buf.write("\7$\2\2\u01d0\u01d1\7$\2\2\u01d1|\3\2\2\2\u01d2\u01d3")
        buf.write("\7)\2\2\u01d3~\3\2\2\2\u01d4\u01d6\t\6\2\2\u01d5\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u0080\3\2\2\2\u01d9\u01db\t\7\2\2")
        buf.write("\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01df")
        buf.write("\bA\2\2\u01df\u0082\3\2\2\2\16\2\u008f\u0095\u009e\u00a4")
        buf.write("\u01be\u01c0\u01c7\u01c9\u01cd\u01d7\u01dc\3\b\2\2")
        return buf.getvalue()


class XPathLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AXES = 1
    NODE_NAME = 2
    PREDICATE_OPERATOR = 3
    PREDICATE_CONNECTIVES = 4
    AT = 5
    BANG = 6
    CB = 7
    CC = 8
    CEQ = 9
    COLON = 10
    COLONCOLON = 11
    COMMA = 12
    CP = 13
    CS = 14
    D = 15
    DD = 16
    DOLLAR = 17
    EG = 18
    EQ = 19
    GE = 20
    GG = 21
    GT = 22
    LE = 23
    LL = 24
    LT = 25
    MINUS = 26
    NE = 27
    OB = 28
    OC = 29
    OP = 30
    P = 31
    PLUS = 32
    POUND = 33
    PP = 34
    QM = 35
    SC = 36
    SLASH = 37
    SS = 38
    STAR = 39
    KW_ANCESTOR = 40
    KW_ANCESTOR_OR_SELF = 41
    KW_AND = 42
    KW_ATTRIBUTE = 43
    KW_CHILD = 44
    KW_COMMENT = 45
    KW_DESCENDANT = 46
    KW_DESCENDANT_OR_SELF = 47
    KW_FOLLOWING = 48
    KW_FOLLOWING_SIBLING = 49
    KW_NODE = 50
    KW_NOT = 51
    KW_OR = 52
    KW_PARENT = 53
    KW_PRECEDING = 54
    KW_PRECEDING_SIBLING = 55
    KW_PROCESSING_INSTRUCTION = 56
    KW_SELF = 57
    KW_TEXT = 58
    IntegerLiteral = 59
    StringLiteral = 60
    WS = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@'", "'!'", "']'", "'}'", "':='", "':'", "'::'", "','", "')'", 
            "':*'", "'.'", "'..'", "'$'", "'=>'", "'='", "'>='", "'>>'", 
            "'>'", "'<='", "'<<'", "'<'", "'-'", "'!='", "'['", "'{'", "'('", 
            "'|'", "'+'", "'#'", "'||'", "'?'", "'*:'", "'/'", "'//'", "'*'", 
            "'ancestor'", "'ancestor-or-self'", "'and'", "'attribute'", 
            "'child'", "'comment'", "'descendant'", "'descendant-or-self'", 
            "'following'", "'following-sibling'", "'node'", "'not'", "'or'", 
            "'parent'", "'preceding'", "'preceding-sibling'", "'processing-instruction'", 
            "'self'", "'text'" ]

    symbolicNames = [ "<INVALID>",
            "AXES", "NODE_NAME", "PREDICATE_OPERATOR", "PREDICATE_CONNECTIVES", 
            "AT", "BANG", "CB", "CC", "CEQ", "COLON", "COLONCOLON", "COMMA", 
            "CP", "CS", "D", "DD", "DOLLAR", "EG", "EQ", "GE", "GG", "GT", 
            "LE", "LL", "LT", "MINUS", "NE", "OB", "OC", "OP", "P", "PLUS", 
            "POUND", "PP", "QM", "SC", "SLASH", "SS", "STAR", "KW_ANCESTOR", 
            "KW_ANCESTOR_OR_SELF", "KW_AND", "KW_ATTRIBUTE", "KW_CHILD", 
            "KW_COMMENT", "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", 
            "KW_FOLLOWING_SIBLING", "KW_NODE", "KW_NOT", "KW_OR", "KW_PARENT", 
            "KW_PRECEDING", "KW_PRECEDING_SIBLING", "KW_PROCESSING_INSTRUCTION", 
            "KW_SELF", "KW_TEXT", "IntegerLiteral", "StringLiteral", "WS" ]

    ruleNames = [ "AXES", "NODE_NAME", "PREDICATE_OPERATOR", "PREDICATE_CONNECTIVES", 
                  "AT", "BANG", "CB", "CC", "CEQ", "COLON", "COLONCOLON", 
                  "COMMA", "CP", "CS", "D", "DD", "DOLLAR", "EG", "EQ", 
                  "GE", "GG", "GT", "LE", "LL", "LT", "MINUS", "NE", "OB", 
                  "OC", "OP", "P", "PLUS", "POUND", "PP", "QM", "SC", "SLASH", 
                  "SS", "STAR", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", "KW_AND", 
                  "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", "KW_DESCENDANT", 
                  "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
                  "KW_NODE", "KW_NOT", "KW_OR", "KW_PARENT", "KW_PRECEDING", 
                  "KW_PRECEDING_SIBLING", "KW_PROCESSING_INSTRUCTION", "KW_SELF", 
                  "KW_TEXT", "IntegerLiteral", "StringLiteral", "FragEscapeQuot", 
                  "FragEscapeApos", "FragDigits", "WS" ]

    grammarFileName = "XPath.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


