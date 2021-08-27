import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_assign_stmt_01(self):
        input = """function _main(){ $a = 123; }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))

    def test_assign_stmt_02(self):
        input = """function _main(){ A = 123; }"""
        expect = "Error on line 1 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_assign_stmt_03(self):
        input = """function _main(){123 = 123;}"""
        expect = "Error on line 1 col 17: 123"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_assign_stmt_04(self):
        input = """function _main(){ _$a = 123; }"""
        expect = "Error on line 1 col 19: $a"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_assign_stmt_05(self):
        input = """function _main(){ $a + $b = 123; }"""
        expect = "Error on line 1 col 21: +"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_assign_stmt_06(self):
        input = """$a = 1_23;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_assign_stmt_07(self):
        input = """function _main(){ $a = $b = 123; }"""
        expect = "Error on line 1 col 26: ="
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_assign_stmt_08(self):
        input = """$a = $b;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_assign_stmt_09(self):
        input = """$a = (1 + 2) / (3 - 4);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_assign_stmt_10(self):
        input = """$a = "abc" ==. "123";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_assign_stmt_11(self):
        input = """$a = "abc" +. "def";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_assign_stmt_12(self):
        input = """$a = ("a" || "b") && "c";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_assign_stmt_13(self):
        input = """$a = !(true == !false);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_assign_stmt_14(self):
        input = """$a = ((1 > 2) == (2 < 3)) != ((3 <= 4) >= 5);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_assign_stmt_15(self):
        input = """function _main(){ $a[1][2] = 123;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_assign_stmt_16(self):
        input = """function _main(){$a = $b[1][2];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_assign_stmt_17(self):
        input = """function _main(){$a = $b[1] [2];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_assign_stmt_18(self):
        input = """function _main(){$a = $b[1.23];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_assign_stmt_19(self):
        input = """function _main(){$a = $b["abc"][12_3];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_assign_stmt_20(self):
        input = """function _main(){$a = $b[12 + 3 - 1];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_assign_stmt_21(self):
        input = """function _main(){$a = $b[str2int("123")];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_assign_stmt_22(self):
        input = """function _main(){$a = $b[$c[123]];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_assign_stmt_23(self):
        input = """function _main(){$a = $b[_abc(123) + _def(123)];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_assign_stmt_24(self):
        input = """function _main(){$a = $b[_abc(123) + _def(str2int("123"))];} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_func_call_01(self):
        input = """_abc() = 123;"""
        expect = "Error on line 1 col 0: _abc"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_func_call_02(self):
        input = """function _main(){_abc() = 123;}"""
        expect = "Error on line 1 col 24: ="
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_func_call_03(self):
        input = """$a = _abc();"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_func_call_04(self):
        input = """$a = _abc("abc");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_func_call_05(self):
        input = """function _main(){$a = _abc(1_23, $b, 12.123e-123, "123");} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_func_call_06(self):
        input = """function _main(){$a = _abc(1 + 2 - 3);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_func_call_07(self):
        input = """function _main(){$a = str2bool(1 + 2 - 3) + float2str("123") || str2int("123");} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_func_call_08(self):
        input = """function _main(){ $a = _abc(_def(123));}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_func_call_09(self):
        input = """function _main(){$a = _abc(_def(123) * 2);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_func_call_10(self):
        input = """function _main(){$a = _abc($b[1][2][3] + 123);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_func_call_11(self):
        input = """function _main(){$a = _abc($b[1][2][3] + str2int("123"));} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_array_01(self):
        input = """function _main(){$a = array();} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_array_02(self):
        input = """function _main(){$a = array(123, "abc", 0.12_3, 123.123e-123);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_array_03(self):
        input = """
function _main(){
    $a = array(
        1 => 123, 
        "abc" => 123, 
        0xabc => "abc", 
        123 => 12e12 + 3 - 1.3 * 5.2 );
} 
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_array_04(self):
        input = """
function _main(){
    $a = array(
        array(1,2,3), 
        array("a","b","c"), 
        array(1 => 123, 2 => $a + $b, "abc" => 123));
}
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_define_01(self):
        input = """define(A)"""
        expect = "Error on line 1 col 8: )"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_define_02(self):
        input = """define(A, "123")"""
        expect = "Error on line 1 col 16: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_define_03(self):
        input = """define(A, "123");"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_define_04(self):
        input = """define($a, "123");"""
        expect = "Error on line 1 col 7: $a"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_define_05(self):
        input = """define(A, 12_3);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_define_06(self):
        input = """define(A, 1.23e-23);"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_define_07(self):
        input = """define(A, str2int("123"));"""
        expect = "Error on line 1 col 10: str2int"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_define_08(self):
        input = """define("A", 123);"""
        expect = "Error on line 1 col 7: A"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_define_09(self):
        input = """define(_A, 123);"""
        expect = "Error on line 1 col 7: _A"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_define_10(self):
        input = """define(123, 123);"""
        expect = "Error on line 1 col 7: 123"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_define_11(self):
        input = """define(A, 1 + 2 - 3 / 4 * 5);"""
        expect = "Error on line 1 col 12: +"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_define_12(self):
        input = """define(A, 1, 2);"""
        expect = "Error on line 1 col 11: ,"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_define_13(self):
        input = """define(A, array(1, 2, 3));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_define_14(self):
        input = """define(A, array($a, $b, $c));"""
        expect = "Error on line 1 col 16: $a"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_define_15(self):
        input = """define(A, array("a", "b", "c"));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_define_16(self):
        input = """define(A, array(1.0123, 2.1_2, 3e-1_2));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_define_17(self):
        input = """define(A, array(1 => 123, 2 => $a + $b, "abc" => 123));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_define_18(self):
        input = """define(A, array(array(1,2,3), array("a","b","c"), array(1 => 123, 2 => $a + $b, "abc" => 123)));"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_stmt_01(self):
        input = """function _main(){break;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_stmt_02(self):
        input = """function _main(){continue;} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_stmt_03(self):
        input = """function _main(){$a = break;}"""
        expect = "Error on line 1 col 22: break"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_stmt_04(self):
        input = """function _main(){break 123;}"""
        expect = "Error on line 1 col 23: 123"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_echo_01(self):
        input = """function _main(){_echo(123);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_echo_02(self):
        input = """function _main(){_echo("123");} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_echo_03(self):
        input = """function _main(){_echo(1 + 2 - 3 / 4);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_echo_04(self):
        input = """function _main(){_echo($a[1][2]);} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_echo_05(self):
        input = """function _main(){_echo(_abc(123));} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_read_01(self):
        input = """function _main(){_read();} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_read_02(self):
        input = """function _main(){_read(123);}"""
        expect = "Error on line 1 col 23: 123"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_ifelse_01(self):
        input = """function _main(){if(){}} """
        expect = "Error on line 1 col 20: )"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_ifelse_02(self):
        input = """function _main(){if(true){};} """
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_ifelse_03(self):
        input = """function _main(){if("abc"){}} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_ifelse_04(self):
        input = """function _main(){if(12 + 3 - 1){}} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_ifelse_05(self):
        input = """function _main(){if($a[1][2][3] - _abc(123) + A){}} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_ifelse_06(self):
        input = """function _main(){if(true){ $a = 123; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_ifelse_07(self):
        input = """function _main(){if(true){ $a = 123; $a[1][2] = 123; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_ifelse_08(self):
        input = """function _main(){if(true){ $a = 123; $a[1][2] = 123; _abc(123); } else { $a = 123; $a[1][2] = 123; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_ifelse_09(self):
        input = """
function _main(){
    if(true){ 
        $a = 123; 
        $a[1][2] = 123; 
        _abc(123); 
    } 
    else(true) { 
        $a = 123; 
        $a[1][2] = 123; 
    }
}
"""
        expect = "Error on line 8 col 8: ("
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_ifelse_10(self):
        input = """
function _main(){
    if(true){ 
        $a = 123; 
        $a[1][2] = 123; 
        _abc(123); 
    } 
    elseif{ 
        $a = 123; 
        $a[1][2] = 123; 
    }
}
"""
        expect = "Error on line 8 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_ifelse_11(self):
        input = """function _main(){if(true){ $a = 123; $a[1][2] = 123; _abc(123); } elseif (false) { $a = 123; $a[1][2] = 123; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_ifelse_12(self):
        input = """function _main(){if(true){ $a = 123; $a[1][2] = 123; _abc(123); } elseif (false) { $a = 123; $a[1][2] = 123; } elseif (false) { $a = 123; $a[1][2] = 123; } else { break; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_foreach_13(self):
        input = """function _main(){foreach(){}} """
        expect = "Error on line 1 col 25: )"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_foreach_14(self):
        input = """function _main(){foreach($a as $b => $c){ $a = 1 + 2 - 3; $a[1][2] = "abc"; _abc(123);}} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_foreach_15(self):
        input = """function _main(){foreach($a as $b => $c){ _echo((("abc" +. int2str($key)) +. "123") +. int2str(123)); }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_while_01(self):
        input = """function _main(){while(){}}"""
        expect = "Error on line 1 col 23: )"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_while_02(self):
        input = """function _main(){while(true){ break; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_while_03(self):
        input = """function _main(){while(true){ $a = $a[1][2][3] - _abc(123) + A / 123; }} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_while_04(self):
        input = """function _main(){while(true){ $a = 123; $b = 456; break; continue;}} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_function_01(self):
        input = """function _main(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_function_02(self):
        input = """function _main($a, $b){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))

    def test_function_03(self):
        input = """function _main(123){}"""
        expect = "Error on line 1 col 15: 123"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_function_04(self):
        input = """function _main(){ $a = $a[1][2][3] - _abc(123) + A / 123;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_function_05(self):
        input = """function _main(){  $a = 123; $b = 456; break; continue; return 123;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_program_01(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_program_02(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_program_03(self):
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_program_04(self):
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_program_05(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_program_06(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_program_07(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_program_08(self):
        input = """
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

   