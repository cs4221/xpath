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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u008c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\3\3\3\7\3\60\n\3\f")
        buf.write("\3\16\3\63\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4;\n\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\5\7D\n\7\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\5\nR\n\n\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\7\22o\n\22\f\22\16\22r\13\22\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\7\24{\n\24\f\24\16\24~\13\24\3\24\3\24\3\24")
        buf.write("\7\24\u0083\n\24\f\24\16\24\u0086\13\24\5\24\u0088\n\24")
        buf.write("\3\25\3\25\3\25\2\2\26\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(\2\3\3\2=>\2\u0083\2*\3\2\2\2\4-\3\2\2\2\6")
        buf.write(":\3\2\2\2\b<\3\2\2\2\n?\3\2\2\2\fC\3\2\2\2\16E\3\2\2\2")
        buf.write("\20G\3\2\2\2\22Q\3\2\2\2\24S\3\2\2\2\26U\3\2\2\2\30Y\3")
        buf.write("\2\2\2\32]\3\2\2\2\34a\3\2\2\2\36e\3\2\2\2 g\3\2\2\2\"")
        buf.write("k\3\2\2\2$s\3\2\2\2&\u0087\3\2\2\2(\u0089\3\2\2\2*+\5")
        buf.write("\4\3\2+,\7\2\2\3,\3\3\2\2\2-\61\5\6\4\2.\60\5\6\4\2/.")
        buf.write("\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\5")
        buf.write("\3\2\2\2\63\61\3\2\2\2\64\65\7\'\2\2\65;\5\n\6\2\66\67")
        buf.write("\7\'\2\2\678\5\n\6\289\5 \21\29;\3\2\2\2:\64\3\2\2\2:")
        buf.write("\66\3\2\2\2;\7\3\2\2\2<=\7\'\2\2=>\5\f\7\2>\t\3\2\2\2")
        buf.write("?@\5\f\7\2@\13\3\2\2\2AD\5\16\b\2BD\5\20\t\2CA\3\2\2\2")
        buf.write("CB\3\2\2\2D\r\3\2\2\2EF\5\22\n\2F\17\3\2\2\2GH\7\3\2\2")
        buf.write("HI\7\r\2\2IJ\5\22\n\2J\21\3\2\2\2KR\5\26\f\2LR\5\30\r")
        buf.write("\2MR\5\32\16\2NR\5\34\17\2OR\5\24\13\2PR\5\36\20\2QK\3")
        buf.write("\2\2\2QL\3\2\2\2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2QP\3\2\2")
        buf.write("\2R\23\3\2\2\2ST\7)\2\2T\25\3\2\2\2UV\7\64\2\2VW\7 \2")
        buf.write("\2WX\7\17\2\2X\27\3\2\2\2YZ\7<\2\2Z[\7 \2\2[\\\7\17\2")
        buf.write("\2\\\31\3\2\2\2]^\7/\2\2^_\7 \2\2_`\7\17\2\2`\33\3\2\2")
        buf.write("\2ab\7:\2\2bc\7 \2\2cd\7\17\2\2d\35\3\2\2\2ef\7\4\2\2")
        buf.write("f\37\3\2\2\2gh\7\36\2\2hi\5\"\22\2ij\7\t\2\2j!\3\2\2\2")
        buf.write("kp\5$\23\2lm\7\6\2\2mo\5$\23\2nl\3\2\2\2or\3\2\2\2pn\3")
        buf.write("\2\2\2pq\3\2\2\2q#\3\2\2\2rp\3\2\2\2st\5&\24\2tu\7\5\2")
        buf.write("\2uv\5(\25\2v%\3\2\2\2w|\5\b\5\2xy\7\'\2\2y{\5\n\6\2z")
        buf.write("x\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\u0088\3\2\2\2")
        buf.write("~|\3\2\2\2\177\u0084\5\n\6\2\u0080\u0081\7\'\2\2\u0081")
        buf.write("\u0083\5\n\6\2\u0082\u0080\3\2\2\2\u0083\u0086\3\2\2\2")
        buf.write("\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0088\3")
        buf.write("\2\2\2\u0086\u0084\3\2\2\2\u0087w\3\2\2\2\u0087\177\3")
        buf.write("\2\2\2\u0088\'\3\2\2\2\u0089\u008a\t\2\2\2\u008a)\3\2")
        buf.write("\2\2\n\61:CQp|\u0084\u0087")
        return buf.getvalue()


