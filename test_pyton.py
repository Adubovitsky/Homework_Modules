import math
from Functions import check_numbers

def test_filter():
    assert list(filter(check_numbers, [1,2,3,-3,-4,-5]))==[1,2,3]
    assert list(filter(lambda x: x<0,[1,2,3,-3,-4,-5]))==[-3,-4,-5]

def test_map():
    assert list(map(lambda x: x+1,[1,2,3]))==[2,3,4]
    assert list(map(lambda x: x**3, [1, 2, 3])) == [1, 8, 27]

def test_sorted():
    assert sorted(("g","e","k",'a'),reverse=False)==['a','e','g',"k"]
    score_of_students = [("Ivan",95),("Nick", 93), ("Anna", 91)]
    assert sorted(score_of_students,key=lambda x: x[1],reverse=True)== [('Ivan', 95), ('Nick', 93), ('Anna', 91)]

def test_pi():
    assert math.pi==3.141592653589793

def test_sqrt():
    assert math.sqrt(100)==10
    assert math.sqrt(64)==8

def test_pow():
    assert math.pow(2,3)==8
    assert math.pow(-5,4)==625

def test_hypot():
    assert math.hypot(3,4)==5
    assert math.hypot(6,8)==10





