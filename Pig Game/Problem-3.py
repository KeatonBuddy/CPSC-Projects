from math import *
import sys
turns = int(sys.argv[1])
pig_out = 0
num_list = []
c = 0
for i in range(turns):
    import random
    b = random.randint(1,6)
    if b != 1:
        pig_out += 1
    else:
        pig_out += 1
        num_list.append(pig_out)
        c += 1
        pig_out = 0

num_sum= sum(num_list)
print("Rolling Dice", turns ,"times...")
if c != 0:
    average_pig_out = num_sum/c
    print("Average turns 'Pigged Out'", average_pig_out)
else:
    print("Average turns 'Pigged Out'", 0) 