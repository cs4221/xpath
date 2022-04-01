# Generated from .\xpath\xpathgrammer\XPath.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XPathParser import XPathParser
else:
    from XPathParser import XPathParser

# This class defines a complete listener for a parse tree produced by XPathParser.
class XPathListener(ParseTreeListener):

    # Enter a parse tree produced by XPathParser#xpath.
    def enterXpath(self, ctx:XPathParser.XpathContext):
        pass

    # Exit a parse tree produced by XPathParser#xpath.
    def exitXpath(self, ctx:XPathParser.XpathContext):
        pass


    # Enter a parse tree produced by XPathParser#expr.
    def enterExpr(self, ctx:XPathParser.ExprContext):
        pass

    # Exit a parse tree produced by XPathParser#expr.
    def exitExpr(self, ctx:XPathParser.ExprContext):
        pass


    # Enter a parse tree produced by XPathParser#locationstepexpr.
    def enterLocationstepexpr(self, ctx:XPathParser.LocationstepexprContext):
        pass

    # Exit a parse tree produced by XPathParser#locationstepexpr.
    def exitLocationstepexpr(self, ctx:XPathParser.LocationstepexprContext):
        pass


    # Enter a parse tree produced by XPathParser#absolutepath.
    def enterAbsolutepath(self, ctx:XPathParser.AbsolutepathContext):
        pass

    # Exit a parse tree produced by XPathParser#absolutepath.
    def exitAbsolutepath(self, ctx:XPathParser.AbsolutepathContext):
        pass


    # Enter a parse tree produced by XPathParser#relativepath.
    def enterRelativepath(self, ctx:XPathParser.RelativepathContext):
        pass

    # Exit a parse tree produced by XPathParser#relativepath.
    def exitRelativepath(self, ctx:XPathParser.RelativepathContext):
        pass


    # Enter a parse tree produced by XPathParser#path.
    def enterPath(self, ctx:XPathParser.PathContext):
        pass

    # Exit a parse tree produced by XPathParser#path.
    def exitPath(self, ctx:XPathParser.PathContext):
        pass


    # Enter a parse tree produced by XPathParser#unqualifiedpath.
    def enterUnqualifiedpath(self, ctx:XPathParser.UnqualifiedpathContext):
        pass

    # Exit a parse tree produced by XPathParser#unqualifiedpath.
    def exitUnqualifiedpath(self, ctx:XPathParser.UnqualifiedpathContext):
        pass


    # Enter a parse tree produced by XPathParser#qualifiedpath.
    def enterQualifiedpath(self, ctx:XPathParser.QualifiedpathContext):
        pass

    # Exit a parse tree produced by XPathParser#qualifiedpath.
    def exitQualifiedpath(self, ctx:XPathParser.QualifiedpathContext):
        pass


    # Enter a parse tree produced by XPathParser#nodetest.
    def enterNodetest(self, ctx:XPathParser.NodetestContext):
        pass

    # Exit a parse tree produced by XPathParser#nodetest.
    def exitNodetest(self, ctx:XPathParser.NodetestContext):
        pass


    # Enter a parse tree produced by XPathParser#allselector.
    def enterAllselector(self, ctx:XPathParser.AllselectorContext):
        pass

    # Exit a parse tree produced by XPathParser#allselector.
    def exitAllselector(self, ctx:XPathParser.AllselectorContext):
        pass


    # Enter a parse tree produced by XPathParser#allnodeselector.
    def enterAllnodeselector(self, ctx:XPathParser.AllnodeselectorContext):
        pass

    # Exit a parse tree produced by XPathParser#allnodeselector.
    def exitAllnodeselector(self, ctx:XPathParser.AllnodeselectorContext):
        pass


    # Enter a parse tree produced by XPathParser#alltextselector.
    def enterAlltextselector(self, ctx:XPathParser.AlltextselectorContext):
        pass

    # Exit a parse tree produced by XPathParser#alltextselector.
    def exitAlltextselector(self, ctx:XPathParser.AlltextselectorContext):
        pass


    # Enter a parse tree produced by XPathParser#allcommentselector.
    def enterAllcommentselector(self, ctx:XPathParser.AllcommentselectorContext):
        pass

    # Exit a parse tree produced by XPathParser#allcommentselector.
    def exitAllcommentselector(self, ctx:XPathParser.AllcommentselectorContext):
        pass


    # Enter a parse tree produced by XPathParser#allprocessinginstructionselector.
    def enterAllprocessinginstructionselector(self, ctx:XPathParser.AllprocessinginstructionselectorContext):
        pass

    # Exit a parse tree produced by XPathParser#allprocessinginstructionselector.
    def exitAllprocessinginstructionselector(self, ctx:XPathParser.AllprocessinginstructionselectorContext):
        pass


    # Enter a parse tree produced by XPathParser#nodeselector.
    def enterNodeselector(self, ctx:XPathParser.NodeselectorContext):
        pass

    # Exit a parse tree produced by XPathParser#nodeselector.
    def exitNodeselector(self, ctx:XPathParser.NodeselectorContext):
        pass


    # Enter a parse tree produced by XPathParser#pred.
    def enterPred(self, ctx:XPathParser.PredContext):
        pass

    # Exit a parse tree produced by XPathParser#pred.
    def exitPred(self, ctx:XPathParser.PredContext):
        pass


    # Enter a parse tree produced by XPathParser#predexpr.
    def enterPredexpr(self, ctx:XPathParser.PredexprContext):
        pass

    # Exit a parse tree produced by XPathParser#predexpr.
    def exitPredexpr(self, ctx:XPathParser.PredexprContext):
        pass


    # Enter a parse tree produced by XPathParser#predexprsingle.
    def enterPredexprsingle(self, ctx:XPathParser.PredexprsingleContext):
        pass

    # Exit a parse tree produced by XPathParser#predexprsingle.
    def exitPredexprsingle(self, ctx:XPathParser.PredexprsingleContext):
        pass


    # Enter a parse tree produced by XPathParser#predpath.
    def enterPredpath(self, ctx:XPathParser.PredpathContext):
        pass

    # Exit a parse tree produced by XPathParser#predpath.
    def exitPredpath(self, ctx:XPathParser.PredpathContext):
        pass


    # Enter a parse tree produced by XPathParser#literal.
    def enterLiteral(self, ctx:XPathParser.LiteralContext):
        pass

    # Exit a parse tree produced by XPathParser#literal.
    def exitLiteral(self, ctx:XPathParser.LiteralContext):
        pass



del XPathParser