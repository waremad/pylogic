global bit
bit = 8

def NOT(a):
    return str(-int(a)+1)

def AND(a,b):
    return str(int(a)*int(b))

def OR(a,b):
    return NOT(AND(NOT(a),NOT(b)))

def XOR(a,b):
    return AND(NOT(AND(a,b)),OR(a,b))

def HalfAdd(a,b):#半加算器
    return XOR(a,b),AND(a,b)

def FullAdd(a,b,x=0):#全加算器
    c,s = HalfAdd(a,b)
    c,s2 = HalfAdd(c,x)
    return c,OR(s,s2)

def point(self,i,n):#selfのi番目をnにする
    self = list(self)
    self[i] = str(n)
    return "".join(self)

def bitnum(n):#bitをそろえる
    global bit

    n = "0"*bit + n
    n = n[::-1]
    n = n[:bit]
    n = n[::-1]
    return n

def EightBitAdd(a,b):#8bit加算器
    global bit
    out = ""
    s = 0
    #print("a,b",a,b)

    for i in range(bit):
        #print("int(a[bit-i-1]),int(b[bit-i-1]",int(a[bit-i-1]),int(b[bit-i-1]))
        c ,s = FullAdd(int(a[bit-i-1]),int(b[bit-i-1]),s)
        #print("c,s",c,s)
        out = str(c) + out

    return out

def EightBitSub(a,b):#8bit減算器
    global bit
    
    for i in range(bit):
        b = point(b,i,NOT(b[i]))
    b = EightBitAdd(bitnum("1"),b)
    
    return EightBitAdd(a,b)

def EqualAB(a,b):#aとbが等しいか
    global bit
    a = bitnum(a)
    b = bitnum(b)

    out = "1"
    for i in range(bit):
        out = AND(out,NOT(XOR(a[i],b[i])))
    
    return out

def MoreThanA(a,b):#aがbより大きいか
    global bit
    a = bitnum(a)
    b = bitnum(b)
    out = bitnum("0")
    for i in range(bit):
        out = point(out,-1,OR(
            AND(
                AND(
                    EqualAB(a[i],"1"),
                    XOR(a[i],b[i])),
                EqualAB(out[-2],"0")),
            out[-1]))
        out = point(out,-2,OR(
            AND(
                AND(
                    EqualAB(b[i],"1"),
                    XOR(a[i],b[i])),
                EqualAB(out[-1],"0")),
            out[-2]))
        print("a,b,i,out",a,b,i,out)
    return NOT(EightBitSub(out,bitnum("1"))[-1])

def MoreEqualA(a,b):#aがb以上か
    return OR(MoreThanA(a,b),EqualAB(a,b))

def EightOneBitMul(a,b):#8bitと1bitの乗算
    #print("a,b",a,b,1)
    global bit
    a = bitnum(a)
    b = ("0" + b)[-1]
    #print("b",b)
    for i in range(bit):
        a = point(a,i,AND(a[i],b))
    #print("a",a)
    return a

def EightBitMul(a,b):#8bit乗算器
    #print("a,b",a,b)
    global bit
    a = bitnum(a)
    b = bitnum(b)
    b = b[::-1]
    out = bitnum("0")
    BIT = ""
    for i in range(bit):
        print("out,EightOneBitMul(a,b[i])",out,EightOneBitMul(a,b[i]))
        out = EightBitAdd(out,EightOneBitMul(a,b[i]))
        a = a[1:] + "0"
    return out

def EightBitDiv(a,b):#8bit徐算器（割り切り）
    pass

def EightBitRem(a,b):#8bit余算器（余り）
    pass

def IFELSE(DO,ELSE,how):#ある条件によって異なる実行をする
    pass

def FOR(self,n,i=0):#ある処理を指定した回数ループする
    pass
