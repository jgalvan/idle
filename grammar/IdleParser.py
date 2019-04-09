# Generated from grammar/Idle.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from IdleCompiler import IdleCompiler


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u01b0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\7\2C\n\2\f\2\16\2F\13\2\3\2\6")
        buf.write("\2I\n\2\r\2\16\2J\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4X\n\4\3\4\3\4\3\4\3\4\3\5\3\5\7\5`\n\5\f\5")
        buf.write("\16\5c\13\5\3\5\7\5f\n\5\f\5\16\5i\13\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7v\n\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7}\n\7\3\7\7\7\u0080\n\7\f\7\16\7\u0083\13\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u008d\n\7\3\7\3\7")
        buf.write("\7\7\u0091\n\7\f\7\16\7\u0094\13\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u009a\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b")
        buf.write("\u00a6\n\b\f\b\16\b\u00a9\13\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\7\n\u00b4\n\n\f\n\16\n\u00b7\13\n\3\n\3\n")
        buf.write("\3\n\5\n\u00bc\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00ca\n\f\f\f\16\f\u00cd\13\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00dc")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u00eb\n\17\5\17\u00ed\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\7\20\u00f6\n\20\f\20\16\20")
        buf.write("\u00f9\13\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u0102")
        buf.write("\n\21\f\21\16\21\u0105\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u010e\n\22\3\22\5\22\u0111\n\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u011b\n\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0125\n\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u0137\n\27\3\27\3\27\3")
        buf.write("\30\6\30\u013c\n\30\r\30\16\30\u013d\3\30\3\30\3\30\3")
        buf.write("\30\6\30\u0144\n\30\r\30\16\30\u0145\3\30\3\30\5\30\u014a")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\5\34")
        buf.write("\u0160\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0169")
        buf.write("\n\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0176\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u017f\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0189\n\35\3\35\3\35\5\35\u018d\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\7\36\u0195\n\36\f\36\16\36\u0198")
        buf.write("\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \5 \u01ab\n \3 \3 \3 \3 \2\2!\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>\2\6\7\2\b\b\13\13\17\17\21\21\30\30\5\2&&,\60")
        buf.write("\62\63\4\2%%\64\64\4\2**\61\61\2\u01c2\2@\3\2\2\2\4N\3")
        buf.write("\2\2\2\6S\3\2\2\2\b]\3\2\2\2\nl\3\2\2\2\f\u0099\3\2\2")
        buf.write("\2\16\u009b\3\2\2\2\20\u00aa\3\2\2\2\22\u00ad\3\2\2\2")
        buf.write("\24\u00c0\3\2\2\2\26\u00c5\3\2\2\2\30\u00db\3\2\2\2\32")
        buf.write("\u00dd\3\2\2\2\34\u00ec\3\2\2\2\36\u00ee\3\2\2\2 \u00fa")
        buf.write("\3\2\2\2\"\u0110\3\2\2\2$\u011a\3\2\2\2&\u0124\3\2\2\2")
        buf.write("(\u0126\3\2\2\2*\u012c\3\2\2\2,\u0130\3\2\2\2.\u0149\3")
        buf.write("\2\2\2\60\u014b\3\2\2\2\62\u0152\3\2\2\2\64\u0156\3\2")
        buf.write("\2\2\66\u015d\3\2\2\28\u018c\3\2\2\2:\u018e\3\2\2\2<\u0199")
        buf.write("\3\2\2\2>\u01a2\3\2\2\2@D\b\2\1\2AC\5\4\3\2BA\3\2\2\2")
        buf.write("CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2EH\3\2\2\2FD\3\2\2\2GI\5")
        buf.write("\6\4\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2")
        buf.write("\2LM\b\2\1\2M\3\3\2\2\2NO\7\16\2\2OP\7\30\2\2PQ\7\"\2")
        buf.write("\2QR\b\3\1\2R\5\3\2\2\2ST\7\22\2\2TW\7\30\2\2UV\7\'\2")
        buf.write("\2VX\7\30\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\t\2\2")
        buf.write("Z[\b\4\1\2[\\\5\b\5\2\\\7\3\2\2\2]a\7\36\2\2^`\5\n\6\2")
        buf.write("_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bg\3\2\2\2ca\3")
        buf.write("\2\2\2df\5\f\7\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2")
        buf.write("\2hj\3\2\2\2ig\3\2\2\2jk\7\37\2\2k\t\3\2\2\2lm\7\30\2")
        buf.write("\2mn\b\6\1\2no\5\20\t\2op\7\"\2\2p\13\3\2\2\2qr\7\30\2")
        buf.write("\2rs\b\7\1\2su\7\34\2\2tv\5\16\b\2ut\3\2\2\2uv\3\2\2\2")
        buf.write("vw\3\2\2\2w|\7\35\2\2xy\5\20\t\2yz\b\7\1\2z}\3\2\2\2{")
        buf.write("}\7\24\2\2|x\3\2\2\2|{\3\2\2\2}\u0081\3\2\2\2~\u0080\5")
        buf.write("\22\n\2\177~\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081")
        buf.write("\3\2\2\2\u0084\u0085\5\26\f\2\u0085\u0086\b\7\1\2\u0086")
        buf.write("\u0087\b\7\1\2\u0087\u009a\3\2\2\2\u0088\u0089\7\30\2")
        buf.write("\2\u0089\u008a\b\7\1\2\u008a\u008c\7\34\2\2\u008b\u008d")
        buf.write("\5\16\b\2\u008c\u008b\3\2\2\2\u008c\u008d\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0092\7\35\2\2\u008f\u0091\5\22\n")
        buf.write("\2\u0090\u008f\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0095\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0095\u0096\5\26\f\2\u0096\u0097\b\7\1")
        buf.write("\2\u0097\u0098\b\7\1\2\u0098\u009a\3\2\2\2\u0099q\3\2")
        buf.write("\2\2\u0099\u0088\3\2\2\2\u009a\r\3\2\2\2\u009b\u009c\7")
        buf.write("\30\2\2\u009c\u009d\b\b\1\2\u009d\u009e\5\20\t\2\u009e")
        buf.write("\u00a7\b\b\1\2\u009f\u00a0\7#\2\2\u00a0\u00a1\7\30\2\2")
        buf.write("\u00a1\u00a2\b\b\1\2\u00a2\u00a3\5\20\t\2\u00a3\u00a4")
        buf.write("\b\b\1\2\u00a4\u00a6\3\2\2\2\u00a5\u009f\3\2\2\2\u00a6")
        buf.write("\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2")
        buf.write("\u00a8\17\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\t\2")
        buf.write("\2\2\u00ab\u00ac\b\t\1\2\u00ac\21\3\2\2\2\u00ad\u00ae")
        buf.write("\7\23\2\2\u00ae\u00af\7\30\2\2\u00af\u00b5\b\n\1\2\u00b0")
        buf.write("\u00b1\7#\2\2\u00b1\u00b2\7\30\2\2\u00b2\u00b4\b\n\1\2")
        buf.write("\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3")
        buf.write("\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00bb\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b8\u00b9\7 \2\2\u00b9\u00ba\7\31\2\2\u00ba")
        buf.write("\u00bc\7!\2\2\u00bb\u00b8\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00be\5\20\t\2\u00be\u00bf")
        buf.write("\7\"\2\2\u00bf\23\3\2\2\2\u00c0\u00c1\5&\24\2\u00c1\u00c2")
        buf.write("\7(\2\2\u00c2\u00c3\5\34\17\2\u00c3\u00c4\b\13\1\2\u00c4")
        buf.write("\25\3\2\2\2\u00c5\u00cb\7\36\2\2\u00c6\u00c7\5\30\r\2")
        buf.write("\u00c7\u00c8\b\f\1\2\u00c8\u00ca\3\2\2\2\u00c9\u00c6\3")
        buf.write("\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce")
        buf.write("\u00cf\7\37\2\2\u00cf\27\3\2\2\2\u00d0\u00d1\5\24\13\2")
        buf.write("\u00d1\u00d2\7\"\2\2\u00d2\u00dc\3\2\2\2\u00d3\u00dc\5")
        buf.write(",\27\2\u00d4\u00d5\58\35\2\u00d5\u00d6\7\"\2\2\u00d6\u00dc")
        buf.write("\3\2\2\2\u00d7\u00dc\5\66\34\2\u00d8\u00dc\5\64\33\2\u00d9")
        buf.write("\u00dc\5<\37\2\u00da\u00dc\5\32\16\2\u00db\u00d0\3\2\2")
        buf.write("\2\u00db\u00d3\3\2\2\2\u00db\u00d4\3\2\2\2\u00db\u00d7")
        buf.write("\3\2\2\2\u00db\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2\u00db")
        buf.write("\u00da\3\2\2\2\u00dc\31\3\2\2\2\u00dd\u00de\7\20\2\2\u00de")
        buf.write("\u00df\5\34\17\2\u00df\u00e0\7\"\2\2\u00e0\u00e1\b\16")
        buf.write("\1\2\u00e1\33\3\2\2\2\u00e2\u00e3\7)\2\2\u00e3\u00ed\5")
        buf.write("\36\20\2\u00e4\u00ea\5\36\20\2\u00e5\u00e6\t\3\2\2\u00e6")
        buf.write("\u00e7\b\17\1\2\u00e7\u00e8\5\36\20\2\u00e8\u00e9\b\17")
        buf.write("\1\2\u00e9\u00eb\3\2\2\2\u00ea\u00e5\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00e2\3\2\2\2\u00ec")
        buf.write("\u00e4\3\2\2\2\u00ed\35\3\2\2\2\u00ee\u00ef\5 \21\2\u00ef")
        buf.write("\u00f7\b\20\1\2\u00f0\u00f1\t\4\2\2\u00f1\u00f2\b\20\1")
        buf.write("\2\u00f2\u00f3\5 \21\2\u00f3\u00f4\b\20\1\2\u00f4\u00f6")
        buf.write("\3\2\2\2\u00f5\u00f0\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7")
        buf.write("\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\37\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00fa\u00fb\5\"\22\2\u00fb\u0103\b\21\1")
        buf.write("\2\u00fc\u00fd\t\5\2\2\u00fd\u00fe\b\21\1\2\u00fe\u00ff")
        buf.write("\5\"\22\2\u00ff\u0100\b\21\1\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00fc\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0104\3\2\2\2\u0104!\3\2\2\2\u0105\u0103\3\2\2")
        buf.write("\2\u0106\u0107\7\34\2\2\u0107\u0108\b\22\1\2\u0108\u0109")
        buf.write("\5\34\17\2\u0109\u010a\7\35\2\2\u010a\u010b\b\22\1\2\u010b")
        buf.write("\u0111\3\2\2\2\u010c\u010e\t\4\2\2\u010d\u010c\3\2\2\2")
        buf.write("\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\5")
        buf.write("$\23\2\u0110\u0106\3\2\2\2\u0110\u010d\3\2\2\2\u0111#")
        buf.write("\3\2\2\2\u0112\u0113\5&\24\2\u0113\u0114\b\23\1\2\u0114")
        buf.write("\u011b\3\2\2\2\u0115\u011b\7\31\2\2\u0116\u011b\7\32\2")
        buf.write("\2\u0117\u011b\7\33\2\2\u0118\u011b\7\27\2\2\u0119\u011b")
        buf.write("\58\35\2\u011a\u0112\3\2\2\2\u011a\u0115\3\2\2\2\u011a")
        buf.write("\u0116\3\2\2\2\u011a\u0117\3\2\2\2\u011a\u0118\3\2\2\2")
        buf.write("\u011a\u0119\3\2\2\2\u011b%\3\2\2\2\u011c\u011d\7\30\2")
        buf.write("\2\u011d\u0125\b\24\1\2\u011e\u011f\5(\25\2\u011f\u0120")
        buf.write("\b\24\1\2\u0120\u0125\3\2\2\2\u0121\u0122\5*\26\2\u0122")
        buf.write("\u0123\b\24\1\2\u0123\u0125\3\2\2\2\u0124\u011c\3\2\2")
        buf.write("\2\u0124\u011e\3\2\2\2\u0124\u0121\3\2\2\2\u0125\'\3\2")
        buf.write("\2\2\u0126\u0127\7\30\2\2\u0127\u0128\b\25\1\2\u0128\u0129")
        buf.write("\7 \2\2\u0129\u012a\5\34\17\2\u012a\u012b\7!\2\2\u012b")
        buf.write(")\3\2\2\2\u012c\u012d\7+\2\2\u012d\u012e\7\30\2\2\u012e")
        buf.write("\u012f\b\26\1\2\u012f+\3\2\2\2\u0130\u0131\7\r\2\2\u0131")
        buf.write("\u0132\5\34\17\2\u0132\u0133\b\27\1\2\u0133\u0136\5\26")
        buf.write("\f\2\u0134\u0135\b\27\1\2\u0135\u0137\5.\30\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2\u0138")
        buf.write("\u0139\b\27\1\2\u0139-\3\2\2\2\u013a\u013c\5\60\31\2\u013b")
        buf.write("\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\b")
        buf.write("\30\1\2\u0140\u014a\3\2\2\2\u0141\u014a\5\62\32\2\u0142")
        buf.write("\u0144\5\60\31\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2")
        buf.write("\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0148\5\62\32\2\u0148\u014a\3\2\2\2\u0149")
        buf.write("\u013b\3\2\2\2\u0149\u0141\3\2\2\2\u0149\u0143\3\2\2\2")
        buf.write("\u014a/\3\2\2\2\u014b\u014c\7\n\2\2\u014c\u014d\7\r\2")
        buf.write("\2\u014d\u014e\b\31\1\2\u014e\u014f\5\34\17\2\u014f\u0150")
        buf.write("\b\31\1\2\u0150\u0151\5\26\f\2\u0151\61\3\2\2\2\u0152")
        buf.write("\u0153\7\n\2\2\u0153\u0154\b\32\1\2\u0154\u0155\5\26\f")
        buf.write("\2\u0155\63\3\2\2\2\u0156\u0157\7\25\2\2\u0157\u0158\b")
        buf.write("\33\1\2\u0158\u0159\5\34\17\2\u0159\u015a\b\33\1\2\u015a")
        buf.write("\u015b\5\26\f\2\u015b\u015c\b\33\1\2\u015c\65\3\2\2\2")
        buf.write("\u015d\u015f\7\f\2\2\u015e\u0160\5\24\13\2\u015f\u015e")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\u0162\7\"\2\2\u0162\u0163\b\34\1\2\u0163\u0164\5\34\17")
        buf.write("\2\u0164\u0165\b\34\1\2\u0165\u0166\7\"\2\2\u0166\u0168")
        buf.write("\b\34\1\2\u0167\u0169\5\24\13\2\u0168\u0167\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\b\34\1")
        buf.write("\2\u016b\u016c\5\26\f\2\u016c\u016d\b\34\1\2\u016d\u016e")
        buf.write("\b\34\1\2\u016e\67\3\2\2\2\u016f\u0170\5&\24\2\u0170\u0171")
        buf.write("\7$\2\2\u0171\u0172\7\30\2\2\u0172\u0173\b\35\1\2\u0173")
        buf.write("\u0175\7\34\2\2\u0174\u0176\5:\36\2\u0175\u0174\3\2\2")
        buf.write("\2\u0175\u0176\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178")
        buf.write("\7\35\2\2\u0178\u0179\b\35\1\2\u0179\u018d\3\2\2\2\u017a")
        buf.write("\u017b\7\30\2\2\u017b\u017c\b\35\1\2\u017c\u017e\7\34")
        buf.write("\2\2\u017d\u017f\5:\36\2\u017e\u017d\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\7\35\2\2\u0181")
        buf.write("\u018d\b\35\1\2\u0182\u018d\5> \2\u0183\u0184\7\3\2\2")
        buf.write("\u0184\u0185\7\30\2\2\u0185\u0186\b\35\1\2\u0186\u0188")
        buf.write("\7\34\2\2\u0187\u0189\5:\36\2\u0188\u0187\3\2\2\2\u0188")
        buf.write("\u0189\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\7\35\2")
        buf.write("\2\u018b\u018d\b\35\1\2\u018c\u016f\3\2\2\2\u018c\u017a")
        buf.write("\3\2\2\2\u018c\u0182\3\2\2\2\u018c\u0183\3\2\2\2\u018d")
        buf.write("9\3\2\2\2\u018e\u018f\5\34\17\2\u018f\u0196\b\36\1\2\u0190")
        buf.write("\u0191\7#\2\2\u0191\u0192\5\34\17\2\u0192\u0193\b\36\1")
        buf.write("\2\u0193\u0195\3\2\2\2\u0194\u0190\3\2\2\2\u0195\u0198")
        buf.write("\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write(";\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7\26\2\2\u019a")
        buf.write("\u019b\7$\2\2\u019b\u019c\7\4\2\2\u019c\u019d\7\34\2\2")
        buf.write("\u019d\u019e\5\34\17\2\u019e\u019f\7\35\2\2\u019f\u01a0")
        buf.write("\7\"\2\2\u01a0\u01a1\b\37\1\2\u01a1=\3\2\2\2\u01a2\u01a3")
        buf.write("\7\26\2\2\u01a3\u01aa\7$\2\2\u01a4\u01a5\7\5\2\2\u01a5")
        buf.write("\u01ab\b \1\2\u01a6\u01a7\7\6\2\2\u01a7\u01ab\b \1\2\u01a8")
        buf.write("\u01a9\7\7\2\2\u01a9\u01ab\b \1\2\u01aa\u01a4\3\2\2\2")
        buf.write("\u01aa\u01a6\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01ad\7\34\2\2\u01ad\u01ae\7\35\2\2\u01ae")
        buf.write("?\3\2\2\2&DJWagu|\u0081\u008c\u0092\u0099\u00a7\u00b5")
        buf.write("\u00bb\u00cb\u00db\u00ea\u00ec\u00f7\u0103\u010d\u0110")
        buf.write("\u011a\u0124\u0136\u013d\u0145\u0149\u015f\u0168\u0175")
        buf.write("\u017e\u0188\u018c\u0196\u01aa")
        return buf.getvalue()


class IdleParser ( Parser ):

    grammarFileName = "Idle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'new'", "'print'", "'readString'", "'readInt'", 
                     "'readFloat'", "'bool'", "'class'", "'else'", "'float'", 
                     "'for'", "'if'", "'import'", "'int'", "'return'", "'string'", 
                     "'type'", "'var'", "'void'", "'while'", "'IO'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", 
                     "'.'", "'+'", "'&&'", "'<-'", "'='", "'!'", "'/'", 
                     "'$'", "'=='", "'>='", "'>'", "'<='", "'<'", "'*'", 
                     "'!='", "'||'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "CLASS", "ELSE", 
                      "FLOAT", "FOR", "IF", "IMPORT", "INT", "RETURN", "STRING", 
                      "TYPE", "VAR", "VOID", "WHILE", "IO", "BOOL_LITERAL", 
                      "ID", "INT_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
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
    RULE_elseIfs = 22
    RULE_elseIf = 23
    RULE_finalElse = 24
    RULE_whileLoop = 25
    RULE_forLoop = 26
    RULE_call = 27
    RULE_callArguments = 28
    RULE_printState = 29
    RULE_read = 30

    ruleNames =  [ "fileState", "imp", "classState", "classBlock", "attribute", 
                   "method", "methodArguments", "typeState", "varsDecl", 
                   "assignment", "block", "statement", "returnState", "expression", 
                   "exp", "term", "factor", "literal", "reference", "arrPos", 
                   "instanceVar", "condition", "elseIfs", "elseIf", "finalElse", 
                   "whileLoop", "forLoop", "call", "callArguments", "printState", 
                   "read" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    BOOL=6
    CLASS=7
    ELSE=8
    FLOAT=9
    FOR=10
    IF=11
    IMPORT=12
    INT=13
    RETURN=14
    STRING=15
    TYPE=16
    VAR=17
    VOID=18
    WHILE=19
    IO=20
    BOOL_LITERAL=21
    ID=22
    INT_LITERAL=23
    FLOAT_LITERAL=24
    STRING_LITERAL=25
    LPAREN=26
    RPAREN=27
    LBRACE=28
    RBRACE=29
    LBRACK=30
    RBRACK=31
    SEMICOLON=32
    COMMA=33
    DOT=34
    ADD=35
    AND=36
    ARROW=37
    ASSIGN=38
    BANG=39
    DIV=40
    DSYMBOL=41
    EQUAL=42
    GE=43
    GT=44
    LE=45
    LT=46
    MUL=47
    NOTEQUAL=48
    OR=49
    SUB=50
    COMMENT=51
    LINE_COMMENT=52
    WS=53

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
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.IMPORT:
                self.state = 63
                self.imp()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.classState()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==IdleParser.TYPE):
                    break

            self.icomp.printQuads()
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
            self.state = 76
            self.match(IdleParser.IMPORT)
            self.state = 77
            localctx._ID = self.match(IdleParser.ID)
            self.state = 78
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
            self.state = 81
            self.match(IdleParser.TYPE)
            self.state = 82
            localctx.class_name = self.match(IdleParser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ARROW:
                self.state = 83
                self.match(IdleParser.ARROW)
                self.state = 84
                localctx.parent_name = self.match(IdleParser.ID)


            self.state = 87
            self.match(IdleParser.CLASS)
            self.icomp.add_class((None if localctx.class_name is None else localctx.class_name.text), (0 if localctx.class_name is None else localctx.class_name.line), (None if localctx.parent_name is None else localctx.parent_name.text))
            self.state = 89
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
            self.state = 91
            self.match(IdleParser.LBRACE)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.attribute() 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ID:
                self.state = 98
                self.method()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
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
            self.state = 106
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 108
            self.typeState()
            self.state = 109
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
            self._typeState = None # TypeStateContext
            self._block = None # BlockContext

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
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_func((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 113
                self.match(IdleParser.LPAREN)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ID:
                    self.state = 114
                    self.methodArguments()


                self.state = 117
                self.match(IdleParser.RPAREN)
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IdleParser.BOOL, IdleParser.FLOAT, IdleParser.INT, IdleParser.STRING, IdleParser.ID]:
                    self.state = 118
                    localctx._typeState = self.typeState()
                    self.icomp.add_func_return_type((None if localctx._typeState is None else self._input.getText((localctx._typeState.start,localctx._typeState.stop))))
                    pass
                elif token in [IdleParser.VOID]:
                    self.state = 121
                    self.match(IdleParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IdleParser.VAR:
                    self.state = 124
                    self.varsDecl()
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                localctx._block = self.block()
                self.icomp.quad_add_endproc((None if localctx._block is None else localctx._block.stop).line)
                self.icomp.end_scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_constructor((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 136
                self.match(IdleParser.LPAREN)
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ID:
                    self.state = 137
                    self.methodArguments()


                self.state = 140
                self.match(IdleParser.RPAREN)
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IdleParser.VAR:
                    self.state = 141
                    self.varsDecl()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 147
                localctx._block = self.block()
                self.icomp.quad_add_endproc((None if localctx._block is None else localctx._block.stop).line)
                self.icomp.end_scope()
                pass


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
            self.state = 153
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 155
            self.typeState()
            self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 157
                self.match(IdleParser.COMMA)
                self.state = 158
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 160
                self.typeState()
                self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
                self.state = 167
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
            self.state = 168
            localctx.type_name = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.BOOL) | (1 << IdleParser.FLOAT) | (1 << IdleParser.INT) | (1 << IdleParser.STRING) | (1 << IdleParser.ID))) != 0)):
                localctx.type_name = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.icomp.commit_vars((None if localctx.type_name is None else localctx.type_name.text), (0 if localctx.type_name is None else localctx.type_name.line))
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
            self.state = 171
            self.match(IdleParser.VAR)
            self.state = 172
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 174
                self.match(IdleParser.COMMA)
                self.state = 175
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.LBRACK:
                self.state = 182
                self.match(IdleParser.LBRACK)
                self.state = 183
                self.match(IdleParser.INT_LITERAL)
                self.state = 184
                self.match(IdleParser.RBRACK)


            self.state = 187
            self.typeState()
            self.state = 188
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
            self._reference = None # ReferenceContext

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
            self.state = 190
            localctx._reference = self.reference()
            self.state = 191
            self.match(IdleParser.ASSIGN)
            self.state = 192
            self.expression()
            self.icomp.quad_assign((None if localctx._reference is None else self._input.getText((localctx._reference.start,localctx._reference.stop))), (None if localctx._reference is None else localctx._reference.start).line)
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
            self.state = 195
            self.match(IdleParser.LBRACE)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.FOR) | (1 << IdleParser.IF) | (1 << IdleParser.RETURN) | (1 << IdleParser.WHILE) | (1 << IdleParser.IO) | (1 << IdleParser.ID) | (1 << IdleParser.DSYMBOL))) != 0):
                self.state = 196
                self.statement()
                self.icomp.reset_new_line()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
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
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.assignment()
                self.state = 207
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
                self.call()
                self.state = 211
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.printState()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 216
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
            self._expression = None # ExpressionContext

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
            self.state = 219
            self.match(IdleParser.RETURN)
            self.state = 220
            localctx._expression = self.expression()
            self.state = 221
            self.match(IdleParser.SEMICOLON)
            self.icomp.quad_add_func_return((None if localctx._expression is None else localctx._expression.start).line)
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
            self._exp = None # ExpContext
            self.operator = None # Token

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
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(IdleParser.BANG)
                self.state = 225
                self.exp()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.LPAREN, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                localctx._exp = self.exp()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0):
                    self.state = 227
                    localctx.operator = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0)):
                        localctx.operator = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                    self.state = 229
                    localctx._exp = self.exp()
                    self.icomp.quad_check_relop((None if localctx._exp is None else localctx._exp.start).line)


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
            self._term = None # TermContext
            self.operator = None # Token

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
            self.state = 236
            localctx._term = self.term()
            self.icomp.quad_check_addsub((None if localctx._term is None else localctx._term.start).line)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ADD or _la==IdleParser.SUB:
                self.state = 238
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                self.state = 240
                localctx._term = self.term()
                self.icomp.quad_check_addsub((None if localctx._term is None else localctx._term.start).line)
                self.state = 247
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
            self._factor = None # FactorContext
            self.operator = None # Token

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
            self.state = 248
            localctx._factor = self.factor()
            self.icomp.quad_check_divmult((None if localctx._factor is None else localctx._factor.start).line)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.DIV or _la==IdleParser.MUL:
                self.state = 250
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IdleParser.DIV or _la==IdleParser.MUL):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                self.state = 252
                localctx._factor = self.factor()
                self.icomp.quad_check_divmult((None if localctx._factor is None else localctx._factor.start).line)
                self.state = 259
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
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(IdleParser.LPAREN)
                self.icomp.quad_open_parenthesis()
                self.state = 262
                self.expression()
                self.state = 263
                self.match(IdleParser.RPAREN)
                self.icomp.quad_close_parenthesis()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ADD or _la==IdleParser.SUB:
                    self.state = 266
                    _la = self._input.LA(1)
                    if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 269
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
            self._reference = None # ReferenceContext

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
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                localctx._reference = self.reference()
                self.icomp.quad_add_var((None if localctx._reference is None else self._input.getText((localctx._reference.start,localctx._reference.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.match(IdleParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 276
                self.match(IdleParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 277
                self.match(IdleParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 278
                self.match(IdleParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 279
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
            self.attr_ref = None
            self._ID = None # Token
            self._arrPos = None # ArrPosContext
            self._instanceVar = None # InstanceVarContext

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
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                localctx._arrPos = self.arrPos()
                localctx.attr_ref = localctx._arrPos.attr_ref
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                localctx._instanceVar = self.instanceVar()
                localctx.attr_ref = localctx._instanceVar.attr_ref
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
            self.attr_ref = None
            self._ID = None # Token

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
            self.state = 292
            localctx._ID = self.match(IdleParser.ID)
            localctx.attr_ref = self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 294
            self.match(IdleParser.LBRACK)
            self.state = 295
            self.expression()
            self.state = 296
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
            self.attr_ref = None
            self._ID = None # Token

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
            self.state = 298
            self.match(IdleParser.DSYMBOL)
            self.state = 299
            localctx._ID = self.match(IdleParser.ID)
            localctx.attr_ref = self.icomp.check_instance_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
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
            self._expression = None # ExpressionContext

        def IF(self):
            return self.getToken(IdleParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def elseIfs(self):
            return self.getTypedRuleContext(IdleParser.ElseIfsContext,0)


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
            self.state = 302
            self.match(IdleParser.IF)
            self.state = 303
            localctx._expression = self.expression()
            self.icomp.quad_end_if_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 305
            self.block()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ELSE:
                self.icomp.quad_start_else_ifs()
                self.state = 307
                self.elseIfs()


            self.icomp.quad_fill_if_end_jumps()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseIf(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ElseIfContext)
            else:
                return self.getTypedRuleContext(IdleParser.ElseIfContext,i)


        def finalElse(self):
            return self.getTypedRuleContext(IdleParser.FinalElseContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_elseIfs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfs" ):
                listener.enterElseIfs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfs" ):
                listener.exitElseIfs(self)




    def elseIfs(self):

        localctx = IdleParser.ElseIfsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elseIfs)
        self._la = 0 # Token type
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 312
                    self.elseIf()
                    self.state = 315 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==IdleParser.ELSE):
                        break

                self.icomp.quad_fill_if_end_jumps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                self.finalElse()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 321 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 320
                        self.elseIf()

                    else:
                        raise NoViableAltException(self)
                    self.state = 323 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

                self.state = 325
                self.finalElse()
                pass


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
            self._expression = None # ExpressionContext

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
        self.enterRule(localctx, 46, self.RULE_elseIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(IdleParser.ELSE)
            self.state = 330
            self.match(IdleParser.IF)
            self.icomp.quad_add_else()
            self.state = 332
            localctx._expression = self.expression()
            self.icomp.quad_end_if_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 334
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinalElseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(IdleParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_finalElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalElse" ):
                listener.enterFinalElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalElse" ):
                listener.exitFinalElse(self)




    def finalElse(self):

        localctx = IdleParser.FinalElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_finalElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(IdleParser.ELSE)
            self.icomp.quad_add_else()
            self.state = 338
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
            self._expression = None # ExpressionContext

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
        self.enterRule(localctx, 50, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(IdleParser.WHILE)
            self.icomp.quad_start_while()
            self.state = 342
            localctx._expression = self.expression()
            self.icomp.quad_end_while_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 344
            self.block()
            self.icomp.quad_end_while()
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
            self._expression = None # ExpressionContext

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
        self.enterRule(localctx, 52, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(IdleParser.FOR)
            self.state = 349
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 348
                self.assignment()


            self.state = 351
            self.match(IdleParser.SEMICOLON)
            self.icomp.quad_start_while()
            self.state = 353
            localctx._expression = self.expression()
            self.icomp.quad_end_while_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 355
            self.match(IdleParser.SEMICOLON)
            self.icomp.quad_start_for_assign()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 357
                self.assignment()


            self.icomp.quad_end_for_assign()
            self.state = 361
            self.block()
            self.icomp.quad_end_for_block()
            self.icomp.quad_end_while()
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
            self._reference = None # ReferenceContext
            self._ID = None # Token

        def reference(self):
            return self.getTypedRuleContext(IdleParser.ReferenceContext,0)


        def DOT(self):
            return self.getToken(IdleParser.DOT, 0)

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

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
        self.enterRule(localctx, 54, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                localctx._reference = self.reference()
                self.state = 366
                self.match(IdleParser.DOT)
                self.state = 367
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_obj_func_exists(localctx._reference.attr_ref, (None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 369
                self.match(IdleParser.LPAREN)
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 370
                    self.callArguments()


                self.state = 373
                self.match(IdleParser.RPAREN)
                self.icomp.quad_add_func_gosub((0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_func_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 378
                self.match(IdleParser.LPAREN)
                self.state = 380
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 379
                    self.callArguments()


                self.state = 382
                self.match(IdleParser.RPAREN)
                self.icomp.quad_add_func_gosub((0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.read()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
                self.match(IdleParser.T__0)
                self.state = 386
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_class_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 388
                self.match(IdleParser.LPAREN)
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 389
                    self.callArguments()


                self.state = 392
                self.match(IdleParser.RPAREN)
                self.icomp.quad_add_func_gosub((0 if localctx._ID is None else localctx._ID.line))
                pass


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
            self._expression = None # ExpressionContext

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
        self.enterRule(localctx, 56, self.RULE_callArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            localctx._expression = self.expression()
            self.icomp.quad_add_func_param((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 404
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 398
                self.match(IdleParser.COMMA)
                self.state = 399
                localctx._expression = self.expression()
                self.icomp.quad_add_func_param((None if localctx._expression is None else localctx._expression.start).line)
                self.state = 406
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
        self.enterRule(localctx, 58, self.RULE_printState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(IdleParser.IO)
            self.state = 408
            self.match(IdleParser.DOT)
            self.state = 409
            self.match(IdleParser.T__1)
            self.state = 410
            self.match(IdleParser.LPAREN)
            self.state = 411
            self.expression()
            self.state = 412
            self.match(IdleParser.RPAREN)
            self.state = 413
            self.match(IdleParser.SEMICOLON)
            self.icomp.quad_print_st()
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
        self.enterRule(localctx, 60, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(IdleParser.IO)
            self.state = 417
            self.match(IdleParser.DOT)
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.T__2]:
                self.state = 418
                self.match(IdleParser.T__2)
                self.icomp.quad_read('string')
                pass
            elif token in [IdleParser.T__3]:
                self.state = 420
                self.match(IdleParser.T__3)
                self.icomp.quad_read('int')
                pass
            elif token in [IdleParser.T__4]:
                self.state = 422
                self.match(IdleParser.T__4)
                self.icomp.quad_read('float')
                pass
            else:
                raise NoViableAltException(self)

            self.state = 426
            self.match(IdleParser.LPAREN)
            self.state = 427
            self.match(IdleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





