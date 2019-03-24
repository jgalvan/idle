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
	: {self.icomp = IdleCompiler()} imp* classState+ {self.icomp.printQuads()};

imp
	: 'import' ID ';' {self.icomp.import_file($ID.text)};

classState
	: 'type' class_name=ID ('<-' parent_name=ID)? 'class' {self.icomp.add_class($class_name.text, $class_name.line, $parent_name.text)} classBlock ;

classBlock
	: '{' attribute* method* '}';

attribute
	: ID {self.icomp.add_var($ID.text, $ID.line)} typeState ';';

method
	: ID {self.icomp.add_func($ID.text, $ID.line)} '(' methodArguments? ')' (typeState {self.icomp.add_func_return_type($typeState.text)} | 'void') varsDecl* block {self.icomp.end_scope()}
	| ID {self.icomp.add_constructor($ID.text, $ID.line)} '(' methodArguments? ')' varsDecl* block {self.icomp.end_scope()};

methodArguments
	: ID {self.icomp.add_var($ID.text, $ID.line)} typeState {self.icomp.add_arg($ID.text)} (',' ID {self.icomp.add_var($ID.text, $ID.line)} typeState {self.icomp.add_arg($ID.text)})*;

typeState
	: type_name=('bool' | 'int' | 'float' | 'string' | ID) {self.icomp.commit_vars($type_name.text, $type_name.line)};

varsDecl
	: 'var' ID {self.icomp.add_var($ID.text, $ID.line)} (',' ID {self.icomp.add_var($ID.text, $ID.line)})* ('[' INT_LITERAL ']')? typeState ';';

assignment
	: <assoc=right> reference '=' expression {self.icomp.quad_assign($reference.text, $reference.start.line)};

block
	: '{' (statement {self.icomp.reset_new_line()})* '}';

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
	| exp (operator=( '<' | '>' | '<=' | '>=' | '==' | '!=' | '&&' | '||') {self.icomp.quad_add_oper($operator.text)} exp {self.icomp.quad_check_relop($exp.start.line)} )?;

exp
	: term {self.icomp.quad_check_addsub($term.start.line)} (operator=('+' | '-'){self.icomp.quad_add_oper($operator.text)} term {self.icomp.quad_check_addsub($term.start.line)})*;

term
	: factor {self.icomp.quad_check_divmult($factor.start.line)} (operator=('/' | '*'){self.icomp.quad_add_oper($operator.text)} factor {self.icomp.quad_check_divmult($factor.start.line)})*;

factor
	: '(' {self.icomp.quad_open_parenthesis()} expression ')' {self.icomp.quad_close_parenthesis()} | ('+' | '-')? literal;

literal
	: reference {self.icomp.quad_add_var($reference.text)}
	| INT_LITERAL
	| FLOAT_LITERAL
	| STRING_LITERAL
	| BOOL_LITERAL
	| call;

reference returns [attr_ref]
	: ID {self.icomp.check_var_exists($ID.text, $ID.line)}
	| arrPos {$attr_ref = $arrPos.attr_ref}
	| instanceVar {$attr_ref = $instanceVar.attr_ref};

arrPos returns [attr_ref]
	: ID {$attr_ref = self.icomp.check_var_exists($ID.text, $ID.line)} '[' expression ']';

instanceVar returns [attr_ref]
	: '$' ID {$attr_ref = self.icomp.check_instance_var_exists($ID.text, $ID.line)};

condition
	: 'if' expression block elseIf* ('else' block)?;

elseIf
	: 'else' 'if' expression block;

whileLoop
	: 'while' expression block;

forLoop
	: 'for' assignment? ';' expression ';' assignment? block;

call
	: reference '.' ID {self.icomp.check_obj_func_exists($reference.attr_ref, $ID.text, $ID.line)} '(' callArguments? ')'
	| ID {self.icomp.check_func_exists($ID.text, $ID.line)} '(' callArguments? ')'
	| read
	| 'new' ID {self.icomp.check_class_exists($ID.text, $ID.line)} '(' callArguments? ')';

callArguments
	: expression (',' expression)*;

printState
	: 'IO' '.' 'print' '(' expression ')' ';';

read
	: 'IO' '.' ('readString' | 'readInt' | 'readFloat') '(' ')';
