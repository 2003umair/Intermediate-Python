random_number = [15, 5, 10, 2, 9, 1, 46, 99]

def divisible(num):
    if num % 5 == 0:
        return True
    else:
        return False

abc = (x for x in random_number if divisible(x))

'''abc = []
for x in random_number:
    if divisible(x):
        abc.append(x)'''

#[print(x) for x in abc]
#print(abc)

abc = [x for x in random_number if divisible(x)]
#print(abc)

#[[print(x, xx) for xx in range(4)] for x in range(4)]


#for x in range(4):
#    for xx in range(4):
#        print(x, xx)

abc = (((x, xx) for xx in range(4)) for x in range(4))
print(abc)

for x in abc:
    for xx in x:
        print(xx)