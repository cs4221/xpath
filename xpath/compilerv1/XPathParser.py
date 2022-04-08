# Generated from .\xpath\xpathgrammer\XPath.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u0093\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\3\3\3\7\3")
        buf.write("\62\n\3\f\3\16\3\65\13\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5B\n\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\5")
        buf.write("\bK\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13Y\n\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\7\23v\n\23\f")
        buf.write("\23\16\23y\13\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\7")
        buf.write("\25\u0082\n\25\f\25\16\25\u0085\13\25\3\25\3\25\3\25\7")
        buf.write("\25\u008a\n\25\f\25\16\25\u008d\13\25\5\25\u008f\n\25")
        buf.write("\3\26\3\26\3\26\2\2\27\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*\2\3\3\2?@\2\u0089\2,\3\2\2\2\4/\3\2\2\2")
        buf.write("\6\66\3\2\2\2\bA\3\2\2\2\nC\3\2\2\2\fF\3\2\2\2\16J\3\2")
        buf.write("\2\2\20L\3\2\2\2\22N\3\2\2\2\24X\3\2\2\2\26Z\3\2\2\2\30")
        buf.write("\\\3\2\2\2\32`\3\2\2\2\34d\3\2\2\2\36h\3\2\2\2 l\3\2\2")
        buf.write("\2\"n\3\2\2\2$r\3\2\2\2&z\3\2\2\2(\u008e\3\2\2\2*\u0090")
        buf.write("\3\2\2\2,-\5\4\3\2-.\7\2\2\3.\3\3\2\2\2/\63\5\6\4\2\60")
        buf.write("\62\5\b\5\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2")
        buf.write("\63\64\3\2\2\2\64\5\3\2\2\2\65\63\3\2\2\2\66\67\7\3\2")
        buf.write("\2\678\7\"\2\289\7@\2\29:\7\21\2\2:\7\3\2\2\2;<\7)\2\2")
        buf.write("<B\5\f\7\2=>\7)\2\2>?\5\f\7\2?@\5\"\22\2@B\3\2\2\2A;\3")
        buf.write("\2\2\2A=\3\2\2\2B\t\3\2\2\2CD\7)\2\2DE\5\16\b\2E\13\3")
        buf.write("\2\2\2FG\5\16\b\2G\r\3\2\2\2HK\5\20\t\2IK\5\22\n\2JH\3")
        buf.write("\2\2\2JI\3\2\2\2K\17\3\2\2\2LM\5\24\13\2M\21\3\2\2\2N")
        buf.write("O\7\4\2\2OP\7\17\2\2PQ\5\24\13\2Q\23\3\2\2\2RY\5\30\r")
        buf.write("\2SY\5\32\16\2TY\5\34\17\2UY\5\36\20\2VY\5\26\f\2WY\5")
        buf.write(" \21\2XR\3\2\2\2XS\3\2\2\2XT\3\2\2\2XU\3\2\2\2XV\3\2\2")
        buf.write("\2XW\3\2\2\2Y\25\3\2\2\2Z[\7+\2\2[\27\3\2\2\2\\]\7\66")
        buf.write("\2\2]^\7\"\2\2^_\7\21\2\2_\31\3\2\2\2`a\7>\2\2ab\7\"\2")
        buf.write("\2bc\7\21\2\2c\33\3\2\2\2de\7\61\2\2ef\7\"\2\2fg\7\21")
        buf.write("\2\2g\35\3\2\2\2hi\7<\2\2ij\7\"\2\2jk\7\21\2\2k\37\3\2")
        buf.write("\2\2lm\7\5\2\2m!\3\2\2\2no\7 \2\2op\5$\23\2pq\7\13\2\2")
        buf.write("q#\3\2\2\2rw\5&\24\2st\7\b\2\2tv\5&\24\2us\3\2\2\2vy\3")
        buf.write("\2\2\2wu\3\2\2\2wx\3\2\2\2x%\3\2\2\2yw\3\2\2\2z{\5(\25")
        buf.write("\2{|\7\7\2\2|}\5*\26\2}\'\3\2\2\2~\u0083\5\n\6\2\177\u0080")
        buf.write("\7)\2\2\u0080\u0082\5\f\7\2\u0081\177\3\2\2\2\u0082\u0085")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084")
        buf.write("\u008f\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u008b\5\f\7\2")
        buf.write("\u0087\u0088\7)\2\2\u0088\u008a\5\f\7\2\u0089\u0087\3")
        buf.write("\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008e")
        buf.write("~\3\2\2\2\u008e\u0086\3\2\2\2\u008f)\3\2\2\2\u0090\u0091")
        buf.write("\t\2\2\2\u0091+\3\2\2\2\n\63AJXw\u0083\u008b\u008e")
        return buf.getvalue()


