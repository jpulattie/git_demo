import math


def contrived_func(val):

    a = val + math.sqrt(abs(val*3)) >= 23
    b = val ** 3 % 2 != 0
    c = val * 6 - 14 < 107
    d = val ** 3 < 0

    print('val= ', val)
    print('a= ', a)
    print('b= ', b)
    print('c= ', c)
    print('d= ', d)
    print('----------')

contrived_func(-1)
contrived_func(-2)
contrived_func(0)
contrived_func(22)
contrived_func(23)
contrived_func(18)
contrived_func(15)
contrived_func(19)
