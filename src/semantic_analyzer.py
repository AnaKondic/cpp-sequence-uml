from antlr.CppParserVisitor import CppParserVisitor
from antlr.CppParser import CppParser

class SemanticAnalyzer(CppParserVisitor):
    def __init__(self):
        # simbolicka tabela
        # struktura: {"ClassName": {"variables": [...], "methods": [...], "instances": [...] } }
        self.symbol_table = {}

        self.current_class = None
        self.current_function = None
        self.global_objects = {}
        
    def visitProgram(self, ctx:CppParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitClassDeclaration(self, ctx:CppParser.ClassDeclarationContext):
        class_name = ctx.ID().getText()

        # Provjera da li je klasa vec deklarisana
        if class_name in self.symbol_table:
            print(f"Greška: klasa {class_name} je već deklarisana (linija {ctx.start.line})")
        else:
            self.symbol_table[class_name] = {"variables": [], "methods": [], "instances": []}

        self.current_class = class_name

        # Dodavanje svih atributa i metoda klase u tabelu simbola
        for element in ctx.classBody().classBodyElement():
            # varijable
            var_decl = element.variableDeclaration() if hasattr(element, "variableDeclaration") else None
            if var_decl:
                type_name = var_decl.type_().getText()
                var_name = var_decl.ID().getText()
                self.symbol_table[class_name]["variables"].append({"type": type_name, "name": var_name})
                self.global_objects[var_name] = type_name
            # metode
            method_decl = getattr(element, "methodDefinition", None)
            if method_decl and callable(method_decl):
                m_ctx = method_decl()
                if m_ctx:
                    method_name = m_ctx.ID().getText()
                    self.symbol_table[class_name]["methods"].append({"name": method_name})

        
        self.visitChildren(ctx)
        self.current_class = None
        return None

    def visitFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        func_name = ctx.ID().getText()
        
        if func_name not in self.symbol_table:
            self.symbol_table[func_name] = {"variables": [], "methods": []}  # globalna funkcija
        self.visitChildren(ctx)
        return None
    
    def visitMethodDefinition(self, ctx:CppParser.MethodDefinitionContext):
        method_name = ctx.ID().getText()
        return_type = ctx.type_().getText() if ctx.type_() else "void"

        # Zapis metode za tabelu simbola
        method_entry = {
            "name": method_name,
            "return_type": return_type,
            "params": []
        }

        # Paremetri metode
        current_locals = {}
        if ctx.parameterList():
            for param in ctx.parameterList().variableDeclaration():
                p_type = param.type_().getText()
                p_name = param.ID().getText()
                method_entry["params"].append({"type": p_type, "name": p_name})
                current_locals[p_name] = p_type

        # Dodavanje metode u simbolicku tabelu
        if self.current_class:
            self.symbol_table[self.current_class]["methods"].append(method_entry)
        else:
            # Globalne funkcije
            self.symbol_table[method_name] = {"variables": [], "methods": [method_entry], "instances": []}


        self.current_function = method_name
        self.current_locals = current_locals  # čuvamo parametre dok posjećujemo tijelo metode
        
        self.visitChildren(ctx)

        self.current_locals = None
        self.current_function = None
        return None

    def visitVariableDeclaration(self, ctx:CppParser.VariableDeclarationContext):
        type_name = ctx.type_().getText() if ctx.type_() else "unknown"
        var_name = ctx.ID().getText()

        var_entry = {"type": type_name, "name": var_name}

        if self.current_class:
            # atribut klase
            self.symbol_table[self.current_class]["variables"].append(var_entry)
        elif self.current_function:
            # lokalna promenljiva funkcije
            if "locals" not in self.symbol_table[self.current_function]:
                self.symbol_table[self.current_function]["locals"] = []
            self.symbol_table[self.current_function]["locals"].append(var_entry)
        else:
            # globalna promenljiva
            self.global_objects[var_name] = type_name

        return None

    def visitObjectDeclaration(self, ctx:CppParser.ObjectDeclarationContext):
        obj_type = ctx.ID(0).getText()
        obj_name = ctx.ID(1).getText()

        # Provjera da li klasa postoji
        if obj_type not in self.symbol_table:
            print(f"Greška: nepoznata klasa {obj_type} na liniji {ctx.start.line}")

        # Dodavanje instance u tabelu simbola klase
        if obj_type in self.symbol_table:
            self.symbol_table[obj_type]["instances"].append(obj_name)

        # Globalni objekti
        self.global_objects[obj_name] = obj_type

        return None

    def visitMethodCall(self, ctx:CppParser.MethodCallContext):
        obj_name = ctx.ID(0).getText()
        method_name = ctx.ID(1).getText()

        obj_type = None

        # Trazimo u lokalnim parametrima
        if self.current_locals and obj_name in self.current_locals:
            obj_type = self.current_locals[obj_name]

        # Ako nije, trazimo globalno
        if not obj_type:
            obj_type = self.global_objects.get(obj_name, None)
        if not obj_type:
            # Moze biti instanca klase
            for cls_name, cls_info in self.symbol_table.items():
                if obj_name in cls_info.get("instances", []):
                    obj_type = cls_name
                    break

        if not obj_type:
            print(f"Greška: objekat {obj_name} ne postoji (linija {ctx.start.line})")
            return None

        # Provjera da li metoda postoji u klasi
        methods = [m["name"] for m in self.symbol_table[obj_type]["methods"]]
        if method_name not in methods:
            print(f"Greška: metoda {method_name} ne postoji u klasi {obj_type} (linija {ctx.start.line})")

        self.visitChildren(ctx)
        return None

    def visitFunctionCall(self, ctx:CppParser.FunctionCallContext):
        func_name = ctx.ID().getText()

        # Globalna funkcija ili metoda trenutne klase
        if self.current_class:
            methods = [m["name"] for m in self.symbol_table[self.current_class]["methods"]]
            if func_name not in methods and func_name not in self.symbol_table:
                print(f"Greška: metoda {func_name} nije deklarisana (linija {ctx.start.line})")
                print(f"Klasa {self.current_class}")
        else:
            if func_name not in self.symbol_table:
                print(f"Greška: funkcija {func_name} nije deklarisana (linija {ctx.start.line})")

        self.visitChildren(ctx)
        return None
