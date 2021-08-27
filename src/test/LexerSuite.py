import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test_function_01(self):
        self.assertTrue(TestLexer.checkLexeme('''while ($i < 10) { $u = $i + 1; $i = $i + 1; $d = 0.123e-456;}''','''while,(,$i,<,10,),{,$u,=,$i,+,1,;,$i,=,$i,+,1,;,$d,=,0.123e-456,;,},<EOF>''',100))
      
    def test_id_01(self):
        self.assertTrue(TestLexer.checkLexeme('''''','''<EOF>''',101))
      
    def test_id_02(self):
        self.assertTrue(TestLexer.checkLexeme('''$''','''$,<EOF>''',102))
      
    def test_id_03(self):
        self.assertTrue(TestLexer.checkLexeme('''$abc''','''$abc,<EOF>''',103))
      
    def test_id_04(self):
        self.assertTrue(TestLexer.checkLexeme('''$Abc''','''$Abc,<EOF>''',104))
      
    def test_id_05(self):
        self.assertTrue(TestLexer.checkLexeme('''$_abc''','''$_abc,<EOF>''',105))
      
    def test_id_06(self):
        self.assertTrue(TestLexer.checkLexeme('''$123abc''','''$123abc,<EOF>''',106))
      
    def test_id_07(self):
        self.assertTrue(TestLexer.checkLexeme('''_''','''_,<EOF>''',107))
      
    def test_id_08(self):
        self.assertTrue(TestLexer.checkLexeme('''__''','''__,<EOF>''',108))
      
    def test_id_09(self):
        self.assertTrue(TestLexer.checkLexeme('''_abc''','''_abc,<EOF>''',109))
      
    def test_id_10(self):
        self.assertTrue(TestLexer.checkLexeme('''_Abc''','''_Abc,<EOF>''',110))
      
    def test_id_11(self):
        self.assertTrue(TestLexer.checkLexeme('''_123''','''_123,<EOF>''',111))
      
    def test_id_12(self):
        self.assertTrue(TestLexer.checkLexeme('''Abc''','''Abc,<EOF>''',112))
      
    def test_id_13(self):
        self.assertTrue(TestLexer.checkLexeme('''A_bc''','''A_bc,<EOF>''',113))
      
    def test_id_14(self):
        self.assertTrue(TestLexer.checkLexeme('''A123''','''A123,<EOF>''',114))
      
    def test_id_15(self):
        self.assertTrue(TestLexer.checkLexeme('''abc''','''Error Token a''',115))
      
    def test_id_16(self):
        self.assertTrue(TestLexer.checkLexeme('''123abc''','''123,Error Token a''',116))
      
    def test_id_17(self):
        self.assertTrue(TestLexer.checkLexeme('''Abc$#''','''Abc,$,Error Token #''',117))
      
    def test_key_01(self):
        self.assertTrue(TestLexer.checkLexeme('''break return''','''break,return,<EOF>''',118))
      
    def test_key_02(self):
        self.assertTrue(TestLexer.checkLexeme('''if elseif else''','''if,elseif,else,<EOF>''',119))
      
    def test_key_03(self):
        self.assertTrue(TestLexer.checkLexeme('''breakreturn''','''break,return,<EOF>''',120))
      
    def test_key_04(self):
        self.assertTrue(TestLexer.checkLexeme('''_echo''','''_echo,<EOF>''',121))
      
    def test_key_05(self):
        self.assertTrue(TestLexer.checkLexeme('''bool2str''','''bool2str,<EOF>''',122))
      
    def test_key_06(self):
        self.assertTrue(TestLexer.checkLexeme('''true false''','''true,false,<EOF>''',123))
      
    def test_num_01(self):
        self.assertTrue(TestLexer.checkLexeme('''0''','''0,<EOF>''',124))
      
    def test_num_02(self):
        self.assertTrue(TestLexer.checkLexeme('''123''','''123,<EOF>''',125))
      
    def test_num_03(self):
        self.assertTrue(TestLexer.checkLexeme('''1_23''','''123,<EOF>''',126))
      
    def test_num_04(self):
        self.assertTrue(TestLexer.checkLexeme('''123_''','''123,_,<EOF>''',127))
      
    def test_num_05(self):
        self.assertTrue(TestLexer.checkLexeme('''0x12_3abc''','''0x123abc,<EOF>''',128))
      
    def test_num_06(self):
        self.assertTrue(TestLexer.checkLexeme('''0X1_23A_bC''','''0X123AbC,<EOF>''',129))
      
    def test_num_07(self):
        self.assertTrue(TestLexer.checkLexeme('''0b1_01''','''0b101,<EOF>''',130))
      
    def test_num_08(self):
        self.assertTrue(TestLexer.checkLexeme('''0B11_001''','''0B11001,<EOF>''',131))
      
    def test_num_09(self):
        self.assertTrue(TestLexer.checkLexeme('''012_345''','''012345,<EOF>''',132))
      
    def test_num_10(self):
        self.assertTrue(TestLexer.checkLexeme('''001234''','''001234,<EOF>''',133))
      
    def test_num_11(self):
        self.assertTrue(TestLexer.checkLexeme('''0987''','''0,987,<EOF>''',134))
      
    def test_num_12(self):
        self.assertTrue(TestLexer.checkLexeme('''0.''','''0.,<EOF>''',135))
      
    def test_num_13(self):
        self.assertTrue(TestLexer.checkLexeme('''0.123''','''0.123,<EOF>''',136))
      
    def test_num_14(self):
        self.assertTrue(TestLexer.checkLexeme('''0.0123''','''0.0123,<EOF>''',137))
      
    def test_num_15(self):
        self.assertTrue(TestLexer.checkLexeme('''12_3.12_3''','''123.123,<EOF>''',138))
      
    def test_num_16(self):
        self.assertTrue(TestLexer.checkLexeme('''.123''','''.123,<EOF>''',139))
      
    def test_num_17(self):
        self.assertTrue(TestLexer.checkLexeme('''123.123.123''','''123.123,.123,<EOF>''',140))
      
    def test_num_18(self):
        self.assertTrue(TestLexer.checkLexeme('''.12_3e''','''.123,Error Token e''',141))
      
    def test_num_19(self):
        self.assertTrue(TestLexer.checkLexeme('''e+123''','''e+123,<EOF>''',142))
      
    def test_num_20(self):
        self.assertTrue(TestLexer.checkLexeme('''.e-123''','''.e-123,<EOF>''',143))
      
    def test_num_21(self):
        self.assertTrue(TestLexer.checkLexeme('''.123e12_3''','''.123e123,<EOF>''',144))
      
    def test_num_22(self):
        self.assertTrue(TestLexer.checkLexeme('''.123E-123''','''.123E-123,<EOF>''',145))
      
    def test_num_23(self):
        self.assertTrue(TestLexer.checkLexeme('''.0123e+123''','''.0123e+123,<EOF>''',146))
      
    def test_num_24(self):
        self.assertTrue(TestLexer.checkLexeme('''1_23.12_3e-12_3''','''123.123e-123,<EOF>''',147))
      
    def test_num_25(self):
        self.assertTrue(TestLexer.checkLexeme('''123_.123''','''123,_,.123,<EOF>''',148))
      
    def test_num_26(self):
        self.assertTrue(TestLexer.checkLexeme('''123.123_e123''','''123.123,_e123,<EOF>''',149))
      
    def test_num_27(self):
        self.assertTrue(TestLexer.checkLexeme('''012_3.1_23e''','''0123,.123,Error Token e''',150))
      
    def test_num_28(self):
        self.assertTrue(TestLexer.checkLexeme('''00123.123e123''','''00123,.123e123,<EOF>''',151))
      
    def test_num_29(self):
        self.assertTrue(TestLexer.checkLexeme('''123.e''','''123.,Error Token e''',152))
      
    def test_num_30(self):
        self.assertTrue(TestLexer.checkLexeme('''123.e-''','''123.,Error Token e''',153))
      
    def test_num_31(self):
        self.assertTrue(TestLexer.checkLexeme('''123.e-0123''','''123.e-0,123,<EOF>''',154))
      
    def test_str_01(self):
        self.assertTrue(TestLexer.checkLexeme('''""''',''',<EOF>''',155))
      
    def test_str_02(self):
        self.assertTrue(TestLexer.checkLexeme('''"qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM"''','''qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM,<EOF>''',156))
      
    def test_str_03(self):
        self.assertTrue(TestLexer.checkLexeme('''"$a _abc() array ABC"''','''$a _abc() array ABC,<EOF>''',157))
      
    def test_str_04(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc 123 ~!@#$%^&*()_+=-`[]"''','''abc 123 ~!@#$%^&*()_+=-`[],<EOF>''',158))
      
    def test_str_05(self):
        self.assertTrue(TestLexer.checkLexeme('''"\\b \\f \\r \\n \\t \\\' \\\\"''','''\\b \\f \\r \\n \\t \\\' \\\\,<EOF>''',159))
      
    def test_str_06(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc \n \t \n \r 123"''','''Unclosed String: abc \n''',160))
      
    def test_str_07(self):
        self.assertTrue(TestLexer.checkLexeme('''"'"'""''',''''"'",<EOF>''',161))
      
    def test_str_08(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc '"123'" abc"''','''abc '"123'" abc,<EOF>''',162))
      
    def test_str_09(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc '"123  '"abc'" 123'" abc"''','''abc '"123  '"abc'" 123'" abc,<EOF>''',163))
      
    def test_str_10(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc""abc"''','''abc,abc,<EOF>''',164))
      
    def test_str_11(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc"123"abc"''','''abc,123,abc,<EOF>''',165))
      
    def test_str_12(self):
        self.assertTrue(TestLexer.checkLexeme('''123"abc"123"abc"123''','''123,abc,123,abc,123,<EOF>''',166))
      
    def test_str_13(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc 123''','''Unclosed String: abc 123''',167))
      
    def test_str_14(self):
        self.assertTrue(TestLexer.checkLexeme('''abc 123"''','''Error Token a''',168))
      
    def test_str_15(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc '"123'"''','''abc '"123',<EOF>''',169))
      
    def test_str_16(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc \\z 123"''','''Illegal Escape In String: abc \z''',170))
      
    def test_cmt_01(self):
        self.assertTrue(TestLexer.checkLexeme('''/**/''','''<EOF>''',171))
      
    def test_cmt_02(self):
        self.assertTrue(TestLexer.checkLexeme('''/*abcd ef123456 78ABCDEF*/''','''<EOF>''',172))
      
    def test_cmt_03(self):
        self.assertTrue(TestLexer.checkLexeme('''/*~!@#$%^&*()_+=-{}[]|\';:"/.,<>~`*/''','''<EOF>''',173))
      
    def test_cmt_04(self):
        self.assertTrue(TestLexer.checkLexeme('''/*\\a \\b \\c \\d \\1 \\2 \\3 \\n \\b \\f \\r \\t */''','''<EOF>''',174))
      
    def test_cmt_05(self):
        self.assertTrue(TestLexer.checkLexeme('''/*\n abc \n123 \nabc \n*/''','''<EOF>''',175))
      
    def test_cmt_06(self):
        self.assertTrue(TestLexer.checkLexeme('''/*abc /* 123 */ abc*/''','''Error Token a''',176))
      
    def test_cmt_07(self):
        self.assertTrue(TestLexer.checkLexeme('''/*abc 123''','''Unterminated Comment''',177))
      
    def test_cmt_08(self):
        self.assertTrue(TestLexer.checkLexeme('''/ * abc */''','''/,*,Error Token a''',178))
      
    def test_cmt_09(self):
        self.assertTrue(TestLexer.checkLexeme('''/* abc * /''','''Unterminated Comment''',179))
      
    def test_cmt_10(self):
        self.assertTrue(TestLexer.checkLexeme('''123/*abc*/123''','''123,123,<EOF>''',180))
      
    def test_opr_01(self):
        self.assertTrue(TestLexer.checkLexeme('''=>==.<=>=!===+.&&||+-*/%!=<>''','''=>,==.,<=,>=,!=,==,+.,&&,||,+,-,*,/,%,!=,<,>,<EOF>''',181))
      
    def test_opr_02(self):
        self.assertTrue(TestLexer.checkLexeme('''{[(.,:)]};''','''{,[,(,.,,,:,),],},;,<EOF>''',182))
      
    def test_opr_03(self):
        self.assertTrue(TestLexer.checkLexeme('''123 + 12_3 - 210.01_2 * 0.12_3e123 / 0.1_2e-3 % 12e+12_3''','''123,+,123,-,210.012,*,0.123e123,/,0.12e-3,%,12e+123,<EOF>''',183))
      
    def test_opr_04(self):
        self.assertTrue(TestLexer.checkLexeme('''123 > 12_3 < 210.01_2 = 0.12_3e123 . 0.1_2e-3 % 12e+12_3''','''123,>,123,<,210.012,=,0.123e123,.,0.12e-3,%,12e+123,<EOF>''',184))
      
    def test_opr_05(self):
        self.assertTrue(TestLexer.checkLexeme('''--123''','''-,-,123,<EOF>''',185))
      
    def test_opr_06(self):
        self.assertTrue(TestLexer.checkLexeme('''$a + $b - $c * $d / $e % $f''','''$a,+,$b,-,$c,*,$d,/,$e,%,$f,<EOF>''',186))
      
    def test_opr_07(self):
        self.assertTrue(TestLexer.checkLexeme('''"abc" +. "123" ==. "abc" != "abc" !true = 123''','''abc,+.,123,==.,abc,!=,abc,!,true,=,123,<EOF>''',187))
      
    def test_opr_08(self):
        self.assertTrue(TestLexer.checkLexeme('''($a >= $b) || ($c <= $d) && ($e == $f);''','''(,$a,>=,$b,),||,(,$c,<=,$d,),&&,(,$e,==,$f,),;,<EOF>''',188))
      
    def test_array_01(self):
        self.assertTrue(TestLexer.checkLexeme('''$a[0.123 + 2 - 3.456];''','''$a,[,0.123,+,2,-,3.456,],;,<EOF>''',189))
      
    def test_array_02(self):
        self.assertTrue(TestLexer.checkLexeme('''$a[123 + _b(4) - _c[5] / $d["678"]];''','''$a,[,123,+,_b,(,4,),-,_c,[,5,],/,$d,[,678,],],;,<EOF>''',190))
      
    def test_array_03(self):
        self.assertTrue(TestLexer.checkLexeme('''$a[3 + _foo(2)] = $a[$b[2]["abc"]] + 4;''','''$a,[,3,+,_foo,(,2,),],=,$a,[,$b,[,2,],[,abc,],],+,4,;,<EOF>''',191))
      
    def test_array_04(self):
        self.assertTrue(TestLexer.checkLexeme('''array(1 , 1.234, 0.123, .0123e45, 1 - 2 + 3, abc == "123")''','''array,(,1,,,1.234,,,0.123,,,.0123e45,,,1,-,2,+,3,,,Error Token a''',192))
      
    def test_array_05(self):
        self.assertTrue(TestLexer.checkLexeme('''array(1 => "ab", "cd" => 2 + 3.4 * 5, "ef" => "fh")''','''array,(,1,=>,ab,,,cd,=>,2,+,3.4,*,5,,,ef,=>,fh,),<EOF>''',193))
      
    def test_array_06(self):
        self.assertTrue(TestLexer.checkLexeme('''array(array(1,2,3), array("ab", "bc", "de"), array(1 => "ab", "cd" => 2 + 3.4 * 5, "ef" => "fh"));''','''array,(,array,(,1,,,2,,,3,),,,array,(,ab,,,bc,,,de,),,,array,(,1,=>,ab,,,cd,=>,2,+,3.4,*,5,,,ef,=>,fh,),),;,<EOF>''',194))
      
    def test_array_07(self):
        self.assertTrue(TestLexer.checkLexeme('''123.132 + $x * array(1, 2, 3);''','''123.132,+,$x,*,array,(,1,,,2,,,3,),;,<EOF>''',195))
      
    def test_define_01(self):
        self.assertTrue(TestLexer.checkLexeme('''define(Abc, "abc")''','''define,(,Abc,,,abc,),<EOF>''',196))
      
    def test_function_02(self):
        self.assertTrue(TestLexer.checkLexeme('''function _abc(0, 1.2, -3e-45){}''','''function,_abc,(,0,,,1.2,,,-,3e-45,),{,},<EOF>''',197))
      
    def test_function_03(self):
        self.assertTrue(TestLexer.checkLexeme('''function _abc($a,$b,$c){}''','''function,_abc,(,$a,,,$b,,,$c,),{,},<EOF>''',198))
      
    def test_function_04(self):
        self.assertTrue(TestLexer.checkLexeme('''if ($a[12 + 5e12 - 4.4] == 10) { return _abc(123, $a); }''','''if,(,$a,[,12,+,5e12,-,4.4,],==,10,),{,return,_abc,(,123,,,$a,),;,},<EOF>''',199))
      
 