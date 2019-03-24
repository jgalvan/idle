# Generated from grammar/Idle.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from IdleCompiler import IdleCompiler

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\67")
        buf.write("\u016a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2\3\2\6\2E\n\2\r\2\16\2")
        buf.write("F\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4R\n\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\7\5Z\n\5\f\5\16\5]\13\5\3\5\7\5`\n\5")
        buf.write("\f\5\16\5c\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\5\7p\n\7\3\7\3\7\3\7\3\7\3\7\5\7w\n\7\3\7\7\7z")
        buf.write("\n\7\f\7\16\7}\13\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0086")
        buf.write("\n\7\3\7\3\7\7\7\u008a\n\7\f\7\16\7\u008d\13\7\3\7\3\7")
        buf.write("\3\7\5\7\u0092\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\7\b\u009e\n\b\f\b\16\b\u00a1\13\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\7\n\u00ac\n\n\f\n\16\n\u00af\13\n")
        buf.write("\3\n\3\n\3\n\5\n\u00b4\n\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\7\f\u00bf\n\f\f\f\16\f\u00c2\13\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00d1")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00dc\n\17\5\17\u00de\n\17\3\20\3\20\3\20\7\20\u00e3")
        buf.write("\n\20\f\20\16\20\u00e6\13\20\3\21\3\21\3\21\7\21\u00eb")
        buf.write("\n\21\f\21\16\21\u00ee\13\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u00f5\n\22\3\22\5\22\u00f8\n\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\5\23\u0100\n\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\5\24\u010a\n\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27")
        buf.write("\u011a\n\27\f\27\16\27\u011d\13\27\3\27\3\27\5\27\u0121")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\5\32\u012e\n\32\3\32\3\32\3\32\3\32\5\32\u0134\n")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u013e")
        buf.write("\n\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0146\n\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u014f\n\33\3\33")
        buf.write("\5\33\u0152\n\33\3\34\3\34\3\34\7\34\u0157\n\34\f\34\16")
        buf.write("\34\u015a\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\2\2\37\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:\2\7")
        buf.write("\7\2\b\b\13\13\17\17\21\21\30\30\5\2&&,\60\62\63\4\2%")
        buf.write("%\64\64\4\2**\61\61\3\2\5\7\2\u0179\2<\3\2\2\2\4H\3\2")
        buf.write("\2\2\6M\3\2\2\2\bW\3\2\2\2\nf\3\2\2\2\f\u0091\3\2\2\2")
        buf.write("\16\u0093\3\2\2\2\20\u00a2\3\2\2\2\22\u00a5\3\2\2\2\24")
        buf.write("\u00b8\3\2\2\2\26\u00bc\3\2\2\2\30\u00d0\3\2\2\2\32\u00d2")
        buf.write("\3\2\2\2\34\u00dd\3\2\2\2\36\u00df\3\2\2\2 \u00e7\3\2")
        buf.write("\2\2\"\u00f7\3\2\2\2$\u00ff\3\2\2\2&\u0109\3\2\2\2(\u010b")
        buf.write("\3\2\2\2*\u0111\3\2\2\2,\u0115\3\2\2\2.\u0122\3\2\2\2")
        buf.write("\60\u0127\3\2\2\2\62\u012b\3\2\2\2\64\u0151\3\2\2\2\66")
        buf.write("\u0153\3\2\2\28\u015b\3\2\2\2:\u0163\3\2\2\2<@\b\2\1\2")
        buf.write("=?\5\4\3\2>=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2AD\3")
        buf.write("\2\2\2B@\3\2\2\2CE\5\6\4\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2")
        buf.write("\2FG\3\2\2\2G\3\3\2\2\2HI\7\16\2\2IJ\7\30\2\2JK\7\"\2")
        buf.write("\2KL\b\3\1\2L\5\3\2\2\2MN\7\22\2\2NQ\7\30\2\2OP\7\'\2")
        buf.write("\2PR\7\30\2\2QO\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\7\t\2\2")
        buf.write("TU\b\4\1\2UV\5\b\5\2V\7\3\2\2\2W[\7\36\2\2XZ\5\n\6\2Y")
        buf.write("X\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\a\3\2\2\2][")
        buf.write("\3\2\2\2^`\5\f\7\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2")
        buf.write("\2\2bd\3\2\2\2ca\3\2\2\2de\7\37\2\2e\t\3\2\2\2fg\7\30")
        buf.write("\2\2gh\b\6\1\2hi\5\20\t\2ij\7\"\2\2j\13\3\2\2\2kl\7\30")
        buf.write("\2\2lm\b\7\1\2mo\7\34\2\2np\5\16\b\2on\3\2\2\2op\3\2\2")
        buf.write("\2pq\3\2\2\2qv\7\35\2\2rs\5\20\t\2st\b\7\1\2tw\3\2\2\2")
        buf.write("uw\7\24\2\2vr\3\2\2\2vu\3\2\2\2w{\3\2\2\2xz\5\22\n\2y")
        buf.write("x\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3")
        buf.write("\2\2\2~\177\5\26\f\2\177\u0080\b\7\1\2\u0080\u0092\3\2")
        buf.write("\2\2\u0081\u0082\7\30\2\2\u0082\u0083\b\7\1\2\u0083\u0085")
        buf.write("\7\34\2\2\u0084\u0086\5\16\b\2\u0085\u0084\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u008b\7\35\2")
        buf.write("\2\u0088\u008a\5\22\n\2\u0089\u0088\3\2\2\2\u008a\u008d")
        buf.write("\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\5\26\f")
        buf.write("\2\u008f\u0090\b\7\1\2\u0090\u0092\3\2\2\2\u0091k\3\2")
        buf.write("\2\2\u0091\u0081\3\2\2\2\u0092\r\3\2\2\2\u0093\u0094\7")
        buf.write("\30\2\2\u0094\u0095\b\b\1\2\u0095\u0096\5\20\t\2\u0096")
        buf.write("\u009f\b\b\1\2\u0097\u0098\7#\2\2\u0098\u0099\7\30\2\2")
        buf.write("\u0099\u009a\b\b\1\2\u009a\u009b\5\20\t\2\u009b\u009c")
        buf.write("\b\b\1\2\u009c\u009e\3\2\2\2\u009d\u0097\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\17\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\t\2")
        buf.write("\2\2\u00a3\u00a4\b\t\1\2\u00a4\21\3\2\2\2\u00a5\u00a6")
        buf.write("\7\23\2\2\u00a6\u00a7\7\30\2\2\u00a7\u00ad\b\n\1\2\u00a8")
        buf.write("\u00a9\7#\2\2\u00a9\u00aa\7\30\2\2\u00aa\u00ac\b\n\1\2")
        buf.write("\u00ab\u00a8\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3")
        buf.write("\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00b3\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00b0\u00b1\7 \2\2\u00b1\u00b2\7\31\2\2\u00b2")
        buf.write("\u00b4\7!\2\2\u00b3\u00b0\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00b6\5\20\t\2\u00b6\u00b7")
        buf.write("\7\"\2\2\u00b7\23\3\2\2\2\u00b8\u00b9\5&\24\2\u00b9\u00ba")
        buf.write("\7(\2\2\u00ba\u00bb\5\34\17\2\u00bb\25\3\2\2\2\u00bc\u00c0")
        buf.write("\7\36\2\2\u00bd\u00bf\5\30\r\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7")
        buf.write("\37\2\2\u00c4\27\3\2\2\2\u00c5\u00c6\5\24\13\2\u00c6\u00c7")
        buf.write("\7\"\2\2\u00c7\u00d1\3\2\2\2\u00c8\u00d1\5,\27\2\u00c9")
        buf.write("\u00ca\5\64\33\2\u00ca\u00cb\7\"\2\2\u00cb\u00d1\3\2\2")
        buf.write("\2\u00cc\u00d1\5\62\32\2\u00cd\u00d1\5\60\31\2\u00ce\u00d1")
        buf.write("\58\35\2\u00cf\u00d1\5\32\16\2\u00d0\u00c5\3\2\2\2\u00d0")
        buf.write("\u00c8\3\2\2\2\u00d0\u00c9\3\2\2\2\u00d0\u00cc\3\2\2\2")
        buf.write("\u00d0\u00cd\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3")
        buf.write("\2\2\2\u00d1\31\3\2\2\2\u00d2\u00d3\7\20\2\2\u00d3\u00d4")
        buf.write("\5\34\17\2\u00d4\u00d5\7\"\2\2\u00d5\33\3\2\2\2\u00d6")
        buf.write("\u00d7\7)\2\2\u00d7\u00de\5\36\20\2\u00d8\u00db\5\36\20")
        buf.write("\2\u00d9\u00da\t\3\2\2\u00da\u00dc\5\36\20\2\u00db\u00d9")
        buf.write("\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00de\3\2\2\2\u00dd")
        buf.write("\u00d6\3\2\2\2\u00dd\u00d8\3\2\2\2\u00de\35\3\2\2\2\u00df")
        buf.write("\u00e4\5 \21\2\u00e0\u00e1\t\4\2\2\u00e1\u00e3\5 \21\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\37\3\2\2\2\u00e6\u00e4")
        buf.write("\3\2\2\2\u00e7\u00ec\5\"\22\2\u00e8\u00e9\t\5\2\2\u00e9")
        buf.write("\u00eb\5\"\22\2\u00ea\u00e8\3\2\2\2\u00eb\u00ee\3\2\2")
        buf.write("\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed!\3\2")
        buf.write("\2\2\u00ee\u00ec\3\2\2\2\u00ef\u00f0\7\34\2\2\u00f0\u00f1")
        buf.write("\5\34\17\2\u00f1\u00f2\7\35\2\2\u00f2\u00f8\3\2\2\2\u00f3")
        buf.write("\u00f5\t\4\2\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f8\5$\23\2\u00f7\u00ef\3")
        buf.write("\2\2\2\u00f7\u00f4\3\2\2\2\u00f8#\3\2\2\2\u00f9\u0100")
        buf.write("\5&\24\2\u00fa\u0100\7\31\2\2\u00fb\u0100\7\32\2\2\u00fc")
        buf.write("\u0100\7\33\2\2\u00fd\u0100\7\27\2\2\u00fe\u0100\5\64")
        buf.write("\33\2\u00ff\u00f9\3\2\2\2\u00ff\u00fa\3\2\2\2\u00ff\u00fb")
        buf.write("\3\2\2\2\u00ff\u00fc\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff")
        buf.write("\u00fe\3\2\2\2\u0100%\3\2\2\2\u0101\u0102\7\30\2\2\u0102")
        buf.write("\u010a\b\24\1\2\u0103\u0104\5(\25\2\u0104\u0105\b\24\1")
        buf.write("\2\u0105\u010a\3\2\2\2\u0106\u0107\5*\26\2\u0107\u0108")
        buf.write("\b\24\1\2\u0108\u010a\3\2\2\2\u0109\u0101\3\2\2\2\u0109")
        buf.write("\u0103\3\2\2\2\u0109\u0106\3\2\2\2\u010a\'\3\2\2\2\u010b")
        buf.write("\u010c\7\30\2\2\u010c\u010d\b\25\1\2\u010d\u010e\7 \2")
        buf.write("\2\u010e\u010f\5\34\17\2\u010f\u0110\7!\2\2\u0110)\3\2")
        buf.write("\2\2\u0111\u0112\7+\2\2\u0112\u0113\7\30\2\2\u0113\u0114")
        buf.write("\b\26\1\2\u0114+\3\2\2\2\u0115\u0116\7\r\2\2\u0116\u0117")
        buf.write("\5\34\17\2\u0117\u011b\5\26\f\2\u0118\u011a\5.\30\2\u0119")
        buf.write("\u0118\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119\3\2\2\2")
        buf.write("\u011b\u011c\3\2\2\2\u011c\u0120\3\2\2\2\u011d\u011b\3")
        buf.write("\2\2\2\u011e\u011f\7\n\2\2\u011f\u0121\5\26\f\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121-\3\2\2\2\u0122")
        buf.write("\u0123\7\n\2\2\u0123\u0124\7\r\2\2\u0124\u0125\5\34\17")
        buf.write("\2\u0125\u0126\5\26\f\2\u0126/\3\2\2\2\u0127\u0128\7\25")
        buf.write("\2\2\u0128\u0129\5\34\17\2\u0129\u012a\5\26\f\2\u012a")
        buf.write("\61\3\2\2\2\u012b\u012d\7\f\2\2\u012c\u012e\5\24\13\2")
        buf.write("\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\3")
        buf.write("\2\2\2\u012f\u0130\7\"\2\2\u0130\u0131\5\34\17\2\u0131")
        buf.write("\u0133\7\"\2\2\u0132\u0134\5\24\13\2\u0133\u0132\3\2\2")
        buf.write("\2\u0133\u0134\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136")
        buf.write("\5\26\f\2\u0136\63\3\2\2\2\u0137\u0138\5&\24\2\u0138\u0139")
        buf.write("\7$\2\2\u0139\u013a\7\30\2\2\u013a\u013b\b\33\1\2\u013b")
        buf.write("\u013d\7\34\2\2\u013c\u013e\5\66\34\2\u013d\u013c\3\2")
        buf.write("\2\2\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140")
        buf.write("\7\35\2\2\u0140\u0152\3\2\2\2\u0141\u0142\7\30\2\2\u0142")
        buf.write("\u0143\b\33\1\2\u0143\u0145\7\34\2\2\u0144\u0146\5\66")
        buf.write("\34\2\u0145\u0144\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0152\7\35\2\2\u0148\u0152\5:\36\2\u0149")
        buf.write("\u014a\7\3\2\2\u014a\u014b\7\30\2\2\u014b\u014c\b\33\1")
        buf.write("\2\u014c\u014e\7\34\2\2\u014d\u014f\5\66\34\2\u014e\u014d")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0152\7\35\2\2\u0151\u0137\3\2\2\2\u0151\u0141\3\2\2")
        buf.write("\2\u0151\u0148\3\2\2\2\u0151\u0149\3\2\2\2\u0152\65\3")
        buf.write("\2\2\2\u0153\u0158\5\34\17\2\u0154\u0155\7#\2\2\u0155")
        buf.write("\u0157\5\34\17\2\u0156\u0154\3\2\2\2\u0157\u015a\3\2\2")
        buf.write("\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\67\3")
        buf.write("\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\7\26\2\2\u015c")
        buf.write("\u015d\7$\2\2\u015d\u015e\7\4\2\2\u015e\u015f\7\34\2\2")
        buf.write("\u015f\u0160\5\34\17\2\u0160\u0161\7\35\2\2\u0161\u0162")
        buf.write("\7\"\2\2\u01629\3\2\2\2\u0163\u0164\7\26\2\2\u0164\u0165")
        buf.write("\7$\2\2\u0165\u0166\t\6\2\2\u0166\u0167\7\34\2\2\u0167")
        buf.write("\u0168\7\35\2\2\u0168;\3\2\2\2#@FQ[aov{\u0085\u008b\u0091")
        buf.write("\u009f\u00ad\u00b3\u00c0\u00d0\u00db\u00dd\u00e4\u00ec")
        buf.write("\u00f4\u00f7\u00ff\u0109\u011b\u0120\u012d\u0133\u013d")
        buf.write("\u0145\u014e\u0151\u0158")
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
        self.checkVersion("4.7.1")
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

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

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

        def classBlock(self):
            return self.getTypedRuleContext(IdleParser.ClassBlockContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.ID)
            else:
                return self.getToken(IdleParser.ID, i)

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
            self.icomp.add_class((None if localctx.class_name is None else localctx.class_name.text), (0 if localctx.class_name is None else localctx.class_name.line), (None if localctx.parent_name is None else localctx.parent_name.text))
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
            self._typeState = None # TypeStateContext

        def ID(self):
            return self.getToken(IdleParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(IdleParser.BlockContext,0)


        def typeState(self):
            return self.getTypedRuleContext(IdleParser.TypeStateContext,0)


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
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
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
                self.state = 116
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IdleParser.BOOL, IdleParser.FLOAT, IdleParser.INT, IdleParser.STRING, IdleParser.ID]:
                    self.state = 112
                    localctx._typeState = self.typeState()
                    self.icomp.add_func_return_type((None if localctx._typeState is None else self._input.getText((localctx._typeState.start,localctx._typeState.stop))))
                    pass
                elif token in [IdleParser.VOID]:
                    self.state = 115
                    self.match(IdleParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IdleParser.VAR:
                    self.state = 118
                    self.varsDecl()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 124
                self.block()
                self.icomp.end_scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_constructor((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 129
                self.match(IdleParser.LPAREN)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ID:
                    self.state = 130
                    self.methodArguments()


                self.state = 133
                self.match(IdleParser.RPAREN)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IdleParser.VAR:
                    self.state = 134
                    self.varsDecl()
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 140
                self.block()
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
            self.state = 145
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 147
            self.typeState()
            self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 149
                self.match(IdleParser.COMMA)
                self.state = 150
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 152
                self.typeState()
                self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
                self.state = 159
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
            self.state = 160
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(IdleParser.ID)
            else:
                return self.getToken(IdleParser.ID, i)

        def typeState(self):
            return self.getTypedRuleContext(IdleParser.TypeStateContext,0)


        def INT_LITERAL(self):
            return self.getToken(IdleParser.INT_LITERAL, 0)

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
            self.state = 163
            self.match(IdleParser.VAR)
            self.state = 164
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 166
                self.match(IdleParser.COMMA)
                self.state = 167
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.LBRACK:
                self.state = 174
                self.match(IdleParser.LBRACK)
                self.state = 175
                self.match(IdleParser.INT_LITERAL)
                self.state = 176
                self.match(IdleParser.RBRACK)


            self.state = 179
            self.typeState()
            self.state = 180
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
            self.state = 182
            self.reference()
            self.state = 183
            self.match(IdleParser.ASSIGN)
            self.state = 184
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
            self.state = 186
            self.match(IdleParser.LBRACE)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.FOR) | (1 << IdleParser.IF) | (1 << IdleParser.RETURN) | (1 << IdleParser.WHILE) | (1 << IdleParser.IO) | (1 << IdleParser.ID) | (1 << IdleParser.DSYMBOL))) != 0):
                self.state = 187
                self.statement()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 193
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
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.assignment()
                self.state = 196
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.call()
                self.state = 200
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 202
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 203
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 204
                self.printState()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 205
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

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


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
            self.state = 208
            self.match(IdleParser.RETURN)
            self.state = 209
            self.expression()
            self.state = 210
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ExpContext)
            else:
                return self.getTypedRuleContext(IdleParser.ExpContext,i)


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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.match(IdleParser.BANG)
                self.state = 213
                self.exp()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.LPAREN, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.exp()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0):
                    self.state = 215
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 216
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
            self.state = 221
            self.term()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ADD or _la==IdleParser.SUB:
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.term()
                self.state = 228
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
            self.state = 229
            self.factor()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.DIV or _la==IdleParser.MUL:
                self.state = 230
                _la = self._input.LA(1)
                if not(_la==IdleParser.DIV or _la==IdleParser.MUL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 231
                self.factor()
                self.state = 236
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

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


        def literal(self):
            return self.getTypedRuleContext(IdleParser.LiteralContext,0)


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
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(IdleParser.LPAREN)
                self.state = 238
                self.expression()
                self.state = 239
                self.match(IdleParser.RPAREN)
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ADD or _la==IdleParser.SUB:
                    self.state = 241
                    _la = self._input.LA(1)
                    if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 244
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
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.reference()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(IdleParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(IdleParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.match(IdleParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 251
                self.match(IdleParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 252
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
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                localctx._arrPos = self.arrPos()
                localctx.attr_ref = localctx._arrPos.attr_ref
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 260
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

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


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
            self.state = 265
            localctx._ID = self.match(IdleParser.ID)
            localctx.attr_ref = self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 267
            self.match(IdleParser.LBRACK)
            self.state = 268
            self.expression()
            self.state = 269
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
            self.state = 271
            self.match(IdleParser.DSYMBOL)
            self.state = 272
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
            self.state = 275
            self.match(IdleParser.IF)
            self.state = 276
            self.expression()
            self.state = 277
            self.block()
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 278
                    self.elseIf() 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ELSE:
                self.state = 284
                self.match(IdleParser.ELSE)
                self.state = 285
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
            self.state = 288
            self.match(IdleParser.ELSE)
            self.state = 289
            self.match(IdleParser.IF)
            self.state = 290
            self.expression()
            self.state = 291
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
            self.state = 293
            self.match(IdleParser.WHILE)
            self.state = 294
            self.expression()
            self.state = 295
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
            self.state = 297
            self.match(IdleParser.FOR)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 298
                self.assignment()


            self.state = 301
            self.match(IdleParser.SEMICOLON)
            self.state = 302
            self.expression()
            self.state = 303
            self.match(IdleParser.SEMICOLON)
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 304
                self.assignment()


            self.state = 307
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
            self._reference = None # ReferenceContext
            self._ID = None # Token

        def reference(self):
            return self.getTypedRuleContext(IdleParser.ReferenceContext,0)


        def ID(self):
            return self.getToken(IdleParser.ID, 0)

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
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                localctx._reference = self.reference()
                self.state = 310
                self.match(IdleParser.DOT)
                self.state = 311
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_obj_func_exists(localctx._reference.attr_ref, (None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 313
                self.match(IdleParser.LPAREN)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 314
                    self.callArguments()


                self.state = 317
                self.match(IdleParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 319
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_func_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 321
                self.match(IdleParser.LPAREN)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 322
                    self.callArguments()


                self.state = 325
                self.match(IdleParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
                self.read()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 327
                self.match(IdleParser.T__0)
                self.state = 328
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_class_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 330
                self.match(IdleParser.LPAREN)
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 331
                    self.callArguments()


                self.state = 334
                self.match(IdleParser.RPAREN)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IdleParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(IdleParser.ExpressionContext,i)


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
            self.state = 337
            self.expression()
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 338
                self.match(IdleParser.COMMA)
                self.state = 339
                self.expression()
                self.state = 344
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

        def expression(self):
            return self.getTypedRuleContext(IdleParser.ExpressionContext,0)


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
            self.state = 345
            self.match(IdleParser.IO)
            self.state = 346
            self.match(IdleParser.DOT)
            self.state = 347
            self.match(IdleParser.T__1)
            self.state = 348
            self.match(IdleParser.LPAREN)
            self.state = 349
            self.expression()
            self.state = 350
            self.match(IdleParser.RPAREN)
            self.state = 351
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
            self.state = 353
            self.match(IdleParser.IO)
            self.state = 354
            self.match(IdleParser.DOT)
            self.state = 355
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__2) | (1 << IdleParser.T__3) | (1 << IdleParser.T__4))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 356
            self.match(IdleParser.LPAREN)
            self.state = 357
            self.match(IdleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





