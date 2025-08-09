import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess
from antlr4 import *
from antlr.CppLexer import CppLexer
from antlr.CppParser import CppParser
from uml_visitor import UMLSequenceVisitor  

from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Greška na liniji {line}:{column} - {msg}")
        print(f"Problematični token: {offendingSymbol.text} (tip: {offendingSymbol.type})")


def parse_cpp_file(input_file):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    full_path = os.path.join(base_dir, input_file)
    with open(full_path, "r") as f:
        code = f.read()
    
    input_stream = InputStream(code)
    lexer = CppLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CppParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program() # pocetno pravilo

    visitor = UMLSequenceVisitor()
    visitor.visit(tree)
    return visitor

if __name__ == "__main__":
    visitor = parse_cpp_file("examples/example1.txt")
    print(visitor.known_objects)
    uml_code = visitor.uml.generate()

    # Snimanje UML koda u fajl
    with open("diagram.uml", "w") as f:
        f.write(uml_code)
    
    # PlantUML generise PNG
    subprocess.run(["java", "-jar", "plantuml.jar", "diagram.uml"])

    print("UML fajl je generisan: diagram.uml")