class XPathParser ( Parser ):

    grammarFileName = "XPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'doc'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'@'", "'!'", "']'", "'}'", 
                     "':='", "':'", "'::'", "','", "')'", "':*'", "'.'", 
                     "'..'", "'$'", "'=>'", "'='", "'>='", "'>>'", "'>'", 
                     "'<='", "'<<'", "'<'", "'-'", "'!='", "'['", "'{'", 
                     "'('", "'|'", "'+'", "'#'", "'||'", "'?'", "'*:'", 
                     "'/'", "'//'", "'*'", "'ancestor'", "'ancestor-or-self'", 
                     "'and'", "'attribute'", "'child'", "'comment'", "'descendant'", 
                     "'descendant-or-self'", "'following'", "'following-sibling'", 
                     "'node'", "'not'", "'or'", "'parent'", "'preceding'", 
                     "'preceding-sibling'", "'processing-instruction'", 
                     "'self'", "'text'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "AXES", "NODE_NAME", "DOCUMENT_NAME", 
                      "PREDICATE_OPERATOR", "PREDICATE_CONNECTIVES", "AT", 
                      "BANG", "CB", "CC", "CEQ", "COLON", "COLONCOLON", 
                      "COMMA", "CP", "CS", "D", "DD", "DOLLAR", "EG", "EQ", 
                      "GE", "GG", "GT", "LE", "LL", "LT", "MINUS", "NE", 
                      "OB", "OC", "OP", "P", "PLUS", "POUND", "PP", "QM", 
                      "SC", "SLASH", "SS", "STAR", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", 
                      "KW_AND", "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", 
                      "KW_DESCENDANT", "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", 
                      "KW_FOLLOWING_SIBLING", "KW_NODE", "KW_NOT", "KW_OR", 
                      "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                      "KW_PROCESSING_INSTRUCTION", "KW_SELF", "KW_TEXT", 
                      "IntegerLiteral", "StringLiteral", "WS" ]

    RULE_xpath = 0
    RULE_expr = 1
    RULE_document = 2
    RULE_locationstepexpr = 3
    RULE_absolutepath = 4
    RULE_relativepath = 5
    RULE_path = 6
    RULE_unqualifiedpath = 7
    RULE_qualifiedpath = 8
    RULE_nodetest = 9
    RULE_allselector = 10
    RULE_allnodeselector = 11
    RULE_alltextselector = 12
    RULE_allcommentselector = 13
    RULE_allprocessinginstructionselector = 14
    RULE_nodeselector = 15
    RULE_pred = 16
    RULE_predexpr = 17
    RULE_predexprsingle = 18
    RULE_predpath = 19
    RULE_literal = 20

    ruleNames =  [ "xpath", "expr", "document", "locationstepexpr", "absolutepath", 
                   "relativepath", "path", "unqualifiedpath", "qualifiedpath", 
                   "nodetest", "allselector", "allnodeselector", "alltextselector", 
                   "allcommentselector", "allprocessinginstructionselector", 
                   "nodeselector", "pred", "predexpr", "predexprsingle", 
                   "predpath", "literal" ]

    EOF = Token.EOF
    T__0=1
    AXES=2
    NODE_NAME=3
    DOCUMENT_NAME=4
    PREDICATE_OPERATOR=5
    PREDICATE_CONNECTIVES=6
    AT=7
    BANG=8
    CB=9
    CC=10
    CEQ=11
    COLON=12
    COLONCOLON=13
    COMMA=14
    CP=15
    CS=16
    D=17
    DD=18
    DOLLAR=19
    EG=20
    EQ=21
    GE=22
    GG=23
    GT=24
    LE=25
    LL=26
    LT=27
    MINUS=28
    NE=29
    OB=30
    OC=31
    OP=32
    P=33
    PLUS=34
    POUND=35
    PP=36
    QM=37
    SC=38
    SLASH=39
    SS=40
    STAR=41
    KW_ANCESTOR=42
    KW_ANCESTOR_OR_SELF=43
    KW_AND=44
    KW_ATTRIBUTE=45
    KW_CHILD=46
    KW_COMMENT=47
    KW_DESCENDANT=48
    KW_DESCENDANT_OR_SELF=49
    KW_FOLLOWING=50
    KW_FOLLOWING_SIBLING=51
    KW_NODE=52
    KW_NOT=53
    KW_OR=54
    KW_PARENT=55
    KW_PRECEDING=56
    KW_PRECEDING_SIBLING=57
    KW_PROCESSING_INSTRUCTION=58
    KW_SELF=59
    KW_TEXT=60
    IntegerLiteral=61
    StringLiteral=62
    WS=63

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
            return self.getTypedRuleContext(XPathParser.ExprContext,0)


        def EOF(self):
            return self.getToken(XPathParser.EOF, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_xpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXpath" ):
                listener.enterXpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXpath" ):
                listener.exitXpath(self)




    def xpath(self):

        localctx = XPathParser.XpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_xpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.expr()
            self.state = 43
            self.match(XPathParser.EOF)
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

        def document(self):
            return self.getTypedRuleContext(XPathParser.DocumentContext,0)


        def locationstepexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPathParser.LocationstepexprContext)
            else:
                return self.getTypedRuleContext(XPathParser.LocationstepexprContext,i)


        def getRuleIndex(self):
            return XPathParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = XPathParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.document()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPathParser.SLASH:
                self.state = 46
                self.locationstepexpr()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DocumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP(self):
            return self.getToken(XPathParser.OP, 0)

        def StringLiteral(self):
            return self.getToken(XPathParser.StringLiteral, 0)

        def CP(self):
            return self.getToken(XPathParser.CP, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_document

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDocument" ):
                listener.enterDocument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDocument" ):
                listener.exitDocument(self)




    def document(self):

        localctx = XPathParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_document)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(XPathParser.T__0)
            self.state = 53
            self.match(XPathParser.OP)
            self.state = 54
            self.match(XPathParser.StringLiteral)
            self.state = 55
            self.match(XPathParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationstepexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(XPathParser.SLASH, 0)

        def relativepath(self):
            return self.getTypedRuleContext(XPathParser.RelativepathContext,0)


        def pred(self):
            return self.getTypedRuleContext(XPathParser.PredContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_locationstepexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocationstepexpr" ):
                listener.enterLocationstepexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocationstepexpr" ):
                listener.exitLocationstepexpr(self)




    def locationstepexpr(self):

        localctx = XPathParser.LocationstepexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_locationstepexpr)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(XPathParser.SLASH)
                self.state = 58
                self.relativepath()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(XPathParser.SLASH)
                self.state = 60
                self.relativepath()
                self.state = 61
                self.pred()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AbsolutepathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(XPathParser.SLASH, 0)

        def path(self):
            return self.getTypedRuleContext(XPathParser.PathContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_absolutepath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbsolutepath" ):
                listener.enterAbsolutepath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbsolutepath" ):
                listener.exitAbsolutepath(self)




    def absolutepath(self):

        localctx = XPathParser.AbsolutepathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_absolutepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(XPathParser.SLASH)
            self.state = 66
            self.path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelativepathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def path(self):
            return self.getTypedRuleContext(XPathParser.PathContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_relativepath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelativepath" ):
                listener.enterRelativepath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelativepath" ):
                listener.exitRelativepath(self)




    def relativepath(self):

        localctx = XPathParser.RelativepathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relativepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unqualifiedpath(self):
            return self.getTypedRuleContext(XPathParser.UnqualifiedpathContext,0)


        def qualifiedpath(self):
            return self.getTypedRuleContext(XPathParser.QualifiedpathContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)




    def path(self):

        localctx = XPathParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_path)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.NODE_NAME, XPathParser.STAR, XPathParser.KW_COMMENT, XPathParser.KW_NODE, XPathParser.KW_PROCESSING_INSTRUCTION, XPathParser.KW_TEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.unqualifiedpath()
                pass
            elif token in [XPathParser.AXES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.qualifiedpath()
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


    class UnqualifiedpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodetest(self):
            return self.getTypedRuleContext(XPathParser.NodetestContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_unqualifiedpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnqualifiedpath" ):
                listener.enterUnqualifiedpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnqualifiedpath" ):
                listener.exitUnqualifiedpath(self)




    def unqualifiedpath(self):

        localctx = XPathParser.UnqualifiedpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_unqualifiedpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.nodetest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualifiedpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AXES(self):
            return self.getToken(XPathParser.AXES, 0)

        def COLONCOLON(self):
            return self.getToken(XPathParser.COLONCOLON, 0)

        def nodetest(self):
            return self.getTypedRuleContext(XPathParser.NodetestContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_qualifiedpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQualifiedpath" ):
                listener.enterQualifiedpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQualifiedpath" ):
                listener.exitQualifiedpath(self)




    def qualifiedpath(self):

        localctx = XPathParser.QualifiedpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_qualifiedpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(XPathParser.AXES)
            self.state = 77
            self.match(XPathParser.COLONCOLON)
            self.state = 78
            self.nodetest()
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

        def allnodeselector(self):
            return self.getTypedRuleContext(XPathParser.AllnodeselectorContext,0)


        def alltextselector(self):
            return self.getTypedRuleContext(XPathParser.AlltextselectorContext,0)


        def allcommentselector(self):
            return self.getTypedRuleContext(XPathParser.AllcommentselectorContext,0)


        def allprocessinginstructionselector(self):
            return self.getTypedRuleContext(XPathParser.AllprocessinginstructionselectorContext,0)


        def allselector(self):
            return self.getTypedRuleContext(XPathParser.AllselectorContext,0)


        def nodeselector(self):
            return self.getTypedRuleContext(XPathParser.NodeselectorContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_nodetest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodetest" ):
                listener.enterNodetest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodetest" ):
                listener.exitNodetest(self)




    def nodetest(self):

        localctx = XPathParser.NodetestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nodetest)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.KW_NODE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.allnodeselector()
                pass
            elif token in [XPathParser.KW_TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.alltextselector()
                pass
            elif token in [XPathParser.KW_COMMENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.allcommentselector()
                pass
            elif token in [XPathParser.KW_PROCESSING_INSTRUCTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.allprocessinginstructionselector()
                pass
            elif token in [XPathParser.STAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.allselector()
                pass
            elif token in [XPathParser.NODE_NAME]:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.nodeselector()
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


    class AllselectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(XPathParser.STAR, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_allselector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllselector" ):
                listener.enterAllselector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllselector" ):
                listener.exitAllselector(self)




    def allselector(self):

        localctx = XPathParser.AllselectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_allselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(XPathParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllnodeselectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NODE(self):
            return self.getToken(XPathParser.KW_NODE, 0)

        def OP(self):
            return self.getToken(XPathParser.OP, 0)

        def CP(self):
            return self.getToken(XPathParser.CP, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_allnodeselector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllnodeselector" ):
                listener.enterAllnodeselector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllnodeselector" ):
                listener.exitAllnodeselector(self)




    def allnodeselector(self):

        localctx = XPathParser.AllnodeselectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_allnodeselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(XPathParser.KW_NODE)
            self.state = 91
            self.match(XPathParser.OP)
            self.state = 92
            self.match(XPathParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlltextselectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TEXT(self):
            return self.getToken(XPathParser.KW_TEXT, 0)

        def OP(self):
            return self.getToken(XPathParser.OP, 0)

        def CP(self):
            return self.getToken(XPathParser.CP, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_alltextselector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlltextselector" ):
                listener.enterAlltextselector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlltextselector" ):
                listener.exitAlltextselector(self)




    def alltextselector(self):

        localctx = XPathParser.AlltextselectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_alltextselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(XPathParser.KW_TEXT)
            self.state = 95
            self.match(XPathParser.OP)
            self.state = 96
            self.match(XPathParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllcommentselectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_COMMENT(self):
            return self.getToken(XPathParser.KW_COMMENT, 0)

        def OP(self):
            return self.getToken(XPathParser.OP, 0)

        def CP(self):
            return self.getToken(XPathParser.CP, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_allcommentselector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllcommentselector" ):
                listener.enterAllcommentselector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllcommentselector" ):
                listener.exitAllcommentselector(self)




    def allcommentselector(self):

        localctx = XPathParser.AllcommentselectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_allcommentselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(XPathParser.KW_COMMENT)
            self.state = 99
            self.match(XPathParser.OP)
            self.state = 100
            self.match(XPathParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllprocessinginstructionselectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PROCESSING_INSTRUCTION(self):
            return self.getToken(XPathParser.KW_PROCESSING_INSTRUCTION, 0)

        def OP(self):
            return self.getToken(XPathParser.OP, 0)

        def CP(self):
            return self.getToken(XPathParser.CP, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_allprocessinginstructionselector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllprocessinginstructionselector" ):
                listener.enterAllprocessinginstructionselector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllprocessinginstructionselector" ):
                listener.exitAllprocessinginstructionselector(self)




    def allprocessinginstructionselector(self):

        localctx = XPathParser.AllprocessinginstructionselectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_allprocessinginstructionselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(XPathParser.KW_PROCESSING_INSTRUCTION)
            self.state = 103
            self.match(XPathParser.OP)
            self.state = 104
            self.match(XPathParser.CP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeselectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODE_NAME(self):
            return self.getToken(XPathParser.NODE_NAME, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_nodeselector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeselector" ):
                listener.enterNodeselector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeselector" ):
                listener.exitNodeselector(self)




    def nodeselector(self):

        localctx = XPathParser.NodeselectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nodeselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(XPathParser.NODE_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(XPathParser.OB, 0)

        def predexpr(self):
            return self.getTypedRuleContext(XPathParser.PredexprContext,0)


        def CB(self):
            return self.getToken(XPathParser.CB, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_pred

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPred" ):
                listener.enterPred(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPred" ):
                listener.exitPred(self)




    def pred(self):

        localctx = XPathParser.PredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_pred)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(XPathParser.OB)
            self.state = 109
            self.predexpr()
            self.state = 110
            self.match(XPathParser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predexprsingle(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPathParser.PredexprsingleContext)
            else:
                return self.getTypedRuleContext(XPathParser.PredexprsingleContext,i)


        def PREDICATE_CONNECTIVES(self, i:int=None):
            if i is None:
                return self.getTokens(XPathParser.PREDICATE_CONNECTIVES)
            else:
                return self.getToken(XPathParser.PREDICATE_CONNECTIVES, i)

        def getRuleIndex(self):
            return XPathParser.RULE_predexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredexpr" ):
                listener.enterPredexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredexpr" ):
                listener.exitPredexpr(self)




    def predexpr(self):

        localctx = XPathParser.PredexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_predexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.predexprsingle()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPathParser.PREDICATE_CONNECTIVES:
                self.state = 113
                self.match(XPathParser.PREDICATE_CONNECTIVES)
                self.state = 114
                self.predexprsingle()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredexprsingleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def predpath(self):
            return self.getTypedRuleContext(XPathParser.PredpathContext,0)


        def PREDICATE_OPERATOR(self):
            return self.getToken(XPathParser.PREDICATE_OPERATOR, 0)

        def literal(self):
            return self.getTypedRuleContext(XPathParser.LiteralContext,0)


        def getRuleIndex(self):
            return XPathParser.RULE_predexprsingle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredexprsingle" ):
                listener.enterPredexprsingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredexprsingle" ):
                listener.exitPredexprsingle(self)




    def predexprsingle(self):

        localctx = XPathParser.PredexprsingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_predexprsingle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.predpath()
            self.state = 121
            self.match(XPathParser.PREDICATE_OPERATOR)
            self.state = 122
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def absolutepath(self):
            return self.getTypedRuleContext(XPathParser.AbsolutepathContext,0)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(XPathParser.SLASH)
            else:
                return self.getToken(XPathParser.SLASH, i)

        def relativepath(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XPathParser.RelativepathContext)
            else:
                return self.getTypedRuleContext(XPathParser.RelativepathContext,i)


        def getRuleIndex(self):
            return XPathParser.RULE_predpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredpath" ):
                listener.enterPredpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredpath" ):
                listener.exitPredpath(self)




    def predpath(self):

        localctx = XPathParser.PredpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_predpath)
        self._la = 0 # Token type
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.SLASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.absolutepath()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XPathParser.SLASH:
                    self.state = 125
                    self.match(XPathParser.SLASH)
                    self.state = 126
                    self.relativepath()
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [XPathParser.AXES, XPathParser.NODE_NAME, XPathParser.STAR, XPathParser.KW_COMMENT, XPathParser.KW_NODE, XPathParser.KW_PROCESSING_INSTRUCTION, XPathParser.KW_TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.relativepath()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XPathParser.SLASH:
                    self.state = 133
                    self.match(XPathParser.SLASH)
                    self.state = 134
                    self.relativepath()
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(XPathParser.IntegerLiteral, 0)

        def StringLiteral(self):
            return self.getToken(XPathParser.StringLiteral, 0)

        def getRuleIndex(self):
            return XPathParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = XPathParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==XPathParser.IntegerLiteral or _la==XPathParser.StringLiteral):
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





