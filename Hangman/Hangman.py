"hangman"

import math
import stddraw

def setscreensize(x0,y0,x1,y1):
        global xmin
        global xmax
        global ymin
        global ymax
        xmin = x0
        xmax = x1
        ymin = y0
        ymax = y1
        
        stddraw.setXscale(x0,x1)
        stddraw.setYscale(y0,y1)

#Text

def Text(x, y, sWord):
        stddraw.setFontFamily("Arial")
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.text(x, y,s)
#title
def title(x, y, font, fontsize, fontcolor, s):
    """
    x, y, font, fontsize, fontcolor, s
    """
    stddraw.setFontSize(fontsize)
    stddraw.setFontFamily(font)
    stddraw.setPenColor(fontcolor)
    stddraw.text(x, y, s)



#Hangman Base
def drawHangman(x0, y0, x1, y1,y2):
    """
    x0, y0, x1, y1, y2 = hanging point
    """    
    averagex = ((x0 + x1)/2)
    stddraw.line(x0, y0, x1, y0)
    stddraw.line(averagex, y0, averagex, y1)
    stddraw.line(averagex, y1, x1, y1)
    stddraw.line(x1, y1, x1, y2)

#Word Blanks
def wordBlanks(Letters, y):
        width = abs(xmax) + abs(xmin)  
        lengthX = width/(Letters)
        for i in range(Letters):
                stddraw.line(((lengthX*(i)+ xmin)), y, (lengthX*(i+1) + (xmin - 0.5)), y)

#Fill Blanks
def fillBlanks(letter,letternumber,Letters, y):
        stddraw.setFontFamily("Jokerman")
        width = abs(xmax) + abs(xmin)  
        lengthX = width/(Letters)
        stddraw.text((((lengthX*(letternumber +1)+ xmin) + (lengthX*(letternumber) + (xmin - 0.5)))/2), y, letter)


#Fill Wrong Letters

def wrongLetter(letter, guessesLeft, y):
        stddraw.setFontFamily("Jokerman")
        width = (abs(xmax) + abs(xmin))/2  
        lengthX = width/(8)
        stddraw.text((((lengthX)*(-1*guessesLeft))-0.5), y, letter)     

def HangmanMan(x, y, guessesLeft):
        if guessesLeft <= 7:
                stddraw.circle(x,y-1,1)

                if guessesLeft <= 6:
                        stddraw.line(x, y-1.9,x, y-4)

                        if guessesLeft <= 5:
                                stddraw.line(x, y-2.1, x+0.5, y-4)
                                if guessesLeft <= 4:
                                        stddraw.line(x, y-2.1, x-0.5, y-4)

                                        if guessesLeft <= 3:
                                                stddraw.line(x,y-4,x+0.5, y-6)
                                                if guessesLeft <= 2:
                                                        stddraw.line(x,y-4,x-0.5, y-6)

                                                        if guessesLeft <= 1:
                                                                stddraw.line(x-0.75,y-1, x-0.25, y-0.5)
                                                                stddraw.line(x-0.75,y-0.5, x-0.25, y-1)
                                                                stddraw.line(x+0.75,y-1, x+0.25, y-0.5)
                                                                stddraw.line(x+0.75,y-0.5, x+0.25, y-1)
                                                                if guessesLeft <= 0:
                                                                        stddraw.setPenColor(stddraw.BLACK)
                                                                        stddraw.circle(x, y-1.55, 0.30)
                                                                        stddraw.setPenColor(stddraw.WHITE)
                                                                        stddraw.filledRectangle(x-0.49,y-1.8,0.8,0.3)
                                                                        stddraw.setPenColor(stddraw.BLACK)



                                                                
                