from math import *
import sys
a = int(sys.argv[1])
total_sum = 0

for i in range(int (a)):
    import random
    b = random.randint(1,6)
    total_sum += b
    average = total_sum/a

print("# of Rolls " +str(a))
print("Rolling...")
print("Total Sum = " +str(total_sum))
print("Average for", str(a), "Rolls is", average)