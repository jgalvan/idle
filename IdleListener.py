# Generated from Idle.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IdleParser import IdleParser
else:
    from IdleParser import IdleParser

# This class defines a complete listener for a parse tree produced by IdleParser.
class IdleListener(ParseTreeListener):

    # Enter a parse tree produced by IdleParser#fileState.
    def enterFileState(self, ctx:IdleParser.FileStateContext):
        pass

    # Exit a parse tree produced by IdleParser#fileState.
    def exitFileState(self, ctx:IdleParser.FileStateContext):
        pass


    # Enter a parse tree produced by IdleParser#imp.
    def enterImp(self, ctx:IdleParser.ImpContext):
        pass

    # Exit a parse tree produced by IdleParser#imp.
    def exitImp(self, ctx:IdleParser.ImpContext):
        pass


    # Enter a parse tree produced by IdleParser#classState.
    def enterClassState(self, ctx:IdleParser.ClassStateContext):
        pass

    # Exit a parse tree produced by IdleParser#classState.
    def exitClassState(self, ctx:IdleParser.ClassStateContext):
        pass


    # Enter a parse tree produced by IdleParser#classBlock.
    def enterClassBlock(self, ctx:IdleParser.ClassBlockContext):
        pass

    # Exit a parse tree produced by IdleParser#classBlock.
    def exitClassBlock(self, ctx:IdleParser.ClassBlockContext):
        pass


    # Enter a parse tree produced by IdleParser#attribute.
    def enterAttribute(self, ctx:IdleParser.AttributeContext):
        pass

    # Exit a parse tree produced by IdleParser#attribute.
    def exitAttribute(self, ctx:IdleParser.AttributeContext):
        pass


    # Enter a parse tree produced by IdleParser#method.
    def enterMethod(self, ctx:IdleParser.MethodContext):
        pass

    # Exit a parse tree produced by IdleParser#method.
    def exitMethod(self, ctx:IdleParser.MethodContext):
        pass


    # Enter a parse tree produced by IdleParser#methodArguments.
    def enterMethodArguments(self, ctx:IdleParser.MethodArgumentsContext):
        pass

    # Exit a parse tree produced by IdleParser#methodArguments.
    def exitMethodArguments(self, ctx:IdleParser.MethodArgumentsContext):
        pass


    # Enter a parse tree produced by IdleParser#typeState.
    def enterTypeState(self, ctx:IdleParser.TypeStateContext):
        pass

    # Exit a parse tree produced by IdleParser#typeState.
    def exitTypeState(self, ctx:IdleParser.TypeStateContext):
        pass


    # Enter a parse tree produced by IdleParser#block.
    def enterBlock(self, ctx:IdleParser.BlockContext):
        pass

    # Exit a parse tree produced by IdleParser#block.
    def exitBlock(self, ctx:IdleParser.BlockContext):
        pass


    # Enter a parse tree produced by IdleParser#statement.
    def enterStatement(self, ctx:IdleParser.StatementContext):
        pass

    # Exit a parse tree produced by IdleParser#statement.
    def exitStatement(self, ctx:IdleParser.StatementContext):
        pass


    # Enter a parse tree produced by IdleParser#varsDecl.
    def enterVarsDecl(self, ctx:IdleParser.VarsDeclContext):
        pass

    # Exit a parse tree produced by IdleParser#varsDecl.
    def exitVarsDecl(self, ctx:IdleParser.VarsDeclContext):
        pass


    # Enter a parse tree produced by IdleParser#assignment.
    def enterAssignment(self, ctx:IdleParser.AssignmentContext):
        pass

    # Exit a parse tree produced by IdleParser#assignment.
    def exitAssignment(self, ctx:IdleParser.AssignmentContext):
        pass


    # Enter a parse tree produced by IdleParser#varsDeclAssignment.
    def enterVarsDeclAssignment(self, ctx:IdleParser.VarsDeclAssignmentContext):
        pass

    # Exit a parse tree produced by IdleParser#varsDeclAssignment.
    def exitVarsDeclAssignment(self, ctx:IdleParser.VarsDeclAssignmentContext):
        pass


    # Enter a parse tree produced by IdleParser#returnState.
    def enterReturnState(self, ctx:IdleParser.ReturnStateContext):
        pass

    # Exit a parse tree produced by IdleParser#returnState.
    def exitReturnState(self, ctx:IdleParser.ReturnStateContext):
        pass


    # Enter a parse tree produced by IdleParser#expression.
    def enterExpression(self, ctx:IdleParser.ExpressionContext):
        pass

    # Exit a parse tree produced by IdleParser#expression.
    def exitExpression(self, ctx:IdleParser.ExpressionContext):
        pass


    # Enter a parse tree produced by IdleParser#exp.
    def enterExp(self, ctx:IdleParser.ExpContext):
        pass

    # Exit a parse tree produced by IdleParser#exp.
    def exitExp(self, ctx:IdleParser.ExpContext):
        pass


    # Enter a parse tree produced by IdleParser#term.
    def enterTerm(self, ctx:IdleParser.TermContext):
        pass

    # Exit a parse tree produced by IdleParser#term.
    def exitTerm(self, ctx:IdleParser.TermContext):
        pass


    # Enter a parse tree produced by IdleParser#factor.
    def enterFactor(self, ctx:IdleParser.FactorContext):
        pass

    # Exit a parse tree produced by IdleParser#factor.
    def exitFactor(self, ctx:IdleParser.FactorContext):
        pass


    # Enter a parse tree produced by IdleParser#literal.
    def enterLiteral(self, ctx:IdleParser.LiteralContext):
        pass

    # Exit a parse tree produced by IdleParser#literal.
    def exitLiteral(self, ctx:IdleParser.LiteralContext):
        pass


    # Enter a parse tree produced by IdleParser#arrPos.
    def enterArrPos(self, ctx:IdleParser.ArrPosContext):
        pass

    # Exit a parse tree produced by IdleParser#arrPos.
    def exitArrPos(self, ctx:IdleParser.ArrPosContext):
        pass


    # Enter a parse tree produced by IdleParser#instanceVar.
    def enterInstanceVar(self, ctx:IdleParser.InstanceVarContext):
        pass

    # Exit a parse tree produced by IdleParser#instanceVar.
    def exitInstanceVar(self, ctx:IdleParser.InstanceVarContext):
        pass


    # Enter a parse tree produced by IdleParser#condition.
    def enterCondition(self, ctx:IdleParser.ConditionContext):
        pass

    # Exit a parse tree produced by IdleParser#condition.
    def exitCondition(self, ctx:IdleParser.ConditionContext):
        pass


    # Enter a parse tree produced by IdleParser#elseIf.
    def enterElseIf(self, ctx:IdleParser.ElseIfContext):
        pass

    # Exit a parse tree produced by IdleParser#elseIf.
    def exitElseIf(self, ctx:IdleParser.ElseIfContext):
        pass


    # Enter a parse tree produced by IdleParser#whileLoop.
    def enterWhileLoop(self, ctx:IdleParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by IdleParser#whileLoop.
    def exitWhileLoop(self, ctx:IdleParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by IdleParser#forLoop.
    def enterForLoop(self, ctx:IdleParser.ForLoopContext):
        pass

    # Exit a parse tree produced by IdleParser#forLoop.
    def exitForLoop(self, ctx:IdleParser.ForLoopContext):
        pass


    # Enter a parse tree produced by IdleParser#call.
    def enterCall(self, ctx:IdleParser.CallContext):
        pass

    # Exit a parse tree produced by IdleParser#call.
    def exitCall(self, ctx:IdleParser.CallContext):
        pass


    # Enter a parse tree produced by IdleParser#callArguments.
    def enterCallArguments(self, ctx:IdleParser.CallArgumentsContext):
        pass

    # Exit a parse tree produced by IdleParser#callArguments.
    def exitCallArguments(self, ctx:IdleParser.CallArgumentsContext):
        pass


    # Enter a parse tree produced by IdleParser#printState.
    def enterPrintState(self, ctx:IdleParser.PrintStateContext):
        pass

    # Exit a parse tree produced by IdleParser#printState.
    def exitPrintState(self, ctx:IdleParser.PrintStateContext):
        pass


    # Enter a parse tree produced by IdleParser#read.
    def enterRead(self, ctx:IdleParser.ReadContext):
        pass

    # Exit a parse tree produced by IdleParser#read.
    def exitRead(self, ctx:IdleParser.ReadContext):
        pass


