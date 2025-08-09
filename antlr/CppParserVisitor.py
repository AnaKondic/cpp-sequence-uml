# Generated from CppParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CppParser import CppParser
else:
    from CppParser import CppParser

# This class defines a complete generic visitor for a parse tree produced by CppParser.

class CppParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CppParser#program.
    def visitProgram(self, ctx:CppParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#preprocessorDirective.
    def visitPreprocessorDirective(self, ctx:CppParser.PreprocessorDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CppParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#classBody.
    def visitClassBody(self, ctx:CppParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#accessModifier.
    def visitAccessModifier(self, ctx:CppParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:CppParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#parameterList.
    def visitParameterList(self, ctx:CppParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#type.
    def visitType(self, ctx:CppParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CppParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#statement.
    def visitStatement(self, ctx:CppParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#methodCall.
    def visitMethodCall(self, ctx:CppParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#argumentList.
    def visitArgumentList(self, ctx:CppParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#expression.
    def visitExpression(self, ctx:CppParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#shiftExpression.
    def visitShiftExpression(self, ctx:CppParser.ShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CppParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CppParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#postfixExpression.
    def visitPostfixExpression(self, ctx:CppParser.PostfixExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#postfixOp.
    def visitPostfixOp(self, ctx:CppParser.PostfixOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CppParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#assignement.
    def visitAssignement(self, ctx:CppParser.AssignementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CppParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:CppParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)



del CppParser