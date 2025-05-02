import CandyCrush
import stddraw
import random
import stdarray

boardlist = stdarray.create2D(7,9,None)
column = stdarray.create2D(9,7,None)




stddraw.setXscale(-10,10)
stddraw.setYscale(-10,10)
turns = 0
checkh = ""
checkv = ""
game = True
k = 0



#boardlist = [[None]*9 for _ in range (7)]

#random shape
def randomshape(list,i,j):
    rand = random.randint(1,6)
    if rand == 1:
        
        list[i][j] = "SQUARE"
    if rand == 2:
        
        list[i][j] = "CIRCLE"
    if rand == 3:

        list[i][j] = "HEART"
    if rand == 4:
        
        list[i][j] = "HEXAGON"
    if rand == 5:
        
        list[i][j] = "STAR"
    if rand == 6:
        
        list[i][j] = "TRIANGLE"


#set up board array

for i in range(7):
    for j in range(9):
        randomshape(boardlist,i,j)
        

#Draw Board
CandyCrush.drawboard(-7,-9,7,9)
for i in range(7):
    for j in range(9):
        CandyCrush.fillshapes(boardlist,i,j)

#Three Check

for i in range(7):
    for j in range(7):
        while CandyCrush.threecheckv(boardlist,i,j) is True:
            randomshape(boardlist,i,j)
            CandyCrush.fillshapes(boardlist,i,j)
for j in range(9):
    for i in range(5):
        while CandyCrush.threecheckh(boardlist,i,j) is True:
            randomshape(boardlist,i,j)
            CandyCrush.fillshapes(boardlist,i,j)

#Check Twice for even lower % chance of duplicates

for i in range(7):
    for j in range(7):
        while CandyCrush.threecheckv(boardlist,i,j) is True:
            randomshape(boardlist,i,j)
            CandyCrush.fillshapes(boardlist,i,j)
for j in range(9):
    for i in range(5):
        while CandyCrush.threecheckh(boardlist,i,j) is True:
            randomshape(boardlist,i,j)
            CandyCrush.fillshapes(boardlist,i,j)

for i in range(9):
    for j in range(7):
        column[i][j] = boardlist[j][i] 








