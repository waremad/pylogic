from pylogic import * 

def test_NOT():
    assert NOT("0") == "1"
    assert NOT("1") == "0"

def test_AND():
    assert AND("0","0") == "0"
    assert AND("1","0") == "0"
    assert AND("0","1") == "0"
    assert AND("1","1") == "1"

def test_OR():
    assert OR("0","0") == "0"
    assert OR("1","0") == "1"
    assert OR("0","1") == "1"
    assert OR("1","1") == "1"

def test_XOR():
    assert XOR("0","0") == "0"
    assert XOR("1","0") == "1"
    assert XOR("0","1") == "1"
    assert XOR("1","1") == "0"

def test_HalfAdd():
    assert HalfAdd("0","0") == ("0","0")
    assert HalfAdd("1","0") == ("1","0")
    assert HalfAdd("0","1") == ("1","0")
    assert HalfAdd("1","1") == ("0","1")

def test_FullAdd():
    assert FullAdd("0","0","0") == ("0","0")
    assert FullAdd("0","0","1") == ("1","0")
    assert FullAdd("0","1","0") == ("1","0")
    assert FullAdd("0","1","1") == ("0","1")

    assert FullAdd("1","0","0") == ("1","0")
    assert FullAdd("1","0","1") == ("0","1")
    assert FullAdd("1","1","0") == ("0","1")
    assert FullAdd("1","1","1") == ("1","1")

def TenToTwoEight(n):#10進数から2進数8bitに変換
    bit = 8
    out = ""
    for i in range(bit):
        out = str(int(n%2)) + out
        n = int(n//2)
    return out

def test_TenToTwoEight():
    assert TenToTwoEight(   0) == "00000000"
    assert TenToTwoEight(   1) == "00000001"
    assert TenToTwoEight(  10) == "00001010"
    assert TenToTwoEight(  57) == "00111001"
    assert TenToTwoEight( 127) == "01111111"
    assert TenToTwoEight(  -1) == "11111111"
    assert TenToTwoEight(  -5) == "11111011"
    assert TenToTwoEight( -15) == "11110001"
    assert TenToTwoEight(-127) == "10000001"
    assert TenToTwoEight(-128) == "10000000"

def TwoToTenEight(self):#2進数8bitから10進数に変換
    bit = 8
    minus = self[0] == "1"
    #print("self[0],minus",self[0],minus)
    self = self[bit-1:0:-1]
    out = 0
    n = 1
    for i in range(bit-1):
        out += int(self[i])*n
        n *= 2
    if minus:
        out += -2**(bit-1)
    return out

def test_TwoToTenEight():
    assert TwoToTenEight("00000000")  ==    0
    assert TwoToTenEight("00000001")  ==    1
    assert TwoToTenEight("00001010")  ==   10
    assert TwoToTenEight("00111001")  ==   57
    assert TwoToTenEight("01111111")  ==  127
    assert TwoToTenEight("11111111")  ==   -1
    assert TwoToTenEight("11111011")  ==   -5
    assert TwoToTenEight("11110001")  ==  -15
    assert TwoToTenEight("10000001")  == -127
    assert TwoToTenEight("10000000")  == -128

def test_point():
    assert point("00000000",0,1) == "10000000"
    assert point("00000000",1,1) == "01000000"
    assert point("00000000",2,1) == "00100000"
    assert point("00000000",3,1) == "00010000"
    assert point("00000000",4,1) == "00001000"
    assert point("00000000",5,1) == "00000100"
    assert point("00000000",6,1) == "00000010"
    assert point("00000000",7,1) == "00000001"
    assert point("11111111",5,1) == "11111111"

def test_bitnum():
    assert bitnum("00000000") == "00000000"
    assert bitnum("1") == "00000001"
    assert bitnum("01") == "00000001"
    assert bitnum("0000001") == "00000001"
    assert bitnum("000000001") == "00000001"
    assert bitnum("00000000001") == "00000001"
    assert bitnum("010011000111") == "11000111"

def test_EightBitAdd():
    num = [1,2,3,5,7,11,99,28,6,57]
    for i in num:
        for j in num:
            #print("i,j,i+j",i,j,i+j)
            assert EightBitAdd(TenToTwoEight(i),TenToTwoEight(j)) == TenToTwoEight(i+j)
        
def test_EightBitSub():
    num = [1,2,3,5,7,11,99,28,6,57]
    for i in num:
        for j in num:
            #print("i,j,i+j",i,j,i+j)
            assert EightBitSub(TenToTwoEight(i),TenToTwoEight(j)) == TenToTwoEight(i-j)

