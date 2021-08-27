// ID: 1811486
grammar D95;

@lexer::header {
from lexererr import *
import re
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}


// ============================================= Parser =============================================

program: declaration_constants body EOF;

body: declaration_variable | function | declaration_variable body | function body | ;

declaration_constants: declaration_constant | declaration_constant declaration_constants | ;

// A declaration variable of program
declaration_constant: DEFINE OPEN_ROUND CONSTANT_IDENTIFIER COMMA expression CLOSE_ROUND SEMI;
declaration_variable: assignment_stmt;

// A function of program
function: FUNCTION FUNCTION_IDENTIFIER OPEN_ROUND parameter CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP
        | FUNCTION FUNCTION_IDENTIFIER OPEN_ROUND CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP;
parameter: VARIABLE_IDENTIFIER | VARIABLE_IDENTIFIER COMMA parameter;

// A function have zero or many statement
statements: statement | statement statements |;

// All statement type
statement: assignment_stmt 
        | if_stmt 
        | foreach_stmt 
        | while_stmt 
        | break_stmt 
        | continue_stmt 
        | call_stmt 
        | return_stmt;

// Assignment statement
assignment_stmt: VARIABLE_IDENTIFIER ASSIGN expression SEMI | expression_index ASSIGN expression SEMI;

// If statement
if_stmt: IF OPEN_ROUND expression CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP elseif_stmt else_stmt;
elseif_stmt: ELSE_IF OPEN_ROUND expression CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP 
            | ELSE_IF OPEN_ROUND expression CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP elseif_stmt 
            | ;
else_stmt: ELSE OPEN_SHARP statements CLOSE_SHARP | ;
            

// Foreach statement
foreach_stmt: FOREACH OPEN_ROUND expression AS VARIABLE_IDENTIFIER ASSIGN_GREATER VARIABLE_IDENTIFIER CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP; 

// While statement
while_stmt: WHILE OPEN_ROUND expression CLOSE_ROUND OPEN_SHARP statements CLOSE_SHARP; 

// break;
break_stmt: BREAK SEMI;

// continue;
continue_stmt: CONTINUE SEMI;

// Call function statement
call_stmt: function_call SEMI;

// Return statement
return_stmt: RETURN expression SEMI | RETURN SEMI;

// Expressions 
expression: OPEN_ROUND expression CLOSE_ROUND
            | coercions OPEN_ROUND expression CLOSE_ROUND
            | function_call
            | expression_index
            | MINUS expression
            | NEG expression
            | expression operator_multiplying expression
            | expression operator_adding expression
            | expression operator_logical expression
            | expression operator_relational expression
            | expression operator_string expression
            | operands;

operands: VARIABLE_IDENTIFIER | CONSTANT_IDENTIFIER | types | array;

// Operators for expressions
operator_multiplying: MUL | DIV | MOD;
operator_adding: MINUS | ADD; 
operator_logical: AND | OR; 
operator_relational: ASSIGN_ASSIGN | NEG_ASSIGN | LESS | GREATER | LESS_ASSIGN | GREATER_ASSIGN;
operator_string: ADD_DOT | ASSIGN_ASSIGN_DOT;
operator_index: OPEN_BRACKET expression CLOSE_BRACKET | OPEN_BRACKET expression CLOSE_BRACKET operator_index;

// Type coercions
coercions: STR_INT | INT_STR | FLOAT_STR | STR_FLOAT | BOOL_STR | STR_BOOL;

// Call a element in array $arr[exp][exp]
expression_index: VARIABLE_IDENTIFIER operator_index | CONSTANT_IDENTIFIER operator_index;
 
// Call a function: Each parameter should be a variable.
function_call: FUNCTION_IDENTIFIER OPEN_ROUND call_parameter CLOSE_ROUND | FUNCTION_IDENTIFIER OPEN_ROUND CLOSE_ROUND;
call_parameter: expression | expression COMMA call_parameter;

// All array in D95 grammar
array: ARRAY OPEN_ROUND array_body CLOSE_ROUND;
array_body: array_index | array_multidimensional | array_associative | ;

// Multi-dimensional arrays
array_multidimensional: array | array COMMA array_multidimensional;

// Associative array literal
array_associative : key_associative ASSIGN_GREATER value_associative | key_associative ASSIGN_GREATER value_associative COMMA array_associative;
key_associative: INTEGER | STRING;
value_associative: expression | array; // Any type: integer, float, string, boolean, array, array element, function call, null

// Indexed array literal
array_index: expression | expression COMMA array_index;

// Type
types: INTEGER | FLOAT | STRING | BOOLEAN;


// ============================================= Lexer =============================================

