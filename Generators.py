COMBINATON = (7, 6, 1)

'''
got_combination = False
for C1 in range(10):
    if got_combination:
        break
    for C2 in range(10):
        if got_combination:
            break
        for C3 in range(10):
            if (C1, C2, C3) == COMBINATON:
                print('Got the combination: {}'.format((C1, C2, C3)))
                got_combination = True
                break
            print(C1, C2, C3)'''

def combination():
    for C1 in range(10):
        for C2 in range(10):
            for C3 in range(10):
                yield(C1, C2, C3)

for (C1, C2, C3) in combination():
    print(C1, C2, C3)
    if (C1, C2, C3) == COMBINATON:
        print('Got the combination: {}'.format((C1, C2, C3)))
        break
    print(C1, C2, C3)