from antlr4 import *
from antlr.CppParserVisitor import CppParserVisitor
from antlr.CppParser import CppParser
from uml_generator import UMLGenerator

class UMLSequenceVisitor(CppParserVisitor):
    def __init__(self):
        self.uml = UMLGenerator()
        self.current_function = "Main" # main() je pocetna tacka
        self.known_objects = {} # mapa: varName -> className

    def visitFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        function_name = ctx.ID().getText()
        self.current_function = function_name
        self.uml.add_participant(function_name)
        print(f"Function definition: {function_name}") 
       
        # Posjeti tijelo funkcije
        self.visitChildren(ctx)
        return None
    
    def visitObjectDeclaration(self, ctx):
        var_type = ctx.ID(0).getText()
        var_name = ctx.ID(1).getText()
        print(f"Object declared: {var_name} of type {var_type}")
        self.known_objects[var_name] = var_type
        self.uml.add_participant(var_type)
        return None


    def visitMethodCall(self, ctx:CppParser.MethodCallContext):
        object_name = ctx.ID(0).getText()
        method_name = ctx.ID(1).getText()
        print(f"Method call: {object_name}.{method_name}()")

        if object_name in self.known_objects:
            class_name = self.known_objects[object_name]
            self.uml.add_call(self.current_function, class_name, method_name)

        return None

    def visitVariableDeclaration(self, ctx:CppParser.VariableDeclarationContext):
        if ctx.type() and ctx.ID():
            type_name = ctx.type().getText()
            var_name = ctx.ID().getText()
            print(f"Variable declared: {var_name} of type {type_name}")
            self.known_objects[var_name] = type_name
            self.uml.add_participant(type_name)
        return None
