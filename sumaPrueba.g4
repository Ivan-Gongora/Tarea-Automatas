grammar sumaPrueba;

prog: statement* EOF; // Programa puede tener múltiples sentencias

// Definición de función
functionDef: 'def' IDENTIFIER '(' parameters? ')' ':' block;

// Parámetros de las funciones
parameters: IDENTIFIER (',' IDENTIFIER)*;

// Bloques de código entre llaves
block: '{' statement* '}';

// Sentencias
statement
    : functionDef                # FuncDef
    | assignment                 # Assignment
    | returnStatement            # Return
    | printStatement             # Print
    ;

// Asignación de variables
assignment: IDENTIFIER '=' expression ';';  // Asigna valor a una variable y termina con ';'

// Sentencia de retorno
returnStatement: 'return' expression ';';   // Retorna el valor de una expresión

// Sentencia de impresión
printStatement: 'print' '(' expression ')' ';';  // Imprime una expresión

// Expresiones matemáticas
expression
    : expression ('+' | '-') expression   # AddSub
    | expression ('*' | '/') expression   # MulDiv
    | IDENTIFIER                          # Var
    | NUMBER                              # Number
    | '(' expression ')'                  # Parens
    | functionCall                        # FuncCall
    ;

// Definición de llamada a funciones
functionCall: IDENTIFIER '(' (expression (',' expression)*)? ')';  // Llamada a función

// Tokens
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;  // Identificadores (nombres de variables o funciones)
NUMBER: [0-9]+;  // Números enteros
WS: [ \t\r\n]+ -> skip;  // Espacios en blanco (se omiten)
