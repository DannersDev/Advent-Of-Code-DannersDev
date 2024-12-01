import random

def day1_input(n):
    array1=[random.randrange(10000, 99999, 1) for i in range(n)]
    array2=[random.randrange(10000, 99999, 1) for i in range(n)]
    return array1,array2