class XPathParser ( Parser ):

    grammarFileName = "XPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'@'", "'!'", "']'", "'}'", "':='", "':'", 
                     "'::'", "','", "')'", "':*'", "'.'", "'..'", "'$'", 
                     "'=>'", "'='", "'>='", "'>>'", "'>'", "'<='", "'<<'", 
                     "'<'", "'-'", "'!='", "'['", "'{'", "'('", "'|'", "'+'", 
                     "'#'", "'||'", "'?'", "'*:'", "'/'", "'//'", "'*'", 
                     "'ancestor'", "'ancestor-or-self'", "'and'", "'attribute'", 
                     "'child'", "'comment'", "'descendant'", "'descendant-or-self'", 
                     "'following'", "'following-sibling'", "'node'", "'not'", 
                     "'or'", "'parent'", "'preceding'", "'preceding-sibling'", 
                     "'processing-instruction'", "'self'", "'text'" ]

    symbolicNames = [ "<INVALID>", "AXES", "NODE_NAME", "PREDICATE_OPERATOR", 
                      "PREDICATE_CONNECTIVES", "AT", "BANG", "CB", "CC", 
                      "CEQ", "COLON", "COLONCOLON", "COMMA", "CP", "CS", 
                      "D", "DD", "DOLLAR", "EG", "EQ", "GE", "GG", "GT", 
                      "LE", "LL", "LT", "MINUS", "NE", "OB", "OC", "OP", 
                      "P", "PLUS", "POUND", "PP", "QM", "SC", "SLASH", "SS", 
                      "STAR", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", "KW_AND", 
                      "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", "KW_DESCENDANT", 
                      "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
                      "KW_NODE", "KW_NOT", "KW_OR", "KW_PARENT", "KW_PRECEDING", 
                      "KW_PRECEDING_SIBLING", "KW_PROCESSING_INSTRUCTION", 
                      "KW_SELF", "KW_TEXT", "IntegerLiteral", "StringLiteral", 
                      "WS" ]

    RULE_xpath = 0
    RULE_expr = 1
    RULE_locationstepexpr = 2
    RULE_absolutepath = 3
    RULE_relativepath = 4
    RULE_path = 5
    RULE_unqualifiedpath = 6
    RULE_qualifiedpath = 7
    RULE_nodetest = 8
    RULE_allselector = 9
    RULE_allnodeselector = 10
    RULE_alltextselector = 11
    RULE_allcommentselector = 12
    RULE_allprocessinginstructionselector = 13
    RULE_nodeselector = 14
    RULE_pred = 15
    RULE_predexpr = 16
    RULE_predexprsingle = 17
    RULE_predpath = 18
    RULE_literal = 19

    ruleNames =  [ "xpath", "expr", "locationstepexpr", "absolutepath", 
                   "relativepath", "path", "unqualifiedpath", "qualifiedpath", 
                   "nodetest", "allselector", "allnodeselector", "alltextselector", 
                   "allcommentselector", "allprocessinginstructionselector", 
                   "nodeselector", "pred", "predexpr", "predexprsingle", 
                   "predpath", "literal" ]

    EOF = Token.EOF
    AXES=1
    NODE_NAME=2
    PREDICATE_OPERATOR=3
    PREDICATE_CONNECTIVES=4
    AT=5
    BANG=6
    CB=7
    CC=8
    CEQ=9
    COLON=10
    COLONCOLON=11
    COMMA=12
    CP=13
    CS=14
    D=15
    DD=16
    DOLLAR=17
    EG=18
    EQ=19
    GE=20
    GG=21
    GT=22
    LE=23
    LL=24
    LT=25
    MINUS=26
    NE=27
    OB=28
    OC=29
    OP=30
    P=31
    PLUS=32
    POUND=33
    PP=34
    QM=35
    SC=36
    SLASH=37
    SS=38
    STAR=39
    KW_ANCESTOR=40
    KW_ANCESTOR_OR_SELF=41
    KW_AND=42
    KW_ATTRIBUTE=43
    KW_CHILD=44
    KW_COMMENT=45
    KW_DESCENDANT=46
    KW_DESCENDANT_OR_SELF=47
    KW_FOLLOWING=48
    KW_FOLLOWING_SIBLING=49
    KW_NODE=50
    KW_NOT=51
    KW_OR=52
    KW_PARENT=53
    KW_PRECEDING=54
    KW_PRECEDING_SIBLING=55
    KW_PROCESSING_INSTRUCTION=56
    KW_SELF=57
    KW_TEXT=58
    IntegerLiteral=59
    StringLiteral=60
    WS=61

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
            self.state = 40
            self.expr()
            self.state = 41
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
            self.state = 43
            self.locationstepexpr()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPathParser.SLASH:
                self.state = 44
                self.locationstepexpr()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 4, self.RULE_locationstepexpr)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(XPathParser.SLASH)
                self.state = 51
                self.relativepath()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(XPathParser.SLASH)
                self.state = 53
                self.relativepath()
                self.state = 54
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
        self.enterRule(localctx, 6, self.RULE_absolutepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(XPathParser.SLASH)
            self.state = 59
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
        self.enterRule(localctx, 8, self.RULE_relativepath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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
        self.enterRule(localctx, 10, self.RULE_path)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.NODE_NAME, XPathParser.STAR, XPathParser.KW_COMMENT, XPathParser.KW_NODE, XPathParser.KW_PROCESSING_INSTRUCTION, XPathParser.KW_TEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.unqualifiedpath()
                pass
            elif token in [XPathParser.AXES]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
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
        self.enterRule(localctx, 12, self.RULE_unqualifiedpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
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
        self.enterRule(localctx, 14, self.RULE_qualifiedpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(XPathParser.AXES)
            self.state = 70
            self.match(XPathParser.COLONCOLON)
            self.state = 71
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
        self.enterRule(localctx, 16, self.RULE_nodetest)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.KW_NODE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.allnodeselector()
                pass
            elif token in [XPathParser.KW_TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.alltextselector()
                pass
            elif token in [XPathParser.KW_COMMENT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.allcommentselector()
                pass
            elif token in [XPathParser.KW_PROCESSING_INSTRUCTION]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.allprocessinginstructionselector()
                pass
            elif token in [XPathParser.STAR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.allselector()
                pass
            elif token in [XPathParser.NODE_NAME]:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
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
        self.enterRule(localctx, 18, self.RULE_allselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
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
        self.enterRule(localctx, 20, self.RULE_allnodeselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(XPathParser.KW_NODE)
            self.state = 84
            self.match(XPathParser.OP)
            self.state = 85
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
        self.enterRule(localctx, 22, self.RULE_alltextselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(XPathParser.KW_TEXT)
            self.state = 88
            self.match(XPathParser.OP)
            self.state = 89
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
        self.enterRule(localctx, 24, self.RULE_allcommentselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(XPathParser.KW_COMMENT)
            self.state = 92
            self.match(XPathParser.OP)
            self.state = 93
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
        self.enterRule(localctx, 26, self.RULE_allprocessinginstructionselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(XPathParser.KW_PROCESSING_INSTRUCTION)
            self.state = 96
            self.match(XPathParser.OP)
            self.state = 97
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
        self.enterRule(localctx, 28, self.RULE_nodeselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
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
        self.enterRule(localctx, 30, self.RULE_pred)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(XPathParser.OB)
            self.state = 102
            self.predexpr()
            self.state = 103
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
        self.enterRule(localctx, 32, self.RULE_predexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.predexprsingle()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XPathParser.PREDICATE_CONNECTIVES:
                self.state = 106
                self.match(XPathParser.PREDICATE_CONNECTIVES)
                self.state = 107
                self.predexprsingle()
                self.state = 112
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
        self.enterRule(localctx, 34, self.RULE_predexprsingle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.predpath()
            self.state = 114
            self.match(XPathParser.PREDICATE_OPERATOR)
            self.state = 115
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
        self.enterRule(localctx, 36, self.RULE_predpath)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.SLASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.absolutepath()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XPathParser.SLASH:
                    self.state = 118
                    self.match(XPathParser.SLASH)
                    self.state = 119
                    self.relativepath()
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [XPathParser.AXES, XPathParser.NODE_NAME, XPathParser.STAR, XPathParser.KW_COMMENT, XPathParser.KW_NODE, XPathParser.KW_PROCESSING_INSTRUCTION, XPathParser.KW_TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.relativepath()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XPathParser.SLASH:
                    self.state = 126
                    self.match(XPathParser.SLASH)
                    self.state = 127
                    self.relativepath()
                    self.state = 132
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

        def StringLiteral(self):
            return self.getToken(XPathParser.StringLiteral, 0)

        def IntegerLiteral(self):
            return self.getToken(XPathParser.IntegerLiteral, 0)

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
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
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





