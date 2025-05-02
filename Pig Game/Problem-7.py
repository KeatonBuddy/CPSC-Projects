import math
import random

totalscore = 0
turnscore = 0
turnnumber = 1
print("~ Turn", turnnumber, "~")
while totalscore < 100:
    while turnscore < 20:
        b = random.randint(1,6)
        if b != 1:
            print ("Rolled a", int(b))
            turnscore += b
            if int(turnscore) + int(totalscore) >= 100:
                totalscore += turnscore
                break
        if b == 1:
            print ("Rolled a 1!!!")
            print ("Pigged out :(")
            turnscore = 0   
            print("Your Turn Score is = ", int(turnscore))
            print("Your Total Score is = ", int(totalscore)) 
            turnnumber += 1
            print("~ Turn", turnnumber,"~")
    if turnscore >= 20:
        totalscore += turnscore
        print("Your Turn Score is = ", int(turnscore))
        print("Your Total Score is = ", int(totalscore))
        turnscore = 0
        turnnumber += 1
        print("~ Turn", turnnumber,"~")
print("Your Turn Score is = ", int(turnscore))
print("Your Total Score is = ", int(totalscore))

if totalscore > 100:
    print("~*~*~!!YOU WIN!!~*~*~*")



