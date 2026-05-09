# C++ to UML Sequence Diagram Generator

A tool that automatically translates C++ source code into UML sequence diagrams, built as a Compiler Construction course project.

## About
This system parses C++ code and generates visual UML sequence diagrams that illustrate object interactions and method call flow. It uses ANTLR for lexical and syntactic analysis and PlantUML for diagram rendering.

## How It Works
1. **Lexical analysis** — tokenizes C++ source code (keywords, identifiers, symbols)
2. **Syntactic analysis** — builds a parse tree using defined C++ grammar rules
3. **Semantic analysis** — validates class and method existence via a symbol table
4. **Diagram generation** — traverses the parse tree and produces PlantUML code, which is rendered as a PNG image

## Technologies
- Python
- ANTLR4 (lexer and parser generation)
- PlantUML (diagram rendering)

## How to Run
1. Clone the repository
2. Install dependencies:
```bash
   pip install antlr4-python3-runtime
```
3. Run the tool with a C++ input file:
```bash
   python main.py examples/example.txt
```
4. The generated diagram will be saved as a `.png` file.

## Example
Input C++ code with classes `Book`, `Library`, and `Person` produces a sequence diagram showing method call flow between `Main`, `Person`, `Book`, and `Library`.
<img width="263" height="328" alt="image" src="https://github.com/user-attachments/assets/d3ef3e0f-32db-4cff-a69a-f1ce66406d3b" />

## Author
Ana Kondić  
Faculty of Natural Sciences and Mathematics, Banja Luka  
Compiler Construction — course project
