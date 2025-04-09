
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
    bit = 8

    n = "0"*bit + n
    n = n[::-1]
    n = n[:bit]
    n = n[::-1]
    return n

def EightBitAdd(a,b):#8bit加算器
    bit = 8
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
    bit = 8
    
    for i in range(bit):
        b = point(b,i,NOT(b[i]))
    b = EightBitAdd(bitnum("1"),b)
    
    return EightBitAdd(a,b)

def EqualAB(a,b):#aとbが等しいか
    bit = 8
    a = bitnum(a)
    b = bitnum(b)

    out = "1"
    for i in range(bit):
        out = AND(out,NOT(XOR(a[i],b[i])))
    
    return out

def MoreThanA(a,b):#aがbより大きいか
    bit = 8
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

