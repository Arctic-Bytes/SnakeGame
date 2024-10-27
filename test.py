import random

newlist = [1, 2, 3]

newlist.append(random.randrange(1, 10))

print(newlist)
for i in newlist:
    if i < 3:
        print(i)
