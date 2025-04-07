from pylogic import * 

def test_NOT():
    assert NOT(0) == 1
    assert NOT(1) == 0

def test_AND():
    assert AND(0,0) == 0
    assert AND(1,0) == 0
    assert AND(0,1) == 0
    assert AND(1,1) == 1

def test_OR():
    assert OR(0,0) == 0
    assert OR(1,0) == 1
    assert OR(0,1) == 1
    assert OR(1,1) == 1

def test_XOR():
    assert XOR(0,0) == 0
    assert XOR(1,0) == 1
    assert XOR(0,1) == 1
    assert XOR(1,1) == 0

def test_HalfAdd():
    assert HalfAdd(0,0) == (0,0)
    assert HalfAdd(1,0) == (1,0)
    assert HalfAdd(0,1) == (1,0)
    assert HalfAdd(1,1) == (0,1)

def test_FullAdd():
    assert FullAdd(0,0,0) == (0,0)
    assert FullAdd(0,0,1) == (1,0)
    assert FullAdd(0,1,0) == (1,0)
    assert FullAdd(0,1,1) == (0,1)

    assert FullAdd(1,0,0) == (1,0)
    assert FullAdd(1,0,1) == (0,1)
    assert FullAdd(1,1,0) == (0,1)
    assert FullAdd(1,1,1) == (1,1)