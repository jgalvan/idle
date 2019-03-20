/*
	Idle Language Grammar
	Luis Daniel Villarreal Ortega
	Jesús Alejandro Galván Villarreal
 */

grammar Idle;

@parser::header {
from IdleCompiler import IdleCompiler
}

/* TOKENS */

// Keywords
BOOL:				'bool';
CLASS:              'class';
ELSE:               'else';
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
	: {self.icomp = IdleCompiler()} imp* classState+;

imp
	: 'import' ID ';' {self.icomp.import_file($ID.text)};

classState
	: 'type' class_name=ID ('<-' parent_name=ID)? 'class' {self.icomp.add_class($class_name.text, $class_name.line, $parent_name.text)} classBlock ;

classBlock
	: '{' attribute* method* '}';

attribute
	: ID {self.icomp.add_var($ID.text, $ID.line)} typeState ';';

method
	: ID {self.icomp.add_func($ID.text, $ID.line)} '(' methodArguments? ')' (typeState | 'void') varsDecl* block {self.icomp.end_scope()};

methodArguments
	: ID {self.icomp.add_var($ID.text, $ID.line)} typeState (',' ID {self.icomp.add_var($ID.text, $ID.line)} typeState)*;

typeState
	: type_name=('bool' | 'int' | 'float' | 'string' | ID) {self.icomp.commit_vars($type_name.text)};

varsDecl
	: 'var' ID {self.icomp.add_var($ID.text, $ID.line)} (',' ID {self.icomp.add_var($ID.text, $ID.line)})* ('[' INT_LITERAL ']')? typeState ';';

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
	: ID {self.icomp.check_var_exists($ID.text, $ID.line)}
	| arrPos
	| instanceVar;

arrPos
	: ID {self.icomp.check_var_exists($ID.text, $ID.line)} '[' expression ']';

instanceVar
	: '$' ID {self.icomp.check_instance_var_exists($ID.text, $ID.line)};

condition
	: 'if' expression block elseIf* ('else' block)?;

elseIf
	: 'else' 'if' expression block;

whileLoop
	: 'while' expression block;

forLoop
	: 'for' assignment? ';' expression ';' assignment? block;

call
	: (reference '.')? ID {self.icomp.check_func_exists($ID.text, $ID.line)} '(' callArguments? ')'
	| read;

callArguments
	: expression (',' expression)*;

printState
	: 'IO' '.' 'print' '(' expression ')' ';';

read
	: 'IO' '.' ('readString' | 'readInt' | 'readFloat') '(' ')';
