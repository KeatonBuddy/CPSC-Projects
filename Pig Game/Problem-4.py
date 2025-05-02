from math import *
c = 0
e = 0

print("Rolling dice...")
for i in range(6):
    import random
    b = random.randint(1,6)
    if b == 1:
        c += 1
average_6 = c/6
for i in range(12):
    import random
    d=random.randint(1,6)
    if d == 1:
        e += 1
average_12 = e/12
print("# of times 1 rolled in 6 tries", c)
print("# of times 1 rolled twice in 12 tries", e)
if c >= 1:
    print("Probability of at least 1 once in 6 dice rolls is: ", average_6)
else:
    print("Probability of at least 1 once in 6 dice rolls is: 0")
if e >= 2:
    print("Probability of at least 1 twice in 12 dice rolls is: ", average_12)
else:
    print("Probability of at least 1 twice in 12 dice rolls is: 0")

if c>e:
    print("Therefore, it is more likely to roll 1 once in 6 rolls than it is to roll 1 twice in 12 rolls")
if c<e:
    print("Therefore, it is more likely to roll 1 twice in 12 rolls than it is to roll 1 once in 6 rolls")
if c == e:
    print("Therefore, it is equally likely to roll 1 once in 6 rolls than it is to roll 1 twice in 12 rolls")