#Start Game
while game is True:
"""
    for i in range(7):
        for j in range(9):
            if CandyCrush.threecheckv(boardlist,i,j) is True:
                for m in range(9):
                        if boardlist[i][m] == boardlist[i][j]:
                            del boardlist[i][m]
                        if boardlist[i][m] == boardlist[i][j]:
                            del boardlist[i][m]
                del boardlist[i][j]
                CandyCrush.drawboard(-7,-9,7,9)
                
                break
                    

            except IndexError:
                pass

            for i in range(7):
                for j in range(9):
                    try:
                        CandyCrush.fillshapes(boardlist,i,j)
                    except IndexError:
                        boardlist[i].append(None)
                        randomshape(boardlist,i,j)
                        CandyCrush.fillshapes(boardlist,i,j)   

    for j in range(9):
        for i in range(7):
            try:
                if boardlist[i][j] != None:
                    if CandyCrush.threecheckh(boardlist,i,j) is True:
                        shapeh = boardlist[i][j]
                        for m in range(6):
                            try:
                                if shapeh == boardlist[i+m][j]:
                                    del boardlist[i+m][j]
                                else:
                                    break
                            except IndexError:
                                pass
                        CandyCrush.drawboard(-7,-9,7,9)
                        shapeh = None
                        break
                    

            except IndexError:
                pass

            for i in range(7):
                for j in range(9):
                    try:
                        CandyCrush.fillshapes(boardlist,i,j)
                    except IndexError:
                        boardlist[i].append(None)
                        randomshape(boardlist,i,j)
                        CandyCrush.fillshapes(boardlist,i,j) """



    #First Turn
    if stddraw.mousePressed():
        if turns % 2 == 0:
            mousex = stddraw.mouseX()
            mousey = stddraw.mouseY()
            for i in range(len(boardlist)):
                for j in range(len(boardlist[i])):
                    CandyCrush.click1(mousex,mousey,i,j)
                    if CandyCrush.click1(mousex,mousey,i,j) is True:
                        firstclickx = i
                        firstclicky = j
                        firstclick = boardlist[i][j]
            turns += 1
    #Second Turn
        else:
            mousex = stddraw.mouseX()
            mousey = stddraw.mouseY()
            for i in range(len(boardlist)):
                for j in range(len(boardlist[i])):
                    CandyCrush.click1(mousex,mousey,i,j)
                    if CandyCrush.click1(mousex,mousey,i,j) is True:
                        secondclickx = i
                        secondclicky = j
                        secondclick = boardlist[i][j]
                    
            
            
            
            if firstclickx == secondclickx - 1 and firstclicky == secondclicky or \
               firstclicky == secondclicky + 1 and firstclickx == secondclickx or \
               firstclickx == secondclickx + 1 and firstclicky == secondclicky or \
               firstclicky == secondclicky - 1 and firstclickx == secondclickx :

                CandyCrush.shapeswitch(firstclick,secondclick,firstclickx,secondclickx,firstclicky,secondclicky)
                boardlist[firstclickx][firstclicky] = secondclick
                boardlist[secondclickx][secondclicky] = firstclick
                stddraw.show(500)
                #Check for 3
                
                for i in range(7):
                    for j in range(9):
                        try:
                            if boardlist[i][j] != None:
                                
                                if CandyCrush.threecheckv(boardlist,i,j) is True:
                                    for m in range(9):
                                        try:
                                            if boardlist[i][m] == boardlist[i][j]:
                                                del boardlist[i][m]
                                            if boardlist[i][m] == boardlist[i][j]:
                                                del boardlist[i][m]
                                        except IndexError:
                                            pass
                                    del boardlist[i][j]
                                    CandyCrush.drawboard(-7,-9,7,9)
                                    checkv = "Yes"
                                    break
                                

                        except IndexError:
                            pass
                                

                for j in range(9):
                    for i in range(7):
                        try:
                            if boardlist[i][j] != None:
                                if CandyCrush.threecheckh(boardlist,i,j) is True:
                                    shapeh = boardlist[i][j]
                                    for m in range(6):
                                        try:
                                            if shapeh == boardlist[i+m][j]:
                                                del boardlist[i+m][j]
                                            else:
                                                break
                                        except IndexError:
                                            pass
                                    CandyCrush.drawboard(-7,-9,7,9)
                                    checkh = "Yes"
                                    shapeh = None
                                    break
                                

                        except IndexError:
                            pass
                        
                    
                                    
               
                if checkv != "Yes" and \
                   checkh != "Yes":
                    try:
                        CandyCrush.shapeswitch(secondclick,firstclick,firstclickx,secondclickx,firstclicky,secondclicky)
                        boardlist[firstclickx][firstclicky] = firstclick
                        boardlist[secondclickx][secondclicky] = secondclick
                    except IndexError:
                        pass
                checkv = None
                checkh = None
                CandyCrush.resetboard()

                for i in range(len(boardlist)):
                    for j in range(len(boardlist[i])):
                        CandyCrush.fillshapes(boardlist,i,j)
                stddraw.show(500)

                for i in range(7):
                    for j in range(9):
                        try:
                            CandyCrush.fillshapes(boardlist,i,j)
                        except IndexError:
                            boardlist[i].append(None)
                            randomshape(boardlist,i,j)
                            CandyCrush.fillshapes(boardlist,i,j)

                turns = 0

    
                        

            else:
                for i in range(len(boardlist)):
                    for j in range(len(boardlist[i])):
                        CandyCrush.fillshapes(boardlist,i,j)
                turns = 0
            CandyCrush.drawboard(-7,-9,7,9)

            
            
        
    stddraw.show(10)


                    
    


        










    



