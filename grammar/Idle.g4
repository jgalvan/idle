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
	: {self.icomp = IdleCompiler()} imp* classState+ {self.icomp.set_main()};

imp
	: 'import' ID ';' {self.icomp.import_file($ID.text)};

classState
	: 'type' class_name=ID ('<-' parent_name=ID)? 'class' {self.icomp.add_class($class_name.text, $class_name.line, $parent_name.text)} classBlock ;

classBlock
	: '{' attribute* method* '}';

attribute
	: varsDecl;

method
	: nonVoidMethod
	| voidMethod
	| constructor;

nonVoidMethod
	: ID {self.icomp.add_func($ID.text, $ID.line)} '(' methodArguments? ')' typeState {self.icomp.add_func_return_type($typeState.text)} nonVoidBlock {self.icomp.quad_add_endproc($nonVoidBlock.stop.line)} {self.icomp.end_scope()};

voidMethod
	: ID {self.icomp.add_func($ID.text, $ID.line)} '(' methodArguments? ')' 'void' block {self.icomp.quad_add_endproc($block.stop.line)} {self.icomp.end_scope()};

constructor
	: ID {self.icomp.add_constructor($ID.text, $ID.line)} '(' methodArguments? ')' block {self.icomp.quad_add_endproc($block.stop.line)} {self.icomp.end_scope()} ;

nonVoidBlock
	: '{' (statement {self.icomp.reset_new_line()} )* returnState '}';

methodArguments
	:  singleArgument (',' singleArgument)*;

singleArgument
	: ID {self.icomp.add_var($ID.text, $ID.line)} typeState {self.icomp.add_arg($ID.text)} ('ref' {self.icomp.param_to_ref($ID.text)})?;

typeState
	: type_name=('bool' | 'int' | 'float' | 'string' | ID) {self.icomp.commit_vars($type_name.text, $type_name.line)};

varsDecl
	: 'var' ID {self.icomp.add_var($ID.text, $ID.line)} (',' ID {self.icomp.add_var($ID.text, $ID.line)})* typeState ';'
	| arrayDecl;

arrayDecl
	: 'var' ID {self.icomp.add_var($ID.text, $ID.line)} '[' INT_LITERAL ']' typeState ';' {self.icomp.define_array($ID.text, $INT_LITERAL.text, $ID.line)};

assignment
	: <assoc=right> reference '=' expression {self.icomp.quad_assign($reference.start.line)};

block
	: '{' (statement {self.icomp.reset_new_line()})* '}';

statement
	: varsDecl
	| assignment ';'
	| {self.icomp.start_scope()} condition {self.icomp.end_scope()}
	| call ';' {self.icomp.check_not_void($call.stop.line, check=False)}
	| {self.icomp.start_scope()} forLoop {self.icomp.end_scope()}
	| {self.icomp.start_scope()} whileLoop {self.icomp.end_scope()}
	| printState
	| returnState;

returnState
	: 'return' expression ';' {self.icomp.quad_add_func_return($expression.start.line)};

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
	: reference
	| INT_LITERAL {self.icomp.add_constant($INT_LITERAL.text, 'int')}
	| FLOAT_LITERAL {self.icomp.add_constant($FLOAT_LITERAL.text, 'float')}
	| STRING_LITERAL {self.icomp.add_constant($STRING_LITERAL.text, 'string')}
	| BOOL_LITERAL {self.icomp.add_constant($BOOL_LITERAL.text, 'bool')}
	| expressionCall;

reference
	: ID {self.icomp.check_var_exists($ID.text, $ID.line)}
	| arrPos
	| instanceVar;

arrPos
	: ID '[' expression ']' {self.icomp.check_array_access($ID.text, $ID.line)};

instanceVar
	: '$' ID {self.icomp.check_instance_var_exists($ID.text, $ID.line)}
	| '$' ID '[' expression ']' {self.icomp.check_instance_array_access($ID.text, $ID.line)};

condition
	: 'if' expression {self.icomp.quad_end_if_expr($expression.start.line)} block ({self.icomp.quad_start_else_ifs()} elseIfs)? {self.icomp.quad_fill_if_end_jumps()};

elseIfs
	:  elseIf+ {self.icomp.quad_fill_if_end_jumps()}
	| finalElse
	| elseIf+ finalElse;

elseIf
	: 'else' 'if' {self.icomp.quad_add_else()} expression {self.icomp.quad_end_if_expr($expression.start.line)} block;

finalElse
	: 'else' {self.icomp.quad_add_else()} block;

whileLoop
	: 'while' {self.icomp.quad_start_while()} expression {self.icomp.quad_end_while_expr($expression.start.line)} block {self.icomp.quad_end_while()};

forLoop
	: 'for' assignment? ';' {self.icomp.quad_start_while()} 
			expression {self.icomp.quad_end_while_expr($expression.start.line)} ';' 
			{self.icomp.quad_start_for_assign()} assignment? {self.icomp.quad_end_for_assign()}
			block {self.icomp.quad_end_for_block()} {self.icomp.quad_end_while()};

expressionCall
	: {self.icomp.quad_open_parenthesis()} call {self.icomp.quad_close_parenthesis()} {self.icomp.check_not_void($call.stop.line, check=True)};

call
	: obj_call
	| func_call
	| read
	| constructor_call
	| parent_call;

obj_call
	: reference '.' ID {self.icomp.check_obj_func_exists($ID.text, $ID.line)} '(' callArguments? ')' {self.icomp.quad_add_func_gosub($ID.line)}
	| objectVar;

objectVar
	: class_name=ID '.' var_name=ID {self.icomp.check_obj_var($class_name.text, $var_name.text, $ID.line)}
	| class_name=ID '.' var_name=ID '[' expression ']' {self.icomp.check_obj_array_access($class_name.text, $var_name.text, $ID.line)};

func_call
	: ID {self.icomp.check_func_exists($ID.text, $ID.line)} '(' callArguments? ')' {self.icomp.quad_add_func_gosub($ID.line)};

constructor_call
	: 'new' ID {self.icomp.check_class_exists($ID.text, $ID.line)} '(' callArguments? ')' {self.icomp.quad_add_func_gosub($ID.line)};

parent_call
	: 'super().' ID {self.icomp.check_super_func_exists($ID.text, $ID.line)} '(' callArguments? ')' {self.icomp.quad_add_func_gosub($ID.line)};

callArguments
	: expression {self.icomp.quad_add_func_param($expression.start.line)} (',' expression {self.icomp.quad_add_func_param($expression.start.line)})*;

printState
	: 'print' '(' expression ')' ';' {self.icomp.quad_print_st()};

read
	:	('readString' {self.icomp.quad_read('string')} 
		| 'readInt' {self.icomp.quad_read('int')}
		| 'readFloat' {self.icomp.quad_read('float')}) 
		'(' ')';
