import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test_simple_program_00(self):
        input = """define(ABC, 10);"""
        expect = Program([ConstDecl(Id("ABC"),IntLit(10))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))
    
    def test_simple_program_01(self):
        input = """
        define(A, 1);
        define(B, "abc");   
        define(C, 123.123e-123);
        """
        expect = Program([ConstDecl(Id("A"),IntLit(1)),ConstDecl(Id("B"),StringLit("abc")),ConstDecl(Id("C"),FloatLit(1.23123e-121))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))
    
    def test_simple_program_02(self):
        input = """$x = 5;"""
        expect = Program([],[Assign(Id("$x"),IntLit(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))
    
    def test_simple_program_03(self):
        input = """
        $x = 1;
        $y = "abc";
        $x = 123.123e+123;
        """
        expect = Program([],[Assign(Id("$x"),IntLit(1)),Assign(Id("$y"),StringLit("abc")),Assign(Id("$x"),FloatLit(1.23123e+125))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))
    
    def test_simple_program_04(self):
        input = """
        define(ABC, 10);
        $x = 5;
        $y = 123.123e-123;
        """
        expect = Program([ConstDecl(Id("ABC"),IntLit(10))],[Assign(Id("$x"),IntLit(5)),Assign(Id("$y"),FloatLit(1.23123e-121))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))
    
    def test_simple_program_05(self):
        input = """$a = ((1 > 2) == (2 < 3)) != ((3 <= 4) >= 5);"""
        expect = Program([],[Assign(Id("$a"),BinExp("!=",BinExp("==",BinExp(">",IntLit(1),IntLit(2)),BinExp("<",IntLit(2),IntLit(3))),BinExp(">=",BinExp("<=",IntLit(3),IntLit(4)),IntLit(5))))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))
    
    def test_simple_program_06(self):
        input = """$a = ("a" || "b") && "c";"""
        expect = Program([],[Assign(Id("$a"),BinExp("&&",BinExp("||",StringLit("a"),StringLit("b")),StringLit("c")))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))
    
    def test_simple_program_07(self):
        input = """$a = "abc" +. "def";"""
        expect = Program([],[Assign(Id("$a"),BinExp("+.",StringLit("abc"),StringLit("def")))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))
    
    def test_simple_program_08(self):
        input = """$a = _abc();"""
        expect = Program([],[Assign(Id("$a"),Call(Id("_abc"),[]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))
    
    def test_simple_program_09(self):
        input = """define(A, 1 + 2 - 3 / 4 * 5);"""
        expect = Program([ConstDecl(Id("A"),BinExp("-",BinExp("+",IntLit(1),IntLit(2)),BinExp("*",BinExp("/",IntLit(3),IntLit(4)),IntLit(5))))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))
    
    def test_simple_program_10(self):
        input = """define(A, array(1, 2, 3));"""
        expect = Program([ConstDecl(Id("A"),ArrayLit([IntLit(1),IntLit(2),IntLit(3)]))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))
    
    def test_simple_program_11(self):
        input = """define(A, array($a, $b, $c));"""
        expect = Program([ConstDecl(Id("A"),ArrayLit([Id("$a"),Id("$b"),Id("$c")]))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))
    
    def test_simple_program_12(self):
        input = """define(A, array(1 => 123, 2 => $a + $b, "abc" => 123));"""
        expect = Program([ConstDecl(Id("A"),ArrayLit([AssocExp(IntLit(1),IntLit(123)),AssocExp(IntLit(2),BinExp("+",Id("$a"),Id("$b"))),AssocExp(StringLit("abc"),IntLit(123))]))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))
    
    def test_simple_program_13(self):
        input = """define(A, array(array(1,2,3), array("a","b","c"), array(1 => 123, 2 => $a + $b, "abc" => 123)));"""
        expect = Program([ConstDecl(Id("A"),ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([StringLit("a"),StringLit("b"),StringLit("c")]),ArrayLit([AssocExp(IntLit(1),IntLit(123)),AssocExp(IntLit(2),BinExp("+",Id("$a"),Id("$b"))),AssocExp(StringLit("abc"),IntLit(123))])]))],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))
    
    def test_simple_program_14(self):
        input = """
        define(ABC, 10);
        $x = 5;
        function _myfunc(){}
        """
        expect = Program([ConstDecl(Id("ABC"),IntLit(10))],[Assign(Id("$x"),IntLit(5)),FuncDecl(Id("_myfunc"),[],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))
    
    def test_simple_program_15(self):
        input = """
        define(ABC, 10);
        function _myfunc(){}
        $x = 5;
        """
        expect =Program([ConstDecl(Id("ABC"),IntLit(10))],[FuncDecl(Id("_myfunc"),[],[]),Assign(Id("$x"),IntLit(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))
    
    def test_simple_program_16(self):
        input = """
        define(ABC, 10);
        $x = 5;
        function _myfunc1(){}
        function _myfunc2(){}
        """
        expect = Program([ConstDecl(Id("ABC"),IntLit(10))],[Assign(Id("$x"),IntLit(5)),FuncDecl(Id("_myfunc1"),[],[]),FuncDecl(Id("_myfunc2"),[],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    
    def test_simple_program_17(self):
        input = """
        define(ABC, 10);
        function _myfunc1(){}
        $x = 5;
        function _myfunc2(){}
        """
        expect = Program([ConstDecl(Id("ABC"),IntLit(10))],[FuncDecl(Id("_myfunc1"),[],[]),Assign(Id("$x"),IntLit(5)),FuncDecl(Id("_myfunc2"),[],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))
    
    def test_simple_program_18(self):
        input = """
        define(ABC, 10);
        $x = 5;
        function _myfunc1(){}
        $x = 5;
        function _myfunc2(){}
        $x = 5;
        """
        expect = Program([ConstDecl(Id("ABC"),IntLit(10))],[Assign(Id("$x"),IntLit(5)),FuncDecl(Id("_myfunc1"),[],[]),Assign(Id("$x"),IntLit(5)),FuncDecl(Id("_myfunc2"),[],[]),Assign(Id("$x"),IntLit(5))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))
    
    def test_simple_program_19(self):
        input = """
        function _main($a, $b, $c){}
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b")),ParamDecl(Id("$c"))],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))
    
    def test_simple_program_20(self):
        input = """
        function _main($a, $b){
            $a = 1 + 2 - 3 * 4 / 5 % 6;
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),BinExp("-",BinExp("+",IntLit(1),IntLit(2)),BinExp("%",BinExp("/",BinExp("*",IntLit(3),IntLit(4)),IntLit(5)),IntLit(6))))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))
    
    def test_simple_program_21(self):
        input = """
        function _main($a, $b){
            $a = ((123.123 && 123.e-123) || (3 && 4)) / $a;
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),BinExp("/",BinExp("||",BinExp("&&",FloatLit(123.123),FloatLit(1.23e-121)),BinExp("&&",IntLit(3),IntLit(4))),Id("$a")))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))
    
    def test_simple_program_22(self):
        input = """
        function _main($a, $b){
            $a = !(-1 + 2 >= 3) != !true;
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),BinExp("!=",UnExp("!",BinExp(">=",BinExp("+",UnExp("-",IntLit(1)),IntLit(2)),IntLit(3))),UnExp("!",BoolLit(True))))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))
    
    def test_simple_program_23(self):
        input = """
        function _main($a, $b){
            $a = array(1, 2, 3);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([IntLit(1),IntLit(2),IntLit(3)]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))
    
    def test_simple_program_24(self):
        input = """
        function _main($a, $b){
            $a = array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    
    def test_simple_program_25(self):
        input = """
        function _main($a, $b){
            $a = array("abc", "def", "ghk");
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([StringLit("abc"),StringLit("def"),StringLit("ghk")]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))
    
    def test_simple_program_26(self):
        input = """
        function _main($a, $b){
            $a = array(1, 0.123, "ghk");
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([IntLit(1),FloatLit(0.123),StringLit("ghk")]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))
    
    def test_simple_program_27(self):
        input = """
        function _main($a, $b){
            $a = array($a, $b, $c);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([Id("$a"),Id("$b"),Id("$c")]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))
    
    def test_simple_program_28(self):
        input = """
        function _main($a, $b){
            $a = array();
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))
    
    def test_simple_program_29(self):
        input = """
        function _main($a, $b){
            $a = array(1);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([IntLit(1)]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
    
    def test_simple_program_30(self):
        input = """
        function _main($a, $b){
            $a = array(1 + 2 - 3);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    
    def test_simple_program_31(self):
        input = """
        function _main($a, $b){
            $a = array(1 => "abc", "15" => 15 + 16.1, "place" => "Yanxi");
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([AssocExp(IntLit(1),StringLit("abc")),AssocExp(StringLit(15),BinExp("+",IntLit(15),FloatLit(16.1))),AssocExp(StringLit("place"),StringLit("Yanxi"))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    
    def test_simple_program_32(self):
        input = """
        function _main($a, $b){
            $a = array(123 => 123.123e-123, "abc" => 15 + 16.1, 456 => "abc" + "def");
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([AssocExp(IntLit(123),FloatLit(1.23123e-121)),AssocExp(StringLit("abc"),BinExp("+",IntLit(15),FloatLit(16.1))),AssocExp(IntLit(456),BinExp("+",StringLit("abc"),StringLit("def")))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    
    def test_simple_program_33(self):
        input = """
        function _main($a, $b){
            $a = array(1 => _myfunc());
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([AssocExp(IntLit(1),Call(Id("_myfunc"),[]))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))
    
    def test_simple_program_34(self):
        input = """
        function _main($a, $b){
            $a = array(1 => $a[1][2][3]);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([AssocExp(IntLit(1),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2),IntLit(3)]))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))
    
    def test_simple_program_35(self):
        input = """
        function _main($a, $b){
            $a = array(1 => Abc123);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([AssocExp(IntLit(1),Id("Abc123"))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))
    
    def test_simple_program_36(self):
        input = """
        function _main($a, $b){
            $a = array(1 => $a + $b);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([AssocExp(IntLit(1),BinExp("+",Id("$a"),Id("$b")))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))
    
    def test_simple_program_37(self):
        input = """
        function _main($a, $b){
            $a = array(
                array(1, 2, 3), 
                array("abc", "def", "ghk"), 
                array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123),
                array(1 => "abc", "15" => 15 + 16.1, "place" => "Yanxi")
                );
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([StringLit("abc"),StringLit("def"),StringLit("ghk")]),ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)]),ArrayLit([AssocExp(IntLit(1),StringLit("abc")),AssocExp(StringLit(15),BinExp("+",IntLit(15),FloatLit(16.1))),AssocExp(StringLit("place"),StringLit("Yanxi"))])]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))
    
    def test_simple_program_38(self):
        input = """
        function _main($a, $b){
            $a = array(
                array(), 
                array()
                );
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([ArrayLit([]),ArrayLit([])]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))
    
    def test_simple_program_39(self):
        input = """
        function _main($a, $b){
            $a = array(
                array(1), 
                array("abc"), 
                array(-1.12_3),
                array(1 => "abc")
                );
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([ArrayLit([IntLit(1)]),ArrayLit([StringLit("abc")]),ArrayLit([UnExp("-",FloatLit(1.123))]),ArrayLit([AssocExp(IntLit(1),StringLit("abc"))])]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))
    
    def test_simple_program_40(self):
        input = """
        function _main($a, $b){
            $a = array(
                array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3)), 
                array(array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123), array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123), array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123))
                );
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayLit([ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([IntLit(1),IntLit(2),IntLit(3)])]),ArrayLit([ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)]),ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)]),ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)])])]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))
    
    def test_simple_program_41(self):
        input = """
        function _main($a, $b){
            $a = _myfunc();
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),Call(Id("_myfunc"),[]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))
    
    def test_simple_program_42(self):
        input = """
        function _main($a, $b){
            $a = _myfunc();
            $a = _myfunc(1);
            $a = _myfunc(1, 2);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),Call(Id("_myfunc"),[])),Assign(Id("$a"),Call(Id("_myfunc"),[IntLit(1)])),Assign(Id("$a"),Call(Id("_myfunc"),[IntLit(1),IntLit(2)]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))
    
    def test_simple_program_43(self):
        input = """
        function _main($a, $b){
            _myfunc();
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Call(Id("_myfunc"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    
    def test_simple_program_44(self):
        input = """
        function _main($a, $b){
            $a = _myfunc(1 + 2 - $a ==. "abc");
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),Call(Id("_myfunc"),[BinExp("==.",BinExp("-",BinExp("+",IntLit(1),IntLit(2)),Id("$a")),StringLit("abc"))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))
    
    def test_simple_program_45(self):
        input = """
        function _main($a, $b){
            $a = _myfunc1(_myfunc2(1) + _myfunc3($a));
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),Call(Id("_myfunc1"),[BinExp("+",Call(Id("_myfunc2"),[IntLit(1)]),Call(Id("_myfunc3"),[Id("$a")]))]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))
    
    def test_simple_program_46(self):
        input = """
        function _main($a, $b){
            $a = _myfunc1(123) + 2 - 3 * _myfunc1(_myfunc2(1) + _myfunc3($a));
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),BinExp("-",BinExp("+",Call(Id("_myfunc1"),[IntLit(123)]),IntLit(2)),BinExp("*",IntLit(3),Call(Id("_myfunc1"),[BinExp("+",Call(Id("_myfunc2"),[IntLit(1)]),Call(Id("_myfunc3"),[Id("$a")]))]))))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_simple_program_47(self):
        input = """
        function _main($a, $b){
            $a = $a[1][2];
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    
    def test_simple_program_48(self):
        input = """
        function _main($a, $b){
            $a = $a[1][2];
            $a = $a[1][2];
            $a = $a[1][2];
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)])),Assign(Id("$a"),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)])),Assign(Id("$a"),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))
    
    def test_simple_program_49(self):
        input = """
        function _main($a, $b){
            $a = $a[1][2] + $a[1][2];
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),BinExp("+",ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)])))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))
    
    def test_simple_program_50(self):
        input = """
        function _main($a, $b){
            $a = $a[$b[1][2]][$b[1][2]];
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayAccess(Id("$a"),[ArrayAccess(Id("$b"),[IntLit(1),IntLit(2)]),ArrayAccess(Id("$b"),[IntLit(1),IntLit(2)])]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_simple_program_51(self):
        input = """
        function _main($a, $b){
            $a = $a[1 + 2 - 3][_myfunc()]["abc"];
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$a"),ArrayAccess(Id("$a"),[BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3)),Call(Id("_myfunc"),[]),StringLit("abc")]))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_simple_program_52(self):
        input = """
        function _main($a, $b){
            $a[1][2] = 1 + 2 - 3;
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3)))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_simple_program_53(self):
        input = """
        function _main($a, $b){
            $a[1][2] = _main($a, $b) + $b[1 + 2 - 3][_myfunc()]["abc"] - 123.123e-123;
            $a[3 + _foo(2)] = $a[$b[2]["place"]] + 4;
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),BinExp("-",BinExp("+",Call(Id("_main"),[Id("$a"),Id("$b")]),ArrayAccess(Id("$b"),[BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3)),Call(Id("_myfunc"),[]),StringLit("abc")])),FloatLit(1.23123e-121))),Assign(ArrayAccess(Id("$a"),[BinExp("+",IntLit(3),Call(Id("_foo"),[IntLit(2)]))]),BinExp("+",ArrayAccess(Id("$a"),[ArrayAccess(Id("$b"),[IntLit(2),StringLit("place")])]),IntLit(4)))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_simple_program_54(self):
        input = """
        function _main($a, $b){
            if(true){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_simple_program_55(self):
        input = """
        function _main($a, $b){
            if(1){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(IntLit(1),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_simple_program_56(self):
        input = """
        function _main($a, $b){
            if(123.123e-123){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(FloatLit(1.23123e-121),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_simple_program_57(self):
        input = """
        function _main($a, $b){
            if(true){} elseif(true){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_simple_program_58(self):
        input = """
        function _main($a, $b){
            if(true){} else {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_simple_program_59(self):
        input = """
        function _main($a, $b){
            if(true){} else {}
            if(true){} elseif(true){}
            if(true){} else {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_simple_program_60(self):
        input = """
        function _main($a, $b){
            if(true){} elseif(true){} elseif(true){} elseif(true){} elseif(true){} else{}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[]),(BoolLit(True),[]),(BoolLit(True),[]),(BoolLit(True),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_simple_program_61(self):
        input = """
        function _main($a, $b){
            if(((1 + 2 - 3) > $a) || ("12" ==. "123")){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BinExp("||",BinExp(">",BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3)),Id("$a")),BinExp("==.",StringLit("12"),StringLit("123"))),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_simple_program_62(self):
        input = """
        function _main($a, $b){
            if($a[1][2]){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_simple_program_63(self):
        input = """
        function _main($a, $b){
            if(_myfunc(123)){}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(Call(Id("_myfunc"),[IntLit(123)]),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_simple_program_64(self):
        input = """
        function _main($a, $b){
            if(true){
                $a = 1 + 2 - 3;
                $b = "abc" +. "def";
                return 123;
            }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[Assign(Id("$a"),BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3))),Assign(Id("$b"),BinExp("+.",StringLit("abc"),StringLit("def"))),Return(IntLit(123))])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_simple_program_65(self):
        input = """
        function _main($a, $b){
            if(true){
                $a = 1;
            } elseif(true){
                $a = 1;
            } elseif(true){
                $a = 1;
            }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[Assign(Id("$a"),IntLit(1))]),(BoolLit(True),[Assign(Id("$a"),IntLit(1))])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_simple_program_66(self):
        input = """
        function _main($a, $b){
            if(true){
                $a = 1;
            } 
            elseif(true){
                $a = 1;
            } 
            elseif(true){
                $a = 1;
            }
            else {
                $a = 1;
            }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[Assign(Id("$a"),IntLit(1))]),(BoolLit(True),[Assign(Id("$a"),IntLit(1))])],[Assign(Id("$a"),IntLit(1))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_simple_program_67(self):
        input = """
        function _main($a, $b){
            foreach ($a as $key => $value) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[ForEach(Id("$a"),Id("$key"),Id("$value"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_simple_program_68(self):
        input = """
        function _main($a, $b){
            foreach ($a as $key => $value) {
                $key = 123;
                $value = "abc";
            }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[ForEach(Id("$a"),Id("$key"),Id("$value"),[Assign(Id("$key"),IntLit(123)),Assign(Id("$value"),StringLit("abc"))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_simple_program_69(self):
        input = """
        function _main($a, $b){
            foreach ($a as $key => $value) {
                $key = 123;
                $value = "abc";
                break;
                return 123;
                continue;
            }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[ForEach(Id("$a"),Id("$key"),Id("$value"),[Assign(Id("$key"),IntLit(123)),Assign(Id("$value"),StringLit("abc")),Break(),Return(IntLit(123)),Continue()])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_simple_program_70(self):
        input = """
        function _main($a, $b){
            while (true) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(BoolLit(True),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_simple_program_71(self):
        input = """
        function _main($a, $b){
            while ("true") {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(StringLit("true"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_simple_program_72(self):
        input = """
        function _main($a, $b){
            while (1) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(IntLit(1),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_simple_program_73(self):
        input = """
        function _main($a, $b){
            while (123.e+123) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(FloatLit(1.23e+125),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_simple_program_74(self):
        input = """
        function _main($a, $b){
            while (((1 + 2 - 3) > $a) || ("12" ==. "123")) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(BinExp("||",BinExp(">",BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3)),Id("$a")),BinExp("==.",StringLit("12"),StringLit("123"))),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_simple_program_75(self):
        input = """
        function _main($a, $b){
            while ($a[1][2] + _myfunc(123)) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(BinExp("+",ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),Call(Id("_myfunc"),[IntLit(123)])),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_simple_program_76(self):
        input = """function _main($a, $b){}"""
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_simple_program_77(self):
        input = """
        function _main($a, $b){
             while (true) {
                $a = 123;
                $b = "abc";
                break;
                continue;
                return false;
             }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(BoolLit(True),[Assign(Id("$a"),IntLit(123)),Assign(Id("$b"),StringLit("abc")),Break(),Continue(),Return(BoolLit(False))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_simple_program_78(self):
        input = """
        function _main($a, $b){
            _myfunc();
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Call(Id("_myfunc"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_simple_program_79(self):
        input = """
        function _main($a, $b){
            _myfunc(1 + 2 - 3);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Call(Id("_myfunc"),[BinExp("-",BinExp("+",IntLit(1),IntLit(2)),IntLit(3))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_simple_program_80(self):
        input = """
        function _main($a, $b){
            _myfunc(1, "abc", 123.123e+123);
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Call(Id("_myfunc"),[IntLit(1),StringLit("abc"),FloatLit(1.23123e+125)])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_simple_program_81(self):
        input = """
        function _main($a, $b){
            if(true){} else {}
            if(true){} elseif(true){}
            if(true){} else {}
            while (1) {}
            foreach ($a as $key => $value) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[]),While(IntLit(1),[]),ForEach(Id("$a"),Id("$key"),Id("$value"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_simple_program_82(self):
        input = """
        function _main($a, $b){
            if(true){} else {
                while (1) {}
                foreach ($a as $key => $value) {}
            }
            
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[While(IntLit(1),[]),ForEach(Id("$a"),Id("$key"),Id("$value"),[])])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_simple_program_83(self):
        input = """
        function _main($a, $b){
            while (1) {
                if(true){} else {}
                if(true){} elseif(true){}
                if(true){} else {}
            }
            foreach ($a as $key => $value) {}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[While(IntLit(1),[If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[])]),ForEach(Id("$a"),Id("$key"),Id("$value"),[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_simple_program_84(self):
        input = """
        function _main($a, $b){
            foreach ($a as $key => $value) {
                if(true){} else {}
                if(true){} elseif(true){}
                if(true){} else {}
                while (1) {}
            }
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[ForEach(Id("$a"),Id("$key"),Id("$value"),[If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[]),If([(BoolLit(True),[])],[]),While(IntLit(1),[])])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_simple_program_85(self):
        input = """
        function _main($a, $b){
            if(true){}elseif(true){ if(true){}elseif(true){ if(true){}elseif(true){}}}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BoolLit(True),[])],[])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_simple_program_86(self):
        input = """
        function _main($a, $b){
            foreach ($a as $key => $value) {foreach ($a as $key => $value) {foreach ($a as $key => $value) {foreach ($a as $key => $value) {}}}}
        }
        """
        expect = Program([],[FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[ForEach(Id("$a"),Id("$key"),Id("$value"),[ForEach(Id("$a"),Id("$key"),Id("$value"),[ForEach(Id("$a"),Id("$key"),Id("$value"),[ForEach(Id("$a"),Id("$key"),Id("$value"),[])])])])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_simple_program_87(self):
        input = """
        function _main(){
            if(true){ 
                $a = 123; 
                $a[1][2] = 123;
                _abc(123); 
            } 
            elseif (false) { 
                $a = 123; 
                $a[1][2] = 123; 
            } 
            elseif (false) { 
                $a = 123; 
                $a[1][2] = 123; 
            } 
            else { 
                break; 
            }
        }"""
        expect = Program([],[FuncDecl(Id("_main"),[],[If([(BoolLit(True),[Assign(Id("$a"),IntLit(123)),Assign(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),IntLit(123)),Call(Id("_abc"),[IntLit(123)])]),(BoolLit(False),[Assign(Id("$a"),IntLit(123)),Assign(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]),IntLit(123))])],[Break()])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_simple_program_88(self):
        input = """function _main(){while(true){ $a = 123; $b = 456; break; continue;}} """
        expect = Program([],[FuncDecl(Id("_main"),[],[While(BoolLit(True),[Assign(Id("$a"),IntLit(123)),Assign(Id("$b"),IntLit(456)),Break(),Continue()])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_simple_program_89(self):
        input =  """function _main(){foreach($a as $b => $c){ _echo((("abc" +. int2str($key)) +. "123") +. int2str(123)); }} """
        expect = Program([],[FuncDecl(Id("_main"),[],[ForEach(Id("$a"),Id("$b"),Id("$c"),[Call(Id("_echo"),[BinExp("+.",BinExp("+.",BinExp("+.",StringLit("abc"),UnExp("int2str",Id("$key"))),StringLit("123")),UnExp("int2str",IntLit(123)))])])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_simple_program_90(self):
        input = """
function _search($arr, $n, $x){
    $i = 0;
    while ($i < $n){
        if ($arr[$i] == $x){
            return $i;
        }   
    }
    return -1;
}
/* Driver code */
function _main()
{
    $arr = array(2, 3, 4, 10, 40);
    $x = 10;
    $n = 5;
    /* Function call */
    $result = _search($arr, $n, $x);
    if ($result == -1){
        _echo("Element is not present in array");
    }
    else{
        _echo("Element is present at index " +. int2str($result));
    }
    return 0;
}"""
        expect = Program([],[FuncDecl(Id("_search"),[ParamDecl(Id("$arr")),ParamDecl(Id("$n")),ParamDecl(Id("$x"))],[Assign(Id("$i"),IntLit(0)),While(BinExp("<",Id("$i"),Id("$n")),[If([(BinExp("==",ArrayAccess(Id("$arr"),[Id("$i")]),Id("$x")),[Return(Id("$i"))])],[])]),Return(UnExp("-",IntLit(1)))]),FuncDecl(Id("_main"),[],[Assign(Id("$arr"),ArrayLit([IntLit(2),IntLit(3),IntLit(4),IntLit(10),IntLit(40)])),Assign(Id("$x"),IntLit(10)),Assign(Id("$n"),IntLit(5)),Assign(Id("$result"),Call(Id("_search"),[Id("$arr"),Id("$n"),Id("$x")])),If([(BinExp("==",Id("$result"),UnExp("-",IntLit(1))),[Call(Id("_echo"),[StringLit("Element is not present in array")])])],[Call(Id("_echo"),[BinExp("+.",StringLit("Element is present at index "),UnExp("int2str",Id("$result")))])]),Return(IntLit(0))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_simple_program_91(self):
        input = """
function _swap($xp, $yp){
    $temp = $yp;
    $xp = $yp;
    $yp = $temp;
}
function _selectionSort($arr, $n){
    $i = 0;
    foreach ($arr as $key => $value){
        /* Find the minimum element in unsorted array */
        $min_idx = $i;
        $j = $i + 1;
        while ($j < $n){
            if ($key < $arr[$min_idx]){
                $min_idx = $j;
            }
        }
        /* Swap the found minimum element with the first element*/
        _swap($arr[$min_idx], $arr[$i]);
    }
}
function _main(){
    $arr = array(64, 25, 12, 22, 11);
    $n = 5;
    _selectionSort($arr, $n);
    _echo("Sorted array: ");
    _printArray($arr, $n);
    return 0;
}
"""
        expect = Program([],[FuncDecl(Id("_swap"),[ParamDecl(Id("$xp")),ParamDecl(Id("$yp"))],[Assign(Id("$temp"),Id("$yp")),Assign(Id("$xp"),Id("$yp")),Assign(Id("$yp"),Id("$temp"))]),FuncDecl(Id("_selectionSort"),[ParamDecl(Id("$arr")),ParamDecl(Id("$n"))],[Assign(Id("$i"),IntLit(0)),ForEach(Id("$arr"),Id("$key"),Id("$value"),[Assign(Id("$min_idx"),Id("$i")),Assign(Id("$j"),BinExp("+",Id("$i"),IntLit(1))),While(BinExp("<",Id("$j"),Id("$n")),[If([(BinExp("<",Id("$key"),ArrayAccess(Id("$arr"),[Id("$min_idx")])),[Assign(Id("$min_idx"),Id("$j"))])],[])]),Call(Id("_swap"),[ArrayAccess(Id("$arr"),[Id("$min_idx")]),ArrayAccess(Id("$arr"),[Id("$i")])])])]),FuncDecl(Id("_main"),[],[Assign(Id("$arr"),ArrayLit([IntLit(64),IntLit(25),IntLit(12),IntLit(22),IntLit(11)])),Assign(Id("$n"),IntLit(5)),Call(Id("_selectionSort"),[Id("$arr"),Id("$n")]),Call(Id("_echo"),[StringLit("Sorted array: ")]),Call(Id("_printArray"),[Id("$arr"),Id("$n")]),Return(IntLit(0))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_simple_program_92(self):
        input =  """
function _jumpSearch($arr, $x, $n){
    /* Finding block size to be jumped */
    $step = _sqrt($n);
    /* Finding the block where element is
    present (if it is present) */
    $prev = 0;
    while ($arr[_min($step, $n) - 1] < $x){
        $prev = $step;
        $step = $step + _sqrt($n);
        if ($prev >= $n){
            return -1;
        }
    }
    while ($arr[$prev] < $x){
        $prev = $prev + 1;
        if ($prev == _min($step, $n)){
            return -1;
        }
    }
    if ($arr[$prev] == $x){
        return $prev;
    }
    return -1;
}
"""
        expect = Program([],[FuncDecl(Id("_jumpSearch"),[ParamDecl(Id("$arr")),ParamDecl(Id("$x")),ParamDecl(Id("$n"))],[Assign(Id("$step"),Call(Id("_sqrt"),[Id("$n")])),Assign(Id("$prev"),IntLit(0)),While(BinExp("<",ArrayAccess(Id("$arr"),[BinExp("-",Call(Id("_min"),[Id("$step"),Id("$n")]),IntLit(1))]),Id("$x")),[Assign(Id("$prev"),Id("$step")),Assign(Id("$step"),BinExp("+",Id("$step"),Call(Id("_sqrt"),[Id("$n")]))),If([(BinExp(">=",Id("$prev"),Id("$n")),[Return(UnExp("-",IntLit(1)))])],[])]),While(BinExp("<",ArrayAccess(Id("$arr"),[Id("$prev")]),Id("$x")),[Assign(Id("$prev"),BinExp("+",Id("$prev"),IntLit(1))),If([(BinExp("==",Id("$prev"),Call(Id("_min"),[Id("$step"),Id("$n")])),[Return(UnExp("-",IntLit(1)))])],[])]),If([(BinExp("==",ArrayAccess(Id("$arr"),[Id("$prev")]),Id("$x")),[Return(Id("$prev"))])],[]),Return(UnExp("-",IntLit(1)))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_simple_program_93(self):
        input =  """
function _leftrotate($s, $d){
    _reverse(_begin($s), _begin($s) + $d);
    _reverse(_begin($s) + $d, _end($s));
    _reverse(_begin($s), _end($s));
}
/* In-place rotates s towards right by d */
function _rightrotate($s, $d){
   _leftrotate($s, _length($s) - $d);
}
"""
        expect = Program([],[FuncDecl(Id("_leftrotate"),[ParamDecl(Id("$s")),ParamDecl(Id("$d"))],[Call(Id("_reverse"),[Call(Id("_begin"),[Id("$s")]),BinExp("+",Call(Id("_begin"),[Id("$s")]),Id("$d"))]),Call(Id("_reverse"),[BinExp("+",Call(Id("_begin"),[Id("$s")]),Id("$d")),Call(Id("_end"),[Id("$s")])]),Call(Id("_reverse"),[Call(Id("_begin"),[Id("$s")]),Call(Id("_end"),[Id("$s")])])]),FuncDecl(Id("_rightrotate"),[ParamDecl(Id("$s")),ParamDecl(Id("$d"))],[Call(Id("_leftrotate"),[Id("$s"),BinExp("-",Call(Id("_length"),[Id("$s")]),Id("$d"))])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_simple_program_94(self):
        input = """
define(A, 10);
define(B, "Story of Yanxi Place");
function _foo($a, $b){
    $i = 0;
    while ($i < 5) {
        A[$i] = ($b + 1) * $a;
        $u = $i + 1;
        if ($a[$u] == 10) {
            return $b;
        }
        $i = $i + 1;
    }
    return B + ": Done";
}
"""
        expect = Program([ConstDecl(Id("A"),IntLit(10)),ConstDecl(Id("B"),StringLit("Story of Yanxi Place"))],[FuncDecl(Id("_foo"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$i"),IntLit(0)),While(BinExp("<",Id("$i"),IntLit(5)),[Assign(ArrayAccess(Id("A"),[Id("$i")]),BinExp("*",BinExp("+",Id("$b"),IntLit(1)),Id("$a"))),Assign(Id("$u"),BinExp("+",Id("$i"),IntLit(1))),If([(BinExp("==",ArrayAccess(Id("$a"),[Id("$u")]),IntLit(10)),[Return(Id("$b"))])],[]),Assign(Id("$i"),BinExp("+",Id("$i"),IntLit(1)))]),Return(BinExp("+",Id("B"),StringLit(": Done")))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_simple_program_95(self):
        input = """
/* Returns length of LCS for X[0..m-1], Y[0..n-1] */
function _lcs($X, $Y, $m, $n){
   if ($m == 0 || $n == 0){
       return 0;
   }
   if (X[$m - 1] == Y[$n - 1]){
       return 1 + _lcs(X, Y, $m - 1, $n - 1);
   }
   else{
       return _max(_lcs(X, Y, $m, $n - 1), _lcs($X, $Y, $m - 1, $n));
   }
}
/* Utility function to get max of 2 integers */
function _max($a, $b){
    if($a > $b){
        return $a;
    }
    return $b;
}
/* Driver program to test above function */
function _main(){
  $X = "AGGTAB";
  $Y = "GXTXAYB";
  $m = _strlen($X);
  $n = _strlen($Y);
  _echo(_lcs($X, $Y, $m, $n ));
  return 0;
}
"""
        expect = Program([],[FuncDecl(Id("_lcs"),[ParamDecl(Id("$X")),ParamDecl(Id("$Y")),ParamDecl(Id("$m")),ParamDecl(Id("$n"))],[If([(BinExp("==",BinExp("==",Id("$m"),BinExp("||",IntLit(0),Id("$n"))),IntLit(0)),[Return(IntLit(0))])],[]),If([(BinExp("==",ArrayAccess(Id("X"),[BinExp("-",Id("$m"),IntLit(1))]),ArrayAccess(Id("Y"),[BinExp("-",Id("$n"),IntLit(1))])),[Return(BinExp("+",IntLit(1),Call(Id("_lcs"),[Id("X"),Id("Y"),BinExp("-",Id("$m"),IntLit(1)),BinExp("-",Id("$n"),IntLit(1))])))])],[Return(Call(Id("_max"),[Call(Id("_lcs"),[Id("X"),Id("Y"),Id("$m"),BinExp("-",Id("$n"),IntLit(1))]),Call(Id("_lcs"),[Id("$X"),Id("$Y"),BinExp("-",Id("$m"),IntLit(1)),Id("$n")])]))])]),FuncDecl(Id("_max"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[If([(BinExp(">",Id("$a"),Id("$b")),[Return(Id("$a"))])],[]),Return(Id("$b"))]),FuncDecl(Id("_main"),[],[Assign(Id("$X"),StringLit("AGGTAB")),Assign(Id("$Y"),StringLit("GXTXAYB")),Assign(Id("$m"),Call(Id("_strlen"),[Id("$X")])),Assign(Id("$n"),Call(Id("_strlen"),[Id("$Y")])),Call(Id("_echo"),[Call(Id("_lcs"),[Id("$X"),Id("$Y"),Id("$m"),Id("$n")])]),Return(IntLit(0))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_simple_program_96(self):
        input = """
define(ABC, array(1,2,3));
function _lis($arr, $n, $max_ref){
    /* Base case */
    if ($n == 1){
        return 1;
    }
    /* 'max_ending_here' is length of LIS
    ending with arr[n-1] */
    $max_ending_here = 1;
    /* Recursively get all LIS ending with arr[0],
    arr[1] ... arr[n-2]. If arr[i-1] is smaller
    than arr[n-1], and max ending with arr[n-1]
    needs to be updated, then update it */
    $i = 1;
    while ($i < $n) {
        $res = _lis($arr, $i, $max_ref);
        if ($arr[$i - 1] < $arr[$n - 1] && $res + 1 > $max_ending_here){
            $max_ending_here = $res + 1;
        }
        $i = $i + 1;
    }
    /* Compare max_ending_here with the overall
    max. And update the overall max if needed*/
    if ($max_ref < $max_ending_here){
        $max_ref = $max_ending_here;
    }
    /* Return length of LIS ending with arr[n-1]*/
    return $max_ending_here;
}
"""
        expect = Program([ConstDecl(Id("ABC"),ArrayLit([IntLit(1),IntLit(2),IntLit(3)]))],[FuncDecl(Id("_lis"),[ParamDecl(Id("$arr")),ParamDecl(Id("$n")),ParamDecl(Id("$max_ref"))],[If([(BinExp("==",Id("$n"),IntLit(1)),[Return(IntLit(1))])],[]),Assign(Id("$max_ending_here"),IntLit(1)),Assign(Id("$i"),IntLit(1)),While(BinExp("<",Id("$i"),Id("$n")),[Assign(Id("$res"),Call(Id("_lis"),[Id("$arr"),Id("$i"),Id("$max_ref")])),If([(BinExp(">",BinExp("<",ArrayAccess(Id("$arr"),[BinExp("-",Id("$i"),IntLit(1))]),BinExp("&&",ArrayAccess(Id("$arr"),[BinExp("-",Id("$n"),IntLit(1))]),BinExp("+",Id("$res"),IntLit(1)))),Id("$max_ending_here")),[Assign(Id("$max_ending_here"),BinExp("+",Id("$res"),IntLit(1)))])],[]),Assign(Id("$i"),BinExp("+",Id("$i"),IntLit(1)))]),If([(BinExp("<",Id("$max_ref"),Id("$max_ending_here")),[Assign(Id("$max_ref"),Id("$max_ending_here"))])],[]),Return(Id("$max_ending_here"))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_simple_program_97(self):
        input =   input = """
function _infixToPostfix($exp){
    /* Create a stack of capacity
    equal to expression size */
    $stack = _createStack(_strlen($exp));
    if(!$stack){
        return -1 ;
    } /* See if stack was created successfully */
    $i = 0;
    $k = -1;
    while ($exp[$i]){
        /* If the scanned character is
        an operand, add it to output. */
        if (_isOperand($exp[$i])){
            $k = $k + 1;
            $exp[$k] = $exp[$i];
        }
        /* If the scanned character is an
        "(", push it to the stack. */
        elseif($exp[$i] == "("){
            _push($stack, $exp[$i]);
        }
        elseif($exp[$i] == ")"){
            while (!_isEmpty($stack) && _peek($stack) != "("){
                $k = $k + 1;
                $exp[$k] = _pop($stack);
            }
            if (!_isEmpty($stack) && _peek($stack) != "("){
                return -1; /* invalid expression */ 
            }      
            else {
                _pop($stack);
            }
        }
        else {
            while (!_isEmpty($stack) && _Prec($exp[$i]) < _Prec(_peek($stack)))
            {
                $k = $k + 1;
                $exp[$k] = _pop($stack);
            }
            _push($stack, $exp[$i]);
        }
 
    }
    while (!_isEmpty($stack))
    {
        $k = $k + 1;
        $exp[$k] = _pop($stack);
    }
    $k = $k + 1;
    $exp[$k] = "0";
    _echo($exp);
}
"""
        expect = Program([],[FuncDecl(Id("_infixToPostfix"),[ParamDecl(Id("$exp"))],[Assign(Id("$stack"),Call(Id("_createStack"),[Call(Id("_strlen"),[Id("$exp")])])),If([(UnExp("!",Id("$stack")),[Return(UnExp("-",IntLit(1)))])],[]),Assign(Id("$i"),IntLit(0)),Assign(Id("$k"),UnExp("-",IntLit(1))),While(ArrayAccess(Id("$exp"),[Id("$i")]),[If([(Call(Id("_isOperand"),[ArrayAccess(Id("$exp"),[Id("$i")])]),[Assign(Id("$k"),BinExp("+",Id("$k"),IntLit(1))),Assign(ArrayAccess(Id("$exp"),[Id("$k")]),ArrayAccess(Id("$exp"),[Id("$i")]))]),(BinExp("==",ArrayAccess(Id("$exp"),[Id("$i")]),StringLit("(")),[Call(Id("_push"),[Id("$stack"),ArrayAccess(Id("$exp"),[Id("$i")])])])],[While(BinExp("<",BinExp("&&",UnExp("!",Call(Id("_isEmpty"),[Id("$stack")])),Call(Id("_Prec"),[ArrayAccess(Id("$exp"),[Id("$i")])])),Call(Id("_Prec"),[Call(Id("_peek"),[Id("$stack")])])),[Assign(Id("$k"),BinExp("+",Id("$k"),IntLit(1))),Assign(ArrayAccess(Id("$exp"),[Id("$k")]),Call(Id("_pop"),[Id("$stack")]))]),Call(Id("_push"),[Id("$stack"),ArrayAccess(Id("$exp"),[Id("$i")])])])]),While(UnExp("!",Call(Id("_isEmpty"),[Id("$stack")])),[Assign(Id("$k"),BinExp("+",Id("$k"),IntLit(1))),Assign(ArrayAccess(Id("$exp"),[Id("$k")]),Call(Id("_pop"),[Id("$stack")]))]),Assign(Id("$k"),BinExp("+",Id("$k"),IntLit(1))),Assign(ArrayAccess(Id("$exp"),[Id("$k")]),StringLit("0")),Call(Id("_echo"),[Id("$exp")])])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_simple_program_98(self):
        input = """
        define(Abc, 10);
        $x = 5;
        function _myfunc(){
            return "abc";
        }
        $y = 5;
       function _main($a, $b){
           $z = 123;
            if($a == 2){
                $a = $a + $b - 2 * $a;
                return $a;
            } elseif($b + 3 > 2){
                $x = "123";
            } elseif($b + 3 > 2){
                $y = "123";
            } else{
                $z = "123";
            }
            while(true){
                $a = $a + 1;
                $b = $b - 1;
                $c = $c * 1;
                $d = $d / 1;
                continue;
            }
            $a = array(1, 2, 3);
            $b = array("abc", "def", "ghk");
            $c = array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123);
            $d = array(1 => "abc", "15" => 15 + 16.1, "place" => "Yanxi");
            $e = array(
                array(1, 2, 3), 
                array("abc", "def", "ghk"), 
                array(-1.12_3, 0.01_23, 1_23.12_3e-12_3, 123.e123),
                array(1 => "abc", "15" => 15 + 16.1, "place" => "Yanxi")
                );
            $d = "123";
            foreach($e as $key => $value){
                $key = $value + 10;
                _echo((("Element " +. int2str($key)) +. ": ") +. int2str($value));
                break;
            }
            $e = $d +. "abc" - _foo(2 + $x, 4 / $y);
            $f = str2int(123) + int2str($b) - str2float($c + "123") - float2str(123.123e123) / str2bool("true") - bool2str(true);
            return 12 + _myfunc($e + $a[1][2]) - $d;
        }
        """
        expect = Program([ConstDecl(Id("Abc"),IntLit(10))],[Assign(Id("$x"),IntLit(5)),FuncDecl(Id("_myfunc"),[],[Return(StringLit("abc"))]),Assign(Id("$y"),IntLit(5)),FuncDecl(Id("_main"),[ParamDecl(Id("$a")),ParamDecl(Id("$b"))],[Assign(Id("$z"),IntLit(123)),If([(BinExp("==",Id("$a"),IntLit(2)),[Assign(Id("$a"),BinExp("-",BinExp("+",Id("$a"),Id("$b")),BinExp("*",IntLit(2),Id("$a")))),Return(Id("$a"))]),(BinExp(">",BinExp("+",Id("$b"),IntLit(3)),IntLit(2)),[Assign(Id("$x"),StringLit("123"))])],[Assign(Id("$z"),StringLit("123"))]),While(BoolLit(True),[Assign(Id("$a"),BinExp("+",Id("$a"),IntLit(1))),Assign(Id("$b"),BinExp("-",Id("$b"),IntLit(1))),Assign(Id("$c"),BinExp("*",Id("$c"),IntLit(1))),Assign(Id("$d"),BinExp("/",Id("$d"),IntLit(1))),Continue()]),Assign(Id("$a"),ArrayLit([IntLit(1),IntLit(2),IntLit(3)])),Assign(Id("$b"),ArrayLit([StringLit("abc"),StringLit("def"),StringLit("ghk")])),Assign(Id('$c'),ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)])),Assign(Id("$d"),ArrayLit([AssocExp(IntLit(1),StringLit("abc")),AssocExp(StringLit("15"),BinExp("+",IntLit(15),FloatLit(16.1))),AssocExp(StringLit("place"),StringLit("Yanxi"))])),Assign(Id("$e"),ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([StringLit("abc"),StringLit("def"),StringLit("ghk")]),ArrayLit([UnExp("-",FloatLit(1.123)),FloatLit(0.0123),FloatLit(1.23123e-121),FloatLit(1.23e+125)]),ArrayLit([AssocExp(IntLit(1),StringLit("abc")),AssocExp(StringLit(15),BinExp("+",IntLit(15),FloatLit(16.1))),AssocExp(StringLit("place"),StringLit("Yanxi"))])])),Assign(Id("$d"),StringLit("123")),ForEach(Id("$e"),Id("$key"),Id("$value"),[Assign(Id("$key"),BinExp("+",Id("$value"),IntLit(10))),Call(Id("_echo"),[BinExp("+.",BinExp("+.",BinExp("+.",StringLit("Element "),UnExp("int2str",Id("$key"))),StringLit(": ")),UnExp("int2str",Id("$value")))]),Break()]),Assign(Id("$e"),BinExp("+.",Id("$d"),BinExp("-",StringLit("abc"),Call(Id("_foo"),[BinExp("+",IntLit(2),Id("$x")),BinExp("/",IntLit(4),Id("$y"))])))),Assign(Id("$f"),BinExp("-",BinExp("-",BinExp("-",BinExp("+",UnExp("str2int",IntLit(123)),UnExp("int2str",Id("$b"))),UnExp("str2float",BinExp("+",Id("$c"),StringLit(123)))),BinExp("/",UnExp("float2str",FloatLit(1.23123e+125)),UnExp("str2bool",StringLit("true")))),UnExp("bool2str",BoolLit(True)))),Return(BinExp("-",BinExp("+",IntLit(12),Call(Id("_myfunc"),[BinExp("+",Id("$e"),ArrayAccess(Id("$a"),[IntLit(1),IntLit(2)]))])),Id("$d")))])])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_simple_program_99(self):
        input = """"""
        expect = Program([],[])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))