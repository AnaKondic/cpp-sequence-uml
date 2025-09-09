from antlr4 import *
from antlr.CppParserVisitor import CppParserVisitor
from antlr.CppParser import CppParser
from uml_generator import UMLGenerator

class UMLSequenceVisitor(CppParserVisitor):
    def __init__(self, symbol_table):
        super().__init__()
        self.uml = UMLGenerator()
        self.symbol_table = symbol_table  # simbolička tabela iz SemanticAnalyzer
        self.current_class = None
        self.call_stack = [] # trenutni pozivaoc
        self.known_objects = {} # mapa: varName -> className

    # Program root
    def visitProgram(self, ctx:CppParser.ProgramContext):
        print("Starting UML generation from program root...")
        # Pronađi main funkciju
        for func_ctx in ctx.functionDefinition():
             if func_ctx.ID().getText() == "main":
                self.visitFunctionDefinition(func_ctx)
                break
        return None
    
    # Posjeta deklaraciji klase
    def visitClassDeclaration(self, ctx:CppParser.ClassDeclarationContext):
        class_name = ctx.ID().getText()
        print(f"Class declaration: {class_name}")
        self.current_class = class_name

        self.visitChildren(ctx)
        self.current_class = None  
        return None

    # Posjeta globalnoj funkciji
    def visitFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        function_name = ctx.ID().getText()

        if function_name == "main":
            caller = "Main"
        elif self.current_class:
            caller = self.current_class
        else:
            caller = function_name   

        print(f"Function definition: {function_name} (caller={caller})") 
       
        self.call_stack.append(caller)
        self.visitChildren(ctx)
        self.call_stack.pop()
        return None
    
    # Posjeta definiciji metode
    def visitMethodDefinition(self, ctx:CppParser.MethodDefinitionContext):
        method_name = ctx.ID().getText()
        class_name = self.current_class if self.current_class else "UnknownClass"

         # Privremeni scope za ovu metodu
        old_known_objects = self.known_objects.copy()

        # Dodaj atribute klase u poznate objekte
        if self.current_class in self.symbol_table:
            for var in self.symbol_table[self.current_class]["variables"]:
                self.known_objects[var["name"]] = var["type"]
        
        print(f"Method definition: {method_name}")

        self.call_stack.append(class_name)
        self.visitChildren(ctx)
        self.call_stack.pop()

        if self.call_stack:
            caller = self.call_stack[-1]  
            self.uml.add_return(caller, class_name, "void")

        self.known_objects = old_known_objects

        return None

    # Poziv metode: obj.method(...)
    def visitMethodCall(self, ctx:CppParser.MethodCallContext):
        object_name = ctx.ID(0).getText()
        method_name = ctx.ID(1).getText()
        args = "(" + ctx.argumentList().getText() + ")" if ctx.argumentList() else "()"
        
        print(f"Method call: {object_name}.{method_name}{args}")

        if object_name not in self.known_objects:
            print(f"Unknown object: {object_name}  (linija {ctx.start.line})")
            return None

        class_name = self.known_objects[object_name]
        
        # provjera da li metoda postoji u klasi
        method_list = [m["name"] for m in self.symbol_table.get(class_name, {}).get("methods", [])]
        if method_name not in method_list:
            print(f" {method_name} is not recognised in class {class_name} (linija {ctx.start.line})")

        caller = self.call_stack[-1] if self.call_stack else "Main"
        self.uml.add_call(caller, class_name, f"{method_name}{args}")
        
        methods = [m for m in self.symbol_table[class_name]["methods"] if m["name"] == method_name]
        for m in methods:
            self.current_class = class_name
            self.call_stack.append(caller)
            self.visitMethodDefinition(m["ctx"])  
            self.call_stack.pop()

        return None
    
    def visitFunctionCall(self, ctx:CppParser.FunctionCallContext):
        func_name = ctx.ID().getText()

        if self.current_class:
            # metoda trenutne klase
            methods = [m for m in self.symbol_table[self.current_class]["methods"] if m["name"] == func_name]
            if not methods:
                print(f"Greška: metoda {func_name} nije deklarisana (linija {ctx.start.line})")
            else:
                caller = self.call_stack[-1] if self.call_stack else "Main"
                self.uml.add_call(caller, self.current_class, func_name + "()")
                for m in methods:
                    self.current_class, old_class = self.current_class, self.current_class
                    self.call_stack.append(self.current_class)
                    self.visitMethodDefinition(m["ctx"])
                    self.call_stack.pop()
                    self.current_class = old_class
        else:
            # globalna funkcija
            if func_name not in self.symbol_table:
                print(f"Greška: funkcija {func_name} nije deklarisana (linija {ctx.start.line})")
            else:
                self.visitFunctionDefinition(self.symbol_table[func_name]["methods"][0]["ctx"])

        return self.visitChildren(ctx)

    # Parametri funkcije/metode
    def visitParameterList(self, ctx:CppParser.ParameterListContext):
        for param in ctx.variableDeclaration():
            type_name = param.type_().getText()
            var_name = param.ID().getText()
            print(f"Parameter: {var_name} of type {type_name}")
            self.known_objects[var_name] = type_name
        return self.visitChildren(ctx)

    def visitObjectDeclaration(self, ctx):
        obj_type = ctx.ID(0).getText()
        obj_name = ctx.ID(1).getText()

        if obj_type not in self.symbol_table:
            print(f"Uknown class: {obj_type} (line {ctx.start.line})")
        else:
            # dodaj objekat u poznate objekte
            print(f"Object declared: {obj_name} of type {obj_type}")
            self.known_objects[obj_name] = obj_type
        
        return None

    # Deklaracija lokalne promjenljive
    def visitVariableDeclaration(self, ctx:CppParser.VariableDeclarationContext):
        if ctx.type_() and ctx.ID():
            type_name = ctx.type_().getText()
            var_name = ctx.ID().getText()
            print(f"Variable declared: {var_name} of type {type_name}")
            self.known_objects[var_name] = type_name
        return None

    # Naredba return
    def visitStatement(self, ctx:CppParser.StatementContext):
        if ctx.RETURN():
            caller = self.call_stack[-1] if self.call_stack else "Main"
            if len(self.call_stack) > 1:
                callee = self.call_stack[-1]           # metoda koja vraća
                caller_of_callee = self.call_stack[-2] # stvarni pozivač
                expr = ctx.expression()
                value = expr.getText() if expr else "void"
                self.uml.add_return(caller_of_callee, callee, value)
        return self.visitChildren(ctx)
    
    # Naredba dodjele
    def visitAssignement(self, ctx:CppParser.AssignementContext):
        left = ctx.ID().getText()
        right_expr = ctx.expression().getText()
        print(f"Assignment: {left} = {right_expr}")
        return self.visitChildren(ctx)

