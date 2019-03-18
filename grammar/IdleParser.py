# Generated from grammar/Idle.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from IdleCompiler import IdleCompiler


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u013e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2\3\2\6\2E\n\2\r\2\16\2")
        buf.write("F\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4R\n\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\7\5Z\n\5\f\5\16\5]\13\5\3\5\7\5`\n\5")
        buf.write("\f\5\16\5c\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\5\7p\n\7\3\7\3\7\3\7\5\7u\n\7\3\7\7\7x\n\7\f\7")
        buf.write("\16\7{\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7")
        buf.write("\b\u0087\n\b\f\b\16\b\u008a\13\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\7\n\u0095\n\n\f\n\16\n\u0098\13\n\3\n\3")
        buf.write("\n\3\n\5\n\u009d\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\7\f\u00a8\n\f\f\f\16\f\u00ab\13\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00ba\n\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u00c5")
        buf.write("\n\17\5\17\u00c7\n\17\3\20\3\20\3\20\7\20\u00cc\n\20\f")
        buf.write("\20\16\20\u00cf\13\20\3\21\3\21\3\21\7\21\u00d4\n\21\f")
        buf.write("\21\16\21\u00d7\13\21\3\22\3\22\3\22\3\22\3\22\5\22\u00de")
        buf.write("\n\22\3\22\5\22\u00e1\n\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00e9\n\23\3\24\3\24\3\24\5\24\u00ee\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\7\27\u00fc\n\27\f\27\16\27\u00ff\13\27\3\27\3\27\5\27")
        buf.write("\u0103\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\5\32\u0110\n\32\3\32\3\32\3\32\3\32\5\32")
        buf.write("\u0116\n\32\3\32\3\32\3\33\3\33\3\33\5\33\u011d\n\33\3")
        buf.write("\33\3\33\3\33\5\33\u0122\n\33\3\33\3\33\5\33\u0126\n\33")
        buf.write("\3\34\3\34\3\34\7\34\u012b\n\34\f\34\16\34\u012e\13\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\2\2\37\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:\2\7\7\2\7\7\n\n\16")
        buf.write("\16\20\20\27\27\5\2%%+/\61\62\4\2$$\63\63\4\2))\60\60")
        buf.write("\3\2\4\6\2\u0147\2<\3\2\2\2\4H\3\2\2\2\6M\3\2\2\2\bW\3")
        buf.write("\2\2\2\nf\3\2\2\2\fk\3\2\2\2\16\177\3\2\2\2\20\u008b\3")
        buf.write("\2\2\2\22\u008e\3\2\2\2\24\u00a1\3\2\2\2\26\u00a5\3\2")
        buf.write("\2\2\30\u00b9\3\2\2\2\32\u00bb\3\2\2\2\34\u00c6\3\2\2")
        buf.write("\2\36\u00c8\3\2\2\2 \u00d0\3\2\2\2\"\u00e0\3\2\2\2$\u00e8")
        buf.write("\3\2\2\2&\u00ed\3\2\2\2(\u00ef\3\2\2\2*\u00f4\3\2\2\2")
        buf.write(",\u00f7\3\2\2\2.\u0104\3\2\2\2\60\u0109\3\2\2\2\62\u010d")
        buf.write("\3\2\2\2\64\u0125\3\2\2\2\66\u0127\3\2\2\28\u012f\3\2")
        buf.write("\2\2:\u0137\3\2\2\2<@\b\2\1\2=?\5\4\3\2>=\3\2\2\2?B\3")
        buf.write("\2\2\2@>\3\2\2\2@A\3\2\2\2AD\3\2\2\2B@\3\2\2\2CE\5\6\4")
        buf.write("\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\3\3\2\2\2")
        buf.write("HI\7\r\2\2IJ\7\27\2\2JK\7!\2\2KL\b\3\1\2L\5\3\2\2\2MN")
        buf.write("\7\21\2\2NQ\7\27\2\2OP\7&\2\2PR\7\27\2\2QO\3\2\2\2QR\3")
        buf.write("\2\2\2RS\3\2\2\2ST\7\b\2\2TU\b\4\1\2UV\5\b\5\2V\7\3\2")
        buf.write("\2\2W[\7\35\2\2XZ\5\n\6\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\a\3\2\2\2][\3\2\2\2^`\5\f\7\2_^\3\2\2\2")
        buf.write("`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\7")
        buf.write("\36\2\2e\t\3\2\2\2fg\7\27\2\2gh\b\6\1\2hi\5\20\t\2ij\7")
        buf.write("!\2\2j\13\3\2\2\2kl\7\27\2\2lm\b\7\1\2mo\7\33\2\2np\5")
        buf.write("\16\b\2on\3\2\2\2op\3\2\2\2pq\3\2\2\2qt\7\34\2\2ru\5\20")
        buf.write("\t\2su\7\23\2\2tr\3\2\2\2ts\3\2\2\2uy\3\2\2\2vx\5\22\n")
        buf.write("\2wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{")
        buf.write("y\3\2\2\2|}\5\26\f\2}~\b\7\1\2~\r\3\2\2\2\177\u0080\7")
        buf.write("\27\2\2\u0080\u0081\b\b\1\2\u0081\u0088\5\20\t\2\u0082")
        buf.write("\u0083\7\"\2\2\u0083\u0084\7\27\2\2\u0084\u0085\b\b\1")
        buf.write("\2\u0085\u0087\5\20\t\2\u0086\u0082\3\2\2\2\u0087\u008a")
        buf.write("\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089")
        buf.write("\17\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c\t\2\2\2\u008c")
        buf.write("\u008d\b\t\1\2\u008d\21\3\2\2\2\u008e\u008f\7\22\2\2\u008f")
        buf.write("\u0090\7\27\2\2\u0090\u0096\b\n\1\2\u0091\u0092\7\"\2")
        buf.write("\2\u0092\u0093\7\27\2\2\u0093\u0095\b\n\1\2\u0094\u0091")
        buf.write("\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u009c\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0099\u009a\7\37\2\2\u009a\u009b\7\30\2\2\u009b\u009d")
        buf.write("\7 \2\2\u009c\u0099\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\5\20\t\2\u009f\u00a0\7!\2\2")
        buf.write("\u00a0\23\3\2\2\2\u00a1\u00a2\5&\24\2\u00a2\u00a3\7\'")
        buf.write("\2\2\u00a3\u00a4\5\34\17\2\u00a4\25\3\2\2\2\u00a5\u00a9")
        buf.write("\7\35\2\2\u00a6\u00a8\5\30\r\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7")
        buf.write("\36\2\2\u00ad\27\3\2\2\2\u00ae\u00af\5\24\13\2\u00af\u00b0")
        buf.write("\7!\2\2\u00b0\u00ba\3\2\2\2\u00b1\u00ba\5,\27\2\u00b2")
        buf.write("\u00b3\5\64\33\2\u00b3\u00b4\7!\2\2\u00b4\u00ba\3\2\2")
        buf.write("\2\u00b5\u00ba\5\62\32\2\u00b6\u00ba\5\60\31\2\u00b7\u00ba")
        buf.write("\58\35\2\u00b8\u00ba\5\32\16\2\u00b9\u00ae\3\2\2\2\u00b9")
        buf.write("\u00b1\3\2\2\2\u00b9\u00b2\3\2\2\2\u00b9\u00b5\3\2\2\2")
        buf.write("\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3")
        buf.write("\2\2\2\u00ba\31\3\2\2\2\u00bb\u00bc\7\17\2\2\u00bc\u00bd")
        buf.write("\5\34\17\2\u00bd\u00be\7!\2\2\u00be\33\3\2\2\2\u00bf\u00c0")
        buf.write("\7(\2\2\u00c0\u00c7\5\36\20\2\u00c1\u00c4\5\36\20\2\u00c2")
        buf.write("\u00c3\t\3\2\2\u00c3\u00c5\5\36\20\2\u00c4\u00c2\3\2\2")
        buf.write("\2\u00c4\u00c5\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00bf")
        buf.write("\3\2\2\2\u00c6\u00c1\3\2\2\2\u00c7\35\3\2\2\2\u00c8\u00cd")
        buf.write("\5 \21\2\u00c9\u00ca\t\4\2\2\u00ca\u00cc\5 \21\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2")
        buf.write("\u00cd\u00ce\3\2\2\2\u00ce\37\3\2\2\2\u00cf\u00cd\3\2")
        buf.write("\2\2\u00d0\u00d5\5\"\22\2\u00d1\u00d2\t\5\2\2\u00d2\u00d4")
        buf.write("\5\"\22\2\u00d3\u00d1\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6!\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d8\u00d9\7\33\2\2\u00d9\u00da\5\34\17")
        buf.write("\2\u00da\u00db\7\34\2\2\u00db\u00e1\3\2\2\2\u00dc\u00de")
        buf.write("\t\4\2\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e1\5$\23\2\u00e0\u00d8\3\2\2\2")
        buf.write("\u00e0\u00dd\3\2\2\2\u00e1#\3\2\2\2\u00e2\u00e9\5&\24")
        buf.write("\2\u00e3\u00e9\7\30\2\2\u00e4\u00e9\7\31\2\2\u00e5\u00e9")
        buf.write("\7\32\2\2\u00e6\u00e9\7\26\2\2\u00e7\u00e9\5\64\33\2\u00e8")
        buf.write("\u00e2\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e8\u00e4\3\2\2\2")
        buf.write("\u00e8\u00e5\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3")
        buf.write("\2\2\2\u00e9%\3\2\2\2\u00ea\u00ee\7\27\2\2\u00eb\u00ee")
        buf.write("\5(\25\2\u00ec\u00ee\5*\26\2\u00ed\u00ea\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ec\3\2\2\2\u00ee\'\3\2\2\2\u00ef")
        buf.write("\u00f0\7\27\2\2\u00f0\u00f1\7\37\2\2\u00f1\u00f2\5\34")
        buf.write("\17\2\u00f2\u00f3\7 \2\2\u00f3)\3\2\2\2\u00f4\u00f5\7")
        buf.write("*\2\2\u00f5\u00f6\7\27\2\2\u00f6+\3\2\2\2\u00f7\u00f8")
        buf.write("\7\f\2\2\u00f8\u00f9\5\34\17\2\u00f9\u00fd\5\26\f\2\u00fa")
        buf.write("\u00fc\5.\30\2\u00fb\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2")
        buf.write("\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0102\3")
        buf.write("\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\7\t\2\2\u0101\u0103")
        buf.write("\5\26\f\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("-\3\2\2\2\u0104\u0105\7\t\2\2\u0105\u0106\7\f\2\2\u0106")
        buf.write("\u0107\5\34\17\2\u0107\u0108\5\26\f\2\u0108/\3\2\2\2\u0109")
        buf.write("\u010a\7\24\2\2\u010a\u010b\5\34\17\2\u010b\u010c\5\26")
        buf.write("\f\2\u010c\61\3\2\2\2\u010d\u010f\7\13\2\2\u010e\u0110")
        buf.write("\5\24\13\2\u010f\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0112\7!\2\2\u0112\u0113\5\34\17")
        buf.write("\2\u0113\u0115\7!\2\2\u0114\u0116\5\24\13\2\u0115\u0114")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0118\5\26\f\2\u0118\63\3\2\2\2\u0119\u011a\5&\24\2\u011a")
        buf.write("\u011b\7#\2\2\u011b\u011d\3\2\2\2\u011c\u0119\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f\7")
        buf.write("\27\2\2\u011f\u0121\7\33\2\2\u0120\u0122\5\66\34\2\u0121")
        buf.write("\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2")
        buf.write("\u0123\u0126\7\34\2\2\u0124\u0126\5:\36\2\u0125\u011c")
        buf.write("\3\2\2\2\u0125\u0124\3\2\2\2\u0126\65\3\2\2\2\u0127\u012c")
        buf.write("\5\34\17\2\u0128\u0129\7\"\2\2\u0129\u012b\5\34\17\2\u012a")
        buf.write("\u0128\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a\3\2\2\2")
        buf.write("\u012c\u012d\3\2\2\2\u012d\67\3\2\2\2\u012e\u012c\3\2")
        buf.write("\2\2\u012f\u0130\7\25\2\2\u0130\u0131\7#\2\2\u0131\u0132")
        buf.write("\7\3\2\2\u0132\u0133\7\33\2\2\u0133\u0134\5\34\17\2\u0134")
        buf.write("\u0135\7\34\2\2\u0135\u0136\7!\2\2\u01369\3\2\2\2\u0137")
        buf.write("\u0138\7\25\2\2\u0138\u0139\7#\2\2\u0139\u013a\t\6\2\2")
        buf.write("\u013a\u013b\7\33\2\2\u013b\u013c\7\34\2\2\u013c;\3\2")
        buf.write("\2\2\37@FQ[aoty\u0088\u0096\u009c\u00a9\u00b9\u00c4\u00c6")
        buf.write("\u00cd\u00d5\u00dd\u00e0\u00e8\u00ed\u00fd\u0102\u010f")
        buf.write("\u0115\u011c\u0121\u0125\u012c")
        return buf.getvalue()


class IdleParser ( Parser ):

    grammarFileName = "Idle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'readString'", "'readInt'", 
                     "'readFloat'", "'bool'", "'class'", "'else'", "'float'", 
                     "'for'", "'if'", "'import'", "'int'", "'return'", "'string'", 
                     "'type'", "'var'", "'void'", "'while'", "'IO'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "'+'", "'&&'", "'<-'", "'='", "'!'", "'/'", 
                     "'$'", "'=='", "'>='", "'>'", "'<='", "'<'", "'*'", 
                     "'!='", "'||'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BOOL", "CLASS", "ELSE", "FLOAT", "FOR", 
                      "IF", "IMPORT", "INT", "RETURN", "STRING", "TYPE", 
                      "VAR", "VOID", "WHILE", "IO", "BOOL_LITERAL", "ID", 
                      "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "SEMICOLON", "COMMA", "DOT", "ADD", "AND", 
                      "ARROW", "ASSIGN", "BANG", "DIV", "DSYMBOL", "EQUAL", 
                      "GE", "GT", "LE", "LT", "MUL", "NOTEQUAL", "OR", "SUB", 
                      "COMMENT", "LINE_COMMENT", "WS" ]

    RULE_fileState = 0
    RULE_imp = 1
    RULE_classState = 2
    RULE_classBlock = 3
    RULE_attribute = 4
    RULE_method = 5
    RULE_methodArguments = 6
    RULE_typeState = 7
    RULE_varsDecl = 8
    RULE_assignment = 9
    RULE_block = 10
    RULE_statement = 11
    RULE_returnState = 12
    RULE_expression = 13
    RULE_exp = 14
    RULE_term = 15
    RULE_factor = 16
    RULE_literal = 17
    RULE_reference = 18
    RULE_arrPos = 19
    RULE_instanceVar = 20
    RULE_condition = 21
    RULE_elseIf = 22
    RULE_whileLoop = 23
    RULE_forLoop = 24
    RULE_call = 25
    RULE_callArguments = 26
    RULE_printState = 27
    RULE_read = 28

    ruleNames =  [ "fileState", "imp", "classState", "classBlock", "attribute", 
                   "method", "methodArguments", "typeState", "varsDecl", 
                   "assignment", "block", "statement", "returnState", "expression", 
                   "exp", "term", "factor", "literal", "reference", "arrPos", 
                   "instanceVar", "condition", "elseIf", "whileLoop", "forLoop", 
                   "call", "callArguments", "printState", "read" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    BOOL=5
    CLASS=6
    ELSE=7
    FLOAT=8
    FOR=9
    IF=10
    IMPORT=11
    INT=12
    RETURN=13
    STRING=14
    TYPE=15
    VAR=16
    VOID=17
    WHILE=18
    IO=19
    BOOL_LITERAL=20
    ID=21
    INT_LITERAL=22
    FLOAT_LITERAL=23
    STRING_LITERAL=24
    LPAREN=25
    RPAREN=26
    LBRACE=27
    RBRACE=28
    LBRACK=29
    RBRACK=30
    SEMICOLON=31
    COMMA=32
    DOT=33
    ADD=34
    AND=35
    ARROW=36
    ASSIGN=37
    BANG=38
    DIV=39
    DSYMBOL=40
    EQUAL=41
    GE=42
    GT=43
    LE=44
    LT=45
    MUL=46
    NOTEQUAL=47
    OR=48
    SUB=49
    COMMENT=50
    LINE_COMMENT=51
    WS=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileStateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ImpContext)
            else:
                return self.getTypedRuleContext(IdleParser.ImpContext,i)


        def classState(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ClassStateContext)
            else:
                return self.getTypedRuleContext(IdleParser.ClassStateContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_fileState

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileState" ):
                listener.enterFileState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileState" ):
                listener.exitFileState(self)




    def fileState(self):

        localctx = IdleParser.FileStateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_fileState)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.icomp = IdleCompiler()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.IMPORT:
                self.state = 59
                self.imp()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.classState()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IdleParser.TYPE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def IMPORT(self):
            return self.getToken(IdleParser.IMPORT, 0)

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(IdleParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_imp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImp" ):
                listener.enterImp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImp" ):
                listener.exitImp(self)




    def imp(self):

        localctx = IdleParser.ImpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_imp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(IdleParser.IMPORT)
            self.state = 71
            localctx._ID = self.match(IdleParser.ID)
            self.state = 72
            self.match(IdleParser.SEMICOLON)
            self.icomp.import_file((None if localctx._ID is None else localctx._ID.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassStateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.class_name = None # Token
            self.parent_name = None # Token

        def TYPE(self):
            return self.getToken(IdleParser.TYPE, 0)

        def CLASS(self):
            return self.getToken(IdleParser.CLASS, 0)

        def classBlock(self):
            return self.getTypedRuleContext(IdleParser.ClassBlockContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.ID)
            else:
                return self.getToken(IdleParser.ID, i)

        def ARROW(self):
            return self.getToken(IdleParser.ARROW, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_classState

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassState" ):
                listener.enterClassState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassState" ):
                listener.exitClassState(self)




    def classState(self):

        localctx = IdleParser.ClassStateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classState)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(IdleParser.TYPE)
            self.state = 76
            localctx.class_name = self.match(IdleParser.ID)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ARROW:
                self.state = 77
                self.match(IdleParser.ARROW)
                self.state = 78
                localctx.parent_name = self.match(IdleParser.ID)


            self.state = 81
            self.match(IdleParser.CLASS)
            self.icomp.add_class((None if localctx.class_name is None else localctx.class_name.text), (0 if localctx.class_name is None else localctx.class_name.line))
            self.state = 83
            self.classBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(IdleParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(IdleParser.RBRACE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.AttributeContext)
            else:
                return self.getTypedRuleContext(IdleParser.AttributeContext,i)


        def method(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.MethodContext)
            else:
                return self.getTypedRuleContext(IdleParser.MethodContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_classBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassBlock" ):
                listener.enterClassBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassBlock" ):
                listener.exitClassBlock(self)




    def classBlock(self):

        localctx = IdleParser.ClassBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(IdleParser.LBRACE)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 86
                    self.attribute() 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ID:
                self.state = 92
                self.method()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(IdleParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def typeState(self):
            return self.getTypedRuleContext(IdleParser.TypeStateContext,0)


        def SEMICOLON(self):
            return self.getToken(IdleParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = IdleParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 102
            self.typeState()
            self.state = 103
            self.match(IdleParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def typeState(self):
            return self.getTypedRuleContext(IdleParser.TypeStateContext,0)


        def VOID(self):
            return self.getToken(IdleParser.VOID, 0)

        def methodArguments(self):
            return self.getTypedRuleContext(IdleParser.MethodArgumentsContext,0)


        def varsDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.VarsDeclContext)
            else:
                return self.getTypedRuleContext(IdleParser.VarsDeclContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod" ):
                listener.enterMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod" ):
                listener.exitMethod(self)




    def method(self):

        localctx = IdleParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_func((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 107
            self.match(IdleParser.LPAREN)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID:
                self.state = 108
                self.methodArguments()


            self.state = 111
            self.match(IdleParser.RPAREN)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.BOOL, IdleParser.FLOAT, IdleParser.INT, IdleParser.STRING, IdleParser.ID]:
                self.state = 112
                self.typeState()
                pass
            elif token in [IdleParser.VOID]:
                self.state = 113
                self.match(IdleParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.VAR:
                self.state = 116
                self.varsDecl()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.block()
            self.icomp.end_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.ID)
            else:
                return self.getToken(IdleParser.ID, i)

        def typeState(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.TypeStateContext)
            else:
                return self.getTypedRuleContext(IdleParser.TypeStateContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.COMMA)
            else:
                return self.getToken(IdleParser.COMMA, i)

        def getRuleIndex(self):
            return IdleParser.RULE_methodArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodArguments" ):
                listener.enterMethodArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodArguments" ):
                listener.exitMethodArguments(self)




    def methodArguments(self):

        localctx = IdleParser.MethodArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_methodArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 127
            self.typeState()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 128
                self.match(IdleParser.COMMA)
                self.state = 129
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 131
                self.typeState()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeStateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_name = None # Token

        def BOOL(self):
            return self.getToken(IdleParser.BOOL, 0)

        def INT(self):
            return self.getToken(IdleParser.INT, 0)

        def FLOAT(self):
            return self.getToken(IdleParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(IdleParser.STRING, 0)

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_typeState

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeState" ):
                listener.enterTypeState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeState" ):
                listener.exitTypeState(self)




    def typeState(self):

        localctx = IdleParser.TypeStateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typeState)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            localctx.type_name = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.BOOL) | (1 << IdleParser.FLOAT) | (1 << IdleParser.INT) | (1 << IdleParser.STRING) | (1 << IdleParser.ID))) != 0)):
                localctx.type_name = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.icomp.commit_vars((None if localctx.type_name is None else localctx.type_name.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def VAR(self):
            return self.getToken(IdleParser.VAR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.ID)
            else:
                return self.getToken(IdleParser.ID, i)

        def typeState(self):
            return self.getTypedRuleContext(IdleParser.TypeStateContext,0)


        def SEMICOLON(self):
            return self.getToken(IdleParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.COMMA)
            else:
                return self.getToken(IdleParser.COMMA, i)

        def LBRACK(self):
            return self.getToken(IdleParser.LBRACK, 0)

        def INT_LITERAL(self):
            return self.getToken(IdleParser.INT_LITERAL, 0)

        def RBRACK(self):
            return self.getToken(IdleParser.RBRACK, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_varsDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsDecl" ):
                listener.enterVarsDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsDecl" ):
                listener.exitVarsDecl(self)




    def varsDecl(self):

        localctx = IdleParser.VarsDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(IdleParser.VAR)
            self.state = 141
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 143
                self.match(IdleParser.COMMA)
                self.state = 144
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.LBRACK:
                self.state = 151
                self.match(IdleParser.LBRACK)
                self.state = 152
                self.match(IdleParser.INT_LITERAL)
                self.state = 153
                self.match(IdleParser.RBRACK)


            self.state = 156
            self.typeState()
            self.state = 157
            self.match(IdleParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reference(self):
            return self.getTypedRuleContext(IdleParser.ReferenceContext,0)


        def ASSIGN(self):
            return self.getToken(IdleParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = IdleParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.reference()
            self.state = 160
            self.match(IdleParser.ASSIGN)
            self.state = 161
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(IdleParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(IdleParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.StatementContext)
            else:
                return self.getTypedRuleContext(IdleParser.StatementContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = IdleParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(IdleParser.LBRACE)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.FOR) | (1 << IdleParser.IF) | (1 << IdleParser.RETURN) | (1 << IdleParser.WHILE) | (1 << IdleParser.IO) | (1 << IdleParser.ID) | (1 << IdleParser.DSYMBOL))) != 0):
                self.state = 164
                self.statement()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(IdleParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(IdleParser.AssignmentContext,0)


        def SEMICOLON(self):
            return self.getToken(IdleParser.SEMICOLON, 0)

        def condition(self):
            return self.getTypedRuleContext(IdleParser.ConditionContext,0)


        def call(self):
            return self.getTypedRuleContext(IdleParser.CallContext,0)


        def forLoop(self):
            return self.getTypedRuleContext(IdleParser.ForLoopContext,0)


        def whileLoop(self):
            return self.getTypedRuleContext(IdleParser.WhileLoopContext,0)


        def printState(self):
            return self.getTypedRuleContext(IdleParser.PrintStateContext,0)


        def returnState(self):
            return self.getTypedRuleContext(IdleParser.ReturnStateContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = IdleParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.assignment()
                self.state = 173
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.call()
                self.state = 177
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 180
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 181
                self.printState()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 182
                self.returnState()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(IdleParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(IdleParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_returnState

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnState" ):
                listener.enterReturnState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnState" ):
                listener.exitReturnState(self)




    def returnState(self):

        localctx = IdleParser.ReturnStateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(IdleParser.RETURN)
            self.state = 186
            self.expression()
            self.state = 187
            self.match(IdleParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BANG(self):
            return self.getToken(IdleParser.BANG, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ExpContext)
            else:
                return self.getTypedRuleContext(IdleParser.ExpContext,i)


        def LT(self):
            return self.getToken(IdleParser.LT, 0)

        def GT(self):
            return self.getToken(IdleParser.GT, 0)

        def LE(self):
            return self.getToken(IdleParser.LE, 0)

        def GE(self):
            return self.getToken(IdleParser.GE, 0)

        def EQUAL(self):
            return self.getToken(IdleParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(IdleParser.NOTEQUAL, 0)

        def AND(self):
            return self.getToken(IdleParser.AND, 0)

        def OR(self):
            return self.getToken(IdleParser.OR, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = IdleParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(IdleParser.BANG)
                self.state = 190
                self.exp()
                pass
            elif token in [IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.LPAREN, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.exp()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0):
                    self.state = 192
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 193
                    self.exp()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.TermContext)
            else:
                return self.getTypedRuleContext(IdleParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.ADD)
            else:
                return self.getToken(IdleParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.SUB)
            else:
                return self.getToken(IdleParser.SUB, i)

        def getRuleIndex(self):
            return IdleParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = IdleParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.term()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ADD or _la==IdleParser.SUB:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.term()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.FactorContext)
            else:
                return self.getTypedRuleContext(IdleParser.FactorContext,i)


        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.DIV)
            else:
                return self.getToken(IdleParser.DIV, i)

        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.MUL)
            else:
                return self.getToken(IdleParser.MUL, i)

        def getRuleIndex(self):
            return IdleParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = IdleParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.factor()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.DIV or _la==IdleParser.MUL:
                self.state = 207
                _la = self._input.LA(1)
                if not(_la==IdleParser.DIV or _la==IdleParser.MUL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.factor()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(IdleParser.LiteralContext,0)


        def ADD(self):
            return self.getToken(IdleParser.ADD, 0)

        def SUB(self):
            return self.getToken(IdleParser.SUB, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = IdleParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(IdleParser.LPAREN)
                self.state = 215
                self.expression()
                self.state = 216
                self.match(IdleParser.RPAREN)
                pass
            elif token in [IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ADD or _la==IdleParser.SUB:
                    self.state = 218
                    _la = self._input.LA(1)
                    if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 221
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def reference(self):
            return self.getTypedRuleContext(IdleParser.ReferenceContext,0)


        def INT_LITERAL(self):
            return self.getToken(IdleParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(IdleParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(IdleParser.STRING_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(IdleParser.BOOL_LITERAL, 0)

        def call(self):
            return self.getTypedRuleContext(IdleParser.CallContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = IdleParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.reference()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(IdleParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self.match(IdleParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.match(IdleParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 228
                self.match(IdleParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 229
                self.call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def arrPos(self):
            return self.getTypedRuleContext(IdleParser.ArrPosContext,0)


        def instanceVar(self):
            return self.getTypedRuleContext(IdleParser.InstanceVarContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)




    def reference(self):

        localctx = IdleParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_reference)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(IdleParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.arrPos()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.instanceVar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrPosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LBRACK(self):
            return self.getToken(IdleParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(IdleParser.RBRACK, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_arrPos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrPos" ):
                listener.enterArrPos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrPos" ):
                listener.exitArrPos(self)




    def arrPos(self):

        localctx = IdleParser.ArrPosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arrPos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(IdleParser.ID)
            self.state = 238
            self.match(IdleParser.LBRACK)
            self.state = 239
            self.expression()
            self.state = 240
            self.match(IdleParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DSYMBOL(self):
            return self.getToken(IdleParser.DSYMBOL, 0)

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_instanceVar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstanceVar" ):
                listener.enterInstanceVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstanceVar" ):
                listener.exitInstanceVar(self)




    def instanceVar(self):

        localctx = IdleParser.InstanceVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_instanceVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(IdleParser.DSYMBOL)
            self.state = 243
            self.match(IdleParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(IdleParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.BlockContext)
            else:
                return self.getTypedRuleContext(IdleParser.BlockContext,i)


        def elseIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ElseIfContext)
            else:
                return self.getTypedRuleContext(IdleParser.ElseIfContext,i)


        def ELSE(self):
            return self.getToken(IdleParser.ELSE, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = IdleParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(IdleParser.IF)
            self.state = 246
            self.expression()
            self.state = 247
            self.block()
            self.state = 251
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 248
                    self.elseIf() 
                self.state = 253
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ELSE:
                self.state = 254
                self.match(IdleParser.ELSE)
                self.state = 255
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(IdleParser.ELSE, 0)

        def IF(self):
            return self.getToken(IdleParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_elseIf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIf" ):
                listener.enterElseIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIf" ):
                listener.exitElseIf(self)




    def elseIf(self):

        localctx = IdleParser.ElseIfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elseIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(IdleParser.ELSE)
            self.state = 259
            self.match(IdleParser.IF)
            self.state = 260
            self.expression()
            self.state = 261
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileLoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(IdleParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_whileLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileLoop" ):
                listener.enterWhileLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileLoop" ):
                listener.exitWhileLoop(self)




    def whileLoop(self):

        localctx = IdleParser.WhileLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(IdleParser.WHILE)
            self.state = 264
            self.expression()
            self.state = 265
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForLoopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(IdleParser.FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.SEMICOLON)
            else:
                return self.getToken(IdleParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(IdleParser.AssignmentContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_forLoop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForLoop" ):
                listener.enterForLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForLoop" ):
                listener.exitForLoop(self)




    def forLoop(self):

        localctx = IdleParser.ForLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(IdleParser.FOR)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 268
                self.assignment()


            self.state = 271
            self.match(IdleParser.SEMICOLON)
            self.state = 272
            self.expression()
            self.state = 273
            self.match(IdleParser.SEMICOLON)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 274
                self.assignment()


            self.state = 277
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def reference(self):
            return self.getTypedRuleContext(IdleParser.ReferenceContext,0)


        def DOT(self):
            return self.getToken(IdleParser.DOT, 0)

        def callArguments(self):
            return self.getTypedRuleContext(IdleParser.CallArgumentsContext,0)


        def read(self):
            return self.getTypedRuleContext(IdleParser.ReadContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)




    def call(self):

        localctx = IdleParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.ID, IdleParser.DSYMBOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 279
                    self.reference()
                    self.state = 280
                    self.match(IdleParser.DOT)


                self.state = 284
                self.match(IdleParser.ID)
                self.state = 285
                self.match(IdleParser.LPAREN)
                self.state = 287
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 286
                    self.callArguments()


                self.state = 289
                self.match(IdleParser.RPAREN)
                pass
            elif token in [IdleParser.IO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.read()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallArgumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(IdleParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.COMMA)
            else:
                return self.getToken(IdleParser.COMMA, i)

        def getRuleIndex(self):
            return IdleParser.RULE_callArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallArguments" ):
                listener.enterCallArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallArguments" ):
                listener.exitCallArguments(self)




    def callArguments(self):

        localctx = IdleParser.CallArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_callArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.expression()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 294
                self.match(IdleParser.COMMA)
                self.state = 295
                self.expression()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IO(self):
            return self.getToken(IdleParser.IO, 0)

        def DOT(self):
            return self.getToken(IdleParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(IdleParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_printState

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintState" ):
                listener.enterPrintState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintState" ):
                listener.exitPrintState(self)




    def printState(self):

        localctx = IdleParser.PrintStateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_printState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(IdleParser.IO)
            self.state = 302
            self.match(IdleParser.DOT)
            self.state = 303
            self.match(IdleParser.T__0)
            self.state = 304
            self.match(IdleParser.LPAREN)
            self.state = 305
            self.expression()
            self.state = 306
            self.match(IdleParser.RPAREN)
            self.state = 307
            self.match(IdleParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IO(self):
            return self.getToken(IdleParser.IO, 0)

        def DOT(self):
            return self.getToken(IdleParser.DOT, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def getRuleIndex(self):
            return IdleParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = IdleParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(IdleParser.IO)
            self.state = 310
            self.match(IdleParser.DOT)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__1) | (1 << IdleParser.T__2) | (1 << IdleParser.T__3))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 312
            self.match(IdleParser.LPAREN)
            self.state = 313
            self.match(IdleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





