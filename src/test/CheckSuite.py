import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *
from main.d95.checker.StaticError import NoEntryPoint

class CheckSuite(unittest.TestCase):

    # def test_00(self):
    #     input = """
    #     define(A, 1);
    #     define(A, 2);
    #     """
    #     expect = str(Redeclared(Const(), "A"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,400))

    # def test_01(self):
    #     input = """
    #     function _main($a, $a){
    #     }
    #     """
    #     expect = str(Redeclared(Param(), "$a"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,401))

    # def test_02(self):
    #     input = """
    #     function _abc($a){
    #     }
    #     function _abc($b){
    #     }
    #     """
    #     expect = str(Redeclared(Func(), "_abc"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,402))

    # def test_03(self):
    #     input = """
    #     function _main(){
    #         $a = $b;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$b"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,403))

    # def test_04(self):
    #     input = """
    #     function _main(){
    #         $a = A;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("A"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,404))

    # def test_05(self):
    #     input = """
    #     function _main(){
    #         $a = _foo();
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("_foo"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,405))

    # def test_06(self):
    #     input = """"""
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.checkStatic(input,expect,406))

    # def test_07(self):
    #     input = """
    #     define(A, 123);
    #     $a = 123;
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.checkStatic(input,expect,407))

    # def test_08(self):
    #     input = """
    #     function _main($a){
    #         $c = $a;
    #     }
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id("$c"), Id("$a"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,408))

    # def test_09(self):
    #     input = """
    #     function _foo($a){
    #         return 1;
    #     }
    #     function _main($a){
    #         _foo($a);
    #     }
    #     """
    #     expect = str(TypeCannotBeInferred(Call(Id("_foo"),[Id("$a")])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,409))

    # def test_10(self):
    #     input = """
    #     function _foo($a){
    #         return 1;
    #     }
    #     function _main($b){
    #         $b = _foo($b) + 1;
    #     }
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id("$b"),BinExp("+",Call(Id("_foo"),[Id("$b")]),IntLit(1)))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,410))

    # def test_11(self):
    #     input = """
    #     function _foo($a){
    #     }
    #     function _main($b){
    #         _foo(1, 2);
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Call(Id("_foo"),[IntLit(1), IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,411))

    # def test_12(self):
    #     input = """
    #     function _foo($a){
    #         $a = 1;
    #     }
    #     function _main($b){
    #         _foo("abc");
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Call(Id("_foo"),[StringLit("abc")])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,412))

    # def test_13(self):
    #     input = """
    #     function _main(){
    #         if(1){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(IntLit(1),[Return(IntLit(1))])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,413))

    # def test_14(self):
    #     input = """
    #     function _main(){
    #         if("abc"){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(StringLit("abc"),[Return(IntLit(1))])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,414))

    # def test_15(self):
    #     input = """
    #     function _main(){
    #         while(1){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(While(IntLit(1),[Return(IntLit(1))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,415))

    # def test_16(self):
    #     input = """
    #     function _main(){
    #         while("abc"){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(While(StringLit("abc"),[Return(IntLit(1))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,416))

    # def test_17(self):
    #     input = """
    #     function _foo(){
    #         $a = 1;
    #     }
    #     function _main(){
    #         $b = _foo() + 1;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",Call(Id("_foo"),[]),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,417))

    # def test_18(self):
    #     input = """
    #     function _main(){
    #         $a = 1 + 2 + "123";
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",BinExp("+",IntLit(1),IntLit(2)),StringLit("123"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,418))

    # def test_19(self):
    #     input = """
    #     function _main(){
    #         $a = "abc" +. "123" - 1;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("-",StringLit("123"),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,419))

    # def test_20(self):
    #     input = """
    #     function _main(){
    #         $a = 123 == "abc";
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("==",IntLit(123),StringLit("abc"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,420))

    # def test_21(self):
    #     input = """
    #     define(A, array(1, 2, 3));
    #     function _main(){
    #         $a = A[1][2];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[IntLit(1),IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,421))

    # def test_22(self):
    #     input = """
    #     define(A, array(1 => "a", 2 => "b", 3 => "c"));
    #     function _main(){
    #         $a = A["1"];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[StringLit("1")])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,422))

    # def test_23(self):
    #     input = """
    #     define(A, array(array(1, 2 ,3), array(1, 2 ,3), array(1, 2 ,3)));
    #     function _main(){
    #         $a = A[1][1][1];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[IntLit(1),IntLit(1),IntLit(1)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,423))

    # def test_24(self):
    #     input = """
    #     $a = array(1, "123", 2);
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([IntLit(1),StringLit("123"),IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,424))

    # def test_25(self):
    #     input = """
    #     $a = array(1 => "a", 2 => 123);
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([AssocExp(IntLit(1),StringLit("a")),AssocExp(IntLit(2),IntLit(123))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,425))

    # def test_26(self):
    #     input = """
    #     $a = array(array(1, 2 ,3), 123);
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),IntLit(123)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,426))

    # def test_27(self):
    #     input = """
    #     $a = array(array(1, 2 ,3), array(1.123, 2.12312 ,3.12e-123));
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([FloatLit(1.123),FloatLit(2.12312),FloatLit(3.12e-123)])])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,427))

    # def test_28(self):
    #     input = """
    #     $a = array(array(1, 2 ,3), array("1", "2", "3"));
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([StringLit("1"),StringLit("2"),StringLit("3")])])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,428))

    # def test_29(self):
    #     input = """
    #     $a = $b + 1;
    #     """
    #     expect = str(UndeclaredIdentifier("$b"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,429))

    # def test_30(self):
    #     input = """
    #     define(A, "123");
    #     $a = A + 1;
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",Id("A"),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,430))

    # def test_31(self):
    #     input = """
    #     define(A, "123.123e-123");
    #     $a = A +. 1;
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+.",Id("A"),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,431))

    # def test_32(self):
    #     input = """
    #     define(A, "123.123e-123");
    #     $a = A ==. "1";
    #     $a = "false";
    #     """
    #     expect = str(TypeMismatchInStmt(Assign(Id("$a"),StringLit("false"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,432))

    # def test_33(self):
    #     input = """
    #     define(A, "123.123e-123");
    #     $a = A ==. "1" || true && 3 + 1;
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("||",StringLit("1"),BoolLit(True))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,433))

    # def test_34(self):
    #     input = """
    #     function _func($a, $b){
    #         return 1;
    #     }
    #     $a = "123";
    #     function _main(){
    #         $a = _func(1, 2);
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Assign(Id("$a"),Call(Id("_func"),[IntLit(1),IntLit(2)]))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,434))

    # def test_35(self):
    #     input = """
    #     function _func($a, $b){
    #         return 1;
    #     }
    #     $a = array("1", "2", "3");
    #     function _main(){
    #         $a[1] = _func(1, 2);
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(Assign(ArrayAccess(Id("$a"),[IntLit(1)]),Call(Id("_func"),[IntLit(1),IntLit(2)]))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,435))

    # def test_36(self):
    #     input = """
    #     function _main(){
    #         if(1 + 2){
    #             _echo(123);
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(BinExp("+",IntLit(1),IntLit(2)),[Call(Id("_echo"),[IntLit(123)])])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,436))

    # def test_37(self):
    #     input = """
    #     function _func(){
    #         return 1;
    #     }
    #     function _main(){
    #         if(_func()){
    #             _echo(123);
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(Call(Id("_func"),[]),[Call(Id("_echo"),[IntLit(123)])])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,437))

    # def test_38(self):
    #     input = """
    #     function _func(){
    #         $a = array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3));
    #         $b = 2 + $a[1];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$a"),[IntLit(1)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,438))

    # def test_39(self):
    #     input = """
    #     function _func(){
    #         $a = array(array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3)), array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3)));
    #         $b = 2 + $a[1][2][3][4];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,439))

    # def test_40(self):
    #     input = """
    #     function _func($a, $b){
    #         return $a + $b;
    #     }
    #     function _main(){
    #         $c = _func(1, 2) + 1;
    #         $d = $e + 1;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$e"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,440))

    # def test_41(self):
    #     input = """
    #     function _main(){
    #         $a = array("1", "2", "3");
    #         foreach($a as $key => $value){
    #             $b = $key + $value;
    #         }
    #         $a = $e;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",Id("$key"),Id("$value"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,441))

    # def test_42(self):
    #     input = """
    #     function _main(){
    #         $a = array(1, 2, 3);
    #         $b = "123";
    #         foreach($a as $b => $c){
    #             $b = $b + $c;
    #         }
    #         $a = $e;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$e"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,442))
        
    # def test_43(self):
    #     input = """
    #     function _main(){
    #         $a = array(1, 2, 3);
    #         $d = 123;
    #         foreach($a as $b => $c){
    #             $d = "123";
    #         }
            
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Assign(Id("$d"),StringLit("123"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,443))
        
    # def test_44(self):
    #     input = """
    #     function _main(){
    #         $a = array("1", "2", "3");
    #         foreach($a as $b => $c){
    #             $d = "123" +. $b;
    #         }
    #         $c = $e;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+.",StringLit("123"),Id("$b"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,444))
        
    # def test_45(self):
    #     input = """
    #     function _main(){
    #         $a = array("1", "2", "3");
    #         foreach($a as $b => $c){
    #             $d = "123" +. $c;
    #         }
    #         $c = $e;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$e"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,445))
        
    # def test_46(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => 1, "2" => 2, "3" => 3);
    #         $a[1] = 2;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$a"),[IntLit(1)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,446))
        
    # def test_47(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => 1, "2" => "2", "3" => 3);
    #     }
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([AssocExp(StringLit("1"),IntLit(1)),AssocExp(StringLit("2"),StringLit("2")),AssocExp(StringLit("3"),IntLit(3))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,447))
        
    # def test_48(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => 1.123, "2" => 2, "3" => 3);
    #     }
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([AssocExp(StringLit(1),FloatLit(1.123)),AssocExp(StringLit(2),IntLit(2)),AssocExp(StringLit(3),IntLit(3))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,448))
        
    # def test_49(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => array(1,2,3), "2" => array(1,2,3), "3" => array(1,2,3));
    #         foreach($a as $key => $value){
    #             $e = $f;
    #         }
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$f"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,449))
        
    # def test_50(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => array(1,2,3), "2" => array(1,2,3), "3" => array(1,2,3));
    #         foreach($a as $key => $value){
    #             $b = $value[1] + 1;
    #         }
    #     }
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.checkStatic(input,expect,450))
        
    # def test_51(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => array(1,2,3), "2" => array(1,2,3), "3" => array(1,2,3));
    #         foreach($a as $key => $value){
    #             $b = $value[1][2] + 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$value"),[IntLit(1),IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,451))
        
    # def test_52(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => array(1,2,3), "2" => array(1,2,3), "3" => array(1,2,3));
    #         foreach($a as $key => $value){
    #             $b = $value[1] +. "123";
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+.",ArrayAccess(Id("$value"),[IntLit(1)]),StringLit("123"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,452))

    # def test_53(self):
    #     input = """
    #     define(A, 1);
    #     define(A, 2);
    #     """
    #     expect = str(Redeclared(Const(), "A"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,453))

    # def test_54(self):
    #     input = """
    #     function _main($a, $a){
    #     }
    #     """
    #     expect = str(Redeclared(Param(), "$a"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,454))

    # def test_55(self):
    #     input = """
    #     function _abc($a){
    #     }
    #     function _abc($b){
    #     }
    #     """
    #     expect = str(Redeclared(Func(), "_abc"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,455))

    # def test_56(self):
    #     input = """
    #     function _main(){
    #         $a = $b;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$b"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,456))

    # def test_57(self):
    #     input = """
    #     function _main(){
    #         $a = A;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("A"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,457))

    # def test_58(self):
    #     input = """
    #     function _main(){
    #         $a = _foo();
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("_foo"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,458))

    # def test_59(self):
    #     input = """"""
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.checkStatic(input,expect,459))

    # def test_60(self):
    #     input = """
    #     define(A, 123);
    #     $a = 123;
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.checkStatic(input,expect,460))

    # def test_61(self):
    #     input = """
    #     function _main($a){
    #         $c = $a;
    #     }
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id("$c"), Id("$a"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,461))

    # def test_62(self):
    #     input = """
    #     function _foo($a){
    #         return 1;
    #     }
    #     function _main($a){
    #         _foo($a);
    #     }
    #     """
    #     expect = str(TypeCannotBeInferred(Call(Id("_foo"),[Id("$a")])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,462))

    # def test_63(self):
    #     input = """
    #     function _foo($a){
    #         return 1;
    #     }
    #     function _main($b){
    #         $b = _foo($b) + 1;
    #     }
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(Id("$b"),BinExp("+",Call(Id("_foo"),[Id("$b")]),IntLit(1)))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,463))

    # def test_64(self):
    #     input = """
    #     function _foo($a){
    #     }
    #     function _main($b){
    #         _foo(1, 2);
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Call(Id("_foo"),[IntLit(1), IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,464))

    # def test_65(self):
    #     input = """
    #     function _foo($a){
    #         $a = 1;
    #     }
    #     function _main($b){
    #         _foo("abc");
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Call(Id("_foo"),[StringLit("abc")])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,465))

    # def test_66(self):
    #     input = """
    #     function _main(){
    #         if(1){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(IntLit(1),[Return(IntLit(1))])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,466))

    # def test_67(self):
    #     input = """
    #     function _main(){
    #         if("abc"){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(StringLit("abc"),[Return(IntLit(1))])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,467))

    # def test_68(self):
    #     input = """
    #     function _main(){
    #         while(1){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(While(IntLit(1),[Return(IntLit(1))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,468))

    # def test_69(self):
    #     input = """
    #     function _main(){
    #         while("abc"){
    #             return 1;
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(While(StringLit("abc"),[Return(IntLit(1))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,469))

    # def test_70(self):
    #     input = """
    #     function _foo(){
    #         $a = 1;
    #     }
    #     function _main(){
    #         $b = _foo() + 1;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",Call(Id("_foo"),[]),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,470))

    # def test_71(self):
    #     input = """
    #     function _main(){
    #         $a = 1 + 2 + "123";
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",BinExp("+",IntLit(1),IntLit(2)),StringLit("123"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,471))

    # def test_72(self):
    #     input = """
    #     function _main(){
    #         $a = "abc" +. "123" - 1;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("-",StringLit("123"),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,472))

    # def test_73(self):
    #     input = """
    #     function _main(){
    #         $a = 123 == "abc";
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("==",IntLit(123),StringLit("abc"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,473))

    # def test_74(self):
    #     input = """
    #     define(A, array(1, 2, 3));
    #     function _main(){
    #         $a = A[1][2];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[IntLit(1),IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,474))

    # def test_75(self):
    #     input = """
    #     define(A, array(1 => "a", 2 => "b", 3 => "c"));
    #     function _main(){
    #         $a = A["1"];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[StringLit("1")])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,475))

    # def test_76(self):
    #     input = """
    #     define(A, array(array(1, 2 ,3), array(1, 2 ,3), array(1, 2 ,3)));
    #     function _main(){
    #         $a = A[1][1][1];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("A"),[IntLit(1),IntLit(1),IntLit(1)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,476))

    # def test_77(self):
    #     input = """
    #     $a = array(1, "123", 2);
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([IntLit(1),StringLit("123"),IntLit(2)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,477))

    # def test_78(self):
    #     input = """
    #     $a = array(1 => "a", 2 => 123);
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([AssocExp(IntLit(1),StringLit("a")),AssocExp(IntLit(2),IntLit(123))])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,478))

    # def test_79(self):
    #     input = """
    #     $a = array(array(1, 2 ,3), 123);
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),IntLit(123)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,479))

    # def test_80(self):
    #     input = """
    #     $a = array(array(1, 2 ,3), array(1.123, 2.12312 ,3.12e-123));
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([FloatLit(1.123),FloatLit(2.12312),FloatLit(3.12e-123)])])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,480))

    # def test_81(self):
    #     input = """
    #     $a = array(array(1, 2 ,3), array("1", "2", "3"));
    #     """
    #     expect = str(InvalidArrayLiteral(ArrayLit([ArrayLit([IntLit(1),IntLit(2),IntLit(3)]),ArrayLit([StringLit("1"),StringLit("2"),StringLit("3")])])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,481))

    # def test_82(self):
    #     input = """
    #     $a = $b + 1;
    #     """
    #     expect = str(UndeclaredIdentifier("$b"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,482))

    # def test_83(self):
    #     input = """
    #     define(A, "123");
    #     $a = A + 1;
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",Id("A"),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,483))

    # def test_84(self):
    #     input = """
    #     define(A, "123.123e-123");
    #     $a = A +. 1;
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+.",Id("A"),IntLit(1))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,484))

    # def test_85(self):
    #     input = """
    #     define(A, "123.123e-123");
    #     $a = A ==. "1";
    #     $a = "false";
    #     """
    #     expect = str(TypeMismatchInStmt(Assign(Id("$a"),StringLit("false"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,485))

    # def test_86(self):
    #     input = """
    #     define(A, "123.123e-123");
    #     $a = A ==. "1" || true && 3 + 1;
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("||",StringLit("1"),BoolLit(True))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,486))

    # def test_87(self):
    #     input = """
    #     function _func($a, $b){
    #         return 1;
    #     }
    #     $a = "123";
    #     function _main(){
    #         $a = _func(1, 2);
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Assign(Id("$a"),Call(Id("_func"),[IntLit(1),IntLit(2)]))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,487))

    # def test_88(self):
    #     input = """
    #     function _main(){
    #         if(1 + 2){
    #             _echo(123);
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(BinExp("+",IntLit(1),IntLit(2)),[Call(Id("_echo"),[IntLit(123)])])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,488))

    # def test_89(self):
    #     input = """
    #     function _func(){
    #         return 1;
    #     }
    #     function _main(){
    #         if(_func()){
    #             _echo(123);
    #         }
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(If([(Call(Id("_func"),[]),[Call(Id("_echo"),[IntLit(123)])])],[])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,489))

    # def test_90(self):
    #     input = """
    #     function _func(){
    #         $a = array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3));
    #         $b = 2 + $a[1];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$a"),[IntLit(1)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,490))

    # def test_91(self):
    #     input = """
    #     function _func(){
    #         $a = array(array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3)), array(array(1, 2, 3), array(1, 2, 3), array(1, 2, 3)));
    #         $b = 2 + $a[1][2][3][4];
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$a"),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,491))

    # def test_92(self):
    #     input = """
    #     function _func($a, $b){
    #         return $a + $b;
    #     }
    #     function _main(){
    #         $c = _func(1, 2) + 1;
    #         $d = $e + 1;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$e"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,492))

    # def test_93(self):
    #     input = """
    #     function _main(){
    #         $a = array("1", "2", "3");
    #         foreach($a as $key => $value){
    #             $b = $key + $value;
    #         }
    #         $a = $e;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+",Id("$key"),Id("$value"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,493))

    # def test_94(self):
    #     input = """
    #     function _main(){
    #         $a = array(1, 2, 3);
    #         $b = "123";
    #         foreach($a as $b => $c){
    #             $b = $b + $c;
    #         }
    #         $a = $e;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$e"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,494))
        
    # def test_95(self):
    #     input = """
    #     function _main(){
    #         $a = array(1, 2, 3);
    #         $d = 123;
    #         foreach($a as $b => $c){
    #             $d = "123";
    #         }
            
    #     }
    #     """
    #     expect = str(TypeMismatchInStmt(Assign(Id("$d"),StringLit("123"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,495))
        
    # def test_96(self):
    #     input = """
    #     function _main(){
    #         $a = array("1", "2", "3");
    #         foreach($a as $b => $c){
    #             $d = "123" +. $b;
    #         }
    #         $c = $e;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(BinExp("+.",StringLit("123"),Id("$b"))))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,496))
        
    # def test_97(self):
    #     input = """
    #     function _main(){
    #         $a = array("1", "2", "3");
    #         foreach($a as $b => $c){
    #             $d = "123" +. $c;
    #         }
    #         $c = $e;
    #     }
    #     """
    #     expect = str(UndeclaredIdentifier("$e"))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,497))
        
    # def test_98(self):
    #     input = """
    #     function _foo(){
    #         $a = array("1" => 1, "2" => 2, "3" => 3);
    #         $a[1] = 2;
    #     }
    #     """
    #     expect = str(TypeMismatchInExpr(ArrayAccess(Id("$a"),[IntLit(1)])))
    #     self.assertTrue(TestChecker.checkStatic(input,expect,498))
        
    def test_99(self):
        input = """
        function _foo($b){
            $a = array(1,2,3);
            $b = $a;
        }
        function _main(){
            $c = array(1,2,3);
            _foo($c);
        }
        """
        expect = str(InvalidArrayLiteral(ArrayLit([AssocExp(StringLit("1"),IntLit(1)),AssocExp(StringLit("2"),StringLit("2")),AssocExp(StringLit("3"),IntLit(3))])))
        self.assertTrue(TestChecker.checkStatic(input,expect,499))