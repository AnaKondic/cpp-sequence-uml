# Generated from CppParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CppParser import CppParser
else:
    from CppParser import CppParser

# This class defines a complete listener for a parse tree produced by CppParser.
class CppParserListener(ParseTreeListener):

    # Enter a parse tree produced by CppParser#program.
    def enterProgram(self, ctx:CppParser.ProgramContext):
        pass

    # Exit a parse tree produced by CppParser#program.
    def exitProgram(self, ctx:CppParser.ProgramContext):
        pass


    # Enter a parse tree produced by CppParser#preprocessorDirective.
    def enterPreprocessorDirective(self, ctx:CppParser.PreprocessorDirectiveContext):
        pass

    # Exit a parse tree produced by CppParser#preprocessorDirective.
    def exitPreprocessorDirective(self, ctx:CppParser.PreprocessorDirectiveContext):
        pass


    # Enter a parse tree produced by CppParser#classDeclaration.
    def enterClassDeclaration(self, ctx:CppParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#classDeclaration.
    def exitClassDeclaration(self, ctx:CppParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#classBody.
    def enterClassBody(self, ctx:CppParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by CppParser#classBody.
    def exitClassBody(self, ctx:CppParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by CppParser#accessModifier.
    def enterAccessModifier(self, ctx:CppParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by CppParser#accessModifier.
    def exitAccessModifier(self, ctx:CppParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by CppParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:CppParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:CppParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CppParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CppParser#parameterList.
    def enterParameterList(self, ctx:CppParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CppParser#parameterList.
    def exitParameterList(self, ctx:CppParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CppParser#type.
    def enterType(self, ctx:CppParser.TypeContext):
        pass

    # Exit a parse tree produced by CppParser#type.
    def exitType(self, ctx:CppParser.TypeContext):
        pass


    # Enter a parse tree produced by CppParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:CppParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:CppParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#statement.
    def enterStatement(self, ctx:CppParser.StatementContext):
        pass

    # Exit a parse tree produced by CppParser#statement.
    def exitStatement(self, ctx:CppParser.StatementContext):
        pass


    # Enter a parse tree produced by CppParser#methodCall.
    def enterMethodCall(self, ctx:CppParser.MethodCallContext):
        pass

    # Exit a parse tree produced by CppParser#methodCall.
    def exitMethodCall(self, ctx:CppParser.MethodCallContext):
        pass


    # Enter a parse tree produced by CppParser#argumentList.
    def enterArgumentList(self, ctx:CppParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by CppParser#argumentList.
    def exitArgumentList(self, ctx:CppParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by CppParser#expression.
    def enterExpression(self, ctx:CppParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CppParser#expression.
    def exitExpression(self, ctx:CppParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CppParser#shiftExpression.
    def enterShiftExpression(self, ctx:CppParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by CppParser#shiftExpression.
    def exitShiftExpression(self, ctx:CppParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by CppParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CppParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CppParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CppParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CppParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CppParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CppParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CppParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CppParser#postfixExpression.
    def enterPostfixExpression(self, ctx:CppParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by CppParser#postfixExpression.
    def exitPostfixExpression(self, ctx:CppParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by CppParser#postfixOp.
    def enterPostfixOp(self, ctx:CppParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by CppParser#postfixOp.
    def exitPostfixOp(self, ctx:CppParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by CppParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CppParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CppParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CppParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CppParser#assignement.
    def enterAssignement(self, ctx:CppParser.AssignementContext):
        pass

    # Exit a parse tree produced by CppParser#assignement.
    def exitAssignement(self, ctx:CppParser.AssignementContext):
        pass


    # Enter a parse tree produced by CppParser#objectDeclaration.
    def enterObjectDeclaration(self, ctx:CppParser.ObjectDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#objectDeclaration.
    def exitObjectDeclaration(self, ctx:CppParser.ObjectDeclarationContext):
        pass



del CppParser