# Generated from .\xpath\xpathgrammer\XPath20.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3k")
        buf.write("\u024a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\7\3\u0099\n\3\f\3\16\3\u009c\13\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u00a2\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\7\6\u00b3\n\6\f\6\16\6\u00b6\13\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00c3\n")
        buf.write("\7\f\7\16\7\u00c6\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t\u00d7\n\t\f\t\16\t\u00da")
        buf.write("\13\t\3\n\3\n\3\n\7\n\u00df\n\n\f\n\16\n\u00e2\13\n\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00e8\n\13\3\13\3\13\5\13\u00ec")
        buf.write("\n\13\3\f\3\f\3\f\5\f\u00f1\n\f\3\r\3\r\3\r\7\r\u00f6")
        buf.write("\n\r\f\r\16\r\u00f9\13\r\3\16\3\16\3\16\7\16\u00fe\n\16")
        buf.write("\f\16\16\16\u0101\13\16\3\17\3\17\3\17\7\17\u0106\n\17")
        buf.write("\f\17\16\17\u0109\13\17\3\20\3\20\3\20\7\20\u010e\n\20")
        buf.write("\f\20\16\20\u0111\13\20\3\21\3\21\3\21\3\21\5\21\u0117")
        buf.write("\n\21\3\22\3\22\3\22\3\22\5\22\u011d\n\22\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u0123\n\23\3\24\3\24\3\24\3\24\5\24\u0129")
        buf.write("\n\24\3\25\7\25\u012c\n\25\f\25\16\25\u012f\13\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u013d\n\32\3\32\3\32\3\32\5\32\u0142\n\32\3\33\3")
        buf.write("\33\3\33\7\33\u0147\n\33\f\33\16\33\u014a\13\33\3\34\3")
        buf.write("\34\5\34\u014e\n\34\3\35\3\35\5\35\u0152\n\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u015a\n\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u016c\n\37\3 \5 \u016f\n \3 \3 \3!\3!")
        buf.write("\3!\3!\5!\u0177\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\5\"\u0183\n\"\3#\3#\3$\3$\5$\u0189\n$\3%\3%\5%\u018d")
        buf.write("\n%\3&\3&\3&\3&\3&\5&\u0194\n&\3\'\3\'\3\'\3(\7(\u019a")
        buf.write("\n(\f(\16(\u019d\13(\3)\3)\3)\3)\3*\3*\3*\3*\3*\5*\u01a8")
        buf.write("\n*\3+\3+\5+\u01ac\n+\3,\3,\3-\3-\3-\3.\3.\3/\3/\5/\u01b7")
        buf.write("\n/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u01c3\n\61\f\61\16\61\u01c6\13\61\5\61\u01c8\n\61\3\61")
        buf.write("\3\61\3\62\3\62\5\62\u01ce\n\62\3\63\3\63\3\63\3\63\3")
        buf.write("\63\5\63\u01d5\n\63\5\63\u01d7\n\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u01e0\n\65\3\66\3\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u01ed\n\67\38\3")
        buf.write("8\38\38\39\39\39\39\59\u01f7\n9\39\39\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\5<\u0206\n<\3<\3<\3=\3=\3=\3=\3=\5=\u020f")
        buf.write("\n=\5=\u0211\n=\3=\3=\3>\3>\5>\u0217\n>\3?\3?\3?\3?\3")
        buf.write("?\3@\3@\3A\3A\3A\3A\3A\3A\5A\u0226\nA\5A\u0228\nA\5A\u022a")
        buf.write("\nA\3A\3A\3B\3B\5B\u0230\nB\3C\3C\3C\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\3H\3H\3I\3I\3I\6I\u0244\nI\rI\16I\u0245")
        buf.write("\3I\3I\3I\2\2J\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprt")
        buf.write("vxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write("\u0090\2\17\4\288[[\4\2\30\30\36\36\6\2%%\62\62@@KK\4")
        buf.write("\2\35\35``\4\299DD\6\2\21\22\24\25\27\27\31\31\7\2\67")
        buf.write("\67>?GGIINN\5\2\23\23\26\26EE\3\2#$\3\2ac\5\2\36\36!!")
        buf.write("%%\4\2ddii\6\2&]_`eehh\2\u024f\2\u0092\3\2\2\2\4\u0095")
        buf.write("\3\2\2\2\6\u00a1\3\2\2\2\b\u00a3\3\2\2\2\n\u00a7\3\2\2")
        buf.write("\2\f\u00b7\3\2\2\2\16\u00ca\3\2\2\2\20\u00d3\3\2\2\2\22")
        buf.write("\u00db\3\2\2\2\24\u00e3\3\2\2\2\26\u00ed\3\2\2\2\30\u00f2")
        buf.write("\3\2\2\2\32\u00fa\3\2\2\2\34\u0102\3\2\2\2\36\u010a\3")
        buf.write("\2\2\2 \u0112\3\2\2\2\"\u0118\3\2\2\2$\u011e\3\2\2\2&")
        buf.write("\u0124\3\2\2\2(\u012d\3\2\2\2*\u0132\3\2\2\2,\u0134\3")
        buf.write("\2\2\2.\u0136\3\2\2\2\60\u0138\3\2\2\2\62\u0141\3\2\2")
        buf.write("\2\64\u0143\3\2\2\2\66\u014d\3\2\2\28\u0151\3\2\2\2:\u0159")
        buf.write("\3\2\2\2<\u016b\3\2\2\2>\u016e\3\2\2\2@\u0176\3\2\2\2")
        buf.write("B\u0182\3\2\2\2D\u0184\3\2\2\2F\u0188\3\2\2\2H\u018c\3")
        buf.write("\2\2\2J\u0193\3\2\2\2L\u0195\3\2\2\2N\u019b\3\2\2\2P\u019e")
        buf.write("\3\2\2\2R\u01a7\3\2\2\2T\u01ab\3\2\2\2V\u01ad\3\2\2\2")
        buf.write("X\u01af\3\2\2\2Z\u01b2\3\2\2\2\\\u01b4\3\2\2\2^\u01ba")
        buf.write("\3\2\2\2`\u01bc\3\2\2\2b\u01cb\3\2\2\2d\u01d6\3\2\2\2")
        buf.write("f\u01d8\3\2\2\2h\u01df\3\2\2\2j\u01e1\3\2\2\2l\u01ec\3")
        buf.write("\2\2\2n\u01ee\3\2\2\2p\u01f2\3\2\2\2r\u01fa\3\2\2\2t\u01fe")
        buf.write("\3\2\2\2v\u0202\3\2\2\2x\u0209\3\2\2\2z\u0216\3\2\2\2")
        buf.write("|\u0218\3\2\2\2~\u021d\3\2\2\2\u0080\u021f\3\2\2\2\u0082")
        buf.write("\u022f\3\2\2\2\u0084\u0231\3\2\2\2\u0086\u0236\3\2\2\2")
        buf.write("\u0088\u0238\3\2\2\2\u008a\u023a\3\2\2\2\u008c\u023c\3")
        buf.write("\2\2\2\u008e\u023e\3\2\2\2\u0090\u0243\3\2\2\2\u0092\u0093")
        buf.write("\5\4\3\2\u0093\u0094\7\2\2\3\u0094\3\3\2\2\2\u0095\u009a")
        buf.write("\5\6\4\2\u0096\u0097\7\n\2\2\u0097\u0099\5\6\4\2\u0098")
        buf.write("\u0096\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\5\3\2\2\2\u009c\u009a\3\2\2")
        buf.write("\2\u009d\u00a2\5\b\5\2\u009e\u00a2\5\f\7\2\u009f\u00a2")
        buf.write("\5\16\b\2\u00a0\u00a2\5\20\t\2\u00a1\u009d\3\2\2\2\u00a1")
        buf.write("\u009e\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2")
        buf.write("\u00a2\7\3\2\2\2\u00a3\u00a4\5\n\6\2\u00a4\u00a5\7V\2")
        buf.write("\2\u00a5\u00a6\5\6\4\2\u00a6\t\3\2\2\2\u00a7\u00a8\7<")
        buf.write("\2\2\u00a8\u00a9\7\17\2\2\u00a9\u00aa\5Z.\2\u00aa\u00ab")
        buf.write("\7B\2\2\u00ab\u00b4\5\6\4\2\u00ac\u00ad\7\n\2\2\u00ad")
        buf.write("\u00ae\7\17\2\2\u00ae\u00af\5Z.\2\u00af\u00b0\7B\2\2\u00b0")
        buf.write("\u00b1\5\6\4\2\u00b1\u00b3\3\2\2\2\u00b2\u00ac\3\2\2\2")
        buf.write("\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3")
        buf.write("\2\2\2\u00b5\13\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8")
        buf.write("\t\2\2\2\u00b8\u00b9\7\17\2\2\u00b9\u00ba\5Z.\2\u00ba")
        buf.write("\u00bb\7B\2\2\u00bb\u00c4\5\6\4\2\u00bc\u00bd\7\n\2\2")
        buf.write("\u00bd\u00be\7\17\2\2\u00be\u00bf\5Z.\2\u00bf\u00c0\7")
        buf.write("B\2\2\u00c0\u00c1\5\6\4\2\u00c1\u00c3\3\2\2\2\u00c2\u00bc")
        buf.write("\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c7\u00c8\7W\2\2\u00c8\u00c9\5\6\4\2\u00c9\r\3\2\2")
        buf.write("\2\u00ca\u00cb\7A\2\2\u00cb\u00cc\7\34\2\2\u00cc\u00cd")
        buf.write("\5\4\3\2\u00cd\u00ce\7\13\2\2\u00ce\u00cf\7]\2\2\u00cf")
        buf.write("\u00d0\5\6\4\2\u00d0\u00d1\7\65\2\2\u00d1\u00d2\5\6\4")
        buf.write("\2\u00d2\17\3\2\2\2\u00d3\u00d8\5\22\n\2\u00d4\u00d5\7")
        buf.write("Q\2\2\u00d5\u00d7\5\22\n\2\u00d6\u00d4\3\2\2\2\u00d7\u00da")
        buf.write("\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\21\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00e0\5\24\13\2")
        buf.write("\u00dc\u00dd\7(\2\2\u00dd\u00df\5\24\13\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\23\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3")
        buf.write("\u00eb\5\26\f\2\u00e4\u00e8\5.\30\2\u00e5\u00e8\5,\27")
        buf.write("\2\u00e6\u00e8\5\60\31\2\u00e7\u00e4\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9")
        buf.write("\u00ea\5\26\f\2\u00ea\u00ec\3\2\2\2\u00eb\u00e7\3\2\2")
        buf.write("\2\u00eb\u00ec\3\2\2\2\u00ec\25\3\2\2\2\u00ed\u00f0\5")
        buf.write("\30\r\2\u00ee\u00ef\7^\2\2\u00ef\u00f1\5\30\r\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\27\3\2\2\2\u00f2")
        buf.write("\u00f7\5\32\16\2\u00f3\u00f4\t\3\2\2\u00f4\u00f6\5\32")
        buf.write("\16\2\u00f5\u00f3\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\31\3\2\2\2\u00f9\u00f7")
        buf.write("\3\2\2\2\u00fa\u00ff\5\34\17\2\u00fb\u00fc\t\4\2\2\u00fc")
        buf.write("\u00fe\5\34\17\2\u00fd\u00fb\3\2\2\2\u00fe\u0101\3\2\2")
        buf.write("\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\33\3")
        buf.write("\2\2\2\u0101\u00ff\3\2\2\2\u0102\u0107\5\36\20\2\u0103")
        buf.write("\u0104\t\5\2\2\u0104\u0106\5\36\20\2\u0105\u0103\3\2\2")
        buf.write("\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\35\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010f")
        buf.write("\5 \21\2\u010b\u010c\t\6\2\2\u010c\u010e\5 \21\2\u010d")
        buf.write("\u010b\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2")
        buf.write("\u010f\u0110\3\2\2\2\u0110\37\3\2\2\2\u0111\u010f\3\2")
        buf.write("\2\2\u0112\u0116\5\"\22\2\u0113\u0114\7C\2\2\u0114\u0115")
        buf.write("\7P\2\2\u0115\u0117\5d\63\2\u0116\u0113\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117!\3\2\2\2\u0118\u011c\5$\23\2\u0119")
        buf.write("\u011a\7_\2\2\u011a\u011b\7*\2\2\u011b\u011d\5d\63\2\u011c")
        buf.write("\u0119\3\2\2\2\u011c\u011d\3\2\2\2\u011d#\3\2\2\2\u011e")
        buf.write("\u0122\5&\24\2\u011f\u0120\7-\2\2\u0120\u0121\7*\2\2\u0121")
        buf.write("\u0123\5b\62\2\u0122\u011f\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123%\3\2\2\2\u0124\u0128\5(\25\2\u0125\u0126\7,\2\2")
        buf.write("\u0126\u0127\7*\2\2\u0127\u0129\5b\62\2\u0128\u0125\3")
        buf.write("\2\2\2\u0128\u0129\3\2\2\2\u0129\'\3\2\2\2\u012a\u012c")
        buf.write("\t\3\2\2\u012b\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d")
        buf.write("\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u0130\u0131\5*\26\2\u0131)\3\2\2")
        buf.write("\2\u0132\u0133\5\62\32\2\u0133+\3\2\2\2\u0134\u0135\t")
        buf.write("\7\2\2\u0135-\3\2\2\2\u0136\u0137\t\b\2\2\u0137/\3\2\2")
        buf.write("\2\u0138\u0139\t\t\2\2\u0139\61\3\2\2\2\u013a\u013c\7")
        buf.write("#\2\2\u013b\u013d\5\64\33\2\u013c\u013b\3\2\2\2\u013c")
        buf.write("\u013d\3\2\2\2\u013d\u0142\3\2\2\2\u013e\u013f\7$\2\2")
        buf.write("\u013f\u0142\5\64\33\2\u0140\u0142\5\64\33\2\u0141\u013a")
        buf.write("\3\2\2\2\u0141\u013e\3\2\2\2\u0141\u0140\3\2\2\2\u0142")
        buf.write("\63\3\2\2\2\u0143\u0148\5\66\34\2\u0144\u0145\t\n\2\2")
        buf.write("\u0145\u0147\5\66\34\2\u0146\u0144\3\2\2\2\u0147\u014a")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\65\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014e\5L\'\2\u014c")
        buf.write("\u014e\58\35\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\67\3\2\2\2\u014f\u0152\5@!\2\u0150\u0152\5:\36")
        buf.write("\2\u0151\u014f\3\2\2\2\u0151\u0150\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153\u0154\5N(\2\u01549\3\2\2\2\u0155\u0156")
        buf.write("\5<\37\2\u0156\u0157\5F$\2\u0157\u015a\3\2\2\2\u0158\u015a")
        buf.write("\5> \2\u0159\u0155\3\2\2\2\u0159\u0158\3\2\2\2\u015a;")
        buf.write("\3\2\2\2\u015b\u015c\7.\2\2\u015c\u016c\7\t\2\2\u015d")
        buf.write("\u015e\7\60\2\2\u015e\u016c\7\t\2\2\u015f\u0160\7+\2\2")
        buf.write("\u0160\u016c\7\t\2\2\u0161\u0162\7Z\2\2\u0162\u016c\7")
        buf.write("\t\2\2\u0163\u0164\7\61\2\2\u0164\u016c\7\t\2\2\u0165")
        buf.write("\u0166\7;\2\2\u0166\u016c\7\t\2\2\u0167\u0168\7:\2\2\u0168")
        buf.write("\u016c\7\t\2\2\u0169\u016a\7L\2\2\u016a\u016c\7\t\2\2")
        buf.write("\u016b\u015b\3\2\2\2\u016b\u015d\3\2\2\2\u016b\u015f\3")
        buf.write("\2\2\2\u016b\u0161\3\2\2\2\u016b\u0163\3\2\2\2\u016b\u0165")
        buf.write("\3\2\2\2\u016b\u0167\3\2\2\2\u016b\u0169\3\2\2\2\u016c")
        buf.write("=\3\2\2\2\u016d\u016f\7\3\2\2\u016e\u016d\3\2\2\2\u016e")
        buf.write("\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\5F$\2\u0171")
        buf.write("?\3\2\2\2\u0172\u0173\5B\"\2\u0173\u0174\5F$\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0177\5D#\2\u0176\u0172\3\2\2\2\u0176\u0175")
        buf.write("\3\2\2\2\u0177A\3\2\2\2\u0178\u0179\7R\2\2\u0179\u0183")
        buf.write("\7\t\2\2\u017a\u017b\7&\2\2\u017b\u0183\7\t\2\2\u017c")
        buf.write("\u017d\7T\2\2\u017d\u0183\7\t\2\2\u017e\u017f\7S\2\2\u017f")
        buf.write("\u0183\7\t\2\2\u0180\u0181\7\'\2\2\u0181\u0183\7\t\2\2")
        buf.write("\u0182\u0178\3\2\2\2\u0182\u017a\3\2\2\2\u0182\u017c\3")
        buf.write("\2\2\2\u0182\u017e\3\2\2\2\u0182\u0180\3\2\2\2\u0183C")
        buf.write("\3\2\2\2\u0184\u0185\7\16\2\2\u0185E\3\2\2\2\u0186\u0189")
        buf.write("\5l\67\2\u0187\u0189\5H%\2\u0188\u0186\3\2\2\2\u0188\u0187")
        buf.write("\3\2\2\2\u0189G\3\2\2\2\u018a\u018d\5\u008eH\2\u018b\u018d")
        buf.write("\5J&\2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2\u018dI")
        buf.write("\3\2\2\2\u018e\u0194\7%\2\2\u018f\u0190\7i\2\2\u0190\u0194")
        buf.write("\7\f\2\2\u0191\u0192\7\"\2\2\u0192\u0194\7i\2\2\u0193")
        buf.write("\u018e\3\2\2\2\u0193\u018f\3\2\2\2\u0193\u0191\3\2\2\2")
        buf.write("\u0194K\3\2\2\2\u0195\u0196\5R*\2\u0196\u0197\5N(\2\u0197")
        buf.write("M\3\2\2\2\u0198\u019a\5P)\2\u0199\u0198\3\2\2\2\u019a")
        buf.write("\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2")
        buf.write("\u019cO\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u019f\7\32\2")
        buf.write("\2\u019f\u01a0\5\4\3\2\u01a0\u01a1\7\5\2\2\u01a1Q\3\2")
        buf.write("\2\2\u01a2\u01a8\5T+\2\u01a3\u01a8\5X-\2\u01a4\u01a8\5")
        buf.write("\\/\2\u01a5\u01a8\5^\60\2\u01a6\u01a8\5`\61\2\u01a7\u01a2")
        buf.write("\3\2\2\2\u01a7\u01a3\3\2\2\2\u01a7\u01a4\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8S\3\2\2\2\u01a9")
        buf.write("\u01ac\5V,\2\u01aa\u01ac\7d\2\2\u01ab\u01a9\3\2\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01acU\3\2\2\2\u01ad\u01ae\t\13\2\2\u01ae")
        buf.write("W\3\2\2\2\u01af\u01b0\7\17\2\2\u01b0\u01b1\5Z.\2\u01b1")
        buf.write("Y\3\2\2\2\u01b2\u01b3\5\u008eH\2\u01b3[\3\2\2\2\u01b4")
        buf.write("\u01b6\7\34\2\2\u01b5\u01b7\5\4\3\2\u01b6\u01b5\3\2\2")
        buf.write("\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9")
        buf.write("\7\13\2\2\u01b9]\3\2\2\2\u01ba\u01bb\7\r\2\2\u01bb_\3")
        buf.write("\2\2\2\u01bc\u01bd\6\61\2\2\u01bd\u01be\5\u008eH\2\u01be")
        buf.write("\u01c7\7\34\2\2\u01bf\u01c4\5\6\4\2\u01c0\u01c1\7\n\2")
        buf.write("\2\u01c1\u01c3\5\6\4\2\u01c2\u01c0\3\2\2\2\u01c3\u01c6")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01bf\3\2\2\2")
        buf.write("\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\7")
        buf.write("\13\2\2\u01caa\3\2\2\2\u01cb\u01cd\5j\66\2\u01cc\u01ce")
        buf.write("\7!\2\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("c\3\2\2\2\u01cf\u01d0\7\66\2\2\u01d0\u01d1\7\34\2\2\u01d1")
        buf.write("\u01d7\7\13\2\2\u01d2\u01d4\5h\65\2\u01d3\u01d5\5f\64")
        buf.write("\2\u01d4\u01d3\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7")
        buf.write("\3\2\2\2\u01d6\u01cf\3\2\2\2\u01d6\u01d2\3\2\2\2\u01d7")
        buf.write("e\3\2\2\2\u01d8\u01d9\t\f\2\2\u01d9g\3\2\2\2\u01da\u01e0")
        buf.write("\5l\67\2\u01db\u01dc\7F\2\2\u01dc\u01dd\7\34\2\2\u01dd")
        buf.write("\u01e0\7\13\2\2\u01de\u01e0\5j\66\2\u01df\u01da\3\2\2")
        buf.write("\2\u01df\u01db\3\2\2\2\u01df\u01de\3\2\2\2\u01e0i\3\2")
        buf.write("\2\2\u01e1\u01e2\5\u008eH\2\u01e2k\3\2\2\2\u01e3\u01ed")
        buf.write("\5p9\2\u01e4\u01ed\5\u0080A\2\u01e5\u01ed\5x=\2\u01e6")
        buf.write("\u01ed\5\u0084C\2\u01e7\u01ed\5|?\2\u01e8\u01ed\5v<\2")
        buf.write("\u01e9\u01ed\5t;\2\u01ea\u01ed\5r:\2\u01eb\u01ed\5n8\2")
        buf.write("\u01ec\u01e3\3\2\2\2\u01ec\u01e4\3\2\2\2\u01ec\u01e5\3")
        buf.write("\2\2\2\u01ec\u01e6\3\2\2\2\u01ec\u01e7\3\2\2\2\u01ec\u01e8")
        buf.write("\3\2\2\2\u01ec\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01edm\3\2\2\2\u01ee\u01ef\7O\2\2\u01ef")
        buf.write("\u01f0\7\34\2\2\u01f0\u01f1\7\13\2\2\u01f1o\3\2\2\2\u01f2")
        buf.write("\u01f3\7\63\2\2\u01f3\u01f6\7\34\2\2\u01f4\u01f7\5\u0080")
        buf.write("A\2\u01f5\u01f7\5\u0084C\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2\u01f8")
        buf.write("\u01f9\7\13\2\2\u01f9q\3\2\2\2\u01fa\u01fb\7\\\2\2\u01fb")
        buf.write("\u01fc\7\34\2\2\u01fc\u01fd\7\13\2\2\u01fds\3\2\2\2\u01fe")
        buf.write("\u01ff\7/\2\2\u01ff\u0200\7\34\2\2\u0200\u0201\7\13\2")
        buf.write("\2\u0201u\3\2\2\2\u0202\u0203\7U\2\2\u0203\u0205\7\34")
        buf.write("\2\2\u0204\u0206\t\r\2\2\u0205\u0204\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208\7\13\2\2\u0208")
        buf.write("w\3\2\2\2\u0209\u020a\7+\2\2\u020a\u0210\7\34\2\2\u020b")
        buf.write("\u020e\5z>\2\u020c\u020d\7\n\2\2\u020d\u020f\5\u008cG")
        buf.write("\2\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211")
        buf.write("\3\2\2\2\u0210\u020b\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0212\3\2\2\2\u0212\u0213\7\13\2\2\u0213y\3\2\2\2\u0214")
        buf.write("\u0217\5\u0088E\2\u0215\u0217\7%\2\2\u0216\u0214\3\2\2")
        buf.write("\2\u0216\u0215\3\2\2\2\u0217{\3\2\2\2\u0218\u0219\7X\2")
        buf.write("\2\u0219\u021a\7\34\2\2\u021a\u021b\5~@\2\u021b\u021c")
        buf.write("\7\13\2\2\u021c}\3\2\2\2\u021d\u021e\5\u0088E\2\u021e")
        buf.write("\177\3\2\2\2\u021f\u0220\7\64\2\2\u0220\u0229\7\34\2\2")
        buf.write("\u0221\u0227\5\u0082B\2\u0222\u0223\7\n\2\2\u0223\u0225")
        buf.write("\5\u008cG\2\u0224\u0226\7!\2\2\u0225\u0224\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0226\u0228\3\2\2\2\u0227\u0222\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0221\3")
        buf.write("\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u022c")
        buf.write("\7\13\2\2\u022c\u0081\3\2\2\2\u022d\u0230\5\u008aF\2\u022e")
        buf.write("\u0230\7%\2\2\u022f\u022d\3\2\2\2\u022f\u022e\3\2\2\2")
        buf.write("\u0230\u0083\3\2\2\2\u0231\u0232\7Y\2\2\u0232\u0233\7")
        buf.write("\34\2\2\u0233\u0234\5\u0086D\2\u0234\u0235\7\13\2\2\u0235")
        buf.write("\u0085\3\2\2\2\u0236\u0237\5\u008aF\2\u0237\u0087\3\2")
        buf.write("\2\2\u0238\u0239\5\u008eH\2\u0239\u0089\3\2\2\2\u023a")
        buf.write("\u023b\5\u008eH\2\u023b\u008b\3\2\2\2\u023c\u023d\5\u008e")
        buf.write("H\2\u023d\u008d\3\2\2\2\u023e\u023f\t\16\2\2\u023f\u008f")
        buf.write("\3\2\2\2\u0240\u0241\5\4\3\2\u0241\u0242\7k\2\2\u0242")
        buf.write("\u0244\3\2\2\2\u0243\u0240\3\2\2\2\u0244\u0245\3\2\2\2")
        buf.write("\u0245\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\3")
        buf.write("\2\2\2\u0247\u0248\7\2\2\3\u0248\u0091\3\2\2\2\66\u009a")
        buf.write("\u00a1\u00b4\u00c4\u00d8\u00e0\u00e7\u00eb\u00f0\u00f7")
        buf.write("\u00ff\u0107\u010f\u0116\u011c\u0122\u0128\u012d\u013c")
        buf.write("\u0141\u0148\u014d\u0151\u0159\u016b\u016e\u0176\u0182")
        buf.write("\u0188\u018c\u0193\u019b\u01a7\u01ab\u01b6\u01c4\u01c7")
        buf.write("\u01cd\u01d4\u01d6\u01df\u01ec\u01f6\u0205\u020e\u0210")
        buf.write("\u0216\u0225\u0227\u0229\u022f\u0245")
        return buf.getvalue()


class XPath20Parser ( Parser ):

    grammarFileName = "XPath20.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'!'", "']'", "'}'", "':='", "':'", 
                     "'::'", "','", "')'", "':*'", "'.'", "'..'", "'$'", 
                     "'=>'", "'='", "'>='", "'>>'", "'>'", "'<='", "'<<'", 
                     "'<'", "'-'", "'!='", "'['", "'{'", "'('", "'|'", "'+'", 
                     "'#'", "'||'", "'?'", "'*:'", "'/'", "'//'", "'*'", 
                     "'ancestor'", "'ancestor-or-self'", "'and'", "'array'", 
                     "'as'", "'attribute'", "'cast'", "'castable'", "'child'", 
                     "'comment'", "'descendant'", "'descendant-or-self'", 
                     "'div'", "'document-node'", "'element'", "'else'", 
                     "'empty-sequence'", "'eq'", "'every'", "'except'", 
                     "'following'", "'following-sibling'", "'for'", "'function'", 
                     "'ge'", "'gt'", "'idiv'", "'if'", "'in'", "'instance'", 
                     "'intersect'", "'is'", "'item'", "'le'", "'let'", "'lt'", 
                     "'map'", "'mod'", "'namespace'", "'namespace-node'", 
                     "'ne'", "'node'", "'of'", "'or'", "'parent'", "'preceding'", 
                     "'preceding-sibling'", "'processing-instruction'", 
                     "'return'", "'satisfies'", "'schema-attribute'", "'schema-element'", 
                     "'self'", "'some'", "'text'", "'then'", "'to'", "'treat'", 
                     "'union'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'" ]

    symbolicNames = [ "<INVALID>", "AT", "BANG", "CB", "CC", "CEQ", "COLON", 
                      "COLONCOLON", "COMMA", "CP", "CS", "D", "DD", "DOLLAR", 
                      "EG", "EQ", "GE", "GG", "GT", "LE", "LL", "LT", "MINUS", 
                      "NE", "OB", "OC", "OP", "P", "PLUS", "POUND", "PP", 
                      "QM", "SC", "SLASH", "SS", "STAR", "KW_ANCESTOR", 
                      "KW_ANCESTOR_OR_SELF", "KW_AND", "KW_ARRAY", "KW_AS", 
                      "KW_ATTRIBUTE", "KW_CAST", "KW_CASTABLE", "KW_CHILD", 
                      "KW_COMMENT", "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", 
                      "KW_DIV", "KW_DOCUMENT_NODE", "KW_ELEMENT", "KW_ELSE", 
                      "KW_EMPTY_SEQUENCE", "KW_EQ", "KW_EVERY", "KW_EXCEPT", 
                      "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", "KW_FOR", 
                      "KW_FUNCTION", "KW_GE", "KW_GT", "KW_IDIV", "KW_IF", 
                      "KW_IN", "KW_INSTANCE", "KW_INTERSECT", "KW_IS", "KW_ITEM", 
                      "KW_LE", "KW_LET", "KW_LT", "KW_MAP", "KW_MOD", "KW_NAMESPACE", 
                      "KW_NAMESPACE_NODE", "KW_NE", "KW_NODE", "KW_OF", 
                      "KW_OR", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                      "KW_PROCESSING_INSTRUCTION", "KW_RETURN", "KW_SATISFIES", 
                      "KW_SCHEMA_ATTRIBUTE", "KW_SCHEMA_ELEMENT", "KW_SELF", 
                      "KW_SOME", "KW_TEXT", "KW_THEN", "KW_TO", "KW_TREAT", 
                      "KW_UNION", "IntegerLiteral", "DecimalLiteral", "DoubleLiteral", 
                      "StringLiteral", "URIQualifiedName", "BracedURILiteral", 
                      "Comment", "QName", "NCName", "Whitespace", "SEMI" ]

    RULE_xpath = 0
    RULE_expr = 1
    RULE_exprsingle = 2
    RULE_forexpr = 3
    RULE_simpleforclause = 4
    RULE_quantifiedexpr = 5
    RULE_ifexpr = 6
    RULE_orexpr = 7
    RULE_andexpr = 8
    RULE_comparisonexpr = 9
    RULE_rangeexpr = 10
    RULE_additiveexpr = 11
    RULE_multiplicativeexpr = 12
    RULE_unionexpr = 13
    RULE_intersectexceptexpr = 14
    RULE_instanceofexpr = 15
    RULE_treatexpr = 16
    RULE_castableexpr = 17
    RULE_castexpr = 18
    RULE_unaryexpr = 19
    RULE_valueexpr = 20
    RULE_generalcomp = 21
    RULE_valuecomp = 22
    RULE_nodecomp = 23
    RULE_pathexpr = 24
    RULE_relativepathexpr = 25
    RULE_stepexpr = 26
    RULE_axisstep = 27
    RULE_forwardstep = 28
    RULE_forwardaxis = 29
    RULE_abbrevforwardstep = 30
    RULE_reversestep = 31
    RULE_reverseaxis = 32
    RULE_abbrevreversestep = 33
    RULE_nodetest = 34
    RULE_nametest = 35
    RULE_wildcard = 36
    RULE_filterexpr = 37
    RULE_predicatelist = 38
    RULE_predicate = 39
    RULE_primaryexpr = 40
    RULE_literal = 41
    RULE_numericliteral = 42
    RULE_varref = 43
    RULE_varname = 44
    RULE_parenthesizedexpr = 45
    RULE_contextitemexpr = 46
    RULE_functioncall = 47
    RULE_singletype = 48
    RULE_sequencetype = 49
    RULE_occurrenceindicator = 50
    RULE_itemtype = 51
    RULE_atomictype = 52
    RULE_kindtest = 53
    RULE_anykindtest = 54
    RULE_documenttest = 55
    RULE_texttest = 56
    RULE_commenttest = 57
    RULE_pitest = 58
    RULE_attributetest = 59
    RULE_attribnameorwildcard = 60
    RULE_schemaattributetest = 61
    RULE_attributedeclaration = 62
    RULE_elementtest = 63
    RULE_elementnameorwildcard = 64
    RULE_schemaelementtest = 65
    RULE_elementdeclaration = 66
    RULE_attributename = 67
    RULE_elementname = 68
    RULE_typename_ = 69
    RULE_qname = 70
    RULE_auxilary = 71

    ruleNames =  [ "xpath", "expr", "exprsingle", "forexpr", "simpleforclause", 
                   "quantifiedexpr", "ifexpr", "orexpr", "andexpr", "comparisonexpr", 
                   "rangeexpr", "additiveexpr", "multiplicativeexpr", "unionexpr", 
                   "intersectexceptexpr", "instanceofexpr", "treatexpr", 
                   "castableexpr", "castexpr", "unaryexpr", "valueexpr", 
                   "generalcomp", "valuecomp", "nodecomp", "pathexpr", "relativepathexpr", 
                   "stepexpr", "axisstep", "forwardstep", "forwardaxis", 
                   "abbrevforwardstep", "reversestep", "reverseaxis", "abbrevreversestep", 
                   "nodetest", "nametest", "wildcard", "filterexpr", "predicatelist", 
                   "predicate", "primaryexpr", "literal", "numericliteral", 
                   "varref", "varname", "parenthesizedexpr", "contextitemexpr", 
                   "functioncall", "singletype", "sequencetype", "occurrenceindicator", 
                   "itemtype", "atomictype", "kindtest", "anykindtest", 
                   "documenttest", "texttest", "commenttest", "pitest", 
                   "attributetest", "attribnameorwildcard", "schemaattributetest", 
                   "attributedeclaration", "elementtest", "elementnameorwildcard", 
                   "schemaelementtest", "elementdeclaration", "attributename", 
                   "elementname", "typename_", "qname", "auxilary" ]

    EOF = Token.EOF
    AT=1
    BANG=2
    CB=3
    CC=4
    CEQ=5
    COLON=6
    COLONCOLON=7
    COMMA=8
    CP=9
    CS=10
    D=11
    DD=12
    DOLLAR=13
    EG=14
    EQ=15
    GE=16
    GG=17
    GT=18
    LE=19
    LL=20
    LT=21
    MINUS=22
    NE=23
    OB=24
    OC=25
    OP=26
    P=27
    PLUS=28
    POUND=29
    PP=30
    QM=31
    SC=32
    SLASH=33
    SS=34
    STAR=35
    KW_ANCESTOR=36
    KW_ANCESTOR_OR_SELF=37
    KW_AND=38
    KW_ARRAY=39
    KW_AS=40
    KW_ATTRIBUTE=41
    KW_CAST=42
    KW_CASTABLE=43
    KW_CHILD=44
    KW_COMMENT=45
    KW_DESCENDANT=46
    KW_DESCENDANT_OR_SELF=47
    KW_DIV=48
    KW_DOCUMENT_NODE=49
    KW_ELEMENT=50
    KW_ELSE=51
    KW_EMPTY_SEQUENCE=52
    KW_EQ=53
    KW_EVERY=54
    KW_EXCEPT=55
    KW_FOLLOWING=56
    KW_FOLLOWING_SIBLING=57
    KW_FOR=58
    KW_FUNCTION=59
    KW_GE=60
    KW_GT=61
    KW_IDIV=62
    KW_IF=63
    KW_IN=64
    KW_INSTANCE=65
    KW_INTERSECT=66
    KW_IS=67
    KW_ITEM=68
    KW_LE=69
    KW_LET=70
    KW_LT=71
    KW_MAP=72
    KW_MOD=73
    KW_NAMESPACE=74
    KW_NAMESPACE_NODE=75
    KW_NE=76
    KW_NODE=77
    KW_OF=78
    KW_OR=79
    KW_PARENT=80
    KW_PRECEDING=81
    KW_PRECEDING_SIBLING=82
    KW_PROCESSING_INSTRUCTION=83
    KW_RETURN=84
    KW_SATISFIES=85
    KW_SCHEMA_ATTRIBUTE=86
    KW_SCHEMA_ELEMENT=87
    KW_SELF=88
    KW_SOME=89
    KW_TEXT=90
    KW_THEN=91
    KW_TO=92
    KW_TREAT=93
    KW_UNION=94
    IntegerLiteral=95
    DecimalLiteral=96
    DoubleLiteral=97
    StringLiteral=98
    URIQualifiedName=99
    BracedURILiteral=100
    Comment=101
    QName=102
    NCName=103
    Whitespace=104
    SEMI=105

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class XpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(XPath20Parser.ExprContext,0)


        def EOF(self):
            return self.getToken(XPath20Parser.EOF, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_xpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXpath" ):
                listener.enterXpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXpath" ):
                listener.exitXpath(self)




    def xpath(self):

        localctx = XPath20Parser.XpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.expr()
            self.state = 145
            self.match(XPath20Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprsingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ExprsingleContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ExprsingleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.COMMA)
            else:
                return self.getToken(XPath20Parser.COMMA, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = XPath20Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.exprsingle()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.COMMA:
                self.state = 148
                self.match(XPath20Parser.COMMA)
                self.state = 149
                self.exprsingle()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsingleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forexpr(self):
            return self.getTypedRuleContext(XPath20Parser.ForexprContext,0)


        def quantifiedexpr(self):
            return self.getTypedRuleContext(XPath20Parser.QuantifiedexprContext,0)


        def ifexpr(self):
            return self.getTypedRuleContext(XPath20Parser.IfexprContext,0)


        def orexpr(self):
            return self.getTypedRuleContext(XPath20Parser.OrexprContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_exprsingle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprsingle" ):
                listener.enterExprsingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprsingle" ):
                listener.exitExprsingle(self)




    def exprsingle(self):

        localctx = XPath20Parser.ExprsingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exprsingle)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.forexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.quantifiedexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.ifexpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.orexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleforclause(self):
            return self.getTypedRuleContext(XPath20Parser.SimpleforclauseContext,0)


        def KW_RETURN(self):
            return self.getToken(XPath20Parser.KW_RETURN, 0)

        def exprsingle(self):
            return self.getTypedRuleContext(XPath20Parser.ExprsingleContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_forexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForexpr" ):
                listener.enterForexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForexpr" ):
                listener.exitForexpr(self)




    def forexpr(self):

        localctx = XPath20Parser.ForexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_forexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.simpleforclause()
            self.state = 162
            self.match(XPath20Parser.KW_RETURN)
            self.state = 163
            self.exprsingle()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleforclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(XPath20Parser.KW_FOR, 0)

        def DOLLAR(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.DOLLAR)
            else:
                return self.getToken(XPath20Parser.DOLLAR, i)

        def varname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.VarnameContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.VarnameContext,i)


        def KW_IN(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_IN)
            else:
                return self.getToken(XPath20Parser.KW_IN, i)

        def exprsingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ExprsingleContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ExprsingleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.COMMA)
            else:
                return self.getToken(XPath20Parser.COMMA, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_simpleforclause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleforclause" ):
                listener.enterSimpleforclause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleforclause" ):
                listener.exitSimpleforclause(self)




    def simpleforclause(self):

        localctx = XPath20Parser.SimpleforclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simpleforclause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(XPath20Parser.KW_FOR)
            self.state = 166
            self.match(XPath20Parser.DOLLAR)
            self.state = 167
            self.varname()
            self.state = 168
            self.match(XPath20Parser.KW_IN)
            self.state = 169
            self.exprsingle()
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.COMMA:
                self.state = 170
                self.match(XPath20Parser.COMMA)
                self.state = 171
                self.match(XPath20Parser.DOLLAR)
                self.state = 172
                self.varname()
                self.state = 173
                self.match(XPath20Parser.KW_IN)
                self.state = 174
                self.exprsingle()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantifiedexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.DOLLAR)
            else:
                return self.getToken(XPath20Parser.DOLLAR, i)

        def varname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.VarnameContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.VarnameContext,i)


        def KW_IN(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_IN)
            else:
                return self.getToken(XPath20Parser.KW_IN, i)

        def exprsingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ExprsingleContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ExprsingleContext,i)


        def KW_SATISFIES(self):
            return self.getToken(XPath20Parser.KW_SATISFIES, 0)

        def KW_SOME(self):
            return self.getToken(XPath20Parser.KW_SOME, 0)

        def KW_EVERY(self):
            return self.getToken(XPath20Parser.KW_EVERY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.COMMA)
            else:
                return self.getToken(XPath20Parser.COMMA, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_quantifiedexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantifiedexpr" ):
                listener.enterQuantifiedexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantifiedexpr" ):
                listener.exitQuantifiedexpr(self)




    def quantifiedexpr(self):

        localctx = XPath20Parser.QuantifiedexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_quantifiedexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==XPath20Parser.KW_EVERY or _la==XPath20Parser.KW_SOME):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 182
            self.match(XPath20Parser.DOLLAR)
            self.state = 183
            self.varname()
            self.state = 184
            self.match(XPath20Parser.KW_IN)
            self.state = 185
            self.exprsingle()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.COMMA:
                self.state = 186
                self.match(XPath20Parser.COMMA)
                self.state = 187
                self.match(XPath20Parser.DOLLAR)
                self.state = 188
                self.varname()
                self.state = 189
                self.match(XPath20Parser.KW_IN)
                self.state = 190
                self.exprsingle()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 197
            self.match(XPath20Parser.KW_SATISFIES)
            self.state = 198
            self.exprsingle()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(XPath20Parser.KW_IF, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def expr(self):
            return self.getTypedRuleContext(XPath20Parser.ExprContext,0)


        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def KW_THEN(self):
            return self.getToken(XPath20Parser.KW_THEN, 0)

        def exprsingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ExprsingleContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ExprsingleContext,i)


        def KW_ELSE(self):
            return self.getToken(XPath20Parser.KW_ELSE, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_ifexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfexpr" ):
                listener.enterIfexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfexpr" ):
                listener.exitIfexpr(self)




    def ifexpr(self):

        localctx = XPath20Parser.IfexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(XPath20Parser.KW_IF)
            self.state = 201
            self.match(XPath20Parser.OP)
            self.state = 202
            self.expr()
            self.state = 203
            self.match(XPath20Parser.CP)
            self.state = 204
            self.match(XPath20Parser.KW_THEN)
            self.state = 205
            self.exprsingle()
            self.state = 206
            self.match(XPath20Parser.KW_ELSE)
            self.state = 207
            self.exprsingle()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.AndexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.AndexprContext,i)


        def KW_OR(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_OR)
            else:
                return self.getToken(XPath20Parser.KW_OR, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_orexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrexpr" ):
                listener.enterOrexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrexpr" ):
                listener.exitOrexpr(self)




    def orexpr(self):

        localctx = XPath20Parser.OrexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_orexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.andexpr()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.KW_OR:
                self.state = 210
                self.match(XPath20Parser.KW_OR)
                self.state = 211
                self.andexpr()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparisonexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ComparisonexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ComparisonexprContext,i)


        def KW_AND(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_AND)
            else:
                return self.getToken(XPath20Parser.KW_AND, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_andexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndexpr" ):
                listener.enterAndexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndexpr" ):
                listener.exitAndexpr(self)




    def andexpr(self):

        localctx = XPath20Parser.AndexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_andexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.comparisonexpr()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.KW_AND:
                self.state = 218
                self.match(XPath20Parser.KW_AND)
                self.state = 219
                self.comparisonexpr()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rangeexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.RangeexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.RangeexprContext,i)


        def valuecomp(self):
            return self.getTypedRuleContext(XPath20Parser.ValuecompContext,0)


        def generalcomp(self):
            return self.getTypedRuleContext(XPath20Parser.GeneralcompContext,0)


        def nodecomp(self):
            return self.getTypedRuleContext(XPath20Parser.NodecompContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_comparisonexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonexpr" ):
                listener.enterComparisonexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonexpr" ):
                listener.exitComparisonexpr(self)




    def comparisonexpr(self):

        localctx = XPath20Parser.ComparisonexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparisonexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.rangeexpr()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 15)) & ~0x3f) == 0 and ((1 << (_la - 15)) & ((1 << (XPath20Parser.EQ - 15)) | (1 << (XPath20Parser.GE - 15)) | (1 << (XPath20Parser.GG - 15)) | (1 << (XPath20Parser.GT - 15)) | (1 << (XPath20Parser.LE - 15)) | (1 << (XPath20Parser.LL - 15)) | (1 << (XPath20Parser.LT - 15)) | (1 << (XPath20Parser.NE - 15)) | (1 << (XPath20Parser.KW_EQ - 15)) | (1 << (XPath20Parser.KW_GE - 15)) | (1 << (XPath20Parser.KW_GT - 15)) | (1 << (XPath20Parser.KW_IS - 15)) | (1 << (XPath20Parser.KW_LE - 15)) | (1 << (XPath20Parser.KW_LT - 15)) | (1 << (XPath20Parser.KW_NE - 15)))) != 0):
                self.state = 229
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [XPath20Parser.KW_EQ, XPath20Parser.KW_GE, XPath20Parser.KW_GT, XPath20Parser.KW_LE, XPath20Parser.KW_LT, XPath20Parser.KW_NE]:
                    self.state = 226
                    self.valuecomp()
                    pass
                elif token in [XPath20Parser.EQ, XPath20Parser.GE, XPath20Parser.GT, XPath20Parser.LE, XPath20Parser.LT, XPath20Parser.NE]:
                    self.state = 227
                    self.generalcomp()
                    pass
                elif token in [XPath20Parser.GG, XPath20Parser.LL, XPath20Parser.KW_IS]:
                    self.state = 228
                    self.nodecomp()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 231
                self.rangeexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RangeexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.AdditiveexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.AdditiveexprContext,i)


        def KW_TO(self):
            return self.getToken(XPath20Parser.KW_TO, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_rangeexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeexpr" ):
                listener.enterRangeexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeexpr" ):
                listener.exitRangeexpr(self)




    def rangeexpr(self):

        localctx = XPath20Parser.RangeexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_rangeexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.additiveexpr()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.KW_TO:
                self.state = 236
                self.match(XPath20Parser.KW_TO)
                self.state = 237
                self.additiveexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.MultiplicativeexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.MultiplicativeexprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.PLUS)
            else:
                return self.getToken(XPath20Parser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.MINUS)
            else:
                return self.getToken(XPath20Parser.MINUS, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_additiveexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveexpr" ):
                listener.enterAdditiveexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveexpr" ):
                listener.exitAdditiveexpr(self)




    def additiveexpr(self):

        localctx = XPath20Parser.AdditiveexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_additiveexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.multiplicativeexpr()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.MINUS or _la==XPath20Parser.PLUS:
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==XPath20Parser.MINUS or _la==XPath20Parser.PLUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.multiplicativeexpr()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unionexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.UnionexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.UnionexprContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.STAR)
            else:
                return self.getToken(XPath20Parser.STAR, i)

        def KW_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_DIV)
            else:
                return self.getToken(XPath20Parser.KW_DIV, i)

        def KW_IDIV(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_IDIV)
            else:
                return self.getToken(XPath20Parser.KW_IDIV, i)

        def KW_MOD(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_MOD)
            else:
                return self.getToken(XPath20Parser.KW_MOD, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_multiplicativeexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeexpr" ):
                listener.enterMultiplicativeexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeexpr" ):
                listener.exitMultiplicativeexpr(self)




    def multiplicativeexpr(self):

        localctx = XPath20Parser.MultiplicativeexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_multiplicativeexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.unionexpr()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & ((1 << (XPath20Parser.STAR - 35)) | (1 << (XPath20Parser.KW_DIV - 35)) | (1 << (XPath20Parser.KW_IDIV - 35)) | (1 << (XPath20Parser.KW_MOD - 35)))) != 0):
                self.state = 249
                _la = self._input.LA(1)
                if not(((((_la - 35)) & ~0x3f) == 0 and ((1 << (_la - 35)) & ((1 << (XPath20Parser.STAR - 35)) | (1 << (XPath20Parser.KW_DIV - 35)) | (1 << (XPath20Parser.KW_IDIV - 35)) | (1 << (XPath20Parser.KW_MOD - 35)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.unionexpr()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intersectexceptexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.IntersectexceptexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.IntersectexceptexprContext,i)


        def KW_UNION(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_UNION)
            else:
                return self.getToken(XPath20Parser.KW_UNION, i)

        def P(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.P)
            else:
                return self.getToken(XPath20Parser.P, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_unionexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionexpr" ):
                listener.enterUnionexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionexpr" ):
                listener.exitUnionexpr(self)




    def unionexpr(self):

        localctx = XPath20Parser.UnionexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_unionexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.intersectexceptexpr()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.P or _la==XPath20Parser.KW_UNION:
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==XPath20Parser.P or _la==XPath20Parser.KW_UNION):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 258
                self.intersectexceptexpr()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntersectexceptexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceofexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.InstanceofexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.InstanceofexprContext,i)


        def KW_INTERSECT(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_INTERSECT)
            else:
                return self.getToken(XPath20Parser.KW_INTERSECT, i)

        def KW_EXCEPT(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.KW_EXCEPT)
            else:
                return self.getToken(XPath20Parser.KW_EXCEPT, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_intersectexceptexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntersectexceptexpr" ):
                listener.enterIntersectexceptexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntersectexceptexpr" ):
                listener.exitIntersectexceptexpr(self)




    def intersectexceptexpr(self):

        localctx = XPath20Parser.IntersectexceptexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_intersectexceptexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.instanceofexpr()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.KW_EXCEPT or _la==XPath20Parser.KW_INTERSECT:
                self.state = 265
                _la = self._input.LA(1)
                if not(_la==XPath20Parser.KW_EXCEPT or _la==XPath20Parser.KW_INTERSECT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self.instanceofexpr()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceofexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def treatexpr(self):
            return self.getTypedRuleContext(XPath20Parser.TreatexprContext,0)


        def KW_INSTANCE(self):
            return self.getToken(XPath20Parser.KW_INSTANCE, 0)

        def KW_OF(self):
            return self.getToken(XPath20Parser.KW_OF, 0)

        def sequencetype(self):
            return self.getTypedRuleContext(XPath20Parser.SequencetypeContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_instanceofexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceofexpr" ):
                listener.enterInstanceofexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceofexpr" ):
                listener.exitInstanceofexpr(self)




    def instanceofexpr(self):

        localctx = XPath20Parser.InstanceofexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_instanceofexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.treatexpr()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.KW_INSTANCE:
                self.state = 273
                self.match(XPath20Parser.KW_INSTANCE)
                self.state = 274
                self.match(XPath20Parser.KW_OF)
                self.state = 275
                self.sequencetype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TreatexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def castableexpr(self):
            return self.getTypedRuleContext(XPath20Parser.CastableexprContext,0)


        def KW_TREAT(self):
            return self.getToken(XPath20Parser.KW_TREAT, 0)

        def KW_AS(self):
            return self.getToken(XPath20Parser.KW_AS, 0)

        def sequencetype(self):
            return self.getTypedRuleContext(XPath20Parser.SequencetypeContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_treatexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTreatexpr" ):
                listener.enterTreatexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTreatexpr" ):
                listener.exitTreatexpr(self)




    def treatexpr(self):

        localctx = XPath20Parser.TreatexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_treatexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.castableexpr()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.KW_TREAT:
                self.state = 279
                self.match(XPath20Parser.KW_TREAT)
                self.state = 280
                self.match(XPath20Parser.KW_AS)
                self.state = 281
                self.sequencetype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastableexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def castexpr(self):
            return self.getTypedRuleContext(XPath20Parser.CastexprContext,0)


        def KW_CASTABLE(self):
            return self.getToken(XPath20Parser.KW_CASTABLE, 0)

        def KW_AS(self):
            return self.getToken(XPath20Parser.KW_AS, 0)

        def singletype(self):
            return self.getTypedRuleContext(XPath20Parser.SingletypeContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_castableexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastableexpr" ):
                listener.enterCastableexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastableexpr" ):
                listener.exitCastableexpr(self)




    def castableexpr(self):

        localctx = XPath20Parser.CastableexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_castableexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.castexpr()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.KW_CASTABLE:
                self.state = 285
                self.match(XPath20Parser.KW_CASTABLE)
                self.state = 286
                self.match(XPath20Parser.KW_AS)
                self.state = 287
                self.singletype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryexpr(self):
            return self.getTypedRuleContext(XPath20Parser.UnaryexprContext,0)


        def KW_CAST(self):
            return self.getToken(XPath20Parser.KW_CAST, 0)

        def KW_AS(self):
            return self.getToken(XPath20Parser.KW_AS, 0)

        def singletype(self):
            return self.getTypedRuleContext(XPath20Parser.SingletypeContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_castexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastexpr" ):
                listener.enterCastexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastexpr" ):
                listener.exitCastexpr(self)




    def castexpr(self):

        localctx = XPath20Parser.CastexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_castexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.unaryexpr()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.KW_CAST:
                self.state = 291
                self.match(XPath20Parser.KW_CAST)
                self.state = 292
                self.match(XPath20Parser.KW_AS)
                self.state = 293
                self.singletype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valueexpr(self):
            return self.getTypedRuleContext(XPath20Parser.ValueexprContext,0)


        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.MINUS)
            else:
                return self.getToken(XPath20Parser.MINUS, i)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.PLUS)
            else:
                return self.getToken(XPath20Parser.PLUS, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_unaryexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryexpr" ):
                listener.enterUnaryexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryexpr" ):
                listener.exitUnaryexpr(self)




    def unaryexpr(self):

        localctx = XPath20Parser.UnaryexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_unaryexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 296
                    _la = self._input.LA(1)
                    if not(_la==XPath20Parser.MINUS or _la==XPath20Parser.PLUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 302
            self.valueexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pathexpr(self):
            return self.getTypedRuleContext(XPath20Parser.PathexprContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_valueexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueexpr" ):
                listener.enterValueexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueexpr" ):
                listener.exitValueexpr(self)




    def valueexpr(self):

        localctx = XPath20Parser.ValueexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_valueexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.pathexpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneralcompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(XPath20Parser.EQ, 0)

        def NE(self):
            return self.getToken(XPath20Parser.NE, 0)

        def LT(self):
            return self.getToken(XPath20Parser.LT, 0)

        def LE(self):
            return self.getToken(XPath20Parser.LE, 0)

        def GT(self):
            return self.getToken(XPath20Parser.GT, 0)

        def GE(self):
            return self.getToken(XPath20Parser.GE, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_generalcomp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneralcomp" ):
                listener.enterGeneralcomp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneralcomp" ):
                listener.exitGeneralcomp(self)




    def generalcomp(self):

        localctx = XPath20Parser.GeneralcompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_generalcomp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XPath20Parser.EQ) | (1 << XPath20Parser.GE) | (1 << XPath20Parser.GT) | (1 << XPath20Parser.LE) | (1 << XPath20Parser.LT) | (1 << XPath20Parser.NE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValuecompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_EQ(self):
            return self.getToken(XPath20Parser.KW_EQ, 0)

        def KW_NE(self):
            return self.getToken(XPath20Parser.KW_NE, 0)

        def KW_LT(self):
            return self.getToken(XPath20Parser.KW_LT, 0)

        def KW_LE(self):
            return self.getToken(XPath20Parser.KW_LE, 0)

        def KW_GT(self):
            return self.getToken(XPath20Parser.KW_GT, 0)

        def KW_GE(self):
            return self.getToken(XPath20Parser.KW_GE, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_valuecomp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValuecomp" ):
                listener.enterValuecomp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValuecomp" ):
                listener.exitValuecomp(self)




    def valuecomp(self):

        localctx = XPath20Parser.ValuecompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_valuecomp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & ((1 << (XPath20Parser.KW_EQ - 53)) | (1 << (XPath20Parser.KW_GE - 53)) | (1 << (XPath20Parser.KW_GT - 53)) | (1 << (XPath20Parser.KW_LE - 53)) | (1 << (XPath20Parser.KW_LT - 53)) | (1 << (XPath20Parser.KW_NE - 53)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodecompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IS(self):
            return self.getToken(XPath20Parser.KW_IS, 0)

        def LL(self):
            return self.getToken(XPath20Parser.LL, 0)

        def GG(self):
            return self.getToken(XPath20Parser.GG, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_nodecomp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodecomp" ):
                listener.enterNodecomp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodecomp" ):
                listener.exitNodecomp(self)




    def nodecomp(self):

        localctx = XPath20Parser.NodecompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_nodecomp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            _la = self._input.LA(1)
            if not(((((_la - 17)) & ~0x3f) == 0 and ((1 << (_la - 17)) & ((1 << (XPath20Parser.GG - 17)) | (1 << (XPath20Parser.LL - 17)) | (1 << (XPath20Parser.KW_IS - 17)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(XPath20Parser.SLASH, 0)

        def relativepathexpr(self):
            return self.getTypedRuleContext(XPath20Parser.RelativepathexprContext,0)


        def SS(self):
            return self.getToken(XPath20Parser.SS, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_pathexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathexpr" ):
                listener.enterPathexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathexpr" ):
                listener.exitPathexpr(self)




    def pathexpr(self):

        localctx = XPath20Parser.PathexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_pathexpr)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(XPath20Parser.SLASH)
                self.state = 314
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 313
                    self.relativepathexpr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(XPath20Parser.SS)
                self.state = 317
                self.relativepathexpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 318
                self.relativepathexpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelativepathexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stepexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.StepexprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.StepexprContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.SLASH)
            else:
                return self.getToken(XPath20Parser.SLASH, i)

        def SS(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.SS)
            else:
                return self.getToken(XPath20Parser.SS, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_relativepathexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelativepathexpr" ):
                listener.enterRelativepathexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelativepathexpr" ):
                listener.exitRelativepathexpr(self)




    def relativepathexpr(self):

        localctx = XPath20Parser.RelativepathexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relativepathexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.stepexpr()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.SLASH or _la==XPath20Parser.SS:
                self.state = 322
                _la = self._input.LA(1)
                if not(_la==XPath20Parser.SLASH or _la==XPath20Parser.SS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.stepexpr()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StepexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filterexpr(self):
            return self.getTypedRuleContext(XPath20Parser.FilterexprContext,0)


        def axisstep(self):
            return self.getTypedRuleContext(XPath20Parser.AxisstepContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_stepexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStepexpr" ):
                listener.enterStepexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStepexpr" ):
                listener.exitStepexpr(self)




    def stepexpr(self):

        localctx = XPath20Parser.StepexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stepexpr)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.filterexpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.axisstep()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisstepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicatelist(self):
            return self.getTypedRuleContext(XPath20Parser.PredicatelistContext,0)


        def reversestep(self):
            return self.getTypedRuleContext(XPath20Parser.ReversestepContext,0)


        def forwardstep(self):
            return self.getTypedRuleContext(XPath20Parser.ForwardstepContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_axisstep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxisstep" ):
                listener.enterAxisstep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxisstep" ):
                listener.exitAxisstep(self)




    def axisstep(self):

        localctx = XPath20Parser.AxisstepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_axisstep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 333
                self.reversestep()
                pass

            elif la_ == 2:
                self.state = 334
                self.forwardstep()
                pass


            self.state = 337
            self.predicatelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForwardstepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forwardaxis(self):
            return self.getTypedRuleContext(XPath20Parser.ForwardaxisContext,0)


        def nodetest(self):
            return self.getTypedRuleContext(XPath20Parser.NodetestContext,0)


        def abbrevforwardstep(self):
            return self.getTypedRuleContext(XPath20Parser.AbbrevforwardstepContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_forwardstep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardstep" ):
                listener.enterForwardstep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardstep" ):
                listener.exitForwardstep(self)




    def forwardstep(self):

        localctx = XPath20Parser.ForwardstepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forwardstep)
        try:
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.forwardaxis()
                self.state = 340
                self.nodetest()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.abbrevforwardstep()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForwardaxisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CHILD(self):
            return self.getToken(XPath20Parser.KW_CHILD, 0)

        def COLONCOLON(self):
            return self.getToken(XPath20Parser.COLONCOLON, 0)

        def KW_DESCENDANT(self):
            return self.getToken(XPath20Parser.KW_DESCENDANT, 0)

        def KW_ATTRIBUTE(self):
            return self.getToken(XPath20Parser.KW_ATTRIBUTE, 0)

        def KW_SELF(self):
            return self.getToken(XPath20Parser.KW_SELF, 0)

        def KW_DESCENDANT_OR_SELF(self):
            return self.getToken(XPath20Parser.KW_DESCENDANT_OR_SELF, 0)

        def KW_FOLLOWING_SIBLING(self):
            return self.getToken(XPath20Parser.KW_FOLLOWING_SIBLING, 0)

        def KW_FOLLOWING(self):
            return self.getToken(XPath20Parser.KW_FOLLOWING, 0)

        def KW_NAMESPACE(self):
            return self.getToken(XPath20Parser.KW_NAMESPACE, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_forwardaxis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForwardaxis" ):
                listener.enterForwardaxis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForwardaxis" ):
                listener.exitForwardaxis(self)




    def forwardaxis(self):

        localctx = XPath20Parser.ForwardaxisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forwardaxis)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_CHILD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(XPath20Parser.KW_CHILD)
                self.state = 346
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_DESCENDANT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.match(XPath20Parser.KW_DESCENDANT)
                self.state = 348
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_ATTRIBUTE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.match(XPath20Parser.KW_ATTRIBUTE)
                self.state = 350
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(XPath20Parser.KW_SELF)
                self.state = 352
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_DESCENDANT_OR_SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 353
                self.match(XPath20Parser.KW_DESCENDANT_OR_SELF)
                self.state = 354
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_FOLLOWING_SIBLING]:
                self.enterOuterAlt(localctx, 6)
                self.state = 355
                self.match(XPath20Parser.KW_FOLLOWING_SIBLING)
                self.state = 356
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_FOLLOWING]:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.match(XPath20Parser.KW_FOLLOWING)
                self.state = 358
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_NAMESPACE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 359
                self.match(XPath20Parser.KW_NAMESPACE)
                self.state = 360
                self.match(XPath20Parser.COLONCOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbbrevforwardstepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodetest(self):
            return self.getTypedRuleContext(XPath20Parser.NodetestContext,0)


        def AT(self):
            return self.getToken(XPath20Parser.AT, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_abbrevforwardstep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbbrevforwardstep" ):
                listener.enterAbbrevforwardstep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbbrevforwardstep" ):
                listener.exitAbbrevforwardstep(self)




    def abbrevforwardstep(self):

        localctx = XPath20Parser.AbbrevforwardstepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_abbrevforwardstep)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.AT:
                self.state = 363
                self.match(XPath20Parser.AT)


            self.state = 366
            self.nodetest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReversestepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reverseaxis(self):
            return self.getTypedRuleContext(XPath20Parser.ReverseaxisContext,0)


        def nodetest(self):
            return self.getTypedRuleContext(XPath20Parser.NodetestContext,0)


        def abbrevreversestep(self):
            return self.getTypedRuleContext(XPath20Parser.AbbrevreversestepContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_reversestep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReversestep" ):
                listener.enterReversestep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReversestep" ):
                listener.exitReversestep(self)




    def reversestep(self):

        localctx = XPath20Parser.ReversestepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_reversestep)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_ANCESTOR, XPath20Parser.KW_ANCESTOR_OR_SELF, XPath20Parser.KW_PARENT, XPath20Parser.KW_PRECEDING, XPath20Parser.KW_PRECEDING_SIBLING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.reverseaxis()
                self.state = 369
                self.nodetest()
                pass
            elif token in [XPath20Parser.DD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.abbrevreversestep()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReverseaxisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PARENT(self):
            return self.getToken(XPath20Parser.KW_PARENT, 0)

        def COLONCOLON(self):
            return self.getToken(XPath20Parser.COLONCOLON, 0)

        def KW_ANCESTOR(self):
            return self.getToken(XPath20Parser.KW_ANCESTOR, 0)

        def KW_PRECEDING_SIBLING(self):
            return self.getToken(XPath20Parser.KW_PRECEDING_SIBLING, 0)

        def KW_PRECEDING(self):
            return self.getToken(XPath20Parser.KW_PRECEDING, 0)

        def KW_ANCESTOR_OR_SELF(self):
            return self.getToken(XPath20Parser.KW_ANCESTOR_OR_SELF, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_reverseaxis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReverseaxis" ):
                listener.enterReverseaxis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReverseaxis" ):
                listener.exitReverseaxis(self)




    def reverseaxis(self):

        localctx = XPath20Parser.ReverseaxisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_reverseaxis)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_PARENT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(XPath20Parser.KW_PARENT)
                self.state = 375
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_ANCESTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(XPath20Parser.KW_ANCESTOR)
                self.state = 377
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_PRECEDING_SIBLING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.match(XPath20Parser.KW_PRECEDING_SIBLING)
                self.state = 379
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_PRECEDING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                self.match(XPath20Parser.KW_PRECEDING)
                self.state = 381
                self.match(XPath20Parser.COLONCOLON)
                pass
            elif token in [XPath20Parser.KW_ANCESTOR_OR_SELF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 382
                self.match(XPath20Parser.KW_ANCESTOR_OR_SELF)
                self.state = 383
                self.match(XPath20Parser.COLONCOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbbrevreversestepContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DD(self):
            return self.getToken(XPath20Parser.DD, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_abbrevreversestep

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbbrevreversestep" ):
                listener.enterAbbrevreversestep(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbbrevreversestep" ):
                listener.exitAbbrevreversestep(self)




    def abbrevreversestep(self):

        localctx = XPath20Parser.AbbrevreversestepContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_abbrevreversestep)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(XPath20Parser.DD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodetestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kindtest(self):
            return self.getTypedRuleContext(XPath20Parser.KindtestContext,0)


        def nametest(self):
            return self.getTypedRuleContext(XPath20Parser.NametestContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_nodetest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodetest" ):
                listener.enterNodetest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodetest" ):
                listener.exitNodetest(self)




    def nodetest(self):

        localctx = XPath20Parser.NodetestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_nodetest)
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.kindtest()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.nametest()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NametestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def wildcard(self):
            return self.getTypedRuleContext(XPath20Parser.WildcardContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_nametest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNametest" ):
                listener.enterNametest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNametest" ):
                listener.exitNametest(self)




    def nametest(self):

        localctx = XPath20Parser.NametestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_nametest)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_ANCESTOR, XPath20Parser.KW_ANCESTOR_OR_SELF, XPath20Parser.KW_AND, XPath20Parser.KW_ARRAY, XPath20Parser.KW_AS, XPath20Parser.KW_ATTRIBUTE, XPath20Parser.KW_CAST, XPath20Parser.KW_CASTABLE, XPath20Parser.KW_CHILD, XPath20Parser.KW_COMMENT, XPath20Parser.KW_DESCENDANT, XPath20Parser.KW_DESCENDANT_OR_SELF, XPath20Parser.KW_DIV, XPath20Parser.KW_DOCUMENT_NODE, XPath20Parser.KW_ELEMENT, XPath20Parser.KW_ELSE, XPath20Parser.KW_EMPTY_SEQUENCE, XPath20Parser.KW_EQ, XPath20Parser.KW_EVERY, XPath20Parser.KW_EXCEPT, XPath20Parser.KW_FOLLOWING, XPath20Parser.KW_FOLLOWING_SIBLING, XPath20Parser.KW_FOR, XPath20Parser.KW_FUNCTION, XPath20Parser.KW_GE, XPath20Parser.KW_GT, XPath20Parser.KW_IDIV, XPath20Parser.KW_IF, XPath20Parser.KW_IN, XPath20Parser.KW_INSTANCE, XPath20Parser.KW_INTERSECT, XPath20Parser.KW_IS, XPath20Parser.KW_ITEM, XPath20Parser.KW_LE, XPath20Parser.KW_LET, XPath20Parser.KW_LT, XPath20Parser.KW_MAP, XPath20Parser.KW_MOD, XPath20Parser.KW_NAMESPACE, XPath20Parser.KW_NAMESPACE_NODE, XPath20Parser.KW_NE, XPath20Parser.KW_NODE, XPath20Parser.KW_OF, XPath20Parser.KW_OR, XPath20Parser.KW_PARENT, XPath20Parser.KW_PRECEDING, XPath20Parser.KW_PRECEDING_SIBLING, XPath20Parser.KW_PROCESSING_INSTRUCTION, XPath20Parser.KW_RETURN, XPath20Parser.KW_SATISFIES, XPath20Parser.KW_SCHEMA_ATTRIBUTE, XPath20Parser.KW_SCHEMA_ELEMENT, XPath20Parser.KW_SELF, XPath20Parser.KW_SOME, XPath20Parser.KW_TEXT, XPath20Parser.KW_THEN, XPath20Parser.KW_TREAT, XPath20Parser.KW_UNION, XPath20Parser.URIQualifiedName, XPath20Parser.QName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.qname()
                pass
            elif token in [XPath20Parser.SC, XPath20Parser.STAR, XPath20Parser.NCName]:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.wildcard()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(XPath20Parser.STAR, 0)

        def NCName(self):
            return self.getToken(XPath20Parser.NCName, 0)

        def CS(self):
            return self.getToken(XPath20Parser.CS, 0)

        def SC(self):
            return self.getToken(XPath20Parser.SC, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_wildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWildcard" ):
                listener.enterWildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWildcard" ):
                listener.exitWildcard(self)




    def wildcard(self):

        localctx = XPath20Parser.WildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_wildcard)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.match(XPath20Parser.STAR)
                pass
            elif token in [XPath20Parser.NCName]:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.match(XPath20Parser.NCName)
                self.state = 398
                self.match(XPath20Parser.CS)
                pass
            elif token in [XPath20Parser.SC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(XPath20Parser.SC)
                self.state = 400
                self.match(XPath20Parser.NCName)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryexpr(self):
            return self.getTypedRuleContext(XPath20Parser.PrimaryexprContext,0)


        def predicatelist(self):
            return self.getTypedRuleContext(XPath20Parser.PredicatelistContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_filterexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterexpr" ):
                listener.enterFilterexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterexpr" ):
                listener.exitFilterexpr(self)




    def filterexpr(self):

        localctx = XPath20Parser.FilterexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_filterexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.primaryexpr()
            self.state = 404
            self.predicatelist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicatelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.PredicateContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.PredicateContext,i)


        def getRuleIndex(self):
            return XPath20Parser.RULE_predicatelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicatelist" ):
                listener.enterPredicatelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicatelist" ):
                listener.exitPredicatelist(self)




    def predicatelist(self):

        localctx = XPath20Parser.PredicatelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_predicatelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPath20Parser.OB:
                self.state = 406
                self.predicate()
                self.state = 411
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredicateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(XPath20Parser.OB, 0)

        def expr(self):
            return self.getTypedRuleContext(XPath20Parser.ExprContext,0)


        def CB(self):
            return self.getToken(XPath20Parser.CB, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_predicate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicate" ):
                listener.enterPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicate" ):
                listener.exitPredicate(self)




    def predicate(self):

        localctx = XPath20Parser.PredicateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_predicate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(XPath20Parser.OB)
            self.state = 413
            self.expr()
            self.state = 414
            self.match(XPath20Parser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(XPath20Parser.LiteralContext,0)


        def varref(self):
            return self.getTypedRuleContext(XPath20Parser.VarrefContext,0)


        def parenthesizedexpr(self):
            return self.getTypedRuleContext(XPath20Parser.ParenthesizedexprContext,0)


        def contextitemexpr(self):
            return self.getTypedRuleContext(XPath20Parser.ContextitemexprContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(XPath20Parser.FunctioncallContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_primaryexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryexpr" ):
                listener.enterPrimaryexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryexpr" ):
                listener.exitPrimaryexpr(self)




    def primaryexpr(self):

        localctx = XPath20Parser.PrimaryexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_primaryexpr)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.varref()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.parenthesizedexpr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 419
                self.contextitemexpr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 420
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numericliteral(self):
            return self.getTypedRuleContext(XPath20Parser.NumericliteralContext,0)


        def StringLiteral(self):
            return self.getToken(XPath20Parser.StringLiteral, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = XPath20Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literal)
        try:
            self.state = 425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.IntegerLiteral, XPath20Parser.DecimalLiteral, XPath20Parser.DoubleLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.numericliteral()
                pass
            elif token in [XPath20Parser.StringLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.match(XPath20Parser.StringLiteral)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumericliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(XPath20Parser.IntegerLiteral, 0)

        def DecimalLiteral(self):
            return self.getToken(XPath20Parser.DecimalLiteral, 0)

        def DoubleLiteral(self):
            return self.getToken(XPath20Parser.DoubleLiteral, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_numericliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumericliteral" ):
                listener.enterNumericliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumericliteral" ):
                listener.exitNumericliteral(self)




    def numericliteral(self):

        localctx = XPath20Parser.NumericliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_numericliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not(((((_la - 95)) & ~0x3f) == 0 and ((1 << (_la - 95)) & ((1 << (XPath20Parser.IntegerLiteral - 95)) | (1 << (XPath20Parser.DecimalLiteral - 95)) | (1 << (XPath20Parser.DoubleLiteral - 95)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarrefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(XPath20Parser.DOLLAR, 0)

        def varname(self):
            return self.getTypedRuleContext(XPath20Parser.VarnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_varref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarref" ):
                listener.enterVarref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarref" ):
                listener.exitVarref(self)




    def varref(self):

        localctx = XPath20Parser.VarrefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_varref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(XPath20Parser.DOLLAR)
            self.state = 430
            self.varname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_varname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarname" ):
                listener.enterVarname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarname" ):
                listener.exitVarname(self)




    def varname(self):

        localctx = XPath20Parser.VarnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_varname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.qname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenthesizedexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def expr(self):
            return self.getTypedRuleContext(XPath20Parser.ExprContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_parenthesizedexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedexpr" ):
                listener.enterParenthesizedexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedexpr" ):
                listener.exitParenthesizedexpr(self)




    def parenthesizedexpr(self):

        localctx = XPath20Parser.ParenthesizedexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_parenthesizedexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(XPath20Parser.OP)
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 435
                self.expr()


            self.state = 438
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextitemexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def D(self):
            return self.getToken(XPath20Parser.D, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_contextitemexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContextitemexpr" ):
                listener.enterContextitemexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContextitemexpr" ):
                listener.exitContextitemexpr(self)




    def contextitemexpr(self):

        localctx = XPath20Parser.ContextitemexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_contextitemexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(XPath20Parser.D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def exprsingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ExprsingleContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ExprsingleContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.COMMA)
            else:
                return self.getToken(XPath20Parser.COMMA, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_functioncall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctioncall" ):
                listener.enterFunctioncall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctioncall" ):
                listener.exitFunctioncall(self)




    def functioncall(self):

        localctx = XPath20Parser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            if not  !(
                                       getInputStream().LA(1)==KW_ARRAY
                                    || getInputStream().LA(1)==KW_ATTRIBUTE
                                    || getInputStream().LA(1)==KW_COMMENT
                                    || getInputStream().LA(1)==KW_DOCUMENT_NODE
                                    || getInputStream().LA(1)==KW_ELEMENT
                                    || getInputStream().LA(1)==KW_EMPTY_SEQUENCE
                                    || getInputStream().LA(1)==KW_FUNCTION
                                    || getInputStream().LA(1)==KW_IF
                                    || getInputStream().LA(1)==KW_ITEM
                                    || getInputStream().LA(1)==KW_MAP
                                    || getInputStream().LA(1)==KW_NAMESPACE_NODE
                                    || getInputStream().LA(1)==KW_NODE
                                    || getInputStream().LA(1)==KW_PROCESSING_INSTRUCTION
                                    || getInputStream().LA(1)==KW_SCHEMA_ATTRIBUTE
                                    || getInputStream().LA(1)==KW_SCHEMA_ELEMENT
                                    || getInputStream().LA(1)==KW_TEXT
                                    ) :
                from antlr4.error.Errors import FailedPredicateException
                raise FailedPredicateException(self, " !(\n                           getInputStream().LA(1)==KW_ARRAY\n                        || getInputStream().LA(1)==KW_ATTRIBUTE\n                        || getInputStream().LA(1)==KW_COMMENT\n                        || getInputStream().LA(1)==KW_DOCUMENT_NODE\n                        || getInputStream().LA(1)==KW_ELEMENT\n                        || getInputStream().LA(1)==KW_EMPTY_SEQUENCE\n                        || getInputStream().LA(1)==KW_FUNCTION\n                        || getInputStream().LA(1)==KW_IF\n                        || getInputStream().LA(1)==KW_ITEM\n                        || getInputStream().LA(1)==KW_MAP\n                        || getInputStream().LA(1)==KW_NAMESPACE_NODE\n                        || getInputStream().LA(1)==KW_NODE\n                        || getInputStream().LA(1)==KW_PROCESSING_INSTRUCTION\n                        || getInputStream().LA(1)==KW_SCHEMA_ATTRIBUTE\n                        || getInputStream().LA(1)==KW_SCHEMA_ELEMENT\n                        || getInputStream().LA(1)==KW_TEXT\n                        ) ")
            self.state = 443
            self.qname()
            self.state = 444
            self.match(XPath20Parser.OP)
            self.state = 453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 445
                self.exprsingle()
                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XPath20Parser.COMMA:
                    self.state = 446
                    self.match(XPath20Parser.COMMA)
                    self.state = 447
                    self.exprsingle()
                    self.state = 452
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 455
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingletypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomictype(self):
            return self.getTypedRuleContext(XPath20Parser.AtomictypeContext,0)


        def QM(self):
            return self.getToken(XPath20Parser.QM, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_singletype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingletype" ):
                listener.enterSingletype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingletype" ):
                listener.exitSingletype(self)




    def singletype(self):

        localctx = XPath20Parser.SingletypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_singletype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.atomictype()
            self.state = 459
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.QM:
                self.state = 458
                self.match(XPath20Parser.QM)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SequencetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_EMPTY_SEQUENCE(self):
            return self.getToken(XPath20Parser.KW_EMPTY_SEQUENCE, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def itemtype(self):
            return self.getTypedRuleContext(XPath20Parser.ItemtypeContext,0)


        def occurrenceindicator(self):
            return self.getTypedRuleContext(XPath20Parser.OccurrenceindicatorContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_sequencetype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSequencetype" ):
                listener.enterSequencetype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSequencetype" ):
                listener.exitSequencetype(self)




    def sequencetype(self):

        localctx = XPath20Parser.SequencetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_sequencetype)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.match(XPath20Parser.KW_EMPTY_SEQUENCE)
                self.state = 462
                self.match(XPath20Parser.OP)
                self.state = 463
                self.match(XPath20Parser.CP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
                self.itemtype()
                self.state = 466
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 465
                    self.occurrenceindicator()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OccurrenceindicatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QM(self):
            return self.getToken(XPath20Parser.QM, 0)

        def STAR(self):
            return self.getToken(XPath20Parser.STAR, 0)

        def PLUS(self):
            return self.getToken(XPath20Parser.PLUS, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_occurrenceindicator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOccurrenceindicator" ):
                listener.enterOccurrenceindicator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOccurrenceindicator" ):
                listener.exitOccurrenceindicator(self)




    def occurrenceindicator(self):

        localctx = XPath20Parser.OccurrenceindicatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_occurrenceindicator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XPath20Parser.PLUS) | (1 << XPath20Parser.QM) | (1 << XPath20Parser.STAR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kindtest(self):
            return self.getTypedRuleContext(XPath20Parser.KindtestContext,0)


        def KW_ITEM(self):
            return self.getToken(XPath20Parser.KW_ITEM, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def atomictype(self):
            return self.getTypedRuleContext(XPath20Parser.AtomictypeContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_itemtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemtype" ):
                listener.enterItemtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemtype" ):
                listener.exitItemtype(self)




    def itemtype(self):

        localctx = XPath20Parser.ItemtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_itemtype)
        try:
            self.state = 477
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.kindtest()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.match(XPath20Parser.KW_ITEM)
                self.state = 474
                self.match(XPath20Parser.OP)
                self.state = 475
                self.match(XPath20Parser.CP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 476
                self.atomictype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomictypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_atomictype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomictype" ):
                listener.enterAtomictype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomictype" ):
                listener.exitAtomictype(self)




    def atomictype(self):

        localctx = XPath20Parser.AtomictypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_atomictype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.qname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KindtestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def documenttest(self):
            return self.getTypedRuleContext(XPath20Parser.DocumenttestContext,0)


        def elementtest(self):
            return self.getTypedRuleContext(XPath20Parser.ElementtestContext,0)


        def attributetest(self):
            return self.getTypedRuleContext(XPath20Parser.AttributetestContext,0)


        def schemaelementtest(self):
            return self.getTypedRuleContext(XPath20Parser.SchemaelementtestContext,0)


        def schemaattributetest(self):
            return self.getTypedRuleContext(XPath20Parser.SchemaattributetestContext,0)


        def pitest(self):
            return self.getTypedRuleContext(XPath20Parser.PitestContext,0)


        def commenttest(self):
            return self.getTypedRuleContext(XPath20Parser.CommenttestContext,0)


        def texttest(self):
            return self.getTypedRuleContext(XPath20Parser.TexttestContext,0)


        def anykindtest(self):
            return self.getTypedRuleContext(XPath20Parser.AnykindtestContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_kindtest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKindtest" ):
                listener.enterKindtest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKindtest" ):
                listener.exitKindtest(self)




    def kindtest(self):

        localctx = XPath20Parser.KindtestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_kindtest)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_DOCUMENT_NODE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.documenttest()
                pass
            elif token in [XPath20Parser.KW_ELEMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
                self.elementtest()
                pass
            elif token in [XPath20Parser.KW_ATTRIBUTE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.attributetest()
                pass
            elif token in [XPath20Parser.KW_SCHEMA_ELEMENT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.schemaelementtest()
                pass
            elif token in [XPath20Parser.KW_SCHEMA_ATTRIBUTE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 485
                self.schemaattributetest()
                pass
            elif token in [XPath20Parser.KW_PROCESSING_INSTRUCTION]:
                self.enterOuterAlt(localctx, 6)
                self.state = 486
                self.pitest()
                pass
            elif token in [XPath20Parser.KW_COMMENT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 487
                self.commenttest()
                pass
            elif token in [XPath20Parser.KW_TEXT]:
                self.enterOuterAlt(localctx, 8)
                self.state = 488
                self.texttest()
                pass
            elif token in [XPath20Parser.KW_NODE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 489
                self.anykindtest()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnykindtestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NODE(self):
            return self.getToken(XPath20Parser.KW_NODE, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_anykindtest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnykindtest" ):
                listener.enterAnykindtest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnykindtest" ):
                listener.exitAnykindtest(self)




    def anykindtest(self):

        localctx = XPath20Parser.AnykindtestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_anykindtest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(XPath20Parser.KW_NODE)
            self.state = 493
            self.match(XPath20Parser.OP)
            self.state = 494
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumenttestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DOCUMENT_NODE(self):
            return self.getToken(XPath20Parser.KW_DOCUMENT_NODE, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def elementtest(self):
            return self.getTypedRuleContext(XPath20Parser.ElementtestContext,0)


        def schemaelementtest(self):
            return self.getTypedRuleContext(XPath20Parser.SchemaelementtestContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_documenttest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocumenttest" ):
                listener.enterDocumenttest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocumenttest" ):
                listener.exitDocumenttest(self)




    def documenttest(self):

        localctx = XPath20Parser.DocumenttestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_documenttest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(XPath20Parser.KW_DOCUMENT_NODE)
            self.state = 497
            self.match(XPath20Parser.OP)
            self.state = 500
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_ELEMENT]:
                self.state = 498
                self.elementtest()
                pass
            elif token in [XPath20Parser.KW_SCHEMA_ELEMENT]:
                self.state = 499
                self.schemaelementtest()
                pass
            elif token in [XPath20Parser.CP]:
                pass
            else:
                pass
            self.state = 502
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TexttestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TEXT(self):
            return self.getToken(XPath20Parser.KW_TEXT, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_texttest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTexttest" ):
                listener.enterTexttest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTexttest" ):
                listener.exitTexttest(self)




    def texttest(self):

        localctx = XPath20Parser.TexttestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_texttest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(XPath20Parser.KW_TEXT)
            self.state = 505
            self.match(XPath20Parser.OP)
            self.state = 506
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommenttestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_COMMENT(self):
            return self.getToken(XPath20Parser.KW_COMMENT, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_commenttest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommenttest" ):
                listener.enterCommenttest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommenttest" ):
                listener.exitCommenttest(self)




    def commenttest(self):

        localctx = XPath20Parser.CommenttestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_commenttest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(XPath20Parser.KW_COMMENT)
            self.state = 509
            self.match(XPath20Parser.OP)
            self.state = 510
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PitestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PROCESSING_INSTRUCTION(self):
            return self.getToken(XPath20Parser.KW_PROCESSING_INSTRUCTION, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def NCName(self):
            return self.getToken(XPath20Parser.NCName, 0)

        def StringLiteral(self):
            return self.getToken(XPath20Parser.StringLiteral, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_pitest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPitest" ):
                listener.enterPitest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPitest" ):
                listener.exitPitest(self)




    def pitest(self):

        localctx = XPath20Parser.PitestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_pitest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(XPath20Parser.KW_PROCESSING_INSTRUCTION)
            self.state = 513
            self.match(XPath20Parser.OP)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XPath20Parser.StringLiteral or _la==XPath20Parser.NCName:
                self.state = 514
                _la = self._input.LA(1)
                if not(_la==XPath20Parser.StringLiteral or _la==XPath20Parser.NCName):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 517
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributetestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ATTRIBUTE(self):
            return self.getToken(XPath20Parser.KW_ATTRIBUTE, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def attribnameorwildcard(self):
            return self.getTypedRuleContext(XPath20Parser.AttribnameorwildcardContext,0)


        def COMMA(self):
            return self.getToken(XPath20Parser.COMMA, 0)

        def typename_(self):
            return self.getTypedRuleContext(XPath20Parser.Typename_Context,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_attributetest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributetest" ):
                listener.enterAttributetest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributetest" ):
                listener.exitAttributetest(self)




    def attributetest(self):

        localctx = XPath20Parser.AttributetestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_attributetest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(XPath20Parser.KW_ATTRIBUTE)
            self.state = 520
            self.match(XPath20Parser.OP)
            self.state = 526
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XPath20Parser.STAR) | (1 << XPath20Parser.KW_ANCESTOR) | (1 << XPath20Parser.KW_ANCESTOR_OR_SELF) | (1 << XPath20Parser.KW_AND) | (1 << XPath20Parser.KW_ARRAY) | (1 << XPath20Parser.KW_AS) | (1 << XPath20Parser.KW_ATTRIBUTE) | (1 << XPath20Parser.KW_CAST) | (1 << XPath20Parser.KW_CASTABLE) | (1 << XPath20Parser.KW_CHILD) | (1 << XPath20Parser.KW_COMMENT) | (1 << XPath20Parser.KW_DESCENDANT) | (1 << XPath20Parser.KW_DESCENDANT_OR_SELF) | (1 << XPath20Parser.KW_DIV) | (1 << XPath20Parser.KW_DOCUMENT_NODE) | (1 << XPath20Parser.KW_ELEMENT) | (1 << XPath20Parser.KW_ELSE) | (1 << XPath20Parser.KW_EMPTY_SEQUENCE) | (1 << XPath20Parser.KW_EQ) | (1 << XPath20Parser.KW_EVERY) | (1 << XPath20Parser.KW_EXCEPT) | (1 << XPath20Parser.KW_FOLLOWING) | (1 << XPath20Parser.KW_FOLLOWING_SIBLING) | (1 << XPath20Parser.KW_FOR) | (1 << XPath20Parser.KW_FUNCTION) | (1 << XPath20Parser.KW_GE) | (1 << XPath20Parser.KW_GT) | (1 << XPath20Parser.KW_IDIV) | (1 << XPath20Parser.KW_IF))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (XPath20Parser.KW_IN - 64)) | (1 << (XPath20Parser.KW_INSTANCE - 64)) | (1 << (XPath20Parser.KW_INTERSECT - 64)) | (1 << (XPath20Parser.KW_IS - 64)) | (1 << (XPath20Parser.KW_ITEM - 64)) | (1 << (XPath20Parser.KW_LE - 64)) | (1 << (XPath20Parser.KW_LET - 64)) | (1 << (XPath20Parser.KW_LT - 64)) | (1 << (XPath20Parser.KW_MAP - 64)) | (1 << (XPath20Parser.KW_MOD - 64)) | (1 << (XPath20Parser.KW_NAMESPACE - 64)) | (1 << (XPath20Parser.KW_NAMESPACE_NODE - 64)) | (1 << (XPath20Parser.KW_NE - 64)) | (1 << (XPath20Parser.KW_NODE - 64)) | (1 << (XPath20Parser.KW_OF - 64)) | (1 << (XPath20Parser.KW_OR - 64)) | (1 << (XPath20Parser.KW_PARENT - 64)) | (1 << (XPath20Parser.KW_PRECEDING - 64)) | (1 << (XPath20Parser.KW_PRECEDING_SIBLING - 64)) | (1 << (XPath20Parser.KW_PROCESSING_INSTRUCTION - 64)) | (1 << (XPath20Parser.KW_RETURN - 64)) | (1 << (XPath20Parser.KW_SATISFIES - 64)) | (1 << (XPath20Parser.KW_SCHEMA_ATTRIBUTE - 64)) | (1 << (XPath20Parser.KW_SCHEMA_ELEMENT - 64)) | (1 << (XPath20Parser.KW_SELF - 64)) | (1 << (XPath20Parser.KW_SOME - 64)) | (1 << (XPath20Parser.KW_TEXT - 64)) | (1 << (XPath20Parser.KW_THEN - 64)) | (1 << (XPath20Parser.KW_TREAT - 64)) | (1 << (XPath20Parser.KW_UNION - 64)) | (1 << (XPath20Parser.URIQualifiedName - 64)) | (1 << (XPath20Parser.QName - 64)))) != 0):
                self.state = 521
                self.attribnameorwildcard()
                self.state = 524
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==XPath20Parser.COMMA:
                    self.state = 522
                    self.match(XPath20Parser.COMMA)
                    self.state = 523
                    self.typename_()




            self.state = 528
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttribnameorwildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributename(self):
            return self.getTypedRuleContext(XPath20Parser.AttributenameContext,0)


        def STAR(self):
            return self.getToken(XPath20Parser.STAR, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_attribnameorwildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribnameorwildcard" ):
                listener.enterAttribnameorwildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribnameorwildcard" ):
                listener.exitAttribnameorwildcard(self)




    def attribnameorwildcard(self):

        localctx = XPath20Parser.AttribnameorwildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_attribnameorwildcard)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_ANCESTOR, XPath20Parser.KW_ANCESTOR_OR_SELF, XPath20Parser.KW_AND, XPath20Parser.KW_ARRAY, XPath20Parser.KW_AS, XPath20Parser.KW_ATTRIBUTE, XPath20Parser.KW_CAST, XPath20Parser.KW_CASTABLE, XPath20Parser.KW_CHILD, XPath20Parser.KW_COMMENT, XPath20Parser.KW_DESCENDANT, XPath20Parser.KW_DESCENDANT_OR_SELF, XPath20Parser.KW_DIV, XPath20Parser.KW_DOCUMENT_NODE, XPath20Parser.KW_ELEMENT, XPath20Parser.KW_ELSE, XPath20Parser.KW_EMPTY_SEQUENCE, XPath20Parser.KW_EQ, XPath20Parser.KW_EVERY, XPath20Parser.KW_EXCEPT, XPath20Parser.KW_FOLLOWING, XPath20Parser.KW_FOLLOWING_SIBLING, XPath20Parser.KW_FOR, XPath20Parser.KW_FUNCTION, XPath20Parser.KW_GE, XPath20Parser.KW_GT, XPath20Parser.KW_IDIV, XPath20Parser.KW_IF, XPath20Parser.KW_IN, XPath20Parser.KW_INSTANCE, XPath20Parser.KW_INTERSECT, XPath20Parser.KW_IS, XPath20Parser.KW_ITEM, XPath20Parser.KW_LE, XPath20Parser.KW_LET, XPath20Parser.KW_LT, XPath20Parser.KW_MAP, XPath20Parser.KW_MOD, XPath20Parser.KW_NAMESPACE, XPath20Parser.KW_NAMESPACE_NODE, XPath20Parser.KW_NE, XPath20Parser.KW_NODE, XPath20Parser.KW_OF, XPath20Parser.KW_OR, XPath20Parser.KW_PARENT, XPath20Parser.KW_PRECEDING, XPath20Parser.KW_PRECEDING_SIBLING, XPath20Parser.KW_PROCESSING_INSTRUCTION, XPath20Parser.KW_RETURN, XPath20Parser.KW_SATISFIES, XPath20Parser.KW_SCHEMA_ATTRIBUTE, XPath20Parser.KW_SCHEMA_ELEMENT, XPath20Parser.KW_SELF, XPath20Parser.KW_SOME, XPath20Parser.KW_TEXT, XPath20Parser.KW_THEN, XPath20Parser.KW_TREAT, XPath20Parser.KW_UNION, XPath20Parser.URIQualifiedName, XPath20Parser.QName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.attributename()
                pass
            elif token in [XPath20Parser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.match(XPath20Parser.STAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaattributetestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SCHEMA_ATTRIBUTE(self):
            return self.getToken(XPath20Parser.KW_SCHEMA_ATTRIBUTE, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def attributedeclaration(self):
            return self.getTypedRuleContext(XPath20Parser.AttributedeclarationContext,0)


        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_schemaattributetest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaattributetest" ):
                listener.enterSchemaattributetest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaattributetest" ):
                listener.exitSchemaattributetest(self)




    def schemaattributetest(self):

        localctx = XPath20Parser.SchemaattributetestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_schemaattributetest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(XPath20Parser.KW_SCHEMA_ATTRIBUTE)
            self.state = 535
            self.match(XPath20Parser.OP)
            self.state = 536
            self.attributedeclaration()
            self.state = 537
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributename(self):
            return self.getTypedRuleContext(XPath20Parser.AttributenameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_attributedeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributedeclaration" ):
                listener.enterAttributedeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributedeclaration" ):
                listener.exitAttributedeclaration(self)




    def attributedeclaration(self):

        localctx = XPath20Parser.AttributedeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_attributedeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.attributename()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementtestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELEMENT(self):
            return self.getToken(XPath20Parser.KW_ELEMENT, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def elementnameorwildcard(self):
            return self.getTypedRuleContext(XPath20Parser.ElementnameorwildcardContext,0)


        def COMMA(self):
            return self.getToken(XPath20Parser.COMMA, 0)

        def typename_(self):
            return self.getTypedRuleContext(XPath20Parser.Typename_Context,0)


        def QM(self):
            return self.getToken(XPath20Parser.QM, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_elementtest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementtest" ):
                listener.enterElementtest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementtest" ):
                listener.exitElementtest(self)




    def elementtest(self):

        localctx = XPath20Parser.ElementtestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_elementtest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(XPath20Parser.KW_ELEMENT)
            self.state = 542
            self.match(XPath20Parser.OP)
            self.state = 551
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XPath20Parser.STAR) | (1 << XPath20Parser.KW_ANCESTOR) | (1 << XPath20Parser.KW_ANCESTOR_OR_SELF) | (1 << XPath20Parser.KW_AND) | (1 << XPath20Parser.KW_ARRAY) | (1 << XPath20Parser.KW_AS) | (1 << XPath20Parser.KW_ATTRIBUTE) | (1 << XPath20Parser.KW_CAST) | (1 << XPath20Parser.KW_CASTABLE) | (1 << XPath20Parser.KW_CHILD) | (1 << XPath20Parser.KW_COMMENT) | (1 << XPath20Parser.KW_DESCENDANT) | (1 << XPath20Parser.KW_DESCENDANT_OR_SELF) | (1 << XPath20Parser.KW_DIV) | (1 << XPath20Parser.KW_DOCUMENT_NODE) | (1 << XPath20Parser.KW_ELEMENT) | (1 << XPath20Parser.KW_ELSE) | (1 << XPath20Parser.KW_EMPTY_SEQUENCE) | (1 << XPath20Parser.KW_EQ) | (1 << XPath20Parser.KW_EVERY) | (1 << XPath20Parser.KW_EXCEPT) | (1 << XPath20Parser.KW_FOLLOWING) | (1 << XPath20Parser.KW_FOLLOWING_SIBLING) | (1 << XPath20Parser.KW_FOR) | (1 << XPath20Parser.KW_FUNCTION) | (1 << XPath20Parser.KW_GE) | (1 << XPath20Parser.KW_GT) | (1 << XPath20Parser.KW_IDIV) | (1 << XPath20Parser.KW_IF))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (XPath20Parser.KW_IN - 64)) | (1 << (XPath20Parser.KW_INSTANCE - 64)) | (1 << (XPath20Parser.KW_INTERSECT - 64)) | (1 << (XPath20Parser.KW_IS - 64)) | (1 << (XPath20Parser.KW_ITEM - 64)) | (1 << (XPath20Parser.KW_LE - 64)) | (1 << (XPath20Parser.KW_LET - 64)) | (1 << (XPath20Parser.KW_LT - 64)) | (1 << (XPath20Parser.KW_MAP - 64)) | (1 << (XPath20Parser.KW_MOD - 64)) | (1 << (XPath20Parser.KW_NAMESPACE - 64)) | (1 << (XPath20Parser.KW_NAMESPACE_NODE - 64)) | (1 << (XPath20Parser.KW_NE - 64)) | (1 << (XPath20Parser.KW_NODE - 64)) | (1 << (XPath20Parser.KW_OF - 64)) | (1 << (XPath20Parser.KW_OR - 64)) | (1 << (XPath20Parser.KW_PARENT - 64)) | (1 << (XPath20Parser.KW_PRECEDING - 64)) | (1 << (XPath20Parser.KW_PRECEDING_SIBLING - 64)) | (1 << (XPath20Parser.KW_PROCESSING_INSTRUCTION - 64)) | (1 << (XPath20Parser.KW_RETURN - 64)) | (1 << (XPath20Parser.KW_SATISFIES - 64)) | (1 << (XPath20Parser.KW_SCHEMA_ATTRIBUTE - 64)) | (1 << (XPath20Parser.KW_SCHEMA_ELEMENT - 64)) | (1 << (XPath20Parser.KW_SELF - 64)) | (1 << (XPath20Parser.KW_SOME - 64)) | (1 << (XPath20Parser.KW_TEXT - 64)) | (1 << (XPath20Parser.KW_THEN - 64)) | (1 << (XPath20Parser.KW_TREAT - 64)) | (1 << (XPath20Parser.KW_UNION - 64)) | (1 << (XPath20Parser.URIQualifiedName - 64)) | (1 << (XPath20Parser.QName - 64)))) != 0):
                self.state = 543
                self.elementnameorwildcard()
                self.state = 549
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==XPath20Parser.COMMA:
                    self.state = 544
                    self.match(XPath20Parser.COMMA)
                    self.state = 545
                    self.typename_()
                    self.state = 547
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==XPath20Parser.QM:
                        self.state = 546
                        self.match(XPath20Parser.QM)






            self.state = 553
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementnameorwildcardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementname(self):
            return self.getTypedRuleContext(XPath20Parser.ElementnameContext,0)


        def STAR(self):
            return self.getToken(XPath20Parser.STAR, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_elementnameorwildcard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementnameorwildcard" ):
                listener.enterElementnameorwildcard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementnameorwildcard" ):
                listener.exitElementnameorwildcard(self)




    def elementnameorwildcard(self):

        localctx = XPath20Parser.ElementnameorwildcardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_elementnameorwildcard)
        try:
            self.state = 557
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPath20Parser.KW_ANCESTOR, XPath20Parser.KW_ANCESTOR_OR_SELF, XPath20Parser.KW_AND, XPath20Parser.KW_ARRAY, XPath20Parser.KW_AS, XPath20Parser.KW_ATTRIBUTE, XPath20Parser.KW_CAST, XPath20Parser.KW_CASTABLE, XPath20Parser.KW_CHILD, XPath20Parser.KW_COMMENT, XPath20Parser.KW_DESCENDANT, XPath20Parser.KW_DESCENDANT_OR_SELF, XPath20Parser.KW_DIV, XPath20Parser.KW_DOCUMENT_NODE, XPath20Parser.KW_ELEMENT, XPath20Parser.KW_ELSE, XPath20Parser.KW_EMPTY_SEQUENCE, XPath20Parser.KW_EQ, XPath20Parser.KW_EVERY, XPath20Parser.KW_EXCEPT, XPath20Parser.KW_FOLLOWING, XPath20Parser.KW_FOLLOWING_SIBLING, XPath20Parser.KW_FOR, XPath20Parser.KW_FUNCTION, XPath20Parser.KW_GE, XPath20Parser.KW_GT, XPath20Parser.KW_IDIV, XPath20Parser.KW_IF, XPath20Parser.KW_IN, XPath20Parser.KW_INSTANCE, XPath20Parser.KW_INTERSECT, XPath20Parser.KW_IS, XPath20Parser.KW_ITEM, XPath20Parser.KW_LE, XPath20Parser.KW_LET, XPath20Parser.KW_LT, XPath20Parser.KW_MAP, XPath20Parser.KW_MOD, XPath20Parser.KW_NAMESPACE, XPath20Parser.KW_NAMESPACE_NODE, XPath20Parser.KW_NE, XPath20Parser.KW_NODE, XPath20Parser.KW_OF, XPath20Parser.KW_OR, XPath20Parser.KW_PARENT, XPath20Parser.KW_PRECEDING, XPath20Parser.KW_PRECEDING_SIBLING, XPath20Parser.KW_PROCESSING_INSTRUCTION, XPath20Parser.KW_RETURN, XPath20Parser.KW_SATISFIES, XPath20Parser.KW_SCHEMA_ATTRIBUTE, XPath20Parser.KW_SCHEMA_ELEMENT, XPath20Parser.KW_SELF, XPath20Parser.KW_SOME, XPath20Parser.KW_TEXT, XPath20Parser.KW_THEN, XPath20Parser.KW_TREAT, XPath20Parser.KW_UNION, XPath20Parser.URIQualifiedName, XPath20Parser.QName]:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.elementname()
                pass
            elif token in [XPath20Parser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
                self.match(XPath20Parser.STAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemaelementtestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SCHEMA_ELEMENT(self):
            return self.getToken(XPath20Parser.KW_SCHEMA_ELEMENT, 0)

        def OP(self):
            return self.getToken(XPath20Parser.OP, 0)

        def elementdeclaration(self):
            return self.getTypedRuleContext(XPath20Parser.ElementdeclarationContext,0)


        def CP(self):
            return self.getToken(XPath20Parser.CP, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_schemaelementtest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSchemaelementtest" ):
                listener.enterSchemaelementtest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSchemaelementtest" ):
                listener.exitSchemaelementtest(self)




    def schemaelementtest(self):

        localctx = XPath20Parser.SchemaelementtestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_schemaelementtest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(XPath20Parser.KW_SCHEMA_ELEMENT)
            self.state = 560
            self.match(XPath20Parser.OP)
            self.state = 561
            self.elementdeclaration()
            self.state = 562
            self.match(XPath20Parser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementdeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementname(self):
            return self.getTypedRuleContext(XPath20Parser.ElementnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_elementdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementdeclaration" ):
                listener.enterElementdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementdeclaration" ):
                listener.exitElementdeclaration(self)




    def elementdeclaration(self):

        localctx = XPath20Parser.ElementdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_elementdeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            self.elementname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_attributename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributename" ):
                listener.enterAttributename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributename" ):
                listener.exitAttributename(self)




    def attributename(self):

        localctx = XPath20Parser.AttributenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_attributename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.qname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_elementname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElementname" ):
                listener.enterElementname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElementname" ):
                listener.exitElementname(self)




    def elementname(self):

        localctx = XPath20Parser.ElementnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_elementname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.qname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typename_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qname(self):
            return self.getTypedRuleContext(XPath20Parser.QnameContext,0)


        def getRuleIndex(self):
            return XPath20Parser.RULE_typename_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypename_" ):
                listener.enterTypename_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypename_" ):
                listener.exitTypename_(self)




    def typename_(self):

        localctx = XPath20Parser.Typename_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_typename_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.qname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QName(self):
            return self.getToken(XPath20Parser.QName, 0)

        def URIQualifiedName(self):
            return self.getToken(XPath20Parser.URIQualifiedName, 0)

        def KW_ANCESTOR(self):
            return self.getToken(XPath20Parser.KW_ANCESTOR, 0)

        def KW_ANCESTOR_OR_SELF(self):
            return self.getToken(XPath20Parser.KW_ANCESTOR_OR_SELF, 0)

        def KW_AND(self):
            return self.getToken(XPath20Parser.KW_AND, 0)

        def KW_ARRAY(self):
            return self.getToken(XPath20Parser.KW_ARRAY, 0)

        def KW_AS(self):
            return self.getToken(XPath20Parser.KW_AS, 0)

        def KW_ATTRIBUTE(self):
            return self.getToken(XPath20Parser.KW_ATTRIBUTE, 0)

        def KW_CAST(self):
            return self.getToken(XPath20Parser.KW_CAST, 0)

        def KW_CASTABLE(self):
            return self.getToken(XPath20Parser.KW_CASTABLE, 0)

        def KW_CHILD(self):
            return self.getToken(XPath20Parser.KW_CHILD, 0)

        def KW_COMMENT(self):
            return self.getToken(XPath20Parser.KW_COMMENT, 0)

        def KW_DESCENDANT(self):
            return self.getToken(XPath20Parser.KW_DESCENDANT, 0)

        def KW_DESCENDANT_OR_SELF(self):
            return self.getToken(XPath20Parser.KW_DESCENDANT_OR_SELF, 0)

        def KW_DIV(self):
            return self.getToken(XPath20Parser.KW_DIV, 0)

        def KW_DOCUMENT_NODE(self):
            return self.getToken(XPath20Parser.KW_DOCUMENT_NODE, 0)

        def KW_ELEMENT(self):
            return self.getToken(XPath20Parser.KW_ELEMENT, 0)

        def KW_ELSE(self):
            return self.getToken(XPath20Parser.KW_ELSE, 0)

        def KW_EMPTY_SEQUENCE(self):
            return self.getToken(XPath20Parser.KW_EMPTY_SEQUENCE, 0)

        def KW_EQ(self):
            return self.getToken(XPath20Parser.KW_EQ, 0)

        def KW_EVERY(self):
            return self.getToken(XPath20Parser.KW_EVERY, 0)

        def KW_EXCEPT(self):
            return self.getToken(XPath20Parser.KW_EXCEPT, 0)

        def KW_FOLLOWING(self):
            return self.getToken(XPath20Parser.KW_FOLLOWING, 0)

        def KW_FOLLOWING_SIBLING(self):
            return self.getToken(XPath20Parser.KW_FOLLOWING_SIBLING, 0)

        def KW_FOR(self):
            return self.getToken(XPath20Parser.KW_FOR, 0)

        def KW_FUNCTION(self):
            return self.getToken(XPath20Parser.KW_FUNCTION, 0)

        def KW_GE(self):
            return self.getToken(XPath20Parser.KW_GE, 0)

        def KW_GT(self):
            return self.getToken(XPath20Parser.KW_GT, 0)

        def KW_IDIV(self):
            return self.getToken(XPath20Parser.KW_IDIV, 0)

        def KW_IF(self):
            return self.getToken(XPath20Parser.KW_IF, 0)

        def KW_IN(self):
            return self.getToken(XPath20Parser.KW_IN, 0)

        def KW_INSTANCE(self):
            return self.getToken(XPath20Parser.KW_INSTANCE, 0)

        def KW_INTERSECT(self):
            return self.getToken(XPath20Parser.KW_INTERSECT, 0)

        def KW_IS(self):
            return self.getToken(XPath20Parser.KW_IS, 0)

        def KW_ITEM(self):
            return self.getToken(XPath20Parser.KW_ITEM, 0)

        def KW_LE(self):
            return self.getToken(XPath20Parser.KW_LE, 0)

        def KW_LET(self):
            return self.getToken(XPath20Parser.KW_LET, 0)

        def KW_LT(self):
            return self.getToken(XPath20Parser.KW_LT, 0)

        def KW_MAP(self):
            return self.getToken(XPath20Parser.KW_MAP, 0)

        def KW_MOD(self):
            return self.getToken(XPath20Parser.KW_MOD, 0)

        def KW_NAMESPACE(self):
            return self.getToken(XPath20Parser.KW_NAMESPACE, 0)

        def KW_NAMESPACE_NODE(self):
            return self.getToken(XPath20Parser.KW_NAMESPACE_NODE, 0)

        def KW_NE(self):
            return self.getToken(XPath20Parser.KW_NE, 0)

        def KW_NODE(self):
            return self.getToken(XPath20Parser.KW_NODE, 0)

        def KW_OF(self):
            return self.getToken(XPath20Parser.KW_OF, 0)

        def KW_OR(self):
            return self.getToken(XPath20Parser.KW_OR, 0)

        def KW_PARENT(self):
            return self.getToken(XPath20Parser.KW_PARENT, 0)

        def KW_PRECEDING(self):
            return self.getToken(XPath20Parser.KW_PRECEDING, 0)

        def KW_PRECEDING_SIBLING(self):
            return self.getToken(XPath20Parser.KW_PRECEDING_SIBLING, 0)

        def KW_PROCESSING_INSTRUCTION(self):
            return self.getToken(XPath20Parser.KW_PROCESSING_INSTRUCTION, 0)

        def KW_RETURN(self):
            return self.getToken(XPath20Parser.KW_RETURN, 0)

        def KW_SATISFIES(self):
            return self.getToken(XPath20Parser.KW_SATISFIES, 0)

        def KW_SCHEMA_ATTRIBUTE(self):
            return self.getToken(XPath20Parser.KW_SCHEMA_ATTRIBUTE, 0)

        def KW_SCHEMA_ELEMENT(self):
            return self.getToken(XPath20Parser.KW_SCHEMA_ELEMENT, 0)

        def KW_SELF(self):
            return self.getToken(XPath20Parser.KW_SELF, 0)

        def KW_SOME(self):
            return self.getToken(XPath20Parser.KW_SOME, 0)

        def KW_TEXT(self):
            return self.getToken(XPath20Parser.KW_TEXT, 0)

        def KW_THEN(self):
            return self.getToken(XPath20Parser.KW_THEN, 0)

        def KW_TREAT(self):
            return self.getToken(XPath20Parser.KW_TREAT, 0)

        def KW_UNION(self):
            return self.getToken(XPath20Parser.KW_UNION, 0)

        def getRuleIndex(self):
            return XPath20Parser.RULE_qname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQname" ):
                listener.enterQname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQname" ):
                listener.exitQname(self)




    def qname(self):

        localctx = XPath20Parser.QnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_qname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XPath20Parser.KW_ANCESTOR) | (1 << XPath20Parser.KW_ANCESTOR_OR_SELF) | (1 << XPath20Parser.KW_AND) | (1 << XPath20Parser.KW_ARRAY) | (1 << XPath20Parser.KW_AS) | (1 << XPath20Parser.KW_ATTRIBUTE) | (1 << XPath20Parser.KW_CAST) | (1 << XPath20Parser.KW_CASTABLE) | (1 << XPath20Parser.KW_CHILD) | (1 << XPath20Parser.KW_COMMENT) | (1 << XPath20Parser.KW_DESCENDANT) | (1 << XPath20Parser.KW_DESCENDANT_OR_SELF) | (1 << XPath20Parser.KW_DIV) | (1 << XPath20Parser.KW_DOCUMENT_NODE) | (1 << XPath20Parser.KW_ELEMENT) | (1 << XPath20Parser.KW_ELSE) | (1 << XPath20Parser.KW_EMPTY_SEQUENCE) | (1 << XPath20Parser.KW_EQ) | (1 << XPath20Parser.KW_EVERY) | (1 << XPath20Parser.KW_EXCEPT) | (1 << XPath20Parser.KW_FOLLOWING) | (1 << XPath20Parser.KW_FOLLOWING_SIBLING) | (1 << XPath20Parser.KW_FOR) | (1 << XPath20Parser.KW_FUNCTION) | (1 << XPath20Parser.KW_GE) | (1 << XPath20Parser.KW_GT) | (1 << XPath20Parser.KW_IDIV) | (1 << XPath20Parser.KW_IF))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (XPath20Parser.KW_IN - 64)) | (1 << (XPath20Parser.KW_INSTANCE - 64)) | (1 << (XPath20Parser.KW_INTERSECT - 64)) | (1 << (XPath20Parser.KW_IS - 64)) | (1 << (XPath20Parser.KW_ITEM - 64)) | (1 << (XPath20Parser.KW_LE - 64)) | (1 << (XPath20Parser.KW_LET - 64)) | (1 << (XPath20Parser.KW_LT - 64)) | (1 << (XPath20Parser.KW_MAP - 64)) | (1 << (XPath20Parser.KW_MOD - 64)) | (1 << (XPath20Parser.KW_NAMESPACE - 64)) | (1 << (XPath20Parser.KW_NAMESPACE_NODE - 64)) | (1 << (XPath20Parser.KW_NE - 64)) | (1 << (XPath20Parser.KW_NODE - 64)) | (1 << (XPath20Parser.KW_OF - 64)) | (1 << (XPath20Parser.KW_OR - 64)) | (1 << (XPath20Parser.KW_PARENT - 64)) | (1 << (XPath20Parser.KW_PRECEDING - 64)) | (1 << (XPath20Parser.KW_PRECEDING_SIBLING - 64)) | (1 << (XPath20Parser.KW_PROCESSING_INSTRUCTION - 64)) | (1 << (XPath20Parser.KW_RETURN - 64)) | (1 << (XPath20Parser.KW_SATISFIES - 64)) | (1 << (XPath20Parser.KW_SCHEMA_ATTRIBUTE - 64)) | (1 << (XPath20Parser.KW_SCHEMA_ELEMENT - 64)) | (1 << (XPath20Parser.KW_SELF - 64)) | (1 << (XPath20Parser.KW_SOME - 64)) | (1 << (XPath20Parser.KW_TEXT - 64)) | (1 << (XPath20Parser.KW_THEN - 64)) | (1 << (XPath20Parser.KW_TREAT - 64)) | (1 << (XPath20Parser.KW_UNION - 64)) | (1 << (XPath20Parser.URIQualifiedName - 64)) | (1 << (XPath20Parser.QName - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AuxilaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(XPath20Parser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPath20Parser.ExprContext)
            else:
                return self.getTypedRuleContext(XPath20Parser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(XPath20Parser.SEMI)
            else:
                return self.getToken(XPath20Parser.SEMI, i)

        def getRuleIndex(self):
            return XPath20Parser.RULE_auxilary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAuxilary" ):
                listener.enterAuxilary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAuxilary" ):
                listener.exitAuxilary(self)




    def auxilary(self):

        localctx = XPath20Parser.AuxilaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_auxilary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 577 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 574
                    self.expr()
                    self.state = 575
                    self.match(XPath20Parser.SEMI)

                else:
                    raise NoViableAltException(self)
                self.state = 579 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

            self.state = 581
            self.match(XPath20Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[47] = self.functioncall_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def functioncall_sempred(self, localctx:FunctioncallContext, predIndex:int):
            if predIndex == 0:
                return  !(
                                   getInputStream().LA(1)==KW_ARRAY
                                || getInputStream().LA(1)==KW_ATTRIBUTE
                                || getInputStream().LA(1)==KW_COMMENT
                                || getInputStream().LA(1)==KW_DOCUMENT_NODE
                                || getInputStream().LA(1)==KW_ELEMENT
                                || getInputStream().LA(1)==KW_EMPTY_SEQUENCE
                                || getInputStream().LA(1)==KW_FUNCTION
                                || getInputStream().LA(1)==KW_IF
                                || getInputStream().LA(1)==KW_ITEM
                                || getInputStream().LA(1)==KW_MAP
                                || getInputStream().LA(1)==KW_NAMESPACE_NODE
                                || getInputStream().LA(1)==KW_NODE
                                || getInputStream().LA(1)==KW_PROCESSING_INSTRUCTION
                                || getInputStream().LA(1)==KW_SCHEMA_ATTRIBUTE
                                || getInputStream().LA(1)==KW_SCHEMA_ELEMENT
                                || getInputStream().LA(1)==KW_TEXT
                                ) 
         




