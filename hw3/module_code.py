import random

def test1():
    tests_to_generate = 4

    for i in range(tests_to_generate):
        expected = True
        new_number = num_builder(random.randint(14,17))

def num_builder(length):
    number = ''
    #print(length)
    for i in range(0, length):
        number = number + str(random.randint(0,9))
    print(number)
    return number

test1()