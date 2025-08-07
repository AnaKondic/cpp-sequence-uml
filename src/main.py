from antlr4 import *
from antlr.CppLexer import CppLexer
from antlr.CppParser import CppParser

def parse_cpp_file(input_file):
    with open(input_file, "r") as f:
        code = f.read()
    
    input_stream = InputStream(code)
    lexer = CppLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = CppParser(tokens)
    tree = parser.program() # pocetno pravilo


if __name__ == "__main__":
    parse_cpp_file("examples/example1.cpp")
