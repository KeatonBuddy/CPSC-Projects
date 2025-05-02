import math
import random

p1totalscore = 0
p1turnscore = 0
p1turnnumber = 0
p2totalscore = 0
p2turnscore = 0
p2turnnumber = 0

z = input("You are PLAYER ONE!! Are You Ready??[Type yes, or no]")

if z == "yes":
    k = random.choice(["a","b"])
    if k == "a":
        print("*|*|*|*PLAYER 1 STARTS*|*|*|*")
        while p1totalscore < 100 and p2totalscore < 100:
    #PLAYER ONE       
            print("PLAYER 1's TURN")
            p1turnnumber += 1
            print("~ Turn", p1turnnumber, "~")
            print("*PLAYER 1 Total Score is = ", int(p1totalscore))
            while p1turnscore <= 20:
                y = input("Would you like to Roll [r] or Hold [h]??, [Type r or h]")
                if y == "r":
                    b = random.randint(1,6)
                    if b != 1:
                        print ("----Rolled a", int(b))
                        p1turnscore += b
                        if int(p1turnscore) + int(p1totalscore) >= 100:
                            break
                    if b == 1:
                        print ("----Rolled a 1!!!")
                        print ("----Pigged out :(")
                        p1turnscore = 0   
                        p1turnnumber += 1
                        break
                if y == "h":
                    print("Holding Total Score")
                    break

            p1totalscore += p1turnscore
            print("**PLAYER 1 Turn Score is = ", int(p1turnscore))
            print("*PLAYER 1 Total Score is = ", int(p1totalscore))
            p1turnscore = 0
            print(" ")
            print("_____")
            print(" ")

    #PLAYER TWO

            if p1totalscore >= 100:
                break
            else:
                print("PLAYER 2's TURN")
                p2turnnumber += 1
                print("~ Turn", p2turnnumber, "~")
                print("*PLAYER 2 Total Score is = ", int(p2totalscore))
                while p2turnscore <= 20:
                    b = random.randint(1,6)
                    if b != 1:
                        print ("----Rolled a", int(b))
                        p2turnscore += b
                        if int(p2turnscore) + int(p2totalscore) >= 100:
                            break
                    if b == 1:
                        print ("----Rolled a 1!!!")
                        print ("----Pigged out :(")
                        p2turnscore = 0   
                        p2turnnumber += 1
                        break
                p2totalscore += p2turnscore
                print("**PLAYER 2 Turn Score is = ", int(p2turnscore))
                print("*PLAYER 2 Total Score is = ", int(p2totalscore))
                p2turnscore = 0

            print(" ")
            print("_____")
            print(" ")

    else:
        print("*|*|*|*PLAYER 2 STARTS*|*|*|*")
        while p1totalscore < 100 and p2totalscore < 100:
    #PLAYER TWO
            print("PLAYER 2's TURN")
            p2turnnumber += 1
            print("~ Turn", p2turnnumber, "~")
            print("*PLAYER 2 Total Score is = ", int(p2totalscore))
            while p2turnscore <= 20:
                b = random.randint(1,6)
                if b != 1:
                    print ("----Rolled a", int(b))
                    p2turnscore += b
                    if int(p2turnscore) + int(p2totalscore) >= 100:
                        break
                if b == 1:
                    print ("----Rolled a 1!!!")
                    print ("----Pigged out :(")
                    p2turnscore = 0   
                    p2turnnumber += 1
                    break
            p2totalscore += p2turnscore
            print("**PLAYER 2 Turn Score is = ", int(p2turnscore))
            print("*PLAYER 2 Total Score is = ", int(p2totalscore))
            p2turnscore = 0
            print(" ")
            print("_____")
            print(" ")
        
    #PLAYER ONE       
            if p2totalscore >= 100:
                break
            else:
                print("PLAYER 1's TURN")
                p1turnnumber += 1
                print("~ Turn", p1turnnumber, "~")
                print("*PLAYER 1 Total Score is = ", int(p1totalscore))
                while p1turnscore <= 20:
                    y = input("Would you like to Roll [r] or Hold [h]??, [Type r or h]")
                    if y == "r":
                        b = random.randint(1,6)
                        if b != 1:
                            print ("----Rolled a", int(b))
                            p1turnscore += b
                            if int(p1turnscore) + int(p1totalscore) >= 100:
                                break
                        if b == 1:
                            print ("----Rolled a 1!!!")
                            print ("----Pigged out :(")
                            p1turnscore = 0   
                            p1turnnumber += 1
                            break
                    if y == "h":
                        print("Holding Total Score")
                        break

                p1totalscore += p1turnscore
                print("**PLAYER 1 Turn Score is = ", int(p1turnscore))
                print("*PLAYER 1 Total Score is = ", int(p1totalscore))
                p1turnscore = 0
                print(" ")
                print("_____")
                print(" ")

    print(" ")
    print(".........")
    print(" ")

    if p1totalscore >= 100:
        print("~*~*~!!PLAYER ONE WINS!!~*~*~*")
    if p2totalscore >= 100:
        print("~*~*~!!PLAYER TWO WINS!!~*~*~*")

else:
    print("<><><> Game OVER [to Reset press up arrow and enter <><><>")