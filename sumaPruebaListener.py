# Generated from ./sumaPrueba.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .sumaPruebaParser import sumaPruebaParser
else:
    from sumaPruebaParser import sumaPruebaParser

# This class defines a complete listener for a parse tree produced by sumaPruebaParser.
class sumaPruebaListener(ParseTreeListener):

    # Enter a parse tree produced by sumaPruebaParser#prog.
    def enterProg(self, ctx:sumaPruebaParser.ProgContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#prog.
    def exitProg(self, ctx:sumaPruebaParser.ProgContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#functionDef.
    def enterFunctionDef(self, ctx:sumaPruebaParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#functionDef.
    def exitFunctionDef(self, ctx:sumaPruebaParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#parameters.
    def enterParameters(self, ctx:sumaPruebaParser.ParametersContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#parameters.
    def exitParameters(self, ctx:sumaPruebaParser.ParametersContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#block.
    def enterBlock(self, ctx:sumaPruebaParser.BlockContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#block.
    def exitBlock(self, ctx:sumaPruebaParser.BlockContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#statement.
    def enterStatement(self, ctx:sumaPruebaParser.StatementContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#statement.
    def exitStatement(self, ctx:sumaPruebaParser.StatementContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#assignment.
    def enterAssignment(self, ctx:sumaPruebaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#assignment.
    def exitAssignment(self, ctx:sumaPruebaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#returnStatement.
    def enterReturnStatement(self, ctx:sumaPruebaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#returnStatement.
    def exitReturnStatement(self, ctx:sumaPruebaParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#printStatement.
    def enterPrintStatement(self, ctx:sumaPruebaParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#printStatement.
    def exitPrintStatement(self, ctx:sumaPruebaParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#FuncCall.
    def enterFuncCall(self, ctx:sumaPruebaParser.FuncCallContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#FuncCall.
    def exitFuncCall(self, ctx:sumaPruebaParser.FuncCallContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#Number.
    def enterNumber(self, ctx:sumaPruebaParser.NumberContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#Number.
    def exitNumber(self, ctx:sumaPruebaParser.NumberContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#AddSub.
    def enterAddSub(self, ctx:sumaPruebaParser.AddSubContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#AddSub.
    def exitAddSub(self, ctx:sumaPruebaParser.AddSubContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#MulDiv.
    def enterMulDiv(self, ctx:sumaPruebaParser.MulDivContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#MulDiv.
    def exitMulDiv(self, ctx:sumaPruebaParser.MulDivContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#Var.
    def enterVar(self, ctx:sumaPruebaParser.VarContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#Var.
    def exitVar(self, ctx:sumaPruebaParser.VarContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#Parens.
    def enterParens(self, ctx:sumaPruebaParser.ParensContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#Parens.
    def exitParens(self, ctx:sumaPruebaParser.ParensContext):
        pass


    # Enter a parse tree produced by sumaPruebaParser#functionCall.
    def enterFunctionCall(self, ctx:sumaPruebaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by sumaPruebaParser#functionCall.
    def exitFunctionCall(self, ctx:sumaPruebaParser.FunctionCallContext):
        pass



del sumaPruebaParser