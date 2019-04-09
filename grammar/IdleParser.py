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
        buf.write("\u01db\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\3")
        buf.write("\2\7\2M\n\2\f\2\16\2P\13\2\3\2\6\2S\n\2\r\2\16\2T\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4b\n\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\7\5j\n\5\f\5\16\5m\13\5\3\5\7\5p")
        buf.write("\n\5\f\5\16\5s\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\5\7\177\n\7\3\b\3\b\3\b\3\b\5\b\u0085\n\b\3\b\3")
        buf.write("\b\3\b\3\b\7\b\u008b\n\b\f\b\16\b\u008e\13\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\5\t\u0098\n\t\3\t\3\t\3\t\7\t\u009d")
        buf.write("\n\t\f\t\16\t\u00a0\13\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u00aa\n\n\3\n\3\n\7\n\u00ae\n\n\f\n\16\n\u00b1")
        buf.write("\13\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\7\13\u00bb\n")
        buf.write("\13\f\13\16\13\u00be\13\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00cd\n\f\f\f\16\f\u00d0")
        buf.write("\13\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00db")
        buf.write("\n\16\f\16\16\16\u00de\13\16\3\16\3\16\3\16\5\16\u00e3")
        buf.write("\n\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\7\20\u00f1\n\20\f\20\16\20\u00f4\13\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\5\21\u0104\n\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0113\n\23")
        buf.write("\5\23\u0115\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u011e\n\24\f\24\16\24\u0121\13\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u012a\n\25\f\25\16\25\u012d\13")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0136\n\26")
        buf.write("\3\26\5\26\u0139\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u0143\n\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u014d\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u015f\n\33\3\33\3\33\3\34\6\34\u0164\n\34\r\34\16")
        buf.write("\34\u0165\3\34\3\34\3\34\3\34\6\34\u016c\n\34\r\34\16")
        buf.write("\34\u016d\3\34\3\34\5\34\u0172\n\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \5 \u0188\n \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \5 \u0191\n \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u01a1\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u01aa\n\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01b4\n")
        buf.write("\"\3\"\3\"\5\"\u01b8\n\"\3#\3#\3#\3#\3#\3#\7#\u01c0\n")
        buf.write("#\f#\16#\u01c3\13#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\5%\u01d6\n%\3%\3%\3%\3%\2\2&\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668")
        buf.write(":<>@BDFH\2\6\7\2\b\b\13\13\17\17\21\21\30\30\5\2&&,\60")
        buf.write("\62\63\4\2%%\64\64\4\2**\61\61\2\u01eb\2J\3\2\2\2\4X\3")
        buf.write("\2\2\2\6]\3\2\2\2\bg\3\2\2\2\nv\3\2\2\2\f~\3\2\2\2\16")
        buf.write("\u0080\3\2\2\2\20\u0093\3\2\2\2\22\u00a5\3\2\2\2\24\u00b6")
        buf.write("\3\2\2\2\26\u00c2\3\2\2\2\30\u00d1\3\2\2\2\32\u00d4\3")
        buf.write("\2\2\2\34\u00e7\3\2\2\2\36\u00ec\3\2\2\2 \u0103\3\2\2")
        buf.write("\2\"\u0105\3\2\2\2$\u0114\3\2\2\2&\u0116\3\2\2\2(\u0122")
        buf.write("\3\2\2\2*\u0138\3\2\2\2,\u0142\3\2\2\2.\u014c\3\2\2\2")
        buf.write("\60\u014e\3\2\2\2\62\u0154\3\2\2\2\64\u0158\3\2\2\2\66")
        buf.write("\u0171\3\2\2\28\u0173\3\2\2\2:\u017a\3\2\2\2<\u017e\3")
        buf.write("\2\2\2>\u0185\3\2\2\2@\u0197\3\2\2\2B\u01b7\3\2\2\2D\u01b9")
        buf.write("\3\2\2\2F\u01c4\3\2\2\2H\u01cd\3\2\2\2JN\b\2\1\2KM\5\4")
        buf.write("\3\2LK\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO\3\2\2\2OR\3\2\2\2")
        buf.write("PN\3\2\2\2QS\5\6\4\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3")
        buf.write("\2\2\2UV\3\2\2\2VW\b\2\1\2W\3\3\2\2\2XY\7\16\2\2YZ\7\30")
        buf.write("\2\2Z[\7\"\2\2[\\\b\3\1\2\\\5\3\2\2\2]^\7\22\2\2^a\7\30")
        buf.write("\2\2_`\7\'\2\2`b\7\30\2\2a_\3\2\2\2ab\3\2\2\2bc\3\2\2")
        buf.write("\2cd\7\t\2\2de\b\4\1\2ef\5\b\5\2f\7\3\2\2\2gk\7\36\2\2")
        buf.write("hj\5\n\6\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2lq\3")
        buf.write("\2\2\2mk\3\2\2\2np\5\f\7\2on\3\2\2\2ps\3\2\2\2qo\3\2\2")
        buf.write("\2qr\3\2\2\2rt\3\2\2\2sq\3\2\2\2tu\7\37\2\2u\t\3\2\2\2")
        buf.write("vw\7\30\2\2wx\b\6\1\2xy\5\30\r\2yz\7\"\2\2z\13\3\2\2\2")
        buf.write("{\177\5\16\b\2|\177\5\20\t\2}\177\5\22\n\2~{\3\2\2\2~")
        buf.write("|\3\2\2\2~}\3\2\2\2\177\r\3\2\2\2\u0080\u0081\7\30\2\2")
        buf.write("\u0081\u0082\b\b\1\2\u0082\u0084\7\34\2\2\u0083\u0085")
        buf.write("\5\26\f\2\u0084\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0087\7\35\2\2\u0087\u0088\5\30\r")
        buf.write("\2\u0088\u008c\b\b\1\2\u0089\u008b\5\32\16\2\u008a\u0089")
        buf.write("\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008f\u0090\5\24\13\2\u0090\u0091\b\b\1\2\u0091\u0092")
        buf.write("\b\b\1\2\u0092\17\3\2\2\2\u0093\u0094\7\30\2\2\u0094\u0095")
        buf.write("\b\t\1\2\u0095\u0097\7\34\2\2\u0096\u0098\5\26\f\2\u0097")
        buf.write("\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009a\7\35\2\2\u009a\u009e\7\24\2\2\u009b\u009d")
        buf.write("\5\32\16\2\u009c\u009b\3\2\2\2\u009d\u00a0\3\2\2\2\u009e")
        buf.write("\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a1\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a1\u00a2\5\36\20\2\u00a2\u00a3")
        buf.write("\b\t\1\2\u00a3\u00a4\b\t\1\2\u00a4\21\3\2\2\2\u00a5\u00a6")
        buf.write("\7\30\2\2\u00a6\u00a7\b\n\1\2\u00a7\u00a9\7\34\2\2\u00a8")
        buf.write("\u00aa\5\26\f\2\u00a9\u00a8\3\2\2\2\u00a9\u00aa\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u00af\7\35\2\2\u00ac\u00ae")
        buf.write("\5\32\16\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2")
        buf.write("\u00b1\u00af\3\2\2\2\u00b2\u00b3\5\36\20\2\u00b3\u00b4")
        buf.write("\b\n\1\2\u00b4\u00b5\b\n\1\2\u00b5\23\3\2\2\2\u00b6\u00bc")
        buf.write("\7\36\2\2\u00b7\u00b8\5 \21\2\u00b8\u00b9\b\13\1\2\u00b9")
        buf.write("\u00bb\3\2\2\2\u00ba\u00b7\3\2\2\2\u00bb\u00be\3\2\2\2")
        buf.write("\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00bf\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\5\"\22\2\u00c0")
        buf.write("\u00c1\7\37\2\2\u00c1\25\3\2\2\2\u00c2\u00c3\7\30\2\2")
        buf.write("\u00c3\u00c4\b\f\1\2\u00c4\u00c5\5\30\r\2\u00c5\u00ce")
        buf.write("\b\f\1\2\u00c6\u00c7\7#\2\2\u00c7\u00c8\7\30\2\2\u00c8")
        buf.write("\u00c9\b\f\1\2\u00c9\u00ca\5\30\r\2\u00ca\u00cb\b\f\1")
        buf.write("\2\u00cb\u00cd\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cd\u00d0")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\27\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\t\2\2\2\u00d2")
        buf.write("\u00d3\b\r\1\2\u00d3\31\3\2\2\2\u00d4\u00d5\7\23\2\2\u00d5")
        buf.write("\u00d6\7\30\2\2\u00d6\u00dc\b\16\1\2\u00d7\u00d8\7#\2")
        buf.write("\2\u00d8\u00d9\7\30\2\2\u00d9\u00db\b\16\1\2\u00da\u00d7")
        buf.write("\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc")
        buf.write("\u00dd\3\2\2\2\u00dd\u00e2\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00df\u00e0\7 \2\2\u00e0\u00e1\7\31\2\2\u00e1\u00e3\7")
        buf.write("!\2\2\u00e2\u00df\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4")
        buf.write("\3\2\2\2\u00e4\u00e5\5\30\r\2\u00e5\u00e6\7\"\2\2\u00e6")
        buf.write("\33\3\2\2\2\u00e7\u00e8\5.\30\2\u00e8\u00e9\7(\2\2\u00e9")
        buf.write("\u00ea\5$\23\2\u00ea\u00eb\b\17\1\2\u00eb\35\3\2\2\2\u00ec")
        buf.write("\u00f2\7\36\2\2\u00ed\u00ee\5 \21\2\u00ee\u00ef\b\20\1")
        buf.write("\2\u00ef\u00f1\3\2\2\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\7\37\2")
        buf.write("\2\u00f6\37\3\2\2\2\u00f7\u00f8\5\34\17\2\u00f8\u00f9")
        buf.write("\7\"\2\2\u00f9\u0104\3\2\2\2\u00fa\u0104\5\64\33\2\u00fb")
        buf.write("\u00fc\5B\"\2\u00fc\u00fd\7\"\2\2\u00fd\u00fe\b\21\1\2")
        buf.write("\u00fe\u0104\3\2\2\2\u00ff\u0104\5> \2\u0100\u0104\5<")
        buf.write("\37\2\u0101\u0104\5F$\2\u0102\u0104\5\"\22\2\u0103\u00f7")
        buf.write("\3\2\2\2\u0103\u00fa\3\2\2\2\u0103\u00fb\3\2\2\2\u0103")
        buf.write("\u00ff\3\2\2\2\u0103\u0100\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104!\3\2\2\2\u0105\u0106\7\20\2")
        buf.write("\2\u0106\u0107\5$\23\2\u0107\u0108\7\"\2\2\u0108\u0109")
        buf.write("\b\22\1\2\u0109#\3\2\2\2\u010a\u010b\7)\2\2\u010b\u0115")
        buf.write("\5&\24\2\u010c\u0112\5&\24\2\u010d\u010e\t\3\2\2\u010e")
        buf.write("\u010f\b\23\1\2\u010f\u0110\5&\24\2\u0110\u0111\b\23\1")
        buf.write("\2\u0111\u0113\3\2\2\2\u0112\u010d\3\2\2\2\u0112\u0113")
        buf.write("\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u010a\3\2\2\2\u0114")
        buf.write("\u010c\3\2\2\2\u0115%\3\2\2\2\u0116\u0117\5(\25\2\u0117")
        buf.write("\u011f\b\24\1\2\u0118\u0119\t\4\2\2\u0119\u011a\b\24\1")
        buf.write("\2\u011a\u011b\5(\25\2\u011b\u011c\b\24\1\2\u011c\u011e")
        buf.write("\3\2\2\2\u011d\u0118\3\2\2\2\u011e\u0121\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\'\3\2\2\2\u0121")
        buf.write("\u011f\3\2\2\2\u0122\u0123\5*\26\2\u0123\u012b\b\25\1")
        buf.write("\2\u0124\u0125\t\5\2\2\u0125\u0126\b\25\1\2\u0126\u0127")
        buf.write("\5*\26\2\u0127\u0128\b\25\1\2\u0128\u012a\3\2\2\2\u0129")
        buf.write("\u0124\3\2\2\2\u012a\u012d\3\2\2\2\u012b\u0129\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c)\3\2\2\2\u012d\u012b\3\2\2")
        buf.write("\2\u012e\u012f\7\34\2\2\u012f\u0130\b\26\1\2\u0130\u0131")
        buf.write("\5$\23\2\u0131\u0132\7\35\2\2\u0132\u0133\b\26\1\2\u0133")
        buf.write("\u0139\3\2\2\2\u0134\u0136\t\4\2\2\u0135\u0134\3\2\2\2")
        buf.write("\u0135\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\5")
        buf.write(",\27\2\u0138\u012e\3\2\2\2\u0138\u0135\3\2\2\2\u0139+")
        buf.write("\3\2\2\2\u013a\u013b\5.\30\2\u013b\u013c\b\27\1\2\u013c")
        buf.write("\u0143\3\2\2\2\u013d\u0143\7\31\2\2\u013e\u0143\7\32\2")
        buf.write("\2\u013f\u0143\7\33\2\2\u0140\u0143\7\27\2\2\u0141\u0143")
        buf.write("\5@!\2\u0142\u013a\3\2\2\2\u0142\u013d\3\2\2\2\u0142\u013e")
        buf.write("\3\2\2\2\u0142\u013f\3\2\2\2\u0142\u0140\3\2\2\2\u0142")
        buf.write("\u0141\3\2\2\2\u0143-\3\2\2\2\u0144\u0145\7\30\2\2\u0145")
        buf.write("\u014d\b\30\1\2\u0146\u0147\5\60\31\2\u0147\u0148\b\30")
        buf.write("\1\2\u0148\u014d\3\2\2\2\u0149\u014a\5\62\32\2\u014a\u014b")
        buf.write("\b\30\1\2\u014b\u014d\3\2\2\2\u014c\u0144\3\2\2\2\u014c")
        buf.write("\u0146\3\2\2\2\u014c\u0149\3\2\2\2\u014d/\3\2\2\2\u014e")
        buf.write("\u014f\7\30\2\2\u014f\u0150\b\31\1\2\u0150\u0151\7 \2")
        buf.write("\2\u0151\u0152\5$\23\2\u0152\u0153\7!\2\2\u0153\61\3\2")
        buf.write("\2\2\u0154\u0155\7+\2\2\u0155\u0156\7\30\2\2\u0156\u0157")
        buf.write("\b\32\1\2\u0157\63\3\2\2\2\u0158\u0159\7\r\2\2\u0159\u015a")
        buf.write("\5$\23\2\u015a\u015b\b\33\1\2\u015b\u015e\5\36\20\2\u015c")
        buf.write("\u015d\b\33\1\2\u015d\u015f\5\66\34\2\u015e\u015c\3\2")
        buf.write("\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161")
        buf.write("\b\33\1\2\u0161\65\3\2\2\2\u0162\u0164\58\35\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0168\b\34\1")
        buf.write("\2\u0168\u0172\3\2\2\2\u0169\u0172\5:\36\2\u016a\u016c")
        buf.write("\58\35\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u0170\5:\36\2\u0170\u0172\3\2\2\2\u0171\u0163\3")
        buf.write("\2\2\2\u0171\u0169\3\2\2\2\u0171\u016b\3\2\2\2\u0172\67")
        buf.write("\3\2\2\2\u0173\u0174\7\n\2\2\u0174\u0175\7\r\2\2\u0175")
        buf.write("\u0176\b\35\1\2\u0176\u0177\5$\23\2\u0177\u0178\b\35\1")
        buf.write("\2\u0178\u0179\5\36\20\2\u01799\3\2\2\2\u017a\u017b\7")
        buf.write("\n\2\2\u017b\u017c\b\36\1\2\u017c\u017d\5\36\20\2\u017d")
        buf.write(";\3\2\2\2\u017e\u017f\7\25\2\2\u017f\u0180\b\37\1\2\u0180")
        buf.write("\u0181\5$\23\2\u0181\u0182\b\37\1\2\u0182\u0183\5\36\20")
        buf.write("\2\u0183\u0184\b\37\1\2\u0184=\3\2\2\2\u0185\u0187\7\f")
        buf.write("\2\2\u0186\u0188\5\34\17\2\u0187\u0186\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7\"\2\2\u018a")
        buf.write("\u018b\b \1\2\u018b\u018c\5$\23\2\u018c\u018d\b \1\2\u018d")
        buf.write("\u018e\7\"\2\2\u018e\u0190\b \1\2\u018f\u0191\5\34\17")
        buf.write("\2\u0190\u018f\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192\u0193\b \1\2\u0193\u0194\5\36\20\2\u0194")
        buf.write("\u0195\b \1\2\u0195\u0196\b \1\2\u0196?\3\2\2\2\u0197")
        buf.write("\u0198\5B\"\2\u0198\u0199\b!\1\2\u0199A\3\2\2\2\u019a")
        buf.write("\u019b\5.\30\2\u019b\u019c\7$\2\2\u019c\u019d\7\30\2\2")
        buf.write("\u019d\u019e\b\"\1\2\u019e\u01a0\7\34\2\2\u019f\u01a1")
        buf.write("\5D#\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2")
        buf.write("\3\2\2\2\u01a2\u01a3\7\35\2\2\u01a3\u01a4\b\"\1\2\u01a4")
        buf.write("\u01b8\3\2\2\2\u01a5\u01a6\7\30\2\2\u01a6\u01a7\b\"\1")
        buf.write("\2\u01a7\u01a9\7\34\2\2\u01a8\u01aa\5D#\2\u01a9\u01a8")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ac\7\35\2\2\u01ac\u01b8\b\"\1\2\u01ad\u01b8\5H%\2")
        buf.write("\u01ae\u01af\7\3\2\2\u01af\u01b0\7\30\2\2\u01b0\u01b1")
        buf.write("\b\"\1\2\u01b1\u01b3\7\34\2\2\u01b2\u01b4\5D#\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\7\35\2\2\u01b6\u01b8\b\"\1\2\u01b7\u019a")
        buf.write("\3\2\2\2\u01b7\u01a5\3\2\2\2\u01b7\u01ad\3\2\2\2\u01b7")
        buf.write("\u01ae\3\2\2\2\u01b8C\3\2\2\2\u01b9\u01ba\5$\23\2\u01ba")
        buf.write("\u01c1\b#\1\2\u01bb\u01bc\7#\2\2\u01bc\u01bd\5$\23\2\u01bd")
        buf.write("\u01be\b#\1\2\u01be\u01c0\3\2\2\2\u01bf\u01bb\3\2\2\2")
        buf.write("\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3")
        buf.write("\2\2\2\u01c2E\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5")
        buf.write("\7\26\2\2\u01c5\u01c6\7$\2\2\u01c6\u01c7\7\4\2\2\u01c7")
        buf.write("\u01c8\7\34\2\2\u01c8\u01c9\5$\23\2\u01c9\u01ca\7\35\2")
        buf.write("\2\u01ca\u01cb\7\"\2\2\u01cb\u01cc\b$\1\2\u01ccG\3\2\2")
        buf.write("\2\u01cd\u01ce\7\26\2\2\u01ce\u01d5\7$\2\2\u01cf\u01d0")
        buf.write("\7\5\2\2\u01d0\u01d6\b%\1\2\u01d1\u01d2\7\6\2\2\u01d2")
        buf.write("\u01d6\b%\1\2\u01d3\u01d4\7\7\2\2\u01d4\u01d6\b%\1\2\u01d5")
        buf.write("\u01cf\3\2\2\2\u01d5\u01d1\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d7\3\2\2\2\u01d7\u01d8\7\34\2\2\u01d8\u01d9")
        buf.write("\7\35\2\2\u01d9I\3\2\2\2(NTakq~\u0084\u008c\u0097\u009e")
        buf.write("\u00a9\u00af\u00bc\u00ce\u00dc\u00e2\u00f2\u0103\u0112")
        buf.write("\u0114\u011f\u012b\u0135\u0138\u0142\u014c\u015e\u0165")
        buf.write("\u016d\u0171\u0187\u0190\u01a0\u01a9\u01b3\u01b7\u01c1")
        buf.write("\u01d5")
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
    RULE_nonVoidMethod = 6
    RULE_voidMethod = 7
    RULE_constructor = 8
    RULE_nonVoidBlock = 9
    RULE_methodArguments = 10
    RULE_typeState = 11
    RULE_varsDecl = 12
    RULE_assignment = 13
    RULE_block = 14
    RULE_statement = 15
    RULE_returnState = 16
    RULE_expression = 17
    RULE_exp = 18
    RULE_term = 19
    RULE_factor = 20
    RULE_literal = 21
    RULE_reference = 22
    RULE_arrPos = 23
    RULE_instanceVar = 24
    RULE_condition = 25
    RULE_elseIfs = 26
    RULE_elseIf = 27
    RULE_finalElse = 28
    RULE_whileLoop = 29
    RULE_forLoop = 30
    RULE_expressionCall = 31
    RULE_call = 32
    RULE_callArguments = 33
    RULE_printState = 34
    RULE_read = 35

    ruleNames =  [ "fileState", "imp", "classState", "classBlock", "attribute", 
                   "method", "nonVoidMethod", "voidMethod", "constructor", 
                   "nonVoidBlock", "methodArguments", "typeState", "varsDecl", 
                   "assignment", "block", "statement", "returnState", "expression", 
                   "exp", "term", "factor", "literal", "reference", "arrPos", 
                   "instanceVar", "condition", "elseIfs", "elseIf", "finalElse", 
                   "whileLoop", "forLoop", "expressionCall", "call", "callArguments", 
                   "printState", "read" ]

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
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.IMPORT:
                self.state = 73
                self.imp()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 79
                self.classState()
                self.state = 82 
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
            self.state = 86
            self.match(IdleParser.IMPORT)
            self.state = 87
            localctx._ID = self.match(IdleParser.ID)
            self.state = 88
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
            self.state = 91
            self.match(IdleParser.TYPE)
            self.state = 92
            localctx.class_name = self.match(IdleParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ARROW:
                self.state = 93
                self.match(IdleParser.ARROW)
                self.state = 94
                localctx.parent_name = self.match(IdleParser.ID)


            self.state = 97
            self.match(IdleParser.CLASS)
            self.icomp.add_class((None if localctx.class_name is None else localctx.class_name.text), (0 if localctx.class_name is None else localctx.class_name.line), (None if localctx.parent_name is None else localctx.parent_name.text))
            self.state = 99
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
            self.state = 101
            self.match(IdleParser.LBRACE)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 102
                    self.attribute() 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ID:
                self.state = 108
                self.method()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 114
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
            self.state = 116
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 118
            self.typeState()
            self.state = 119
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

        def nonVoidMethod(self):
            return self.getTypedRuleContext(IdleParser.NonVoidMethodContext,0)


        def voidMethod(self):
            return self.getTypedRuleContext(IdleParser.VoidMethodContext,0)


        def constructor(self):
            return self.getTypedRuleContext(IdleParser.ConstructorContext,0)


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
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.nonVoidMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.voidMethod()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonVoidMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._typeState = None # TypeStateContext
            self._nonVoidBlock = None # NonVoidBlockContext

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def typeState(self):
            return self.getTypedRuleContext(IdleParser.TypeStateContext,0)


        def nonVoidBlock(self):
            return self.getTypedRuleContext(IdleParser.NonVoidBlockContext,0)


        def methodArguments(self):
            return self.getTypedRuleContext(IdleParser.MethodArgumentsContext,0)


        def varsDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.VarsDeclContext)
            else:
                return self.getTypedRuleContext(IdleParser.VarsDeclContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_nonVoidMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonVoidMethod" ):
                listener.enterNonVoidMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonVoidMethod" ):
                listener.exitNonVoidMethod(self)




    def nonVoidMethod(self):

        localctx = IdleParser.NonVoidMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nonVoidMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_func((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 128
            self.match(IdleParser.LPAREN)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID:
                self.state = 129
                self.methodArguments()


            self.state = 132
            self.match(IdleParser.RPAREN)
            self.state = 133
            localctx._typeState = self.typeState()
            self.icomp.add_func_return_type((None if localctx._typeState is None else self._input.getText((localctx._typeState.start,localctx._typeState.stop))))
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.VAR:
                self.state = 135
                self.varsDecl()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            localctx._nonVoidBlock = self.nonVoidBlock()
            self.icomp.quad_add_endproc((None if localctx._nonVoidBlock is None else localctx._nonVoidBlock.stop).line)
            self.icomp.end_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._block = None # BlockContext

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def VOID(self):
            return self.getToken(IdleParser.VOID, 0)

        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def methodArguments(self):
            return self.getTypedRuleContext(IdleParser.MethodArgumentsContext,0)


        def varsDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.VarsDeclContext)
            else:
                return self.getTypedRuleContext(IdleParser.VarsDeclContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_voidMethod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVoidMethod" ):
                listener.enterVoidMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVoidMethod" ):
                listener.exitVoidMethod(self)




    def voidMethod(self):

        localctx = IdleParser.VoidMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_voidMethod)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_func((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 147
            self.match(IdleParser.LPAREN)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID:
                self.state = 148
                self.methodArguments()


            self.state = 151
            self.match(IdleParser.RPAREN)
            self.state = 152
            self.match(IdleParser.VOID)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.VAR:
                self.state = 153
                self.varsDecl()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            localctx._block = self.block()
            self.icomp.quad_add_endproc((None if localctx._block is None else localctx._block.stop).line)
            self.icomp.end_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token
            self._block = None # BlockContext

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IdleParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IdleParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def methodArguments(self):
            return self.getTypedRuleContext(IdleParser.MethodArgumentsContext,0)


        def varsDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.VarsDeclContext)
            else:
                return self.getTypedRuleContext(IdleParser.VarsDeclContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_constructor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstructor" ):
                listener.enterConstructor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstructor" ):
                listener.exitConstructor(self)




    def constructor(self):

        localctx = IdleParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_constructor((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 165
            self.match(IdleParser.LPAREN)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID:
                self.state = 166
                self.methodArguments()


            self.state = 169
            self.match(IdleParser.RPAREN)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.VAR:
                self.state = 170
                self.varsDecl()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 176
            localctx._block = self.block()
            self.icomp.quad_add_endproc((None if localctx._block is None else localctx._block.stop).line)
            self.icomp.end_scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonVoidBlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(IdleParser.LBRACE, 0)

        def returnState(self):
            return self.getTypedRuleContext(IdleParser.ReturnStateContext,0)


        def RBRACE(self):
            return self.getToken(IdleParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.StatementContext)
            else:
                return self.getTypedRuleContext(IdleParser.StatementContext,i)


        def getRuleIndex(self):
            return IdleParser.RULE_nonVoidBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonVoidBlock" ):
                listener.enterNonVoidBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonVoidBlock" ):
                listener.exitNonVoidBlock(self)




    def nonVoidBlock(self):

        localctx = IdleParser.NonVoidBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nonVoidBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(IdleParser.LBRACE)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 181
                    self.statement()
                    self.icomp.reset_new_line() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 189
            self.returnState()
            self.state = 190
            self.match(IdleParser.RBRACE)
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
        self.enterRule(localctx, 20, self.RULE_methodArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 194
            self.typeState()
            self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 196
                self.match(IdleParser.COMMA)
                self.state = 197
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 199
                self.typeState()
                self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
                self.state = 206
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
        self.enterRule(localctx, 22, self.RULE_typeState)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
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
        self.enterRule(localctx, 24, self.RULE_varsDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(IdleParser.VAR)
            self.state = 211
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 213
                self.match(IdleParser.COMMA)
                self.state = 214
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.LBRACK:
                self.state = 221
                self.match(IdleParser.LBRACK)
                self.state = 222
                self.match(IdleParser.INT_LITERAL)
                self.state = 223
                self.match(IdleParser.RBRACK)


            self.state = 226
            self.typeState()
            self.state = 227
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
        self.enterRule(localctx, 26, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            localctx._reference = self.reference()
            self.state = 230
            self.match(IdleParser.ASSIGN)
            self.state = 231
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
        self.enterRule(localctx, 28, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(IdleParser.LBRACE)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.FOR) | (1 << IdleParser.IF) | (1 << IdleParser.RETURN) | (1 << IdleParser.WHILE) | (1 << IdleParser.IO) | (1 << IdleParser.ID) | (1 << IdleParser.DSYMBOL))) != 0):
                self.state = 235
                self.statement()
                self.icomp.reset_new_line()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 243
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
            self._call = None # CallContext

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
        self.enterRule(localctx, 30, self.RULE_statement)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.assignment()
                self.state = 246
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                localctx._call = self.call()
                self.state = 250
                self.match(IdleParser.SEMICOLON)
                self.icomp.check_not_void((None if localctx._call is None else localctx._call.stop).line, check=False)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 255
                self.printState()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 256
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
        self.enterRule(localctx, 32, self.RULE_returnState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(IdleParser.RETURN)
            self.state = 260
            localctx._expression = self.expression()
            self.state = 261
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
        self.enterRule(localctx, 34, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(IdleParser.BANG)
                self.state = 265
                self.exp()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.LPAREN, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                localctx._exp = self.exp()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0):
                    self.state = 267
                    localctx.operator = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0)):
                        localctx.operator = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                    self.state = 269
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
        self.enterRule(localctx, 36, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            localctx._term = self.term()
            self.icomp.quad_check_addsub((None if localctx._term is None else localctx._term.start).line)
            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ADD or _la==IdleParser.SUB:
                self.state = 278
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                self.state = 280
                localctx._term = self.term()
                self.icomp.quad_check_addsub((None if localctx._term is None else localctx._term.start).line)
                self.state = 287
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
        self.enterRule(localctx, 38, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            localctx._factor = self.factor()
            self.icomp.quad_check_divmult((None if localctx._factor is None else localctx._factor.start).line)
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.DIV or _la==IdleParser.MUL:
                self.state = 290
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IdleParser.DIV or _la==IdleParser.MUL):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                self.state = 292
                localctx._factor = self.factor()
                self.icomp.quad_check_divmult((None if localctx._factor is None else localctx._factor.start).line)
                self.state = 299
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
        self.enterRule(localctx, 40, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(IdleParser.LPAREN)
                self.icomp.quad_open_parenthesis()
                self.state = 302
                self.expression()
                self.state = 303
                self.match(IdleParser.RPAREN)
                self.icomp.quad_close_parenthesis()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ADD or _la==IdleParser.SUB:
                    self.state = 306
                    _la = self._input.LA(1)
                    if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 309
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

        def expressionCall(self):
            return self.getTypedRuleContext(IdleParser.ExpressionCallContext,0)


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
        self.enterRule(localctx, 42, self.RULE_literal)
        try:
            self.state = 320
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                localctx._reference = self.reference()
                self.icomp.quad_add_var((None if localctx._reference is None else self._input.getText((localctx._reference.start,localctx._reference.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.match(IdleParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.match(IdleParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 317
                self.match(IdleParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 318
                self.match(IdleParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 319
                self.expressionCall()
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
        self.enterRule(localctx, 44, self.RULE_reference)
        try:
            self.state = 330
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                localctx._arrPos = self.arrPos()
                localctx.attr_ref = localctx._arrPos.attr_ref
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
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
        self.enterRule(localctx, 46, self.RULE_arrPos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            localctx._ID = self.match(IdleParser.ID)
            localctx.attr_ref = self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 334
            self.match(IdleParser.LBRACK)
            self.state = 335
            self.expression()
            self.state = 336
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
        self.enterRule(localctx, 48, self.RULE_instanceVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(IdleParser.DSYMBOL)
            self.state = 339
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
        self.enterRule(localctx, 50, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(IdleParser.IF)
            self.state = 343
            localctx._expression = self.expression()
            self.icomp.quad_end_if_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 345
            self.block()
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ELSE:
                self.icomp.quad_start_else_ifs()
                self.state = 347
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
        self.enterRule(localctx, 52, self.RULE_elseIfs)
        self._la = 0 # Token type
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 352
                    self.elseIf()
                    self.state = 355 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==IdleParser.ELSE):
                        break

                self.icomp.quad_fill_if_end_jumps()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 359
                self.finalElse()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 361 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 360
                        self.elseIf()

                    else:
                        raise NoViableAltException(self)
                    self.state = 363 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                self.state = 365
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
        self.enterRule(localctx, 54, self.RULE_elseIf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(IdleParser.ELSE)
            self.state = 370
            self.match(IdleParser.IF)
            self.icomp.quad_add_else()
            self.state = 372
            localctx._expression = self.expression()
            self.icomp.quad_end_if_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 374
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
        self.enterRule(localctx, 56, self.RULE_finalElse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(IdleParser.ELSE)
            self.icomp.quad_add_else()
            self.state = 378
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
        self.enterRule(localctx, 58, self.RULE_whileLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(IdleParser.WHILE)
            self.icomp.quad_start_while()
            self.state = 382
            localctx._expression = self.expression()
            self.icomp.quad_end_while_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 384
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
        self.enterRule(localctx, 60, self.RULE_forLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(IdleParser.FOR)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 388
                self.assignment()


            self.state = 391
            self.match(IdleParser.SEMICOLON)
            self.icomp.quad_start_while()
            self.state = 393
            localctx._expression = self.expression()
            self.icomp.quad_end_while_expr((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 395
            self.match(IdleParser.SEMICOLON)
            self.icomp.quad_start_for_assign()
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 397
                self.assignment()


            self.icomp.quad_end_for_assign()
            self.state = 401
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


    class ExpressionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._call = None # CallContext

        def call(self):
            return self.getTypedRuleContext(IdleParser.CallContext,0)


        def getRuleIndex(self):
            return IdleParser.RULE_expressionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionCall" ):
                listener.enterExpressionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionCall" ):
                listener.exitExpressionCall(self)




    def expressionCall(self):

        localctx = IdleParser.ExpressionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expressionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            localctx._call = self.call()
            self.icomp.check_not_void((None if localctx._call is None else localctx._call.stop).line, check=True)
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
        self.enterRule(localctx, 64, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                localctx._reference = self.reference()
                self.state = 409
                self.match(IdleParser.DOT)
                self.state = 410
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_obj_func_exists(localctx._reference.attr_ref, (None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 412
                self.match(IdleParser.LPAREN)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 413
                    self.callArguments()


                self.state = 416
                self.match(IdleParser.RPAREN)
                self.icomp.quad_add_func_gosub((0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_func_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 421
                self.match(IdleParser.LPAREN)
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 422
                    self.callArguments()


                self.state = 425
                self.match(IdleParser.RPAREN)
                self.icomp.quad_add_func_gosub((0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
                self.read()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 428
                self.match(IdleParser.T__0)
                self.state = 429
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_class_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 431
                self.match(IdleParser.LPAREN)
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 432
                    self.callArguments()


                self.state = 435
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
        self.enterRule(localctx, 66, self.RULE_callArguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            localctx._expression = self.expression()
            self.icomp.quad_add_func_param((None if localctx._expression is None else localctx._expression.start).line)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 441
                self.match(IdleParser.COMMA)
                self.state = 442
                localctx._expression = self.expression()
                self.icomp.quad_add_func_param((None if localctx._expression is None else localctx._expression.start).line)
                self.state = 449
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
        self.enterRule(localctx, 68, self.RULE_printState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(IdleParser.IO)
            self.state = 451
            self.match(IdleParser.DOT)
            self.state = 452
            self.match(IdleParser.T__1)
            self.state = 453
            self.match(IdleParser.LPAREN)
            self.state = 454
            self.expression()
            self.state = 455
            self.match(IdleParser.RPAREN)
            self.state = 456
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
        self.enterRule(localctx, 70, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.match(IdleParser.IO)
            self.state = 460
            self.match(IdleParser.DOT)
            self.state = 467
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.T__2]:
                self.state = 461
                self.match(IdleParser.T__2)
                self.icomp.quad_read('string')
                pass
            elif token in [IdleParser.T__3]:
                self.state = 463
                self.match(IdleParser.T__3)
                self.icomp.quad_read('int')
                pass
            elif token in [IdleParser.T__4]:
                self.state = 465
                self.match(IdleParser.T__4)
                self.icomp.quad_read('float')
                pass
            else:
                raise NoViableAltException(self)

            self.state = 469
            self.match(IdleParser.LPAREN)
            self.state = 470
            self.match(IdleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





