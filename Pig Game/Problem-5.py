import math
import random

score = 0
while score < 20:
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


