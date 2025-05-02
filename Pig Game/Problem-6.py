import math
import random
import sys
a = sys.argv[1]
score = int(a)

if int(a) < 20:
    while int(score) < 20:
        b = random.randint(1,6)
        if b != 1:
            score += b
            print ("Rolled a", int(b))
        if b == 1:
            print ("Rolled a 1!!!")
            print ("Pigged out :(")
            score = 0    
            break
else:
    while score < 100:
        b = random.randint(1,6)
        if b != 1:
            score += b
            print ("Rolled a", int(b))
        if b == 1:
            print ("Rolled a 1!!!")
            print ("Pigged out :(")
            score = 0    
            break
print ("Your score is", int(score)) 
print ("Press up arrow and enter to roll again")


