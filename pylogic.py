
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
    if bit < len(n):
        n = n[::-1]
        n = n[:bit]
        return n[::-1]

    for i in range(bit - len(n)):
        n = "0" + n
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

def MoreThanA(a,b):#aがbより大きいか
    pass

def MoreEqualB(a,b):#aがb以上か
    pass

def EqualB(a,b):#aとbが等しいか
    pass