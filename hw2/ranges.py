import math

def a():
    for i in range(-25, 25):
        a = i + math.sqrt(abs(i*3)) >= 23
        print('a: ', i, a)
    
def b():
    for i in range(-25, 25):
        b = i ** 3 % 2 != 0
        print('b: ', i, b)

def c():
    for i in range(-25, 25):
        c = i * 6 - 14 < 107
        print('c: ', i, c)
        
def d():
    for i in range(-25, 25):
        d = i ** 3 < 0
        print('d: ', i, d)

a()
print('--------')
b()
print('--------')
c()
print('--------')
d()
print('--------')