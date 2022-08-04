directions = ['Left', 'Right', 'Up', 'Down']

#for x in range(len(directions)):
#   print(x, directions[x])

for x, y in enumerate(directions):
    print(x, y)

dict = dict(enumerate(directions))
print(dict)

[print(x, y) for x, y in enumerate(dict)]