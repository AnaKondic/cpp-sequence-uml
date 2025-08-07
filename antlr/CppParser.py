# Generated from CppParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,156,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,5,3,55,8,3,10,
        3,12,3,58,9,3,1,4,3,4,61,8,4,1,4,1,4,1,4,1,4,3,4,67,8,4,1,4,1,4,
        1,4,5,4,72,8,4,10,4,12,4,75,9,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,83,8,
        5,1,5,1,5,1,5,5,5,88,8,5,10,5,12,5,91,9,5,1,5,1,5,1,6,1,6,1,6,5,
        6,98,8,6,10,6,12,6,101,9,6,1,7,1,7,3,7,105,8,7,1,7,1,7,1,8,1,8,1,
        8,1,8,3,8,113,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,128,8,9,1,10,1,10,1,10,1,10,1,10,3,10,135,8,10,1,10,1,
        10,1,11,1,11,1,11,5,11,142,8,11,10,11,12,11,145,9,11,1,12,1,12,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,0,0,15,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,0,2,2,0,4,10,32,32,1,0,32,34,159,0,36,1,0,0,
        0,2,41,1,0,0,0,4,46,1,0,0,0,6,56,1,0,0,0,8,60,1,0,0,0,10,78,1,0,
        0,0,12,94,1,0,0,0,14,104,1,0,0,0,16,108,1,0,0,0,18,127,1,0,0,0,20,
        129,1,0,0,0,22,138,1,0,0,0,24,146,1,0,0,0,26,148,1,0,0,0,28,152,
        1,0,0,0,30,35,3,2,1,0,31,35,3,4,2,0,32,35,3,10,5,0,33,35,3,18,9,
        0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,38,
        1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,36,1,0,0,0,
        39,40,5,0,0,1,40,1,1,0,0,0,41,42,5,17,0,0,42,43,5,30,0,0,43,44,5,
        32,0,0,44,45,5,31,0,0,45,3,1,0,0,0,46,47,5,1,0,0,47,48,5,32,0,0,
        48,49,5,18,0,0,49,50,3,6,3,0,50,51,5,19,0,0,51,5,1,0,0,0,52,55,3,
        8,4,0,53,55,3,16,8,0,54,52,1,0,0,0,54,53,1,0,0,0,55,58,1,0,0,0,56,
        54,1,0,0,0,56,57,1,0,0,0,57,7,1,0,0,0,58,56,1,0,0,0,59,61,5,2,0,
        0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,3,14,7,0,63,64,
        5,32,0,0,64,66,5,20,0,0,65,67,3,12,6,0,66,65,1,0,0,0,66,67,1,0,0,
        0,67,68,1,0,0,0,68,69,5,21,0,0,69,73,5,18,0,0,70,72,3,18,9,0,71,
        70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,
        0,75,73,1,0,0,0,76,77,5,19,0,0,77,9,1,0,0,0,78,79,3,14,7,0,79,80,
        5,32,0,0,80,82,5,20,0,0,81,83,3,12,6,0,82,81,1,0,0,0,82,83,1,0,0,
        0,83,84,1,0,0,0,84,85,5,21,0,0,85,89,5,18,0,0,86,88,3,18,9,0,87,
        86,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,92,1,0,0,
        0,91,89,1,0,0,0,92,93,5,19,0,0,93,11,1,0,0,0,94,99,3,16,8,0,95,96,
        5,23,0,0,96,98,3,16,8,0,97,95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,
        0,99,100,1,0,0,0,100,13,1,0,0,0,101,99,1,0,0,0,102,103,5,11,0,0,
        103,105,5,27,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,
        106,107,7,0,0,0,107,15,1,0,0,0,108,109,3,14,7,0,109,112,5,32,0,0,
        110,111,5,25,0,0,111,113,3,24,12,0,112,110,1,0,0,0,112,113,1,0,0,
        0,113,17,1,0,0,0,114,115,3,20,10,0,115,116,5,22,0,0,116,128,1,0,
        0,0,117,118,3,28,14,0,118,119,5,22,0,0,119,128,1,0,0,0,120,121,3,
        26,13,0,121,122,5,22,0,0,122,128,1,0,0,0,123,124,5,12,0,0,124,125,
        3,24,12,0,125,126,5,22,0,0,126,128,1,0,0,0,127,114,1,0,0,0,127,117,
        1,0,0,0,127,120,1,0,0,0,127,123,1,0,0,0,128,19,1,0,0,0,129,130,5,
        32,0,0,130,131,5,24,0,0,131,132,5,32,0,0,132,134,5,20,0,0,133,135,
        3,22,11,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,
        5,21,0,0,137,21,1,0,0,0,138,143,3,24,12,0,139,140,5,23,0,0,140,142,
        3,24,12,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,23,1,0,0,0,145,143,1,0,0,0,146,147,7,1,0,0,147,25,1,
        0,0,0,148,149,5,32,0,0,149,150,5,25,0,0,150,151,3,24,12,0,151,27,
        1,0,0,0,152,153,5,32,0,0,153,154,5,32,0,0,154,29,1,0,0,0,15,34,36,
        54,56,60,66,73,82,89,99,104,112,127,134,143
    ]

