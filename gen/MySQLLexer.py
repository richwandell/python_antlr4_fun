# Generated from /Users/richwandell/PycharmProjects/mysql-to-rabbit.py/MySQLLexer.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


 

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"M\u021c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\t")
        buf.write(u"J\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\5\6\u00c5\n\6\3\7\3\7\3\7\3\7\5")
        buf.write(u"\7\u00cb\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write(u"\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00ff\n\22\3\23\3")
        buf.write(u"\23\3\23\3\23\5\23\u0105\n\23\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write(u"\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write(u"\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3")
        buf.write(u"\35\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write(u"\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3")
        buf.write(u"\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write(u"-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write(u"\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write(u"\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\39")
        buf.write(u"\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3=\3=\3")
        buf.write(u"=\3=\3>\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?")
        buf.write(u"\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\3A\3A\3")
        buf.write(u"A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3D")
        buf.write(u"\3D\3D\3E\3E\3E\3F\6F\u01dd\nF\rF\16F\u01de\3G\6G\u01e2")
        buf.write(u"\nG\rG\16G\u01e3\3H\5H\u01e7\nH\3H\3H\3H\3H\3I\6I\u01ee")
        buf.write(u"\nI\rI\16I\u01ef\3I\3I\3J\3J\3J\3J\3J\5J\u01f9\nJ\3K")
        buf.write(u"\3K\3L\3L\3M\3M\6M\u0201\nM\rM\16M\u0202\3M\3M\3N\3N")
        buf.write(u"\6N\u0209\nN\rN\16N\u020a\3N\3N\3O\3O\6O\u0211\nO\rO")
        buf.write(u"\16O\u0212\3O\3O\3P\3P\6P\u0219\nP\rP\16P\u021a\2\2Q")
        buf.write(u"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write(u"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write(u"\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(")
        buf.write(u"O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:")
        buf.write(u"s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F")
        buf.write(u"\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099")
        buf.write(u"\2\u009b\2\u009d\2\u009f\2\3\2\b\5\2C\\aac|\5\2\13\f")
        buf.write(u"\17\17\"\"\3\2bb\3\2))\3\2$$\7\2&&\62;C\\aac|\u0227\2")
        buf.write(u"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write(u"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write(u"\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write(u"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write(u"\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write(u"\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2")
        buf.write(u"\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3")
        buf.write(u"\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2")
        buf.write(u"I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2")
        buf.write(u"\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2")
        buf.write(u"\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write(u"\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3")
        buf.write(u"\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write(u"y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write(u"\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2")
        buf.write(u"\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2")
        buf.write(u"\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write(u"\3\2\2\2\2\u0097\3\2\2\2\3\u00a1\3\2\2\2\5\u00a8\3\2")
        buf.write(u"\2\2\7\u00b4\3\2\2\2\t\u00b9\3\2\2\2\13\u00c4\3\2\2\2")
        buf.write(u"\r\u00ca\3\2\2\2\17\u00cc\3\2\2\2\21\u00d0\3\2\2\2\23")
        buf.write(u"\u00d3\3\2\2\2\25\u00d8\3\2\2\2\27\u00dd\3\2\2\2\31\u00e0")
        buf.write(u"\3\2\2\2\33\u00e7\3\2\2\2\35\u00eb\3\2\2\2\37\u00ef\3")
        buf.write(u"\2\2\2!\u00f4\3\2\2\2#\u00fe\3\2\2\2%\u0104\3\2\2\2\'")
        buf.write(u"\u0106\3\2\2\2)\u010e\3\2\2\2+\u0115\3\2\2\2-\u0117\3")
        buf.write(u"\2\2\2/\u0119\3\2\2\2\61\u011b\3\2\2\2\63\u011d\3\2\2")
        buf.write(u"\2\65\u011f\3\2\2\2\67\u0121\3\2\2\29\u0128\3\2\2\2;")
        buf.write(u"\u012b\3\2\2\2=\u012e\3\2\2\2?\u0135\3\2\2\2A\u0137\3")
        buf.write(u"\2\2\2C\u0139\3\2\2\2E\u013b\3\2\2\2G\u013d\3\2\2\2I")
        buf.write(u"\u013f\3\2\2\2K\u0141\3\2\2\2M\u0144\3\2\2\2O\u0146\3")
        buf.write(u"\2\2\2Q\u0148\3\2\2\2S\u014a\3\2\2\2U\u014d\3\2\2\2W")
        buf.write(u"\u0151\3\2\2\2Y\u0154\3\2\2\2[\u0157\3\2\2\2]\u0159\3")
        buf.write(u"\2\2\2_\u015b\3\2\2\2a\u015d\3\2\2\2c\u0165\3\2\2\2e")
        buf.write(u"\u016b\3\2\2\2g\u0171\3\2\2\2i\u0176\3\2\2\2k\u017c\3")
        buf.write(u"\2\2\2m\u0182\3\2\2\2o\u0188\3\2\2\2q\u018c\3\2\2\2s")
        buf.write(u"\u0192\3\2\2\2u\u0198\3\2\2\2w\u019b\3\2\2\2y\u019f\3")
        buf.write(u"\2\2\2{\u01a3\3\2\2\2}\u01aa\3\2\2\2\177\u01b4\3\2\2")
        buf.write(u"\2\u0081\u01c2\3\2\2\2\u0083\u01ca\3\2\2\2\u0085\u01cf")
        buf.write(u"\3\2\2\2\u0087\u01d5\3\2\2\2\u0089\u01d8\3\2\2\2\u008b")
        buf.write(u"\u01dc\3\2\2\2\u008d\u01e1\3\2\2\2\u008f\u01e6\3\2\2")
        buf.write(u"\2\u0091\u01ed\3\2\2\2\u0093\u01f3\3\2\2\2\u0095\u01fa")
        buf.write(u"\3\2\2\2\u0097\u01fc\3\2\2\2\u0099\u01fe\3\2\2\2\u009b")
        buf.write(u"\u0206\3\2\2\2\u009d\u020e\3\2\2\2\u009f\u0218\3\2\2")
        buf.write(u"\2\u00a1\u00a2\7u\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write(u"\7n\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7e\2\2\u00a6\u00a7")
        buf.write(u"\7v\2\2\u00a7\4\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write(u"\7p\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad")
        buf.write(u"\7t\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7\"\2\2\u00af")
        buf.write(u"\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2\7v\2\2\u00b2")
        buf.write(u"\u00b3\7q\2\2\u00b3\6\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5")
        buf.write(u"\u00b6\7t\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7o\2\2\u00b8")
        buf.write(u"\b\3\2\2\2\u00b9\u00ba\7y\2\2\u00ba\u00bb\7j\2\2\u00bb")
        buf.write(u"\u00bc\7g\2\2\u00bc\u00bd\7t\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write(u"\n\3\2\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7p\2\2\u00c1")
        buf.write(u"\u00c5\7f\2\2\u00c2\u00c3\7(\2\2\u00c3\u00c5\7(\2\2\u00c4")
        buf.write(u"\u00bf\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\f\3\2\2\2\u00c6")
        buf.write(u"\u00c7\7q\2\2\u00c7\u00cb\7t\2\2\u00c8\u00c9\7~\2\2\u00c9")
        buf.write(u"\u00cb\7~\2\2\u00ca\u00c6\3\2\2\2\u00ca\u00c8\3\2\2\2")
        buf.write(u"\u00cb\16\3\2\2\2\u00cc\u00cd\7z\2\2\u00cd\u00ce\7q\2")
        buf.write(u"\2\u00ce\u00cf\7t\2\2\u00cf\20\3\2\2\2\u00d0\u00d1\7")
        buf.write(u"k\2\2\u00d1\u00d2\7u\2\2\u00d2\22\3\2\2\2\u00d3\u00d4")
        buf.write(u"\7p\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write(u"\7n\2\2\u00d7\24\3\2\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write(u"\7k\2\2\u00da\u00db\7m\2\2\u00db\u00dc\7g\2\2\u00dc\26")
        buf.write(u"\3\2\2\2\u00dd\u00de\7k\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write(u"\30\3\2\2\2\u00e0\u00e1\7g\2\2\u00e1\u00e2\7z\2\2\u00e2")
        buf.write(u"\u00e3\7k\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5\7v\2\2\u00e5")
        buf.write(u"\u00e6\7u\2\2\u00e6\32\3\2\2\2\u00e7\u00e8\7c\2\2\u00e8")
        buf.write(u"\u00e9\7n\2\2\u00e9\u00ea\7n\2\2\u00ea\34\3\2\2\2\u00eb")
        buf.write(u"\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7{\2\2\u00ee")
        buf.write(u"\36\3\2\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7t\2\2\u00f1")
        buf.write(u"\u00f2\7w\2\2\u00f2\u00f3\7g\2\2\u00f3 \3\2\2\2\u00f4")
        buf.write(u"\u00f5\7h\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7n\2\2\u00f7")
        buf.write(u"\u00f8\7u\2\2\u00f8\u00f9\7g\2\2\u00f9\"\3\2\2\2\u00fa")
        buf.write(u"\u00fb\7f\2\2\u00fb\u00fc\7k\2\2\u00fc\u00ff\7x\2\2\u00fd")
        buf.write(u"\u00ff\7\61\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fd\3\2\2")
        buf.write(u"\2\u00ff$\3\2\2\2\u0100\u0101\7o\2\2\u0101\u0102\7q\2")
        buf.write(u"\2\u0102\u0105\7f\2\2\u0103\u0105\7\'\2\2\u0104\u0100")
        buf.write(u"\3\2\2\2\u0104\u0103\3\2\2\2\u0105&\3\2\2\2\u0106\u0107")
        buf.write(u"\7d\2\2\u0107\u0108\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write(u"\7y\2\2\u010a\u010b\7g\2\2\u010b\u010c\7g\2\2\u010c\u010d")
        buf.write(u"\7p\2\2\u010d(\3\2\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write(u"\7g\2\2\u0110\u0111\7i\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write(u"\7z\2\2\u0113\u0114\7r\2\2\u0114*\3\2\2\2\u0115\u0116")
        buf.write(u"\7-\2\2\u0116,\3\2\2\2\u0117\u0118\7/\2\2\u0118.\3\2")
        buf.write(u"\2\2\u0119\u011a\7\u0080\2\2\u011a\60\3\2\2\2\u011b\u011c")
        buf.write(u"\7~\2\2\u011c\62\3\2\2\2\u011d\u011e\7(\2\2\u011e\64")
        buf.write(u"\3\2\2\2\u011f\u0120\7`\2\2\u0120\66\3\2\2\2\u0121\u0122")
        buf.write(u"\7d\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write(u"\7c\2\2\u0125\u0126\7t\2\2\u0126\u0127\7{\2\2\u01278")
        buf.write(u"\3\2\2\2\u0128\u0129\7>\2\2\u0129\u012a\7>\2\2\u012a")
        buf.write(u":\3\2\2\2\u012b\u012c\7@\2\2\u012c\u012d\7@\2\2\u012d")
        buf.write(u"<\3\2\2\2\u012e\u012f\7g\2\2\u012f\u0130\7u\2\2\u0130")
        buf.write(u"\u0131\7e\2\2\u0131\u0132\7c\2\2\u0132\u0133\7r\2\2\u0133")
        buf.write(u"\u0134\7g\2\2\u0134>\3\2\2\2\u0135\u0136\7,\2\2\u0136")
        buf.write(u"@\3\2\2\2\u0137\u0138\7+\2\2\u0138B\3\2\2\2\u0139\u013a")
        buf.write(u"\7*\2\2\u013aD\3\2\2\2\u013b\u013c\7_\2\2\u013cF\3\2")
        buf.write(u"\2\2\u013d\u013e\7]\2\2\u013eH\3\2\2\2\u013f\u0140\7")
        buf.write(u"<\2\2\u0140J\3\2\2\2\u0141\u0142\7\60\2\2\u0142\u0143")
        buf.write(u"\7,\2\2\u0143L\3\2\2\2\u0144\u0145\7?\2\2\u0145N\3\2")
        buf.write(u"\2\2\u0146\u0147\7>\2\2\u0147P\3\2\2\2\u0148\u0149\7")
        buf.write(u"@\2\2\u0149R\3\2\2\2\u014a\u014b\7#\2\2\u014b\u014c\7")
        buf.write(u"?\2\2\u014cT\3\2\2\2\u014d\u014e\7p\2\2\u014e\u014f\7")
        buf.write(u"q\2\2\u014f\u0150\7v\2\2\u0150V\3\2\2\2\u0151\u0152\7")
        buf.write(u">\2\2\u0152\u0153\7?\2\2\u0153X\3\2\2\2\u0154\u0155\7")
        buf.write(u"@\2\2\u0155\u0156\7?\2\2\u0156Z\3\2\2\2\u0157\u0158\7")
        buf.write(u"=\2\2\u0158\\\3\2\2\2\u0159\u015a\7.\2\2\u015a^\3\2\2")
        buf.write(u"\2\u015b\u015c\7\60\2\2\u015c`\3\2\2\2\u015d\u015e\7")
        buf.write(u"e\2\2\u015e\u015f\7q\2\2\u015f\u0160\7n\2\2\u0160\u0161")
        buf.write(u"\7n\2\2\u0161\u0162\7c\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write(u"\7g\2\2\u0164b\3\2\2\2\u0165\u0166\7k\2\2\u0166\u0167")
        buf.write(u"\7p\2\2\u0167\u0168\7p\2\2\u0168\u0169\7g\2\2\u0169\u016a")
        buf.write(u"\7t\2\2\u016ad\3\2\2\2\u016b\u016c\7q\2\2\u016c\u016d")
        buf.write(u"\7w\2\2\u016d\u016e\7v\2\2\u016e\u016f\7g\2\2\u016f\u0170")
        buf.write(u"\7t\2\2\u0170f\3\2\2\2\u0171\u0172\7l\2\2\u0172\u0173")
        buf.write(u"\7q\2\2\u0173\u0174\7k\2\2\u0174\u0175\7p\2\2\u0175h")
        buf.write(u"\3\2\2\2\u0176\u0177\7e\2\2\u0177\u0178\7t\2\2\u0178")
        buf.write(u"\u0179\7q\2\2\u0179\u017a\7u\2\2\u017a\u017b\7u\2\2\u017b")
        buf.write(u"j\3\2\2\2\u017c\u017d\7w\2\2\u017d\u017e\7u\2\2\u017e")
        buf.write(u"\u017f\7k\2\2\u017f\u0180\7p\2\2\u0180\u0181\7i\2\2\u0181")
        buf.write(u"l\3\2\2\2\u0182\u0183\7k\2\2\u0183\u0184\7p\2\2\u0184")
        buf.write(u"\u0185\7f\2\2\u0185\u0186\7g\2\2\u0186\u0187\7z\2\2\u0187")
        buf.write(u"n\3\2\2\2\u0188\u0189\7m\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write(u"\u018b\7{\2\2\u018bp\3\2\2\2\u018c\u018d\7q\2\2\u018d")
        buf.write(u"\u018e\7t\2\2\u018e\u018f\7f\2\2\u018f\u0190\7g\2\2\u0190")
        buf.write(u"\u0191\7t\2\2\u0191r\3\2\2\2\u0192\u0193\7i\2\2\u0193")
        buf.write(u"\u0194\7t\2\2\u0194\u0195\7q\2\2\u0195\u0196\7w\2\2\u0196")
        buf.write(u"\u0197\7r\2\2\u0197t\3\2\2\2\u0198\u0199\7d\2\2\u0199")
        buf.write(u"\u019a\7{\2\2\u019av\3\2\2\2\u019b\u019c\7h\2\2\u019c")
        buf.write(u"\u019d\7q\2\2\u019d\u019e\7t\2\2\u019ex\3\2\2\2\u019f")
        buf.write(u"\u01a0\7w\2\2\u01a0\u01a1\7u\2\2\u01a1\u01a2\7g\2\2\u01a2")
        buf.write(u"z\3\2\2\2\u01a3\u01a4\7k\2\2\u01a4\u01a5\7i\2\2\u01a5")
        buf.write(u"\u01a6\7p\2\2\u01a6\u01a7\7q\2\2\u01a7\u01a8\7t\2\2\u01a8")
        buf.write(u"\u01a9\7g\2\2\u01a9|\3\2\2\2\u01aa\u01ab\7r\2\2\u01ab")
        buf.write(u"\u01ac\7c\2\2\u01ac\u01ad\7t\2\2\u01ad\u01ae\7v\2\2\u01ae")
        buf.write(u"\u01af\7k\2\2\u01af\u01b0\7v\2\2\u01b0\u01b1\7k\2\2\u01b1")
        buf.write(u"\u01b2\7q\2\2\u01b2\u01b3\7p\2\2\u01b3~\3\2\2\2\u01b4")
        buf.write(u"\u01b5\7u\2\2\u01b5\u01b6\7v\2\2\u01b6\u01b7\7t\2\2\u01b7")
        buf.write(u"\u01b8\7c\2\2\u01b8\u01b9\7k\2\2\u01b9\u01ba\7i\2\2\u01ba")
        buf.write(u"\u01bb\7j\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd\7a\2\2\u01bd")
        buf.write(u"\u01be\7l\2\2\u01be\u01bf\7q\2\2\u01bf\u01c0\7k\2\2\u01c0")
        buf.write(u"\u01c1\7p\2\2\u01c1\u0080\3\2\2\2\u01c2\u01c3\7p\2\2")
        buf.write(u"\u01c3\u01c4\7c\2\2\u01c4\u01c5\7v\2\2\u01c5\u01c6\7")
        buf.write(u"w\2\2\u01c6\u01c7\7t\2\2\u01c7\u01c8\7c\2\2\u01c8\u01c9")
        buf.write(u"\7n\2\2\u01c9\u0082\3\2\2\2\u01ca\u01cb\7n\2\2\u01cb")
        buf.write(u"\u01cc\7g\2\2\u01cc\u01cd\7h\2\2\u01cd\u01ce\7v\2\2\u01ce")
        buf.write(u"\u0084\3\2\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7k\2\2")
        buf.write(u"\u01d1\u01d2\7i\2\2\u01d2\u01d3\7j\2\2\u01d3\u01d4\7")
        buf.write(u"v\2\2\u01d4\u0086\3\2\2\2\u01d5\u01d6\7q\2\2\u01d6\u01d7")
        buf.write(u"\7l\2\2\u01d7\u0088\3\2\2\2\u01d8\u01d9\7q\2\2\u01d9")
        buf.write(u"\u01da\7p\2\2\u01da\u008a\3\2\2\2\u01db\u01dd\t\2\2\2")
        buf.write(u"\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc")
        buf.write(u"\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u008c\3\2\2\2\u01e0")
        buf.write(u"\u01e2\4\62;\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2")
        buf.write(u"\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u008e")
        buf.write(u"\3\2\2\2\u01e5\u01e7\7\17\2\2\u01e6\u01e5\3\2\2\2\u01e6")
        buf.write(u"\u01e7\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\7\f\2")
        buf.write(u"\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\bH\2\2\u01eb\u0090")
        buf.write(u"\3\2\2\2\u01ec\u01ee\t\3\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write(u"\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2")
        buf.write(u"\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\bI\2\2\u01f2\u0092")
        buf.write(u"\3\2\2\2\u01f3\u01f8\7B\2\2\u01f4\u01f9\5\u0099M\2\u01f5")
        buf.write(u"\u01f9\5\u009bN\2\u01f6\u01f9\5\u009dO\2\u01f7\u01f9")
        buf.write(u"\5\u009fP\2\u01f8\u01f4\3\2\2\2\u01f8\u01f5\3\2\2\2\u01f8")
        buf.write(u"\u01f6\3\2\2\2\u01f8\u01f7\3\2\2\2\u01f9\u0094\3\2\2")
        buf.write(u"\2\u01fa\u01fb\7b\2\2\u01fb\u0096\3\2\2\2\u01fc\u01fd")
        buf.write(u"\7)\2\2\u01fd\u0098\3\2\2\2\u01fe\u0200\7b\2\2\u01ff")
        buf.write(u"\u0201\n\4\2\2\u0200\u01ff\3\2\2\2\u0201\u0202\3\2\2")
        buf.write(u"\2\u0202\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0204")
        buf.write(u"\3\2\2\2\u0204\u0205\7b\2\2\u0205\u009a\3\2\2\2\u0206")
        buf.write(u"\u0208\7)\2\2\u0207\u0209\n\5\2\2\u0208\u0207\3\2\2\2")
        buf.write(u"\u0209\u020a\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b")
        buf.write(u"\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\7)\2\2\u020d")
        buf.write(u"\u009c\3\2\2\2\u020e\u0210\7$\2\2\u020f\u0211\n\6\2\2")
        buf.write(u"\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0210")
        buf.write(u"\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write(u"\u0215\7$\2\2\u0215\u009e\3\2\2\2\u0216\u0219\t\7\2\2")
        buf.write(u"\u0217\u0219\5_\60\2\u0218\u0216\3\2\2\2\u0218\u0217")
        buf.write(u"\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u0218\3\2\2\2\u021a")
        buf.write(u"\u021b\3\2\2\2\u021b\u00a0\3\2\2\2\21\2\u00c4\u00ca\u00fe")
        buf.write(u"\u0104\u01de\u01e3\u01e6\u01ef\u01f8\u0202\u020a\u0212")
        buf.write(u"\u0218\u021a\3\b\2\2")
        return buf.getvalue()


class MySQLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    SELECT = 1
    INSERT = 2
    FROM = 3
    WHERE = 4
    AND = 5
    OR = 6
    XOR = 7
    IS = 8
    NULL = 9
    LIKE = 10
    IN = 11
    EXISTS = 12
    ALL = 13
    ANY = 14
    TRUE = 15
    FALSE = 16
    DIVIDE = 17
    MOD = 18
    BETWEEN = 19
    REGEXP = 20
    PLUS = 21
    MINUS = 22
    NEGATION = 23
    VERTBAR = 24
    BITAND = 25
    POWER_OP = 26
    BINARY = 27
    SHIFT_LEFT = 28
    SHIFT_RIGHT = 29
    ESCAPE = 30
    ASTERISK = 31
    RPAREN = 32
    LPAREN = 33
    RBRACK = 34
    LBRACK = 35
    COLON = 36
    ALL_FIELDS = 37
    EQ = 38
    LTH = 39
    GTH = 40
    NOT_EQ = 41
    NOT = 42
    LET = 43
    GET = 44
    SEMI = 45
    COMMA = 46
    DOT = 47
    COLLATE = 48
    INNER = 49
    OUTER = 50
    JOIN = 51
    CROSS = 52
    USING = 53
    INDEX = 54
    KEY = 55
    ORDER = 56
    GROUP = 57
    BY = 58
    FOR = 59
    USE = 60
    IGNORE = 61
    PARTITION = 62
    STRAIGHT_JOIN = 63
    NATURAL = 64
    LEFT = 65
    RIGHT = 66
    OJ = 67
    ON = 68
    ID = 69
    INT = 70
    NEWLINE = 71
    WS = 72
    USER_VAR = 73
    TILDE = 74
    SINGLE_QUOTE = 75

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'select'", u"'insert into'", u"'from'", u"'where'", u"'xor'", 
            u"'is'", u"'null'", u"'like'", u"'in'", u"'exists'", u"'all'", 
            u"'any'", u"'true'", u"'false'", u"'between'", u"'regexp'", 
            u"'+'", u"'-'", u"'~'", u"'|'", u"'&'", u"'^'", u"'binary'", 
            u"'<<'", u"'>>'", u"'escape'", u"'*'", u"')'", u"'('", u"']'", 
            u"'['", u"':'", u"'.*'", u"'='", u"'<'", u"'>'", u"'!='", u"'not'", 
            u"'<='", u"'>='", u"';'", u"','", u"'.'", u"'collate'", u"'inner'", 
            u"'outer'", u"'join'", u"'cross'", u"'using'", u"'index'", u"'key'", 
            u"'order'", u"'group'", u"'by'", u"'for'", u"'use'", u"'ignore'", 
            u"'partition'", u"'straight_join'", u"'natural'", u"'left'", 
            u"'right'", u"'oj'", u"'on'", u"'`'", u"'''" ]

    symbolicNames = [ u"<INVALID>",
            u"SELECT", u"INSERT", u"FROM", u"WHERE", u"AND", u"OR", u"XOR", 
            u"IS", u"NULL", u"LIKE", u"IN", u"EXISTS", u"ALL", u"ANY", u"TRUE", 
            u"FALSE", u"DIVIDE", u"MOD", u"BETWEEN", u"REGEXP", u"PLUS", 
            u"MINUS", u"NEGATION", u"VERTBAR", u"BITAND", u"POWER_OP", u"BINARY", 
            u"SHIFT_LEFT", u"SHIFT_RIGHT", u"ESCAPE", u"ASTERISK", u"RPAREN", 
            u"LPAREN", u"RBRACK", u"LBRACK", u"COLON", u"ALL_FIELDS", u"EQ", 
            u"LTH", u"GTH", u"NOT_EQ", u"NOT", u"LET", u"GET", u"SEMI", 
            u"COMMA", u"DOT", u"COLLATE", u"INNER", u"OUTER", u"JOIN", u"CROSS", 
            u"USING", u"INDEX", u"KEY", u"ORDER", u"GROUP", u"BY", u"FOR", 
            u"USE", u"IGNORE", u"PARTITION", u"STRAIGHT_JOIN", u"NATURAL", 
            u"LEFT", u"RIGHT", u"OJ", u"ON", u"ID", u"INT", u"NEWLINE", 
            u"WS", u"USER_VAR", u"TILDE", u"SINGLE_QUOTE" ]

    ruleNames = [ u"SELECT", u"INSERT", u"FROM", u"WHERE", u"AND", u"OR", 
                  u"XOR", u"IS", u"NULL", u"LIKE", u"IN", u"EXISTS", u"ALL", 
                  u"ANY", u"TRUE", u"FALSE", u"DIVIDE", u"MOD", u"BETWEEN", 
                  u"REGEXP", u"PLUS", u"MINUS", u"NEGATION", u"VERTBAR", 
                  u"BITAND", u"POWER_OP", u"BINARY", u"SHIFT_LEFT", u"SHIFT_RIGHT", 
                  u"ESCAPE", u"ASTERISK", u"RPAREN", u"LPAREN", u"RBRACK", 
                  u"LBRACK", u"COLON", u"ALL_FIELDS", u"EQ", u"LTH", u"GTH", 
                  u"NOT_EQ", u"NOT", u"LET", u"GET", u"SEMI", u"COMMA", 
                  u"DOT", u"COLLATE", u"INNER", u"OUTER", u"JOIN", u"CROSS", 
                  u"USING", u"INDEX", u"KEY", u"ORDER", u"GROUP", u"BY", 
                  u"FOR", u"USE", u"IGNORE", u"PARTITION", u"STRAIGHT_JOIN", 
                  u"NATURAL", u"LEFT", u"RIGHT", u"OJ", u"ON", u"ID", u"INT", 
                  u"NEWLINE", u"WS", u"USER_VAR", u"TILDE", u"SINGLE_QUOTE", 
                  u"USER_VAR_SUBFIX1", u"USER_VAR_SUBFIX2", u"USER_VAR_SUBFIX3", 
                  u"USER_VAR_SUBFIX4" ]

    grammarFileName = u"MySQLLexer.g4"

    def __init__(self, input=None):
        super(MySQLLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


