# Generise PlantUML kod
class UMLGenerator:
    def __init__(self):
        self.lines = ["@startuml"]
        self.participants = set()
    
    def add_participant(self, name):
        if name not in self.participants:
            self.participants.add(name)
            self.lines.append(f"participant {name}")
    
    def add_call(self, caller, callee, method_name):
        self.add_participant(caller)
        self.add_participant(callee)
        self.lines.append(f"{caller} -> {callee} : {method_name}()")

    def add_return(self, from_obj, to_obj, value=""):
        self.lines.append(f"{from_obj} <-- {to_obj} : {value}")
    
    def generate(self):
        self.lines.append("@enduml")
        return "\n".join(self.lines)