class CppParser ( Parser ):

    grammarFileName = "CppParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'public'", "'private'", "'void'", 
                     "'int'", "'float'", "'double'", "'char'", "'bool'", 
                     "'string'", "'std'", "'return'", "'new'", "'if'", "'else'", 
                     "'while'", "'#include'", "'{'", "'}'", "'('", "')'", 
                     "';'", "','", "'.'", "'='", "'\"'", "'::'", "'<<'", 
                     "'>>'", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "PUBLIC", "PRIVATE", "VOID", 
                      "INT", "FLOAT", "DOUBLE", "CHAR", "BOOL", "STRING", 
                      "STD", "RETURN", "NEW", "IF", "ELSE", "WHILE", "INCLUDE", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "SEMI", "COMMA", 
                      "DOT", "ASSIGN", "QUOTE", "COLONCOLON", "LEFT_SHIFT", 
                      "RIGHT_SHIFT", "LT", "GT", "ID", "NUMBER", "STRING_LITERAL", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_preprocessorDirective = 1
    RULE_classDeclaration = 2
    RULE_classBody = 3
    RULE_methodDeclaration = 4
    RULE_functionDefinition = 5
    RULE_parameterList = 6
    RULE_type = 7
    RULE_variableDeclaration = 8
    RULE_statement = 9
    RULE_methodCall = 10
    RULE_argumentList = 11
    RULE_expression = 12
    RULE_assignement = 13
    RULE_objectDeclaration = 14

    ruleNames =  [ "program", "preprocessorDirective", "classDeclaration", 
                   "classBody", "methodDeclaration", "functionDefinition", 
                   "parameterList", "type", "variableDeclaration", "statement", 
                   "methodCall", "argumentList", "expression", "assignement", 
                   "objectDeclaration" ]

    EOF = Token.EOF
    CLASS=1
    PUBLIC=2
    PRIVATE=3
    VOID=4
    INT=5
    FLOAT=6
    DOUBLE=7
    CHAR=8
    BOOL=9
    STRING=10
    STD=11
    RETURN=12
    NEW=13
    IF=14
    ELSE=15
    WHILE=16
    INCLUDE=17
    LBRACE=18
    RBRACE=19
    LPAREN=20
    RPAREN=21
    SEMI=22
    COMMA=23
    DOT=24
    ASSIGN=25
    QUOTE=26
    COLONCOLON=27
    LEFT_SHIFT=28
    RIGHT_SHIFT=29
    LT=30
    GT=31
    ID=32
    NUMBER=33
    STRING_LITERAL=34
    LINE_COMMENT=35
    BLOCK_COMMENT=36
    WS=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CppParser.EOF, 0)

        def preprocessorDirective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.PreprocessorDirectiveContext)
            else:
                return self.getTypedRuleContext(CppParser.PreprocessorDirectiveContext,i)


        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(CppParser.ClassDeclarationContext,i)


        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(CppParser.FunctionDefinitionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.StatementContext)
            else:
                return self.getTypedRuleContext(CppParser.StatementContext,i)


        def getRuleIndex(self):
            return CppParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CppParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4295106546) != 0):
                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.preprocessorDirective()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.classDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 32
                    self.functionDefinition()
                    pass

                elif la_ == 4:
                    self.state = 33
                    self.statement()
                    pass


                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(CppParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreprocessorDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCLUDE(self):
            return self.getToken(CppParser.INCLUDE, 0)

        def LT(self):
            return self.getToken(CppParser.LT, 0)

        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def GT(self):
            return self.getToken(CppParser.GT, 0)

        def getRuleIndex(self):
            return CppParser.RULE_preprocessorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreprocessorDirective" ):
                listener.enterPreprocessorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreprocessorDirective" ):
                listener.exitPreprocessorDirective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreprocessorDirective" ):
                return visitor.visitPreprocessorDirective(self)
            else:
                return visitor.visitChildren(self)




    def preprocessorDirective(self):

        localctx = CppParser.PreprocessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_preprocessorDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(CppParser.INCLUDE)
            self.state = 42
            self.match(CppParser.LT)
            self.state = 43
            self.match(CppParser.ID)
            self.state = 44
            self.match(CppParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CppParser.CLASS, 0)

        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def classBody(self):
            return self.getTypedRuleContext(CppParser.ClassBodyContext,0)


        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def getRuleIndex(self):
            return CppParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = CppParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(CppParser.CLASS)
            self.state = 47
            self.match(CppParser.ID)
            self.state = 48
            self.match(CppParser.LBRACE)
            self.state = 49
            self.classBody()
            self.state = 50
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(CppParser.MethodDeclarationContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(CppParser.VariableDeclarationContext,i)


        def getRuleIndex(self):
            return CppParser.RULE_classBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBody" ):
                listener.enterClassBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBody" ):
                listener.exitClassBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassBody" ):
                return visitor.visitClassBody(self)
            else:
                return visitor.visitChildren(self)




    def classBody(self):

        localctx = CppParser.ClassBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294971380) != 0):
                self.state = 54
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.methodDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 53
                    self.variableDeclaration()
                    pass


                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CppParser.TypeContext,0)


        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def PUBLIC(self):
            return self.getToken(CppParser.PUBLIC, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.StatementContext)
            else:
                return self.getTypedRuleContext(CppParser.StatementContext,i)


        def getRuleIndex(self):
            return CppParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = CppParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 59
                self.match(CppParser.PUBLIC)


            self.state = 62
            self.type_()
            self.state = 63
            self.match(CppParser.ID)
            self.state = 64
            self.match(CppParser.LPAREN)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294971376) != 0):
                self.state = 65
                self.parameterList()


            self.state = 68
            self.match(CppParser.RPAREN)
            self.state = 69
            self.match(CppParser.LBRACE)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==32:
                self.state = 70
                self.statement()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CppParser.TypeContext,0)


        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CppParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CppParser.RBRACE, 0)

        def parameterList(self):
            return self.getTypedRuleContext(CppParser.ParameterListContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.StatementContext)
            else:
                return self.getTypedRuleContext(CppParser.StatementContext,i)


        def getRuleIndex(self):
            return CppParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = CppParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.type_()
            self.state = 79
            self.match(CppParser.ID)
            self.state = 80
            self.match(CppParser.LPAREN)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4294971376) != 0):
                self.state = 81
                self.parameterList()


            self.state = 84
            self.match(CppParser.RPAREN)
            self.state = 85
            self.match(CppParser.LBRACE)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==32:
                self.state = 86
                self.statement()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(CppParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(CppParser.VariableDeclarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = CppParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.variableDeclaration()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 95
                self.match(CppParser.COMMA)
                self.state = 96
                self.variableDeclaration()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(CppParser.VOID, 0)

        def STRING(self):
            return self.getToken(CppParser.STRING, 0)

        def CHAR(self):
            return self.getToken(CppParser.CHAR, 0)

        def INT(self):
            return self.getToken(CppParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CppParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(CppParser.DOUBLE, 0)

        def BOOL(self):
            return self.getToken(CppParser.BOOL, 0)

        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def STD(self):
            return self.getToken(CppParser.STD, 0)

        def COLONCOLON(self):
            return self.getToken(CppParser.COLONCOLON, 0)

        def getRuleIndex(self):
            return CppParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = CppParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 102
                self.match(CppParser.STD)
                self.state = 103
                self.match(CppParser.COLONCOLON)


            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4294969328) != 0)):
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


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(CppParser.TypeContext,0)


        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CppParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CppParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = CppParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.type_()
            self.state = 109
            self.match(CppParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 110
                self.match(CppParser.ASSIGN)
                self.state = 111
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodCall(self):
            return self.getTypedRuleContext(CppParser.MethodCallContext,0)


        def SEMI(self):
            return self.getToken(CppParser.SEMI, 0)

        def objectDeclaration(self):
            return self.getTypedRuleContext(CppParser.ObjectDeclarationContext,0)


        def assignement(self):
            return self.getTypedRuleContext(CppParser.AssignementContext,0)


        def RETURN(self):
            return self.getToken(CppParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(CppParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CppParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.methodCall()
                self.state = 115
                self.match(CppParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.objectDeclaration()
                self.state = 118
                self.match(CppParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.assignement()
                self.state = 121
                self.match(CppParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.match(CppParser.RETURN)
                self.state = 124
                self.expression()
                self.state = 125
                self.match(CppParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ID)
            else:
                return self.getToken(CppParser.ID, i)

        def DOT(self):
            return self.getToken(CppParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(CppParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CppParser.RPAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(CppParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_methodCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = CppParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methodCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(CppParser.ID)
            self.state = 130
            self.match(CppParser.DOT)
            self.state = 131
            self.match(CppParser.ID)
            self.state = 132
            self.match(CppParser.LPAREN)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0):
                self.state = 133
                self.argumentList()


            self.state = 136
            self.match(CppParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CppParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CppParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.COMMA)
            else:
                return self.getToken(CppParser.COMMA, i)

        def getRuleIndex(self):
            return CppParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = CppParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expression()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 139
                self.match(CppParser.COMMA)
                self.state = 140
                self.expression()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def NUMBER(self):
            return self.getToken(CppParser.NUMBER, 0)

        def STRING_LITERAL(self):
            return self.getToken(CppParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return CppParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CppParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
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


    class AssignementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CppParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CppParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CppParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CppParser.RULE_assignement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignement" ):
                listener.enterAssignement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignement" ):
                listener.exitAssignement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignement" ):
                return visitor.visitAssignement(self)
            else:
                return visitor.visitChildren(self)




    def assignement(self):

        localctx = CppParser.AssignementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CppParser.ID)
            self.state = 149
            self.match(CppParser.ASSIGN)
            self.state = 150
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CppParser.ID)
            else:
                return self.getToken(CppParser.ID, i)

        def getRuleIndex(self):
            return CppParser.RULE_objectDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObjectDeclaration" ):
                listener.enterObjectDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObjectDeclaration" ):
                listener.exitObjectDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectDeclaration" ):
                return visitor.visitObjectDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def objectDeclaration(self):

        localctx = CppParser.ObjectDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_objectDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(CppParser.ID)
            self.state = 153
            self.match(CppParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





