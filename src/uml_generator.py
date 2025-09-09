# Generise PlantUML kod
class UMLGenerator:
    def __init__(self):
        self.lines = []
        self.participants = [] # cuva redoslijed
        self.participants_set = set()
        self.call_stack = [] # prati aktivacije
        
    def add_participant(self, name):
        primitives = {"int", "string", "float", "double", "char", "bool", "void"}
        if name.lower() in primitives:
            return # preskacemo primitive
        
        if name not in self.participants_set:
            print(f"Adding participant: {name}")
            self.participants_set.add(name)
            self.participants.append(name)
    
    def add_call(self, caller, callee, method_name):
        self.add_participant(caller)
        self.add_participant(callee)

        self.lines.append(f"{caller} -> {callee} : {method_name}")

        if not self.call_stack or self.call_stack[-1] != callee:
            self.lines.append(f"activate {callee}")
            self.call_stack.append(callee)  # zapamti da je callee aktiviran

    def add_return(self, from_obj, to_obj, value):
        self.lines.append(f"{from_obj} <-- {to_obj} : {value}")
        if self.call_stack and self.call_stack[-1] == to_obj:
            self.lines.append(f"deactivate {to_obj}")
            self.call_stack.pop()

    def generate(self):
        output = ["@startuml"]

        # Doda ucesnike u redoslijedu kako su pozvani
        for name in self.participants:
            output.append(f"participant {name}")
        
        # Doda sve ostale linije
        output.extend(self.lines)

        while self.call_stack:
            obj = self.call_stack.pop()
            output.append(f"deactivate {obj}")

        output.append("@enduml")
        return "\n".join(output)