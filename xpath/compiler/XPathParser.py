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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\5\6&\n\6\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2\2,\2\26\3\2\2")
        buf.write("\2\4\31\3\2\2\2\6\34\3\2\2\2\b\37\3\2\2\2\n%\3\2\2\2\f")
        buf.write("\'\3\2\2\2\16)\3\2\2\2\20,\3\2\2\2\22/\3\2\2\2\24\62\3")
        buf.write("\2\2\2\26\27\5\4\3\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32")
        buf.write("\7\3\2\2\32\33\5\b\5\2\33\5\3\2\2\2\34\35\7\4\2\2\35\36")
        buf.write("\7\5\2\2\36\7\3\2\2\2\37 \5\f\7\2 \t\3\2\2\2!\"\7\7\2")
        buf.write("\2\"#\7\6\2\2#&\7\n\2\2$&\3\2\2\2%!\3\2\2\2%$\3\2\2\2")
        buf.write("&\13\3\2\2\2\'(\7\n\2\2(\r\3\2\2\2)*\7\24\2\2*+\7\b\2")
        buf.write("\2+\17\3\2\2\2,-\7\32\2\2-.\7\b\2\2.\21\3\2\2\2/\60\7")
        buf.write("\17\2\2\60\61\7\b\2\2\61\23\3\2\2\2\62\63\7\30\2\2\63")
        buf.write("\64\7\b\2\2\64\25\3\2\2\2\3%")
        return buf.getvalue()


class XPathParser ( Parser ):

    grammarFileName = "XPath.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'['", "']'", "'::'", "<INVALID>", 
                     "'()'", "<INVALID>", "<INVALID>", "'ancestor'", "'ancestor-or-self'", 
                     "'attribute'", "'child'", "'comment'", "'descendant'", 
                     "'descendant-or-self'", "'following'", "'following-sibling'", 
                     "'node'", "'parent'", "'preceding'", "'preceding-sibling'", 
                     "'processing-instruction'", "'self'", "'text'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AXES", "FUNCTION_CALL", "OPERATOR", 
                      "NODE_NAME", "KW_ANCESTOR", "KW_ANCESTOR_OR_SELF", 
                      "KW_ATTRIBUTE", "KW_CHILD", "KW_COMMENT", "KW_DESCENDANT", 
                      "KW_DESCENDANT_OR_SELF", "KW_FOLLOWING", "KW_FOLLOWING_SIBLING", 
                      "KW_NODE", "KW_PARENT", "KW_PRECEDING", "KW_PRECEDING_SIBLING", 
                      "KW_PROCESSING_INSTRUCTION", "KW_SELF", "KW_TEXT", 
                      "WS" ]

    RULE_xpath = 0
    RULE_expr = 1
    RULE_pred = 2
    RULE_nodetest = 3
    RULE_qualifiedpath = 4
    RULE_unqualifiedpath = 5
    RULE_allnodeselector = 6
    RULE_alltextselector = 7
    RULE_allcommentselector = 8
    RULE_allprocessinginstructionselector = 9

    ruleNames =  [ "xpath", "expr", "pred", "nodetest", "qualifiedpath", 
                   "unqualifiedpath", "allnodeselector", "alltextselector", 
                   "allcommentselector", "allprocessinginstructionselector" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    AXES=5
    FUNCTION_CALL=6
    OPERATOR=7
    NODE_NAME=8
    KW_ANCESTOR=9
    KW_ANCESTOR_OR_SELF=10
    KW_ATTRIBUTE=11
    KW_CHILD=12
    KW_COMMENT=13
    KW_DESCENDANT=14
    KW_DESCENDANT_OR_SELF=15
    KW_FOLLOWING=16
    KW_FOLLOWING_SIBLING=17
    KW_NODE=18
    KW_PARENT=19
    KW_PRECEDING=20
    KW_PRECEDING_SIBLING=21
    KW_PROCESSING_INSTRUCTION=22
    KW_SELF=23
    KW_TEXT=24
    WS=25

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
            self.state = 20
            self.expr()
            self.state = 21
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

        def nodetest(self):
            return self.getTypedRuleContext(XPathParser.NodetestContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(XPathParser.T__0)
            self.state = 24
            self.nodetest()
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
        self.enterRule(localctx, 4, self.RULE_pred)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(XPathParser.T__1)
            self.state = 27
            self.match(XPathParser.T__2)
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

        def unqualifiedpath(self):
            return self.getTypedRuleContext(XPathParser.UnqualifiedpathContext,0)


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
        self.enterRule(localctx, 6, self.RULE_nodetest)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.unqualifiedpath()
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

        def NODE_NAME(self):
            return self.getToken(XPathParser.NODE_NAME, 0)

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
        self.enterRule(localctx, 8, self.RULE_qualifiedpath)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [XPathParser.AXES]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(XPathParser.AXES)
                self.state = 32
                self.match(XPathParser.T__3)
                self.state = 33
                self.match(XPathParser.NODE_NAME)
                pass
            elif token in [XPathParser.EOF]:
                self.enterOuterAlt(localctx, 2)

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

        def NODE_NAME(self):
            return self.getToken(XPathParser.NODE_NAME, 0)

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
        self.enterRule(localctx, 10, self.RULE_unqualifiedpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(XPathParser.NODE_NAME)
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

        def FUNCTION_CALL(self):
            return self.getToken(XPathParser.FUNCTION_CALL, 0)

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
        self.enterRule(localctx, 12, self.RULE_allnodeselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(XPathParser.KW_NODE)
            self.state = 40
            self.match(XPathParser.FUNCTION_CALL)
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

        def FUNCTION_CALL(self):
            return self.getToken(XPathParser.FUNCTION_CALL, 0)

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
        self.enterRule(localctx, 14, self.RULE_alltextselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(XPathParser.KW_TEXT)
            self.state = 43
            self.match(XPathParser.FUNCTION_CALL)
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

        def FUNCTION_CALL(self):
            return self.getToken(XPathParser.FUNCTION_CALL, 0)

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
        self.enterRule(localctx, 16, self.RULE_allcommentselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(XPathParser.KW_COMMENT)
            self.state = 46
            self.match(XPathParser.FUNCTION_CALL)
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

        def FUNCTION_CALL(self):
            return self.getToken(XPathParser.FUNCTION_CALL, 0)

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
        self.enterRule(localctx, 18, self.RULE_allprocessinginstructionselector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(XPathParser.KW_PROCESSING_INSTRUCTION)
            self.state = 49
            self.match(XPathParser.FUNCTION_CALL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





