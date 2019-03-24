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
        buf.write("\u0185\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\3\2\7\2?\n\2\f\2\16\2B\13\2\3\2\6\2E\n\2\r\2\16\2")
        buf.write("F\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4T\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\7\5\\\n\5\f\5\16\5_\13\5\3\5")
        buf.write("\7\5b\n\5\f\5\16\5e\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\5\7r\n\7\3\7\3\7\3\7\3\7\3\7\5\7y\n\7\3")
        buf.write("\7\7\7|\n\7\f\7\16\7\177\13\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u0088\n\7\3\7\3\7\7\7\u008c\n\7\f\7\16\7\u008f")
        buf.write("\13\7\3\7\3\7\3\7\5\7\u0094\n\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\7\b\u00a0\n\b\f\b\16\b\u00a3\13\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00ae\n\n\f\n\16")
        buf.write("\n\u00b1\13\n\3\n\3\n\3\n\5\n\u00b6\n\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u00c4\n\f")
        buf.write("\f\f\16\f\u00c7\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\r\u00d6\n\r\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00e4\n\17")
        buf.write("\5\17\u00e6\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u00ef\n\20\f\20\16\20\u00f2\13\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\7\21\u00fb\n\21\f\21\16\21\u00fe\13")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u0107\n\22")
        buf.write("\3\22\5\22\u010a\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u0114\n\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u011e\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u012e")
        buf.write("\n\27\f\27\16\27\u0131\13\27\3\27\3\27\5\27\u0135\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u0142\n\32\3\32\3\32\3\32\3\32\5\32\u0148\n\32\3")
        buf.write("\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0152\n\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u015a\n\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\5\33\u0163\n\33\3\33\5\33")
        buf.write("\u0166\n\33\3\34\3\34\3\34\7\34\u016b\n\34\f\34\16\34")
        buf.write("\u016e\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0180\n\36")
        buf.write("\3\36\3\36\3\36\3\36\2\2\37\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:\2\6\7\2\b\b\13\13")
        buf.write("\17\17\21\21\30\30\5\2&&,\60\62\63\4\2%%\64\64\4\2**\61")
        buf.write("\61\2\u0196\2<\3\2\2\2\4J\3\2\2\2\6O\3\2\2\2\bY\3\2\2")
        buf.write("\2\nh\3\2\2\2\f\u0093\3\2\2\2\16\u0095\3\2\2\2\20\u00a4")
        buf.write("\3\2\2\2\22\u00a7\3\2\2\2\24\u00ba\3\2\2\2\26\u00bf\3")
        buf.write("\2\2\2\30\u00d5\3\2\2\2\32\u00d7\3\2\2\2\34\u00e5\3\2")
        buf.write("\2\2\36\u00e7\3\2\2\2 \u00f3\3\2\2\2\"\u0109\3\2\2\2$")
        buf.write("\u0113\3\2\2\2&\u011d\3\2\2\2(\u011f\3\2\2\2*\u0125\3")
        buf.write("\2\2\2,\u0129\3\2\2\2.\u0136\3\2\2\2\60\u013b\3\2\2\2")
        buf.write("\62\u013f\3\2\2\2\64\u0165\3\2\2\2\66\u0167\3\2\2\28\u016f")
        buf.write("\3\2\2\2:\u0177\3\2\2\2<@\b\2\1\2=?\5\4\3\2>=\3\2\2\2")
        buf.write("?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2AD\3\2\2\2B@\3\2\2\2CE\5")
        buf.write("\6\4\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GH\3\2\2")
        buf.write("\2HI\b\2\1\2I\3\3\2\2\2JK\7\16\2\2KL\7\30\2\2LM\7\"\2")
        buf.write("\2MN\b\3\1\2N\5\3\2\2\2OP\7\22\2\2PS\7\30\2\2QR\7\'\2")
        buf.write("\2RT\7\30\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\t\2\2")
        buf.write("VW\b\4\1\2WX\5\b\5\2X\7\3\2\2\2Y]\7\36\2\2Z\\\5\n\6\2")
        buf.write("[Z\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^c\3\2\2\2_]")
        buf.write("\3\2\2\2`b\5\f\7\2a`\3\2\2\2be\3\2\2\2ca\3\2\2\2cd\3\2")
        buf.write("\2\2df\3\2\2\2ec\3\2\2\2fg\7\37\2\2g\t\3\2\2\2hi\7\30")
        buf.write("\2\2ij\b\6\1\2jk\5\20\t\2kl\7\"\2\2l\13\3\2\2\2mn\7\30")
        buf.write("\2\2no\b\7\1\2oq\7\34\2\2pr\5\16\b\2qp\3\2\2\2qr\3\2\2")
        buf.write("\2rs\3\2\2\2sx\7\35\2\2tu\5\20\t\2uv\b\7\1\2vy\3\2\2\2")
        buf.write("wy\7\24\2\2xt\3\2\2\2xw\3\2\2\2y}\3\2\2\2z|\5\22\n\2{")
        buf.write("z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080\3\2")
        buf.write("\2\2\177}\3\2\2\2\u0080\u0081\5\26\f\2\u0081\u0082\b\7")
        buf.write("\1\2\u0082\u0094\3\2\2\2\u0083\u0084\7\30\2\2\u0084\u0085")
        buf.write("\b\7\1\2\u0085\u0087\7\34\2\2\u0086\u0088\5\16\b\2\u0087")
        buf.write("\u0086\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008d\7\35\2\2\u008a\u008c\5\22\n\2\u008b\u008a")
        buf.write("\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u0090\u0091\5\26\f\2\u0091\u0092\b\7\1\2\u0092\u0094")
        buf.write("\3\2\2\2\u0093m\3\2\2\2\u0093\u0083\3\2\2\2\u0094\r\3")
        buf.write("\2\2\2\u0095\u0096\7\30\2\2\u0096\u0097\b\b\1\2\u0097")
        buf.write("\u0098\5\20\t\2\u0098\u00a1\b\b\1\2\u0099\u009a\7#\2\2")
        buf.write("\u009a\u009b\7\30\2\2\u009b\u009c\b\b\1\2\u009c\u009d")
        buf.write("\5\20\t\2\u009d\u009e\b\b\1\2\u009e\u00a0\3\2\2\2\u009f")
        buf.write("\u0099\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a1\u00a2\3\2\2\2\u00a2\17\3\2\2\2\u00a3\u00a1\3\2")
        buf.write("\2\2\u00a4\u00a5\t\2\2\2\u00a5\u00a6\b\t\1\2\u00a6\21")
        buf.write("\3\2\2\2\u00a7\u00a8\7\23\2\2\u00a8\u00a9\7\30\2\2\u00a9")
        buf.write("\u00af\b\n\1\2\u00aa\u00ab\7#\2\2\u00ab\u00ac\7\30\2\2")
        buf.write("\u00ac\u00ae\b\n\1\2\u00ad\u00aa\3\2\2\2\u00ae\u00b1\3")
        buf.write("\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b5")
        buf.write("\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3\7 \2\2\u00b3")
        buf.write("\u00b4\7\31\2\2\u00b4\u00b6\7!\2\2\u00b5\u00b2\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\5")
        buf.write("\20\t\2\u00b8\u00b9\7\"\2\2\u00b9\23\3\2\2\2\u00ba\u00bb")
        buf.write("\5&\24\2\u00bb\u00bc\7(\2\2\u00bc\u00bd\5\34\17\2\u00bd")
        buf.write("\u00be\b\13\1\2\u00be\25\3\2\2\2\u00bf\u00c5\7\36\2\2")
        buf.write("\u00c0\u00c1\5\30\r\2\u00c1\u00c2\b\f\1\2\u00c2\u00c4")
        buf.write("\3\2\2\2\u00c3\u00c0\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c8\3\2\2\2")
        buf.write("\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7\37\2\2\u00c9\27\3\2")
        buf.write("\2\2\u00ca\u00cb\5\24\13\2\u00cb\u00cc\7\"\2\2\u00cc\u00d6")
        buf.write("\3\2\2\2\u00cd\u00d6\5,\27\2\u00ce\u00cf\5\64\33\2\u00cf")
        buf.write("\u00d0\7\"\2\2\u00d0\u00d6\3\2\2\2\u00d1\u00d6\5\62\32")
        buf.write("\2\u00d2\u00d6\5\60\31\2\u00d3\u00d6\58\35\2\u00d4\u00d6")
        buf.write("\5\32\16\2\u00d5\u00ca\3\2\2\2\u00d5\u00cd\3\2\2\2\u00d5")
        buf.write("\u00ce\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d2\3\2\2\2")
        buf.write("\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\31\3\2")
        buf.write("\2\2\u00d7\u00d8\7\20\2\2\u00d8\u00d9\5\34\17\2\u00d9")
        buf.write("\u00da\7\"\2\2\u00da\33\3\2\2\2\u00db\u00dc\7)\2\2\u00dc")
        buf.write("\u00e6\5\36\20\2\u00dd\u00e3\5\36\20\2\u00de\u00df\t\3")
        buf.write("\2\2\u00df\u00e0\b\17\1\2\u00e0\u00e1\5\36\20\2\u00e1")
        buf.write("\u00e2\b\17\1\2\u00e2\u00e4\3\2\2\2\u00e3\u00de\3\2\2")
        buf.write("\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00db")
        buf.write("\3\2\2\2\u00e5\u00dd\3\2\2\2\u00e6\35\3\2\2\2\u00e7\u00e8")
        buf.write("\5 \21\2\u00e8\u00f0\b\20\1\2\u00e9\u00ea\t\4\2\2\u00ea")
        buf.write("\u00eb\b\20\1\2\u00eb\u00ec\5 \21\2\u00ec\u00ed\b\20\1")
        buf.write("\2\u00ed\u00ef\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("\37\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\5\"\22\2\u00f4")
        buf.write("\u00fc\b\21\1\2\u00f5\u00f6\t\5\2\2\u00f6\u00f7\b\21\1")
        buf.write("\2\u00f7\u00f8\5\"\22\2\u00f8\u00f9\b\21\1\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00f5\3\2\2\2\u00fb\u00fe\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd!\3\2\2\2\u00fe")
        buf.write("\u00fc\3\2\2\2\u00ff\u0100\7\34\2\2\u0100\u0101\b\22\1")
        buf.write("\2\u0101\u0102\5\34\17\2\u0102\u0103\7\35\2\2\u0103\u0104")
        buf.write("\b\22\1\2\u0104\u010a\3\2\2\2\u0105\u0107\t\4\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u010a\5$\23\2\u0109\u00ff\3\2\2\2\u0109\u0106\3")
        buf.write("\2\2\2\u010a#\3\2\2\2\u010b\u010c\5&\24\2\u010c\u010d")
        buf.write("\b\23\1\2\u010d\u0114\3\2\2\2\u010e\u0114\7\31\2\2\u010f")
        buf.write("\u0114\7\32\2\2\u0110\u0114\7\33\2\2\u0111\u0114\7\27")
        buf.write("\2\2\u0112\u0114\5\64\33\2\u0113\u010b\3\2\2\2\u0113\u010e")
        buf.write("\3\2\2\2\u0113\u010f\3\2\2\2\u0113\u0110\3\2\2\2\u0113")
        buf.write("\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114%\3\2\2\2\u0115")
        buf.write("\u0116\7\30\2\2\u0116\u011e\b\24\1\2\u0117\u0118\5(\25")
        buf.write("\2\u0118\u0119\b\24\1\2\u0119\u011e\3\2\2\2\u011a\u011b")
        buf.write("\5*\26\2\u011b\u011c\b\24\1\2\u011c\u011e\3\2\2\2\u011d")
        buf.write("\u0115\3\2\2\2\u011d\u0117\3\2\2\2\u011d\u011a\3\2\2\2")
        buf.write("\u011e\'\3\2\2\2\u011f\u0120\7\30\2\2\u0120\u0121\b\25")
        buf.write("\1\2\u0121\u0122\7 \2\2\u0122\u0123\5\34\17\2\u0123\u0124")
        buf.write("\7!\2\2\u0124)\3\2\2\2\u0125\u0126\7+\2\2\u0126\u0127")
        buf.write("\7\30\2\2\u0127\u0128\b\26\1\2\u0128+\3\2\2\2\u0129\u012a")
        buf.write("\7\r\2\2\u012a\u012b\5\34\17\2\u012b\u012f\5\26\f\2\u012c")
        buf.write("\u012e\5.\30\2\u012d\u012c\3\2\2\2\u012e\u0131\3\2\2\2")
        buf.write("\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0134\3")
        buf.write("\2\2\2\u0131\u012f\3\2\2\2\u0132\u0133\7\n\2\2\u0133\u0135")
        buf.write("\5\26\f\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("-\3\2\2\2\u0136\u0137\7\n\2\2\u0137\u0138\7\r\2\2\u0138")
        buf.write("\u0139\5\34\17\2\u0139\u013a\5\26\f\2\u013a/\3\2\2\2\u013b")
        buf.write("\u013c\7\25\2\2\u013c\u013d\5\34\17\2\u013d\u013e\5\26")
        buf.write("\f\2\u013e\61\3\2\2\2\u013f\u0141\7\f\2\2\u0140\u0142")
        buf.write("\5\24\13\2\u0141\u0140\3\2\2\2\u0141\u0142\3\2\2\2\u0142")
        buf.write("\u0143\3\2\2\2\u0143\u0144\7\"\2\2\u0144\u0145\5\34\17")
        buf.write("\2\u0145\u0147\7\"\2\2\u0146\u0148\5\24\13\2\u0147\u0146")
        buf.write("\3\2\2\2\u0147\u0148\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u014a\5\26\f\2\u014a\63\3\2\2\2\u014b\u014c\5&\24\2\u014c")
        buf.write("\u014d\7$\2\2\u014d\u014e\7\30\2\2\u014e\u014f\b\33\1")
        buf.write("\2\u014f\u0151\7\34\2\2\u0150\u0152\5\66\34\2\u0151\u0150")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0154\7\35\2\2\u0154\u0166\3\2\2\2\u0155\u0156\7\30\2")
        buf.write("\2\u0156\u0157\b\33\1\2\u0157\u0159\7\34\2\2\u0158\u015a")
        buf.write("\5\66\34\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u0166\7\35\2\2\u015c\u0166\5:\36")
        buf.write("\2\u015d\u015e\7\3\2\2\u015e\u015f\7\30\2\2\u015f\u0160")
        buf.write("\b\33\1\2\u0160\u0162\7\34\2\2\u0161\u0163\5\66\34\2\u0162")
        buf.write("\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\3\2\2\2")
        buf.write("\u0164\u0166\7\35\2\2\u0165\u014b\3\2\2\2\u0165\u0155")
        buf.write("\3\2\2\2\u0165\u015c\3\2\2\2\u0165\u015d\3\2\2\2\u0166")
        buf.write("\65\3\2\2\2\u0167\u016c\5\34\17\2\u0168\u0169\7#\2\2\u0169")
        buf.write("\u016b\5\34\17\2\u016a\u0168\3\2\2\2\u016b\u016e\3\2\2")
        buf.write("\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\67\3")
        buf.write("\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\7\26\2\2\u0170")
        buf.write("\u0171\7$\2\2\u0171\u0172\7\4\2\2\u0172\u0173\7\34\2\2")
        buf.write("\u0173\u0174\5\34\17\2\u0174\u0175\7\35\2\2\u0175\u0176")
        buf.write("\7\"\2\2\u01769\3\2\2\2\u0177\u0178\7\26\2\2\u0178\u017f")
        buf.write("\7$\2\2\u0179\u017a\7\5\2\2\u017a\u0180\b\36\1\2\u017b")
        buf.write("\u017c\7\6\2\2\u017c\u0180\b\36\1\2\u017d\u017e\7\7\2")
        buf.write("\2\u017e\u0180\b\36\1\2\u017f\u0179\3\2\2\2\u017f\u017b")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0182\7\34\2\2\u0182\u0183\7\35\2\2\u0183;\3\2\2\2$@")
        buf.write("FS]cqx}\u0087\u008d\u0093\u00a1\u00af\u00b5\u00c5\u00d5")
        buf.write("\u00e3\u00e5\u00f0\u00fc\u0106\u0109\u0113\u011d\u012f")
        buf.write("\u0134\u0141\u0147\u0151\u0159\u0162\u0165\u016c\u017f")
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
            self.state = 72
            self.match(IdleParser.IMPORT)
            self.state = 73
            localctx._ID = self.match(IdleParser.ID)
            self.state = 74
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
            self.state = 77
            self.match(IdleParser.TYPE)
            self.state = 78
            localctx.class_name = self.match(IdleParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ARROW:
                self.state = 79
                self.match(IdleParser.ARROW)
                self.state = 80
                localctx.parent_name = self.match(IdleParser.ID)


            self.state = 83
            self.match(IdleParser.CLASS)
            self.icomp.add_class((None if localctx.class_name is None else localctx.class_name.text), (0 if localctx.class_name is None else localctx.class_name.line), (None if localctx.parent_name is None else localctx.parent_name.text))
            self.state = 85
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
            self.state = 87
            self.match(IdleParser.LBRACE)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.attribute() 
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ID:
                self.state = 94
                self.method()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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
            self.state = 102
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 104
            self.typeState()
            self.state = 105
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
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_func((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 109
                self.match(IdleParser.LPAREN)
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ID:
                    self.state = 110
                    self.methodArguments()


                self.state = 113
                self.match(IdleParser.RPAREN)
                self.state = 118
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [IdleParser.BOOL, IdleParser.FLOAT, IdleParser.INT, IdleParser.STRING, IdleParser.ID]:
                    self.state = 114
                    localctx._typeState = self.typeState()
                    self.icomp.add_func_return_type((None if localctx._typeState is None else self._input.getText((localctx._typeState.start,localctx._typeState.stop))))
                    pass
                elif token in [IdleParser.VOID]:
                    self.state = 117
                    self.match(IdleParser.VOID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IdleParser.VAR:
                    self.state = 120
                    self.varsDecl()
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.block()
                self.icomp.end_scope()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_constructor((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 131
                self.match(IdleParser.LPAREN)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ID:
                    self.state = 132
                    self.methodArguments()


                self.state = 135
                self.match(IdleParser.RPAREN)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IdleParser.VAR:
                    self.state = 136
                    self.varsDecl()
                    self.state = 141
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 142
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
            self.state = 147
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 149
            self.typeState()
            self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 151
                self.match(IdleParser.COMMA)
                self.state = 152
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 154
                self.typeState()
                self.icomp.add_arg((None if localctx._ID is None else localctx._ID.text))
                self.state = 161
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
            self.state = 162
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
            self.state = 165
            self.match(IdleParser.VAR)
            self.state = 166
            localctx._ID = self.match(IdleParser.ID)
            self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 168
                self.match(IdleParser.COMMA)
                self.state = 169
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.add_var((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.LBRACK:
                self.state = 176
                self.match(IdleParser.LBRACK)
                self.state = 177
                self.match(IdleParser.INT_LITERAL)
                self.state = 178
                self.match(IdleParser.RBRACK)


            self.state = 181
            self.typeState()
            self.state = 182
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
            self.state = 184
            localctx._reference = self.reference()
            self.state = 185
            self.match(IdleParser.ASSIGN)
            self.state = 186
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
            self.state = 189
            self.match(IdleParser.LBRACE)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.FOR) | (1 << IdleParser.IF) | (1 << IdleParser.RETURN) | (1 << IdleParser.WHILE) | (1 << IdleParser.IO) | (1 << IdleParser.ID) | (1 << IdleParser.DSYMBOL))) != 0):
                self.state = 190
                self.statement()
                self.icomp.reset_new_line()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
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
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.assignment()
                self.state = 201
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.call()
                self.state = 205
                self.match(IdleParser.SEMICOLON)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.forLoop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.whileLoop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 209
                self.printState()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 210
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
            self.state = 213
            self.match(IdleParser.RETURN)
            self.state = 214
            self.expression()
            self.state = 215
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
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(IdleParser.BANG)
                self.state = 218
                self.exp()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.LPAREN, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                localctx._exp = self.exp()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0):
                    self.state = 220
                    localctx.operator = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.AND) | (1 << IdleParser.EQUAL) | (1 << IdleParser.GE) | (1 << IdleParser.GT) | (1 << IdleParser.LE) | (1 << IdleParser.LT) | (1 << IdleParser.NOTEQUAL) | (1 << IdleParser.OR))) != 0)):
                        localctx.operator = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                    self.state = 222
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
            self.state = 229
            localctx._term = self.term()
            self.icomp.quad_check_addsub((None if localctx._term is None else localctx._term.start).line)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.ADD or _la==IdleParser.SUB:
                self.state = 231
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                self.state = 233
                localctx._term = self.term()
                self.icomp.quad_check_addsub((None if localctx._term is None else localctx._term.start).line)
                self.state = 240
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
            self.state = 241
            localctx._factor = self.factor()
            self.icomp.quad_check_divmult((None if localctx._factor is None else localctx._factor.start).line)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.DIV or _la==IdleParser.MUL:
                self.state = 243
                localctx.operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IdleParser.DIV or _la==IdleParser.MUL):
                    localctx.operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.icomp.quad_add_oper((None if localctx.operator is None else localctx.operator.text))
                self.state = 245
                localctx._factor = self.factor()
                self.icomp.quad_check_divmult((None if localctx._factor is None else localctx._factor.start).line)
                self.state = 252
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
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.LPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(IdleParser.LPAREN)
                self.icomp.quad_open_parenthesis()
                self.state = 255
                self.expression()
                self.state = 256
                self.match(IdleParser.RPAREN)
                self.icomp.quad_close_parenthesis()
                pass
            elif token in [IdleParser.T__0, IdleParser.IO, IdleParser.BOOL_LITERAL, IdleParser.ID, IdleParser.INT_LITERAL, IdleParser.FLOAT_LITERAL, IdleParser.STRING_LITERAL, IdleParser.ADD, IdleParser.DSYMBOL, IdleParser.SUB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==IdleParser.ADD or _la==IdleParser.SUB:
                    self.state = 259
                    _la = self._input.LA(1)
                    if not(_la==IdleParser.ADD or _la==IdleParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 262
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
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                localctx._reference = self.reference()
                self.icomp.quad_add_var((None if localctx._reference is None else self._input.getText((localctx._reference.start,localctx._reference.stop))))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(IdleParser.INT_LITERAL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(IdleParser.FLOAT_LITERAL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 270
                self.match(IdleParser.STRING_LITERAL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 271
                self.match(IdleParser.BOOL_LITERAL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 272
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
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                localctx._arrPos = self.arrPos()
                localctx.attr_ref = localctx._arrPos.attr_ref
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
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
            self.state = 285
            localctx._ID = self.match(IdleParser.ID)
            localctx.attr_ref = self.icomp.check_var_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
            self.state = 287
            self.match(IdleParser.LBRACK)
            self.state = 288
            self.expression()
            self.state = 289
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
            self.state = 291
            self.match(IdleParser.DSYMBOL)
            self.state = 292
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
            self.state = 295
            self.match(IdleParser.IF)
            self.state = 296
            self.expression()
            self.state = 297
            self.block()
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 298
                    self.elseIf() 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ELSE:
                self.state = 304
                self.match(IdleParser.ELSE)
                self.state = 305
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
            self.state = 308
            self.match(IdleParser.ELSE)
            self.state = 309
            self.match(IdleParser.IF)
            self.state = 310
            self.expression()
            self.state = 311
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
            self.state = 313
            self.match(IdleParser.WHILE)
            self.state = 314
            self.expression()
            self.state = 315
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
            self.state = 317
            self.match(IdleParser.FOR)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 318
                self.assignment()


            self.state = 321
            self.match(IdleParser.SEMICOLON)
            self.state = 322
            self.expression()
            self.state = 323
            self.match(IdleParser.SEMICOLON)
            self.state = 325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==IdleParser.ID or _la==IdleParser.DSYMBOL:
                self.state = 324
                self.assignment()


            self.state = 327
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
        self.enterRule(localctx, 50, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                localctx._reference = self.reference()
                self.state = 330
                self.match(IdleParser.DOT)
                self.state = 331
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_obj_func_exists(localctx._reference.attr_ref, (None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 333
                self.match(IdleParser.LPAREN)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 334
                    self.callArguments()


                self.state = 337
                self.match(IdleParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 339
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_func_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 341
                self.match(IdleParser.LPAREN)
                self.state = 343
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 342
                    self.callArguments()


                self.state = 345
                self.match(IdleParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.read()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.match(IdleParser.T__0)
                self.state = 348
                localctx._ID = self.match(IdleParser.ID)
                self.icomp.check_class_exists((None if localctx._ID is None else localctx._ID.text), (0 if localctx._ID is None else localctx._ID.line))
                self.state = 350
                self.match(IdleParser.LPAREN)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IdleParser.T__0) | (1 << IdleParser.IO) | (1 << IdleParser.BOOL_LITERAL) | (1 << IdleParser.ID) | (1 << IdleParser.INT_LITERAL) | (1 << IdleParser.FLOAT_LITERAL) | (1 << IdleParser.STRING_LITERAL) | (1 << IdleParser.LPAREN) | (1 << IdleParser.ADD) | (1 << IdleParser.BANG) | (1 << IdleParser.DSYMBOL) | (1 << IdleParser.SUB))) != 0):
                    self.state = 351
                    self.callArguments()


                self.state = 354
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
            self.state = 357
            self.expression()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==IdleParser.COMMA:
                self.state = 358
                self.match(IdleParser.COMMA)
                self.state = 359
                self.expression()
                self.state = 364
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
            self.state = 365
            self.match(IdleParser.IO)
            self.state = 366
            self.match(IdleParser.DOT)
            self.state = 367
            self.match(IdleParser.T__1)
            self.state = 368
            self.match(IdleParser.LPAREN)
            self.state = 369
            self.expression()
            self.state = 370
            self.match(IdleParser.RPAREN)
            self.state = 371
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(IdleParser.IO)
            self.state = 374
            self.match(IdleParser.DOT)
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IdleParser.T__2]:
                self.state = 375
                self.match(IdleParser.T__2)
                self.icomp.quad_read('string')
                pass
            elif token in [IdleParser.T__3]:
                self.state = 377
                self.match(IdleParser.T__3)
                self.icomp.quad_read('int')
                pass
            elif token in [IdleParser.T__4]:
                self.state = 379
                self.match(IdleParser.T__4)
                self.icomp.quad_read('float')
                pass
            else:
                raise NoViableAltException(self)

            self.state = 383
            self.match(IdleParser.LPAREN)
            self.state = 384
            self.match(IdleParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





