/*
	Idle Language Grammar
	Luis Daniel Villarreal Ortega
	Jesús Alejandro Galván Villarreal
 */

grammar Idle;

/* TOKENS */

// Keywords
BOOL:				'bool';
CLASS:              'class';
ELSE:               'else';
ELSEIF:				'elseif';
FLOAT:              'float';
FOR:                'for';
IF:                 'if';
IMPORT:             'import';
INT:                'int';
RETURN:             'return';
STRING:				'string';
TYPE:				'type';
VAR:				'var';
VOID:               'void';
WHILE:              'while';
IO:					'IO';

// Literals
BOOL_LITERAL: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z0-9_]*;
INT_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+ '.' [0-9]+;
STRING_LITERAL: '"'.*? '"';

// Separators
LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACK:             '[';
RBRACK:             ']';
SEMICOLON:          ';';
COMMA:              ',';
DOT:                '.';

// Operators
ADD:                '+';
AND:                '&&';
ARROW:              '<-';
ASSIGN:             '=';
BANG:               '!';
DIV:                '/';
DSYMBOL:			'$';
EQUAL:              '==';
GE:                 '>=';
GT:                 '>';
LE:                 '<=';
LT:                 '<';
MUL:                '*';
NOTEQUAL:           '!=';
OR:                 '||';
SUB:                '-';

// Whitespace and comments
COMMENT:            '/*' .*? '*/'    -> skip;
LINE_COMMENT:       '//' ~[\r\n]*    -> skip;
WS:                 [ \t\r\n\u000C]+ -> skip;

/* RULES */

fileState
	: imp* classState+;

imp
	: 'import' ID ';';

classState
	: 'type' ID ('<-' ID)? 'class' classBlock;

classBlock
	: '{' attribute* method* '}';

attribute
	: ID typeState ';';

method
	: ID '(' methodArguments? ')' (typeState | 'void') varsDecl* block;

methodArguments
	: ID typeState (',' ID typeState)*;

typeState
	: 'bool' | 'int' | 'float' | 'string' | ID;

varsDecl
	: 'var' ID (',' ID)* ('[' INT_LITERAL ']')? typeState ';';

assignment
	: <assoc=right> reference '=' expression;

block
	: '{' statement* '}';

statement
	: assignment ';'
	| condition
	| call ';'
	| forLoop
	| whileLoop
	| printState
	| returnState;

returnState
	: 'return' expression ';';

expression
	: <assoc=right> '!' exp
	| exp (( '<' | '>' | '<=' | '>=' | '==' | '!=' | '&&' | '||') exp)?;

exp
	: term (('+' | '-') term)*;

term
	: factor (('/' | '*') factor)*;

factor
	: '(' expression ')' | ('+' | '-')? literal;

literal
	: reference
	| INT_LITERAL
	| FLOAT_LITERAL
	| STRING_LITERAL
	| BOOL_LITERAL
	| call;

reference
	: ID
	| arrPos
	| instanceVar;

arrPos
	: ID '[' expression ']';

instanceVar
	: '$' ID;

condition
	: 'if' expression block elseIf* ('else' block)?;

elseIf
	: 'else' 'if' expression block;

whileLoop
	: 'while' expression block;

forLoop
	: 'for' assignment? ';' expression ';' assignment? block;

call
	: (reference '.')? reference '(' callArguments? ')'
	| read;

callArguments
	: expression (',' expression)*;

printState
	: 'IO' '.' 'print' '(' expression ')' ';';

read
	: 'IO' '.' ('readString' | 'readInt' | 'readFloat') '(' ')';
