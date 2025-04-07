
def NOT(a):
    return -a+1

def AND(a,b):
    return a*b

def OR(a,b):
    return NOT(AND(NOT(a),NOT(b)))

def XOR(a,b):
    return AND(NOT(AND(a,b)),OR(a,b))

def HalfAdd(a,b):
    return XOR(a,b),AND(a,b)

def FullAdd(a,b,x=0):
    c,s = HalfAdd(a,b)
    c,s2 = HalfAdd(c,x)
    return c,OR(s,s2)

def EightBitAdd(a,b):
    pass