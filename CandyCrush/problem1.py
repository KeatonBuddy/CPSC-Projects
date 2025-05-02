import stddraw
import Tictactoe
mousex = 0
mousey = 0
stddraw.setXscale(-10,10)
stddraw.setYscale(-10,10)
turns = 9
Tictactoe.drawboard(-7,-7,7,7)
oldmousex = 11
oldmousey = -11
#Check for new differernt input
stddraw.setFontSize(50)
stddraw.setFontFamily("Comic Sans MS")
stddraw.text(0,8, "Tic-Tac-Toe!")

while turns > 0:
            
    if stddraw.mousePressed():
        mousex = stddraw.mouseX()
        mousey = stddraw.mouseY()
        if oldmousex != mousex and oldmousey != mousey:


            if turns % 2 != 0:
                Tictactoe.drawx(mousex,mousey) 
                turns = turns -1
                stddraw.show(0.001)
            
            else:
                Tictactoe.drawcircle(mousex,mousey,2)
                
                turns = turns -1
                stddraw.show(0.001)
            
        
            oldmousex = mousex
            oldmousey = mousey
        if Tictactoe.checkforwin() == 1:
            Tictactoe.checkforwin()
            print("end")
            
            break
    



    stddraw.show(0.001)


if turns <= 0:
    stddraw.clear()
    stddraw.setFontFamily("IMPACT")
    stddraw.setFontSize(110)
    stddraw.setPenColor(stddraw.DARK_GREEN)
    stddraw.text(0,0, "YOU TIED :|")
if turns > 0:
    
    stddraw.setFontFamily("IMPACT")
    stddraw.setFontSize(100)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.text(0,-7, "YOU WON! :D")


stddraw.show()
