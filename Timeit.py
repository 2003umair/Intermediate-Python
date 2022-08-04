import timeit

#print(timeit.timeit('2+3', number=400000))

random_list = range(100)

def divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False

abc = list((x for x in random_list if divisible(x)))

for x in abc:
    print(x)

#abc = [x for x in random_list if divisible(x)]

"""
#print(timeit.timeit('''random_list = range(100)

def divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False

abc = list(x for x in random_list if divisible(x))''', number=4000))
"""