lexer grammar CppLexer;

// Kljucne rijeci
CLASS   : 'class';
PUBLIC  : 'public';
PRIVATE : 'private';
VOID    : 'void';
INT     : 'int';
FLOAT   : 'float';
DOUBLE  : 'double';
CHAR    : 'char';
BOOL    : 'bool';
STRING  : 'string';
STD     : 'std';
RETURN  : 'return';
NEW     : 'new';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
INCLUDE : '#include';

// Simboli
LBRACE  : '{';
RBRACE  : '}';
LPAREN  : '(';
RPAREN  : ')';
SEMI    : ';';
COMMA   : ',';
DOT     : '.';
ASSIGN  : '=';
PLUS    : '+';
MINUS   : '-';
STAR    : '*';
DIV     : '/';
QUOTE   : '"';
COLON   : ':';
COLONCOLON  : '::';
LEFT_SHIFT  : '<<';
RIGHT_SHIFT : '>>';
LT      : '<';
GT      : '>';

// Identifikatori i literali
ID      : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER  : [0-9]+;
STRING_LITERAL  : '"'.*?'"';

// Komentari i whitespace
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS           : [ \t\r\n] -> skip;
