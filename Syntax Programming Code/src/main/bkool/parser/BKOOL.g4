grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF;

decl: vardecl | funcdecl;

vardecl: type_name id_list ';';

funcdecl: type_name ID '(' param_list? ')' body;

param_list: param (';' param)*;

param: type_name id_list;

id_list: ID (',' ID)*;

type_name: 'int' | 'float';

body: '{' (vardecl | statement)* '}';

statement: assignment | call | return_stmt;

assignment: ID '=' expr ';';

call: ID '(' exp_list? ')' ';';

return_stmt: 'return' expr ';';

exp_list: expr (',' expr)*;

// Expressions
expr: expr1 '+' expr | expr1; // Right associative
expr1: expr2 '-' expr2 | expr2; // Non-associative
expr2: expr2 ('*' | '/') expr3 | expr3; // Left associative
expr3: ID '(' exp_list? ')' | ID | INTLIT | FLOATLIT | '(' expr ')';

// Lexer
INTLIT: [0-9]+;
FLOATLIT: [0-9]+ '.' [0-9]+;
ID: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};