// A literal is a source representation of a value of a integer, float, boolean, string, one of three types of array
// boolean type: true - false
BOOLEAN: TRUE | FALSE;

// String literal
STRING: '"' STRING_BODY* '"'{ self.text = self.text[1:-1] };

// These underscores are removed in integer arithmetic
INTEGER: (DECIMAL | HEXADECIMAL | OCTAL | BINARY) { self.text = re.sub('_', '', self.text) }; 

// Floating arithmetic
FLOAT: (INTEGER_PART DECIMAL_PART? EXPONENT_PART? | DECIMAL_PART EXPONENT_PART? | DECIMAL_PART? EXPONENT_PART){ self.text = re.sub('_', '', self.text) };

// Character '_' not start and end in arithmetic
DECIMAL: DIGIT_NOT_ZERO (UNDERLINE? DIGIT)* | ZERO;
HEXADECIMAL: ZERO [xX] DIGIT_HEXADECIMAL (UNDERLINE? DIGIT_HEXADECIMAL)*;
BINARY: ZERO [bB] DIGIT_BINARY (UNDERLINE? DIGIT_BINARY)*;
OCTAL: ZERO DIGIT_OCTAL (UNDERLINE? DIGIT_OCTAL)*;

// Block comment
COMMENT: ('/*' ((~'*') | ('*' ~'/'))* '*/') -> skip;

//The keywords are allowed
BREAK: 'break';
CONTINUE: 'continue';
ELSE_IF: 'elseif';
IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOREACH: 'foreach';
AS: 'as';
FUNCTION: 'function';
TRUE: 'true';
FALSE: 'false';
ARRAY: 'array';
DEFINE: 'define';

RETURN: 'return';

STR_INT: 'str2int';
INT_STR: 'int2str';
STR_FLOAT: 'str2float';
FLOAT_STR: 'float2str';
STR_BOOL: 'str2bool';
BOOL_STR: 'bool2str';

// Identifiers: Variable names and function names
VARIABLE_IDENTIFIER: [$] [_a-zA-Z0-9]*; 

// Identifiers: Variable names and function names
FUNCTION_IDENTIFIER: [_] [_a-zA-Z0-9]*;

// Identifiers: Constant name
CONSTANT_IDENTIFIER: [A-Z] [_a-zA-Z0-9]*;

// A list of valid operator
ASSIGN_GREATER: '=>';
ASSIGN_ASSIGN_DOT: '==.';
LESS_ASSIGN: '<=';
GREATER_ASSIGN: '>=';
NEG_ASSIGN: '!=';
ASSIGN_ASSIGN: '==';
ADD_DOT: '+.';
AND: '&&';
OR: '||';
ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD : '%';
NEG: '!';
ASSIGN: '=';
LESS: '<';
GREATER: '>';

// The characters are the separators
OPEN_ROUND: '(';
CLOSE_ROUND: ')';
OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';
OPEN_SHARP: '{';
CLOSE_SHARP: '}';
DOT: '.';
COMMA : ',';
COLON : ':';
SEMI : ';'; 

// Skip spaces, tabs, newlines
WS : [ \t\r\n]+ -> skip ; 

// When the lexer detects an illegal escape in string. 
ILLEGAL_ESCAPE: '"' STRING_BODY* '\\' ~[bfrnt'"\\] { self.text = self.text[1:] };

// When the lexer detects an unterminated string
UNCLOSE_STRING: '"' STRING_BODY* { self.text = self.text[1:] };

// Without any lexeme: when the detects an unterminated comment.
UNTERMINATED_COMMENT: '/*' ((~'*') | ('*' ~'/'))*;

// When the lexer detects an unrecognized character.
ERROR_CHAR: ANY;

// ============================================= fragment =============================================

// Any charracter except '"' and '\' | encape sequence special  | string in string 
fragment STRING_BODY:  ~[\\\n"] | ESCAPE_SEQUENCE_SPECIAL | '\'"';

// Encape sequences is allowed
fragment ESCAPE_SEQUENCE_SPECIAL: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\';

// Parts in float arithmetic 
fragment INTEGER_PART: DECIMAL;
fragment DECIMAL_PART: DOT (DIGIT | DIGIT UNDERLINE? DIGIT)*;
fragment EXPONENT_PART: [eE] [+-]? DECIMAL;

// Arithmetic is used
fragment ZERO: '0';
fragment DIGIT: [0-9];
fragment DIGIT_NOT_ZERO: [1-9];
fragment DIGIT_OCTAL: [0-7];
fragment DIGIT_HEXADECIMAL: [0-9a-fA-F];
fragment DIGIT_BINARY: [01];
fragment UNDERLINE: '_';

// ANY chracter
fragment ANY: .;