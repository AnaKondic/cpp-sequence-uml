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
    : CLASS ID LBRACE classBody RBRACE SEMI
    ;

classBody
    : (accessModifier | methodDeclaration | variableDeclaration)*
    ;

// Pristupni modifikator
accessModifier
    : PUBLIC COLON
    | PRIVATE COLON
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
    | variableDeclaration SEMI
    | RETURN expression? SEMI
    ;

// Poziv metode
methodCall
    : ID DOT ID LPAREN argumentList? RPAREN
    ;

argumentList
    : expression (COMMA expression)*
    ;

// Pravilo za izraze (hijerarhijski)
// expression
//     : 
//     | expression PLUS expression
//     | expression MINUS expression
//     | expression STAR expression
//     | expression LEFT_SHIFT expression
//     | expression COLONCOLON expression
//     | ID
//     | NUMBER
//     | STRING_LITERAL
//     ;

expression
    : shiftExpression
    ;

shiftExpression
    : additiveExpression (LEFT_SHIFT additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*
    ;

multiplicativeExpression
    : postfixExpression ((STAR | DIV) postfixExpression)*
    ;

postfixExpression
    : primaryExpression postfixOp*
    ;

postfixOp
    : COLONCOLON ID
    | DOT ID
    ;

primaryExpression
    : ID
    | STRING_LITERAL
    | NUMBER
    | LPAREN expression RPAREN
    ;

// Pravilo za dodjelu
assignement
    : ID ASSIGN expression
    ;
    
// Deklaracija objekta
objectDeclaration
    : ID ID
    ;
