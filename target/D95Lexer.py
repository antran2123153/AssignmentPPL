# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import re



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\5\2\u00a2\n\2\3\3\3\3\7\3")
        buf.write("\u00a6\n\3\f\3\16\3\u00a9\13\3\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\5\4\u00b2\n\4\3\4\3\4\3\5\3\5\5\5\u00b8\n\5\3\5\5")
        buf.write("\5\u00bb\n\5\3\5\3\5\5\5\u00bf\n\5\3\5\5\5\u00c2\n\5\3")
        buf.write("\5\5\5\u00c5\n\5\3\5\3\5\3\6\3\6\5\6\u00cb\n\6\3\6\7\6")
        buf.write("\u00ce\n\6\f\6\16\6\u00d1\13\6\3\6\5\6\u00d4\n\6\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00da\n\7\3\7\7\7\u00dd\n\7\f\7\16\7\u00e0")
        buf.write("\13\7\3\b\3\b\3\b\3\b\5\b\u00e6\n\b\3\b\7\b\u00e9\n\b")
        buf.write("\f\b\16\b\u00ec\13\b\3\t\3\t\3\t\5\t\u00f1\n\t\3\t\7\t")
        buf.write("\u00f4\n\t\f\t\16\t\u00f7\13\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\7\n\u00ff\n\n\f\n\16\n\u0102\13\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\7\37\u0198\n")
        buf.write("\37\f\37\16\37\u019b\13\37\3 \3 \7 \u019f\n \f \16 \u01a2")
        buf.write("\13 \3!\3!\7!\u01a6\n!\f!\16!\u01a9\13!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3")
        buf.write("<\3=\3=\3>\6>\u01ee\n>\r>\16>\u01ef\3>\3>\3?\3?\7?\u01f6")
        buf.write("\n?\f?\16?\u01f9\13?\3?\3?\3?\3?\3@\3@\7@\u0201\n@\f@")
        buf.write("\16@\u0204\13@\3@\3@\3A\3A\3A\3A\3A\3A\7A\u020e\nA\fA")
        buf.write("\16A\u0211\13A\3B\3B\3C\3C\3C\3C\5C\u0219\nC\3D\3D\3D")
        buf.write("\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\3D\5D\u0229\nD\3E\3E\3")
        buf.write("F\3F\3F\3F\5F\u0231\nF\3F\3F\7F\u0235\nF\fF\16F\u0238")
        buf.write("\13F\3G\3G\5G\u023c\nG\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3")
        buf.write("L\3L\3M\3M\3N\3N\3O\3O\2\2P\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C")
        buf.write("\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\3\2")
        buf.write("\24\4\2ZZzz\4\2DDdd\3\2,,\3\2\61\61\3\2&&\6\2\62;C\\a")
        buf.write("ac|\3\2aa\3\2C\\\5\2\13\f\17\17\"\"\n\2$$))^^ddhhpptt")
        buf.write("vv\5\2\f\f$$^^\4\2GGgg\4\2--//\3\2\62;\3\2\63;\3\2\62")
        buf.write("9\5\2\62;CHch\3\2\62\63\2\u026b\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a3\3\2\2\2\7\u00b1\3\2\2\2\t\u00c4\3\2\2")
        buf.write("\2\13\u00d3\3\2\2\2\r\u00d5\3\2\2\2\17\u00e1\3\2\2\2\21")
        buf.write("\u00ed\3\2\2\2\23\u00f8\3\2\2\2\25\u0108\3\2\2\2\27\u010e")
        buf.write("\3\2\2\2\31\u0117\3\2\2\2\33\u011e\3\2\2\2\35\u0121\3")
        buf.write("\2\2\2\37\u0126\3\2\2\2!\u012c\3\2\2\2#\u0134\3\2\2\2")
        buf.write("%\u0137\3\2\2\2\'\u0140\3\2\2\2)\u0145\3\2\2\2+\u014b")
        buf.write("\3\2\2\2-\u0151\3\2\2\2/\u0158\3\2\2\2\61\u015f\3\2\2")
        buf.write("\2\63\u0167\3\2\2\2\65\u016f\3\2\2\2\67\u0179\3\2\2\2")
        buf.write("9\u0183\3\2\2\2;\u018c\3\2\2\2=\u0195\3\2\2\2?\u019c\3")
        buf.write("\2\2\2A\u01a3\3\2\2\2C\u01aa\3\2\2\2E\u01ad\3\2\2\2G\u01b1")
        buf.write("\3\2\2\2I\u01b4\3\2\2\2K\u01b7\3\2\2\2M\u01ba\3\2\2\2")
        buf.write("O\u01bd\3\2\2\2Q\u01c0\3\2\2\2S\u01c3\3\2\2\2U\u01c6\3")
        buf.write("\2\2\2W\u01c8\3\2\2\2Y\u01ca\3\2\2\2[\u01cc\3\2\2\2]\u01ce")
        buf.write("\3\2\2\2_\u01d0\3\2\2\2a\u01d2\3\2\2\2c\u01d4\3\2\2\2")
        buf.write("e\u01d6\3\2\2\2g\u01d8\3\2\2\2i\u01da\3\2\2\2k\u01dc\3")
        buf.write("\2\2\2m\u01de\3\2\2\2o\u01e0\3\2\2\2q\u01e2\3\2\2\2s\u01e4")
        buf.write("\3\2\2\2u\u01e6\3\2\2\2w\u01e8\3\2\2\2y\u01ea\3\2\2\2")
        buf.write("{\u01ed\3\2\2\2}\u01f3\3\2\2\2\177\u01fe\3\2\2\2\u0081")
        buf.write("\u0207\3\2\2\2\u0083\u0212\3\2\2\2\u0085\u0218\3\2\2\2")
        buf.write("\u0087\u0228\3\2\2\2\u0089\u022a\3\2\2\2\u008b\u022c\3")
        buf.write("\2\2\2\u008d\u0239\3\2\2\2\u008f\u023f\3\2\2\2\u0091\u0241")
        buf.write("\3\2\2\2\u0093\u0243\3\2\2\2\u0095\u0245\3\2\2\2\u0097")
        buf.write("\u0247\3\2\2\2\u0099\u0249\3\2\2\2\u009b\u024b\3\2\2\2")
        buf.write("\u009d\u024d\3\2\2\2\u009f\u00a2\5\'\24\2\u00a0\u00a2")
        buf.write("\5)\25\2\u00a1\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2")
        buf.write("\4\3\2\2\2\u00a3\u00a7\7$\2\2\u00a4\u00a6\5\u0085C\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00aa\u00ab\7$\2\2\u00ab\u00ac\b\3\2\2\u00ac\6")
        buf.write("\3\2\2\2\u00ad\u00b2\5\13\6\2\u00ae\u00b2\5\r\7\2\u00af")
        buf.write("\u00b2\5\21\t\2\u00b0\u00b2\5\17\b\2\u00b1\u00ad\3\2\2")
        buf.write("\2\u00b1\u00ae\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\b\4\3\2\u00b4")
        buf.write("\b\3\2\2\2\u00b5\u00b7\5\u0089E\2\u00b6\u00b8\5\u008b")
        buf.write("F\2\u00b7\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba")
        buf.write("\3\2\2\2\u00b9\u00bb\5\u008dG\2\u00ba\u00b9\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00c5\3\2\2\2\u00bc\u00be\5\u008b")
        buf.write("F\2\u00bd\u00bf\5\u008dG\2\u00be\u00bd\3\2\2\2\u00be\u00bf")
        buf.write("\3\2\2\2\u00bf\u00c5\3\2\2\2\u00c0\u00c2\5\u008bF\2\u00c1")
        buf.write("\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c5\5\u008dG\2\u00c4\u00b5\3\2\2\2\u00c4\u00bc")
        buf.write("\3\2\2\2\u00c4\u00c1\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\b\5\4\2\u00c7\n\3\2\2\2\u00c8\u00cf\5\u0093J\2")
        buf.write("\u00c9\u00cb\5\u009bN\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00ce\5\u0091I\2\u00cd")
        buf.write("\u00ca\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d4\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d4\5\u008fH\2\u00d3\u00c8\3\2\2\2\u00d3")
        buf.write("\u00d2\3\2\2\2\u00d4\f\3\2\2\2\u00d5\u00d6\5\u008fH\2")
        buf.write("\u00d6\u00d7\t\2\2\2\u00d7\u00de\5\u0097L\2\u00d8\u00da")
        buf.write("\5\u009bN\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dd\5\u0097L\2\u00dc\u00d9\3\2")
        buf.write("\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\16\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2")
        buf.write("\5\u008fH\2\u00e2\u00e3\t\3\2\2\u00e3\u00ea\5\u0099M\2")
        buf.write("\u00e4\u00e6\5\u009bN\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\5\u0099M\2\u00e8")
        buf.write("\u00e5\3\2\2\2\u00e9\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2")
        buf.write("\u00ea\u00eb\3\2\2\2\u00eb\20\3\2\2\2\u00ec\u00ea\3\2")
        buf.write("\2\2\u00ed\u00ee\5\u008fH\2\u00ee\u00f5\5\u0095K\2\u00ef")
        buf.write("\u00f1\5\u009bN\2\u00f0\u00ef\3\2\2\2\u00f0\u00f1\3\2")
        buf.write("\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\5\u0095K\2\u00f3")
        buf.write("\u00f0\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\22\3\2\2\2\u00f7\u00f5\3\2")
        buf.write("\2\2\u00f8\u00f9\7\61\2\2\u00f9\u00fa\7,\2\2\u00fa\u0100")
        buf.write("\3\2\2\2\u00fb\u00ff\n\4\2\2\u00fc\u00fd\7,\2\2\u00fd")
        buf.write("\u00ff\n\5\2\2\u00fe\u00fb\3\2\2\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3")
        buf.write("\2\2\2\u0101\u0103\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0104")
        buf.write("\7,\2\2\u0104\u0105\7\61\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\u0107\b\n\5\2\u0107\24\3\2\2\2\u0108\u0109\7d\2\2\u0109")
        buf.write("\u010a\7t\2\2\u010a\u010b\7g\2\2\u010b\u010c\7c\2\2\u010c")
        buf.write("\u010d\7m\2\2\u010d\26\3\2\2\2\u010e\u010f\7e\2\2\u010f")
        buf.write("\u0110\7q\2\2\u0110\u0111\7p\2\2\u0111\u0112\7v\2\2\u0112")
        buf.write("\u0113\7k\2\2\u0113\u0114\7p\2\2\u0114\u0115\7w\2\2\u0115")
        buf.write("\u0116\7g\2\2\u0116\30\3\2\2\2\u0117\u0118\7g\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("\u011c\7k\2\2\u011c\u011d\7h\2\2\u011d\32\3\2\2\2\u011e")
        buf.write("\u011f\7k\2\2\u011f\u0120\7h\2\2\u0120\34\3\2\2\2\u0121")
        buf.write("\u0122\7g\2\2\u0122\u0123\7n\2\2\u0123\u0124\7u\2\2\u0124")
        buf.write("\u0125\7g\2\2\u0125\36\3\2\2\2\u0126\u0127\7y\2\2\u0127")
        buf.write("\u0128\7j\2\2\u0128\u0129\7k\2\2\u0129\u012a\7n\2\2\u012a")
        buf.write("\u012b\7g\2\2\u012b \3\2\2\2\u012c\u012d\7h\2\2\u012d")
        buf.write("\u012e\7q\2\2\u012e\u012f\7t\2\2\u012f\u0130\7g\2\2\u0130")
        buf.write("\u0131\7c\2\2\u0131\u0132\7e\2\2\u0132\u0133\7j\2\2\u0133")
        buf.write("\"\3\2\2\2\u0134\u0135\7c\2\2\u0135\u0136\7u\2\2\u0136")
        buf.write("$\3\2\2\2\u0137\u0138\7h\2\2\u0138\u0139\7w\2\2\u0139")
        buf.write("\u013a\7p\2\2\u013a\u013b\7e\2\2\u013b\u013c\7v\2\2\u013c")
        buf.write("\u013d\7k\2\2\u013d\u013e\7q\2\2\u013e\u013f\7p\2\2\u013f")
        buf.write("&\3\2\2\2\u0140\u0141\7v\2\2\u0141\u0142\7t\2\2\u0142")
        buf.write("\u0143\7w\2\2\u0143\u0144\7g\2\2\u0144(\3\2\2\2\u0145")
        buf.write("\u0146\7h\2\2\u0146\u0147\7c\2\2\u0147\u0148\7n\2\2\u0148")
        buf.write("\u0149\7u\2\2\u0149\u014a\7g\2\2\u014a*\3\2\2\2\u014b")
        buf.write("\u014c\7c\2\2\u014c\u014d\7t\2\2\u014d\u014e\7t\2\2\u014e")
        buf.write("\u014f\7c\2\2\u014f\u0150\7{\2\2\u0150,\3\2\2\2\u0151")
        buf.write("\u0152\7f\2\2\u0152\u0153\7g\2\2\u0153\u0154\7h\2\2\u0154")
        buf.write("\u0155\7k\2\2\u0155\u0156\7p\2\2\u0156\u0157\7g\2\2\u0157")
        buf.write(".\3\2\2\2\u0158\u0159\7t\2\2\u0159\u015a\7g\2\2\u015a")
        buf.write("\u015b\7v\2\2\u015b\u015c\7w\2\2\u015c\u015d\7t\2\2\u015d")
        buf.write("\u015e\7p\2\2\u015e\60\3\2\2\2\u015f\u0160\7u\2\2\u0160")
        buf.write("\u0161\7v\2\2\u0161\u0162\7t\2\2\u0162\u0163\7\64\2\2")
        buf.write("\u0163\u0164\7k\2\2\u0164\u0165\7p\2\2\u0165\u0166\7v")
        buf.write("\2\2\u0166\62\3\2\2\2\u0167\u0168\7k\2\2\u0168\u0169\7")
        buf.write("p\2\2\u0169\u016a\7v\2\2\u016a\u016b\7\64\2\2\u016b\u016c")
        buf.write("\7u\2\2\u016c\u016d\7v\2\2\u016d\u016e\7t\2\2\u016e\64")
        buf.write("\3\2\2\2\u016f\u0170\7u\2\2\u0170\u0171\7v\2\2\u0171\u0172")
        buf.write("\7t\2\2\u0172\u0173\7\64\2\2\u0173\u0174\7h\2\2\u0174")
        buf.write("\u0175\7n\2\2\u0175\u0176\7q\2\2\u0176\u0177\7c\2\2\u0177")
        buf.write("\u0178\7v\2\2\u0178\66\3\2\2\2\u0179\u017a\7h\2\2\u017a")
        buf.write("\u017b\7n\2\2\u017b\u017c\7q\2\2\u017c\u017d\7c\2\2\u017d")
        buf.write("\u017e\7v\2\2\u017e\u017f\7\64\2\2\u017f\u0180\7u\2\2")
        buf.write("\u0180\u0181\7v\2\2\u0181\u0182\7t\2\2\u01828\3\2\2\2")
        buf.write("\u0183\u0184\7u\2\2\u0184\u0185\7v\2\2\u0185\u0186\7t")
        buf.write("\2\2\u0186\u0187\7\64\2\2\u0187\u0188\7d\2\2\u0188\u0189")
        buf.write("\7q\2\2\u0189\u018a\7q\2\2\u018a\u018b\7n\2\2\u018b:\3")
        buf.write("\2\2\2\u018c\u018d\7d\2\2\u018d\u018e\7q\2\2\u018e\u018f")
        buf.write("\7q\2\2\u018f\u0190\7n\2\2\u0190\u0191\7\64\2\2\u0191")
        buf.write("\u0192\7u\2\2\u0192\u0193\7v\2\2\u0193\u0194\7t\2\2\u0194")
        buf.write("<\3\2\2\2\u0195\u0199\t\6\2\2\u0196\u0198\t\7\2\2\u0197")
        buf.write("\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a>\3\2\2\2\u019b\u0199\3\2\2")
        buf.write("\2\u019c\u01a0\t\b\2\2\u019d\u019f\t\7\2\2\u019e\u019d")
        buf.write("\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1@\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3")
        buf.write("\u01a7\t\t\2\2\u01a4\u01a6\t\7\2\2\u01a5\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8B\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab")
        buf.write("\7?\2\2\u01ab\u01ac\7@\2\2\u01acD\3\2\2\2\u01ad\u01ae")
        buf.write("\7?\2\2\u01ae\u01af\7?\2\2\u01af\u01b0\7\60\2\2\u01b0")
        buf.write("F\3\2\2\2\u01b1\u01b2\7>\2\2\u01b2\u01b3\7?\2\2\u01b3")
        buf.write("H\3\2\2\2\u01b4\u01b5\7@\2\2\u01b5\u01b6\7?\2\2\u01b6")
        buf.write("J\3\2\2\2\u01b7\u01b8\7#\2\2\u01b8\u01b9\7?\2\2\u01b9")
        buf.write("L\3\2\2\2\u01ba\u01bb\7?\2\2\u01bb\u01bc\7?\2\2\u01bc")
        buf.write("N\3\2\2\2\u01bd\u01be\7-\2\2\u01be\u01bf\7\60\2\2\u01bf")
        buf.write("P\3\2\2\2\u01c0\u01c1\7(\2\2\u01c1\u01c2\7(\2\2\u01c2")
        buf.write("R\3\2\2\2\u01c3\u01c4\7~\2\2\u01c4\u01c5\7~\2\2\u01c5")
        buf.write("T\3\2\2\2\u01c6\u01c7\7-\2\2\u01c7V\3\2\2\2\u01c8\u01c9")
        buf.write("\7/\2\2\u01c9X\3\2\2\2\u01ca\u01cb\7,\2\2\u01cbZ\3\2\2")
        buf.write("\2\u01cc\u01cd\7\61\2\2\u01cd\\\3\2\2\2\u01ce\u01cf\7")
        buf.write("\'\2\2\u01cf^\3\2\2\2\u01d0\u01d1\7#\2\2\u01d1`\3\2\2")
        buf.write("\2\u01d2\u01d3\7?\2\2\u01d3b\3\2\2\2\u01d4\u01d5\7>\2")
        buf.write("\2\u01d5d\3\2\2\2\u01d6\u01d7\7@\2\2\u01d7f\3\2\2\2\u01d8")
        buf.write("\u01d9\7*\2\2\u01d9h\3\2\2\2\u01da\u01db\7+\2\2\u01db")
        buf.write("j\3\2\2\2\u01dc\u01dd\7]\2\2\u01ddl\3\2\2\2\u01de\u01df")
        buf.write("\7_\2\2\u01dfn\3\2\2\2\u01e0\u01e1\7}\2\2\u01e1p\3\2\2")
        buf.write("\2\u01e2\u01e3\7\177\2\2\u01e3r\3\2\2\2\u01e4\u01e5\7")
        buf.write("\60\2\2\u01e5t\3\2\2\2\u01e6\u01e7\7.\2\2\u01e7v\3\2\2")
        buf.write("\2\u01e8\u01e9\7<\2\2\u01e9x\3\2\2\2\u01ea\u01eb\7=\2")
        buf.write("\2\u01ebz\3\2\2\2\u01ec\u01ee\t\n\2\2\u01ed\u01ec\3\2")
        buf.write("\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0")
        buf.write("\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1\u01f2\b>\5\2\u01f2")
        buf.write("|\3\2\2\2\u01f3\u01f7\7$\2\2\u01f4\u01f6\5\u0085C\2\u01f5")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01f5\3\2\2\2")
        buf.write("\u01f7\u01f8\3\2\2\2\u01f8\u01fa\3\2\2\2\u01f9\u01f7\3")
        buf.write("\2\2\2\u01fa\u01fb\7^\2\2\u01fb\u01fc\n\13\2\2\u01fc\u01fd")
        buf.write("\b?\6\2\u01fd~\3\2\2\2\u01fe\u0202\7$\2\2\u01ff\u0201")
        buf.write("\5\u0085C\2\u0200\u01ff\3\2\2\2\u0201\u0204\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u0205\3\2\2\2")
        buf.write("\u0204\u0202\3\2\2\2\u0205\u0206\b@\7\2\u0206\u0080\3")
        buf.write("\2\2\2\u0207\u0208\7\61\2\2\u0208\u0209\7,\2\2\u0209\u020f")
        buf.write("\3\2\2\2\u020a\u020e\n\4\2\2\u020b\u020c\7,\2\2\u020c")
        buf.write("\u020e\n\5\2\2\u020d\u020a\3\2\2\2\u020d\u020b\3\2\2\2")
        buf.write("\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3")
        buf.write("\2\2\2\u0210\u0082\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213")
        buf.write("\5\u009dO\2\u0213\u0084\3\2\2\2\u0214\u0219\n\f\2\2\u0215")
        buf.write("\u0219\5\u0087D\2\u0216\u0217\7)\2\2\u0217\u0219\7$\2")
        buf.write("\2\u0218\u0214\3\2\2\2\u0218\u0215\3\2\2\2\u0218\u0216")
        buf.write("\3\2\2\2\u0219\u0086\3\2\2\2\u021a\u021b\7^\2\2\u021b")
        buf.write("\u0229\7d\2\2\u021c\u021d\7^\2\2\u021d\u0229\7h\2\2\u021e")
        buf.write("\u021f\7^\2\2\u021f\u0229\7t\2\2\u0220\u0221\7^\2\2\u0221")
        buf.write("\u0229\7p\2\2\u0222\u0223\7^\2\2\u0223\u0229\7v\2\2\u0224")
        buf.write("\u0225\7^\2\2\u0225\u0229\7)\2\2\u0226\u0227\7^\2\2\u0227")
        buf.write("\u0229\7^\2\2\u0228\u021a\3\2\2\2\u0228\u021c\3\2\2\2")
        buf.write("\u0228\u021e\3\2\2\2\u0228\u0220\3\2\2\2\u0228\u0222\3")
        buf.write("\2\2\2\u0228\u0224\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u0088")
        buf.write("\3\2\2\2\u022a\u022b\5\13\6\2\u022b\u008a\3\2\2\2\u022c")
        buf.write("\u0236\5s:\2\u022d\u0235\5\u0091I\2\u022e\u0230\5\u0091")
        buf.write("I\2\u022f\u0231\5\u009bN\2\u0230\u022f\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0233\5\u0091I\2\u0233")
        buf.write("\u0235\3\2\2\2\u0234\u022d\3\2\2\2\u0234\u022e\3\2\2\2")
        buf.write("\u0235\u0238\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3")
        buf.write("\2\2\2\u0237\u008c\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023b")
        buf.write("\t\r\2\2\u023a\u023c\t\16\2\2\u023b\u023a\3\2\2\2\u023b")
        buf.write("\u023c\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\5\13\6")
        buf.write("\2\u023e\u008e\3\2\2\2\u023f\u0240\7\62\2\2\u0240\u0090")
        buf.write("\3\2\2\2\u0241\u0242\t\17\2\2\u0242\u0092\3\2\2\2\u0243")
        buf.write("\u0244\t\20\2\2\u0244\u0094\3\2\2\2\u0245\u0246\t\21\2")
        buf.write("\2\u0246\u0096\3\2\2\2\u0247\u0248\t\22\2\2\u0248\u0098")
        buf.write("\3\2\2\2\u0249\u024a\t\23\2\2\u024a\u009a\3\2\2\2\u024b")
        buf.write("\u024c\7a\2\2\u024c\u009c\3\2\2\2\u024d\u024e\13\2\2\2")
        buf.write("\u024e\u009e\3\2\2\2$\2\u00a1\u00a7\u00b1\u00b7\u00ba")
        buf.write("\u00be\u00c1\u00c4\u00ca\u00cf\u00d3\u00d9\u00de\u00e5")
        buf.write("\u00ea\u00f0\u00f5\u00fe\u0100\u0199\u01a0\u01a7\u01ef")
        buf.write("\u01f7\u0202\u020d\u020f\u0218\u0228\u0230\u0234\u0236")
        buf.write("\u023b\b\3\3\2\3\4\3\3\5\4\b\2\2\3?\5\3@\6")
        return buf.getvalue()


class D95Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEAN = 1
    STRING = 2
    INTEGER = 3
    FLOAT = 4
    DECIMAL = 5
    HEXADECIMAL = 6
    BINARY = 7
    OCTAL = 8
    COMMENT = 9
    BREAK = 10
    CONTINUE = 11
    ELSE_IF = 12
    IF = 13
    ELSE = 14
    WHILE = 15
    FOREACH = 16
    AS = 17
    FUNCTION = 18
    TRUE = 19
    FALSE = 20
    ARRAY = 21
    DEFINE = 22
    RETURN = 23
    STR_INT = 24
    INT_STR = 25
    STR_FLOAT = 26
    FLOAT_STR = 27
    STR_BOOL = 28
    BOOL_STR = 29
    VARIABLE_IDENTIFIER = 30
    FUNCTION_IDENTIFIER = 31
    CONSTANT_IDENTIFIER = 32
    ASSIGN_GREATER = 33
    ASSIGN_ASSIGN_DOT = 34
    LESS_ASSIGN = 35
    GREATER_ASSIGN = 36
    NEG_ASSIGN = 37
    ASSIGN_ASSIGN = 38
    ADD_DOT = 39
    AND = 40
    OR = 41
    ADD = 42
    MINUS = 43
    MUL = 44
    DIV = 45
    MOD = 46
    NEG = 47
    ASSIGN = 48
    LESS = 49
    GREATER = 50
    OPEN_ROUND = 51
    CLOSE_ROUND = 52
    OPEN_BRACKET = 53
    CLOSE_BRACKET = 54
    OPEN_SHARP = 55
    CLOSE_SHARP = 56
    DOT = 57
    COMMA = 58
    COLON = 59
    SEMI = 60
    WS = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    UNTERMINATED_COMMENT = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'elseif'", "'if'", "'else'", "'while'", 
            "'foreach'", "'as'", "'function'", "'true'", "'false'", "'array'", 
            "'define'", "'return'", "'str2int'", "'int2str'", "'str2float'", 
            "'float2str'", "'str2bool'", "'bool2str'", "'=>'", "'==.'", 
            "'<='", "'>='", "'!='", "'=='", "'+.'", "'&&'", "'||'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'='", "'<'", "'>'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEAN", "STRING", "INTEGER", "FLOAT", "DECIMAL", "HEXADECIMAL", 
            "BINARY", "OCTAL", "COMMENT", "BREAK", "CONTINUE", "ELSE_IF", 
            "IF", "ELSE", "WHILE", "FOREACH", "AS", "FUNCTION", "TRUE", 
            "FALSE", "ARRAY", "DEFINE", "RETURN", "STR_INT", "INT_STR", 
            "STR_FLOAT", "FLOAT_STR", "STR_BOOL", "BOOL_STR", "VARIABLE_IDENTIFIER", 
            "FUNCTION_IDENTIFIER", "CONSTANT_IDENTIFIER", "ASSIGN_GREATER", 
            "ASSIGN_ASSIGN_DOT", "LESS_ASSIGN", "GREATER_ASSIGN", "NEG_ASSIGN", 
            "ASSIGN_ASSIGN", "ADD_DOT", "AND", "OR", "ADD", "MINUS", "MUL", 
            "DIV", "MOD", "NEG", "ASSIGN", "LESS", "GREATER", "OPEN_ROUND", 
            "CLOSE_ROUND", "OPEN_BRACKET", "CLOSE_BRACKET", "OPEN_SHARP", 
            "CLOSE_SHARP", "DOT", "COMMA", "COLON", "SEMI", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "BOOLEAN", "STRING", "INTEGER", "FLOAT", "DECIMAL", "HEXADECIMAL", 
                  "BINARY", "OCTAL", "COMMENT", "BREAK", "CONTINUE", "ELSE_IF", 
                  "IF", "ELSE", "WHILE", "FOREACH", "AS", "FUNCTION", "TRUE", 
                  "FALSE", "ARRAY", "DEFINE", "RETURN", "STR_INT", "INT_STR", 
                  "STR_FLOAT", "FLOAT_STR", "STR_BOOL", "BOOL_STR", "VARIABLE_IDENTIFIER", 
                  "FUNCTION_IDENTIFIER", "CONSTANT_IDENTIFIER", "ASSIGN_GREATER", 
                  "ASSIGN_ASSIGN_DOT", "LESS_ASSIGN", "GREATER_ASSIGN", 
                  "NEG_ASSIGN", "ASSIGN_ASSIGN", "ADD_DOT", "AND", "OR", 
                  "ADD", "MINUS", "MUL", "DIV", "MOD", "NEG", "ASSIGN", 
                  "LESS", "GREATER", "OPEN_ROUND", "CLOSE_ROUND", "OPEN_BRACKET", 
                  "CLOSE_BRACKET", "OPEN_SHARP", "CLOSE_SHARP", "DOT", "COMMA", 
                  "COLON", "SEMI", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "ERROR_CHAR", "STRING_BODY", "ESCAPE_SEQUENCE_SPECIAL", 
                  "INTEGER_PART", "DECIMAL_PART", "EXPONENT_PART", "ZERO", 
                  "DIGIT", "DIGIT_NOT_ZERO", "DIGIT_OCTAL", "DIGIT_HEXADECIMAL", 
                  "DIGIT_BINARY", "UNDERLINE", "ANY" ]

    grammarFileName = "D95.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.STRING_action 
            actions[2] = self.INTEGER_action 
            actions[3] = self.FLOAT_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text[1:-1] 
     

    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = re.sub('_', '', self.text) 
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             self.text = re.sub('_', '', self.text) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             self.text = self.text[1:] 
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             self.text = self.text[1:] 
     


