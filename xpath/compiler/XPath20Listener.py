# Generated from .\xpath\xpathgrammer\XPath20.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XPath20Parser import XPath20Parser
else:
    from XPath20Parser import XPath20Parser

# This class defines a complete listener for a parse tree produced by XPath20Parser.
class XPath20Listener(ParseTreeListener):

    # Enter a parse tree produced by XPath20Parser#xpath.
    def enterXpath(self, ctx:XPath20Parser.XpathContext):
        pass

    # Exit a parse tree produced by XPath20Parser#xpath.
    def exitXpath(self, ctx:XPath20Parser.XpathContext):
        pass


    # Enter a parse tree produced by XPath20Parser#expr.
    def enterExpr(self, ctx:XPath20Parser.ExprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#expr.
    def exitExpr(self, ctx:XPath20Parser.ExprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#exprsingle.
    def enterExprsingle(self, ctx:XPath20Parser.ExprsingleContext):
        pass

    # Exit a parse tree produced by XPath20Parser#exprsingle.
    def exitExprsingle(self, ctx:XPath20Parser.ExprsingleContext):
        pass


    # Enter a parse tree produced by XPath20Parser#forexpr.
    def enterForexpr(self, ctx:XPath20Parser.ForexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#forexpr.
    def exitForexpr(self, ctx:XPath20Parser.ForexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#simpleforclause.
    def enterSimpleforclause(self, ctx:XPath20Parser.SimpleforclauseContext):
        pass

    # Exit a parse tree produced by XPath20Parser#simpleforclause.
    def exitSimpleforclause(self, ctx:XPath20Parser.SimpleforclauseContext):
        pass


    # Enter a parse tree produced by XPath20Parser#quantifiedexpr.
    def enterQuantifiedexpr(self, ctx:XPath20Parser.QuantifiedexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#quantifiedexpr.
    def exitQuantifiedexpr(self, ctx:XPath20Parser.QuantifiedexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#ifexpr.
    def enterIfexpr(self, ctx:XPath20Parser.IfexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#ifexpr.
    def exitIfexpr(self, ctx:XPath20Parser.IfexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#orexpr.
    def enterOrexpr(self, ctx:XPath20Parser.OrexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#orexpr.
    def exitOrexpr(self, ctx:XPath20Parser.OrexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#andexpr.
    def enterAndexpr(self, ctx:XPath20Parser.AndexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#andexpr.
    def exitAndexpr(self, ctx:XPath20Parser.AndexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#comparisonexpr.
    def enterComparisonexpr(self, ctx:XPath20Parser.ComparisonexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#comparisonexpr.
    def exitComparisonexpr(self, ctx:XPath20Parser.ComparisonexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#rangeexpr.
    def enterRangeexpr(self, ctx:XPath20Parser.RangeexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#rangeexpr.
    def exitRangeexpr(self, ctx:XPath20Parser.RangeexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#additiveexpr.
    def enterAdditiveexpr(self, ctx:XPath20Parser.AdditiveexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#additiveexpr.
    def exitAdditiveexpr(self, ctx:XPath20Parser.AdditiveexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#multiplicativeexpr.
    def enterMultiplicativeexpr(self, ctx:XPath20Parser.MultiplicativeexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#multiplicativeexpr.
    def exitMultiplicativeexpr(self, ctx:XPath20Parser.MultiplicativeexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#unionexpr.
    def enterUnionexpr(self, ctx:XPath20Parser.UnionexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#unionexpr.
    def exitUnionexpr(self, ctx:XPath20Parser.UnionexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#intersectexceptexpr.
    def enterIntersectexceptexpr(self, ctx:XPath20Parser.IntersectexceptexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#intersectexceptexpr.
    def exitIntersectexceptexpr(self, ctx:XPath20Parser.IntersectexceptexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#instanceofexpr.
    def enterInstanceofexpr(self, ctx:XPath20Parser.InstanceofexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#instanceofexpr.
    def exitInstanceofexpr(self, ctx:XPath20Parser.InstanceofexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#treatexpr.
    def enterTreatexpr(self, ctx:XPath20Parser.TreatexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#treatexpr.
    def exitTreatexpr(self, ctx:XPath20Parser.TreatexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#castableexpr.
    def enterCastableexpr(self, ctx:XPath20Parser.CastableexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#castableexpr.
    def exitCastableexpr(self, ctx:XPath20Parser.CastableexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#castexpr.
    def enterCastexpr(self, ctx:XPath20Parser.CastexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#castexpr.
    def exitCastexpr(self, ctx:XPath20Parser.CastexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#unaryexpr.
    def enterUnaryexpr(self, ctx:XPath20Parser.UnaryexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#unaryexpr.
    def exitUnaryexpr(self, ctx:XPath20Parser.UnaryexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#valueexpr.
    def enterValueexpr(self, ctx:XPath20Parser.ValueexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#valueexpr.
    def exitValueexpr(self, ctx:XPath20Parser.ValueexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#generalcomp.
    def enterGeneralcomp(self, ctx:XPath20Parser.GeneralcompContext):
        pass

    # Exit a parse tree produced by XPath20Parser#generalcomp.
    def exitGeneralcomp(self, ctx:XPath20Parser.GeneralcompContext):
        pass


    # Enter a parse tree produced by XPath20Parser#valuecomp.
    def enterValuecomp(self, ctx:XPath20Parser.ValuecompContext):
        pass

    # Exit a parse tree produced by XPath20Parser#valuecomp.
    def exitValuecomp(self, ctx:XPath20Parser.ValuecompContext):
        pass


    # Enter a parse tree produced by XPath20Parser#nodecomp.
    def enterNodecomp(self, ctx:XPath20Parser.NodecompContext):
        pass

    # Exit a parse tree produced by XPath20Parser#nodecomp.
    def exitNodecomp(self, ctx:XPath20Parser.NodecompContext):
        pass


    # Enter a parse tree produced by XPath20Parser#pathexpr.
    def enterPathexpr(self, ctx:XPath20Parser.PathexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#pathexpr.
    def exitPathexpr(self, ctx:XPath20Parser.PathexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#relativepathexpr.
    def enterRelativepathexpr(self, ctx:XPath20Parser.RelativepathexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#relativepathexpr.
    def exitRelativepathexpr(self, ctx:XPath20Parser.RelativepathexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#stepexpr.
    def enterStepexpr(self, ctx:XPath20Parser.StepexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#stepexpr.
    def exitStepexpr(self, ctx:XPath20Parser.StepexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#axisstep.
    def enterAxisstep(self, ctx:XPath20Parser.AxisstepContext):
        pass

    # Exit a parse tree produced by XPath20Parser#axisstep.
    def exitAxisstep(self, ctx:XPath20Parser.AxisstepContext):
        pass


    # Enter a parse tree produced by XPath20Parser#forwardstep.
    def enterForwardstep(self, ctx:XPath20Parser.ForwardstepContext):
        pass

    # Exit a parse tree produced by XPath20Parser#forwardstep.
    def exitForwardstep(self, ctx:XPath20Parser.ForwardstepContext):
        pass


    # Enter a parse tree produced by XPath20Parser#forwardaxis.
    def enterForwardaxis(self, ctx:XPath20Parser.ForwardaxisContext):
        pass

    # Exit a parse tree produced by XPath20Parser#forwardaxis.
    def exitForwardaxis(self, ctx:XPath20Parser.ForwardaxisContext):
        pass


    # Enter a parse tree produced by XPath20Parser#abbrevforwardstep.
    def enterAbbrevforwardstep(self, ctx:XPath20Parser.AbbrevforwardstepContext):
        pass

    # Exit a parse tree produced by XPath20Parser#abbrevforwardstep.
    def exitAbbrevforwardstep(self, ctx:XPath20Parser.AbbrevforwardstepContext):
        pass


    # Enter a parse tree produced by XPath20Parser#reversestep.
    def enterReversestep(self, ctx:XPath20Parser.ReversestepContext):
        pass

    # Exit a parse tree produced by XPath20Parser#reversestep.
    def exitReversestep(self, ctx:XPath20Parser.ReversestepContext):
        pass


    # Enter a parse tree produced by XPath20Parser#reverseaxis.
    def enterReverseaxis(self, ctx:XPath20Parser.ReverseaxisContext):
        pass

    # Exit a parse tree produced by XPath20Parser#reverseaxis.
    def exitReverseaxis(self, ctx:XPath20Parser.ReverseaxisContext):
        pass


    # Enter a parse tree produced by XPath20Parser#abbrevreversestep.
    def enterAbbrevreversestep(self, ctx:XPath20Parser.AbbrevreversestepContext):
        pass

    # Exit a parse tree produced by XPath20Parser#abbrevreversestep.
    def exitAbbrevreversestep(self, ctx:XPath20Parser.AbbrevreversestepContext):
        pass


    # Enter a parse tree produced by XPath20Parser#nodetest.
    def enterNodetest(self, ctx:XPath20Parser.NodetestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#nodetest.
    def exitNodetest(self, ctx:XPath20Parser.NodetestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#nametest.
    def enterNametest(self, ctx:XPath20Parser.NametestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#nametest.
    def exitNametest(self, ctx:XPath20Parser.NametestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#wildcard.
    def enterWildcard(self, ctx:XPath20Parser.WildcardContext):
        pass

    # Exit a parse tree produced by XPath20Parser#wildcard.
    def exitWildcard(self, ctx:XPath20Parser.WildcardContext):
        pass


    # Enter a parse tree produced by XPath20Parser#filterexpr.
    def enterFilterexpr(self, ctx:XPath20Parser.FilterexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#filterexpr.
    def exitFilterexpr(self, ctx:XPath20Parser.FilterexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#predicatelist.
    def enterPredicatelist(self, ctx:XPath20Parser.PredicatelistContext):
        pass

    # Exit a parse tree produced by XPath20Parser#predicatelist.
    def exitPredicatelist(self, ctx:XPath20Parser.PredicatelistContext):
        pass


    # Enter a parse tree produced by XPath20Parser#predicate.
    def enterPredicate(self, ctx:XPath20Parser.PredicateContext):
        pass

    # Exit a parse tree produced by XPath20Parser#predicate.
    def exitPredicate(self, ctx:XPath20Parser.PredicateContext):
        pass


    # Enter a parse tree produced by XPath20Parser#primaryexpr.
    def enterPrimaryexpr(self, ctx:XPath20Parser.PrimaryexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#primaryexpr.
    def exitPrimaryexpr(self, ctx:XPath20Parser.PrimaryexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#literal.
    def enterLiteral(self, ctx:XPath20Parser.LiteralContext):
        pass

    # Exit a parse tree produced by XPath20Parser#literal.
    def exitLiteral(self, ctx:XPath20Parser.LiteralContext):
        pass


    # Enter a parse tree produced by XPath20Parser#numericliteral.
    def enterNumericliteral(self, ctx:XPath20Parser.NumericliteralContext):
        pass

    # Exit a parse tree produced by XPath20Parser#numericliteral.
    def exitNumericliteral(self, ctx:XPath20Parser.NumericliteralContext):
        pass


    # Enter a parse tree produced by XPath20Parser#varref.
    def enterVarref(self, ctx:XPath20Parser.VarrefContext):
        pass

    # Exit a parse tree produced by XPath20Parser#varref.
    def exitVarref(self, ctx:XPath20Parser.VarrefContext):
        pass


    # Enter a parse tree produced by XPath20Parser#varname.
    def enterVarname(self, ctx:XPath20Parser.VarnameContext):
        pass

    # Exit a parse tree produced by XPath20Parser#varname.
    def exitVarname(self, ctx:XPath20Parser.VarnameContext):
        pass


    # Enter a parse tree produced by XPath20Parser#parenthesizedexpr.
    def enterParenthesizedexpr(self, ctx:XPath20Parser.ParenthesizedexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#parenthesizedexpr.
    def exitParenthesizedexpr(self, ctx:XPath20Parser.ParenthesizedexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#contextitemexpr.
    def enterContextitemexpr(self, ctx:XPath20Parser.ContextitemexprContext):
        pass

    # Exit a parse tree produced by XPath20Parser#contextitemexpr.
    def exitContextitemexpr(self, ctx:XPath20Parser.ContextitemexprContext):
        pass


    # Enter a parse tree produced by XPath20Parser#functioncall.
    def enterFunctioncall(self, ctx:XPath20Parser.FunctioncallContext):
        pass

    # Exit a parse tree produced by XPath20Parser#functioncall.
    def exitFunctioncall(self, ctx:XPath20Parser.FunctioncallContext):
        pass


    # Enter a parse tree produced by XPath20Parser#singletype.
    def enterSingletype(self, ctx:XPath20Parser.SingletypeContext):
        pass

    # Exit a parse tree produced by XPath20Parser#singletype.
    def exitSingletype(self, ctx:XPath20Parser.SingletypeContext):
        pass


    # Enter a parse tree produced by XPath20Parser#sequencetype.
    def enterSequencetype(self, ctx:XPath20Parser.SequencetypeContext):
        pass

    # Exit a parse tree produced by XPath20Parser#sequencetype.
    def exitSequencetype(self, ctx:XPath20Parser.SequencetypeContext):
        pass


    # Enter a parse tree produced by XPath20Parser#occurrenceindicator.
    def enterOccurrenceindicator(self, ctx:XPath20Parser.OccurrenceindicatorContext):
        pass

    # Exit a parse tree produced by XPath20Parser#occurrenceindicator.
    def exitOccurrenceindicator(self, ctx:XPath20Parser.OccurrenceindicatorContext):
        pass


    # Enter a parse tree produced by XPath20Parser#itemtype.
    def enterItemtype(self, ctx:XPath20Parser.ItemtypeContext):
        pass

    # Exit a parse tree produced by XPath20Parser#itemtype.
    def exitItemtype(self, ctx:XPath20Parser.ItemtypeContext):
        pass


    # Enter a parse tree produced by XPath20Parser#atomictype.
    def enterAtomictype(self, ctx:XPath20Parser.AtomictypeContext):
        pass

    # Exit a parse tree produced by XPath20Parser#atomictype.
    def exitAtomictype(self, ctx:XPath20Parser.AtomictypeContext):
        pass


    # Enter a parse tree produced by XPath20Parser#kindtest.
    def enterKindtest(self, ctx:XPath20Parser.KindtestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#kindtest.
    def exitKindtest(self, ctx:XPath20Parser.KindtestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#anykindtest.
    def enterAnykindtest(self, ctx:XPath20Parser.AnykindtestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#anykindtest.
    def exitAnykindtest(self, ctx:XPath20Parser.AnykindtestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#documenttest.
    def enterDocumenttest(self, ctx:XPath20Parser.DocumenttestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#documenttest.
    def exitDocumenttest(self, ctx:XPath20Parser.DocumenttestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#texttest.
    def enterTexttest(self, ctx:XPath20Parser.TexttestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#texttest.
    def exitTexttest(self, ctx:XPath20Parser.TexttestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#commenttest.
    def enterCommenttest(self, ctx:XPath20Parser.CommenttestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#commenttest.
    def exitCommenttest(self, ctx:XPath20Parser.CommenttestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#pitest.
    def enterPitest(self, ctx:XPath20Parser.PitestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#pitest.
    def exitPitest(self, ctx:XPath20Parser.PitestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#attributetest.
    def enterAttributetest(self, ctx:XPath20Parser.AttributetestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#attributetest.
    def exitAttributetest(self, ctx:XPath20Parser.AttributetestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#attribnameorwildcard.
    def enterAttribnameorwildcard(self, ctx:XPath20Parser.AttribnameorwildcardContext):
        pass

    # Exit a parse tree produced by XPath20Parser#attribnameorwildcard.
    def exitAttribnameorwildcard(self, ctx:XPath20Parser.AttribnameorwildcardContext):
        pass


    # Enter a parse tree produced by XPath20Parser#schemaattributetest.
    def enterSchemaattributetest(self, ctx:XPath20Parser.SchemaattributetestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#schemaattributetest.
    def exitSchemaattributetest(self, ctx:XPath20Parser.SchemaattributetestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#attributedeclaration.
    def enterAttributedeclaration(self, ctx:XPath20Parser.AttributedeclarationContext):
        pass

    # Exit a parse tree produced by XPath20Parser#attributedeclaration.
    def exitAttributedeclaration(self, ctx:XPath20Parser.AttributedeclarationContext):
        pass


    # Enter a parse tree produced by XPath20Parser#elementtest.
    def enterElementtest(self, ctx:XPath20Parser.ElementtestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#elementtest.
    def exitElementtest(self, ctx:XPath20Parser.ElementtestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#elementnameorwildcard.
    def enterElementnameorwildcard(self, ctx:XPath20Parser.ElementnameorwildcardContext):
        pass

    # Exit a parse tree produced by XPath20Parser#elementnameorwildcard.
    def exitElementnameorwildcard(self, ctx:XPath20Parser.ElementnameorwildcardContext):
        pass


    # Enter a parse tree produced by XPath20Parser#schemaelementtest.
    def enterSchemaelementtest(self, ctx:XPath20Parser.SchemaelementtestContext):
        pass

    # Exit a parse tree produced by XPath20Parser#schemaelementtest.
    def exitSchemaelementtest(self, ctx:XPath20Parser.SchemaelementtestContext):
        pass


    # Enter a parse tree produced by XPath20Parser#elementdeclaration.
    def enterElementdeclaration(self, ctx:XPath20Parser.ElementdeclarationContext):
        pass

    # Exit a parse tree produced by XPath20Parser#elementdeclaration.
    def exitElementdeclaration(self, ctx:XPath20Parser.ElementdeclarationContext):
        pass


    # Enter a parse tree produced by XPath20Parser#attributename.
    def enterAttributename(self, ctx:XPath20Parser.AttributenameContext):
        pass

    # Exit a parse tree produced by XPath20Parser#attributename.
    def exitAttributename(self, ctx:XPath20Parser.AttributenameContext):
        pass


    # Enter a parse tree produced by XPath20Parser#elementname.
    def enterElementname(self, ctx:XPath20Parser.ElementnameContext):
        pass

    # Exit a parse tree produced by XPath20Parser#elementname.
    def exitElementname(self, ctx:XPath20Parser.ElementnameContext):
        pass


    # Enter a parse tree produced by XPath20Parser#typename_.
    def enterTypename_(self, ctx:XPath20Parser.Typename_Context):
        pass

    # Exit a parse tree produced by XPath20Parser#typename_.
    def exitTypename_(self, ctx:XPath20Parser.Typename_Context):
        pass


    # Enter a parse tree produced by XPath20Parser#qname.
    def enterQname(self, ctx:XPath20Parser.QnameContext):
        pass

    # Exit a parse tree produced by XPath20Parser#qname.
    def exitQname(self, ctx:XPath20Parser.QnameContext):
        pass


    # Enter a parse tree produced by XPath20Parser#auxilary.
    def enterAuxilary(self, ctx:XPath20Parser.AuxilaryContext):
        pass

    # Exit a parse tree produced by XPath20Parser#auxilary.
    def exitAuxilary(self, ctx:XPath20Parser.AuxilaryContext):
        pass



del XPath20Parser