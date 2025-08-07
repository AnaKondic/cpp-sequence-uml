parser grammar CppParser;

options { tokenVocab=CppLexer; }

// Pocetno pravilo
program
    : (preprocessorDirective | classDeclaration | functionDefinition | statement)* EOF
    ;

// Preprocesorska direktiva
preprocessorDirective
    : INCLUDE LT ID GT
    ;

// Deklaracija klase
classDeclaration
    : CLASS ID LBRACE classBody RBRACE
    ;

classBody
    : (methodDeclaration | variableDeclaration)*
    ;

// Deklaracija metode 
methodDeclaration 
    : PUBLIC? type ID LPAREN parameterList? RPAREN LBRACE statement* RBRACE
    ;

// Definicija funckije
functionDefinition
    : type ID LPAREN parameterList? RPAREN LBRACE statement* RBRACE
    ;

// Parametri funkcije
parameterList
    : variableDeclaration (COMMA variableDeclaration)*
    ;

// Pravilo za tip
type
    : (STD COLONCOLON)? (VOID | STRING | CHAR | INT | FLOAT | DOUBLE | BOOL | ID)
    ;

// Deklaracija promjenljive
variableDeclaration
    : type ID (ASSIGN expression)?
    ;

// Pravilo za naredbu
statement
    : methodCall SEMI
    | objectDeclaration SEMI
    | assignement SEMI
    | RETURN expression SEMI
    ;

// Poziv metode
methodCall
    : ID DOT ID LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

// Pravilo za izraz
expression
    : ID
    | NUMBER
    | STRING_LITERAL
    ;

// Pravilo za dodjelu
assignement
    : ID ASSIGN expression
    ;
    
// Deklaracija objekta
objectDeclaration
    : ID ID
    ;
