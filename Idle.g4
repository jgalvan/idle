grammar Idle;

ID: [a-z][a-zA-Z0-9_]*;
INT_LITERAL: [0-9]+;
FLOAT_LITERAL: [0-9]+ [.][0-9]+;
STRING_LITERAL: ["].*? ["];
RELOP: '<' | '>' | '<=' | '>=' | '==' | '!=' | '!';
WS: [ \t\r\n]+ -> skip;

fileState: imp* classState+;
imp: 'import' ID ';';
classState: 'type' ID ('<-' ID)? 'class' classBlock;
classBlock: '{' (attribute | method)* '}';
attribute: ID typeState ';';
method: ID '(' methodArguments? ')' (typeState | 'void') block;
methodArguments: ID typeState (',' ID typeState)*;
typeState: 'bool' | 'int' | 'float' | 'string' | ID;
block: '{' statement+ '}';
statement:
	varsDecl
	| assignment
	| varsDeclAssignment
	| condition
	| call ';'
	| forLoop
	| whileLoop
	| printState
	| read
	| returnState;
varsDecl:
	'var' ID (',' ID)* ('[' INT_LITERAL ']')? typeState ';';
assignment: (instanceVar | arrPos | ID) '=' expression ';';
varsDeclAssignment: 'var' ID '=' expression ';';
returnState: 'return' expression ';';
expression: exp (RELOP exp)? | STRING_LITERAL;
exp: term (('+' | '-') term)*;
term: factor (('/' | '*') factor)*;
factor: '(' expression ')' | ('+' | '-')? literal;
literal:
	ID
	| INT_LITERAL
	| FLOAT_LITERAL
	| arrPos
	| instanceVar
	| call;
arrPos: ID '[' INT_LITERAL ']';
instanceVar: '$' ID;
condition: 'if' expression block elseIf* ('else' block)?;
elseIf: 'else' 'if' expression block;
whileLoop: 'while' expression block;
forLoop:
	'for' (varsDeclAssignment | assignment)? ';' expression ';' expression? block;
call: (ID '.')? ID '(' callArguments? ')';
callArguments: ID (',' ID)*;
printState: 'IO.print' '(' expression ')' ';';
read: 'IO.' ('readString' | 'readInt' | 'readFloat') '()' ';';
