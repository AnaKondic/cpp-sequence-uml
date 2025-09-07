import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess
from antlr4 import *
from antlr.CppLexer import CppLexer
from antlr.CppParser import CppParser
from semantic_analyzer import SemanticAnalyzer
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

    sema = SemanticAnalyzer()
    sema.visit(tree)

    visitor = UMLSequenceVisitor(sema.symbol_table)
    visitor.visit(tree)

    return visitor

def generate_uml(plantuml_code, output_file):
    temp_file = "temp.uml"
    with open(temp_file, "w") as f:
        f.write(plantuml_code)
    subprocess.run(["java", "-jar", "plantuml.jar", temp_file])
    print(f"Diagram generated: {output_file}")


if __name__ == "__main__":
    visitor = parse_cpp_file("examples/example5.txt")
    print(visitor.known_objects)
    uml_code = visitor.uml.generate()

    generate_uml(uml_code, "temp.png")
