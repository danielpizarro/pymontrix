from montrix import *
from nose.tools import assert_true, assert_false, assert_equals
import sys

def test_zone_001():
    a=Zone(row0=0, col0=0, row1=100, col1=100, value=1)

def test_zone_002():
    a=Zone(row0=0, col0=0, row1=100, col1=100, value=1)
    b=Zone(row0=1, col0=1, row1=99, col1=99, value=1)
    assert_true(a.intersects(b))

def test_zone_003():
    a=Zone(row0=0, col0=0, row1=100, col1=100, value=1)
    b=Zone(row0=1, col0=1, row1=99, col1=99, value=1)
    c=Zone(row0=1, col0=1, row1=99, col1=99, value=1)
    assert_false(a==b)
    assert_true(b==c)

def test_zone_is_void_001():
    assert_false(Zone(row0=0, col0=0, row1=10, col1=10, value=1).is_void())
    assert_true(Zone(row0=10, col0=10, row1=10, col1=10, value=1).is_void())
    assert_true(Zone(row0=11, col0=11, row1=10, col1=10, value=1).is_void())
    
    assert_true(Zone(row0=0, col0=0, row1=0, col1=1, value=1).is_void())
    

def test_zone_intersects_001():
    a=Zone(row0=0, col0=0, row1=100, col1=100, value=1)
    b=Zone(row0=0, col0=0, row1=10, col1=10, value=1)
    c=Zone(row0=5, col0=5, row1=10, col1=10, value=1)
    d=Zone(row0=0, col0=0, row1=4, col1=4, value=1)

    assert_true(a.intersects(b))
    assert_false(c.intersects(d))

def test_zone_fragment_and_set_001():
    a=Zone(0,0,9,9,0)
    b=Zone(3,3,4,4,1)
    aux = sorted(a.fragment_and_set(b, layout="nine"))
    
    for x in aux:
        print x
    
    assert_equals(aux[0], Zone(0,0,3,3,0))
    assert_equals(aux[1], Zone(0,3,3,4,0))
    assert_equals(aux[2], Zone(0,4,3,9,0))
    assert_equals(aux[3], Zone(3,0,4,3,0))
    assert_equals(aux[4], Zone(3,3,4,4,1))
    assert_equals(aux[5], Zone(3,4,4,9,0))
    assert_equals(aux[6], Zone(4,0,9,3,0))
    assert_equals(aux[7], Zone(4,3,9,4,0))
    assert_equals(aux[8], Zone(4,4,9,9,0))

    

def test_zone_fragment_and_set_002():
    a=Zone(0,0,9,9,0)
    b=Zone(0,0,1,1,1)
    aux = a.fragment_and_set(b, layout="nine")
    
    for x in aux:
        print x
    
    assert_equals(aux[0], Zone(0,0,1,1,1))
    assert_equals(aux[1], Zone(0,1,1,9,0))
    assert_equals(aux[2], Zone(1,0,9,1,0))
    assert_equals(aux[3], Zone(1,1,9,9,0))

def test_zone_fragment_and_set_003():
    a=Zone(0,0,9,9,0)
    b=Zone(3,3,4,4,1)
    aux = sorted(a.fragment_and_set(b, layout="five"))
    
    for x in aux:
        print x
    
    assert_equals(aux[0], Zone(0,0,3,4,0))
    assert_equals(aux[1], Zone(0,4,4,9,0))
    assert_equals(aux[2], Zone(3,0,9,3,0))
    assert_equals(aux[3], Zone(3,3,4,4,1))
    assert_equals(aux[4], Zone(4,3,9,9,0))

    

def test_zone_fragment_and_set_004():
    a=Zone(0,0,9,9,0)
    b=Zone(0,0,1,1,1)
    aux = sorted(a.fragment_and_set(b, layout="five"))
    
    for x in aux:
        print x
    
    assert_equals(aux[0], Zone(0,0,1,1,1))
    assert_equals(aux[1], Zone(0,1,1,9,0))
    assert_equals(aux[2], Zone(1,0,9,9,0))

def test_zone_fragment_and_set_005():
    a=Zone(0,0,9,9,0)
    b=Zone(3,3,4,4,1)
    aux = sorted(a.fragment_and_set(b))
    
    for x in aux:
        print x
    
    assert_equals(aux[0], Zone(0,0,3,4,0))
    assert_equals(aux[1], Zone(0,4,4,9,0))
    assert_equals(aux[2], Zone(3,0,9,3,0))
    assert_equals(aux[3], Zone(3,3,4,4,1))
    assert_equals(aux[4], Zone(4,3,9,9,0))

    

def test_zone_fragment_and_set_006():
    a=Zone(0,0,9,9,0)
    b=Zone(0,0,1,1,1)
    aux = sorted(a.fragment_and_set(b))
    
    for x in aux:
        print x
    
    assert_equals(aux[0], Zone(0,0,1,1,1))
    assert_equals(aux[1], Zone(0,1,1,9,0))
    assert_equals(aux[2], Zone(1,0,9,9,0))
    
def test_montrix_001():
    a = Montrix(9,9,0)
    a.set_zone(Zone(3,3,5,5,1))
    a.set_zone(Zone(7,7,9,9,2))
    a.print_repr(sys.stdout)
    assert_false(False)

def test_montrix_002():
    a = Montrix(9,9,0)
    a.set_zone(Zone(3,3,5,5,1))
    a.set_zone(Zone(7,7,9,9,2))
    x = a.to_list()
    
    print "***"
    print repr(x)
    print "***"
    
    expected =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 2, 2]] 

    assert_equals(expected, x)


def test_montrix_003():
    a = Montrix(9,9,0)
    a.set_zone(Zone(3,3,5,5,1))
    a.set_zone(Zone(7,7,9,9,2))
    x = a.to_list()
    
    print "***"
    print repr(x)
    print "***"
    
    expected =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 2],
        [0, 0, 0, 0, 0, 0, 0, 2, 2]] 

    assert_equals(expected, x)

    max_value, max_coords = a.get_max()
    
    assert_equals(max_value,2)
    assert_equals(max_coords, (7,7))
    