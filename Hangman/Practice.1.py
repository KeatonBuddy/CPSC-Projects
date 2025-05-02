import stddraw
stddraw.setXscale(-10,10)
stddraw.setYscale(-10,10)
def HangmanMan(x, y, guessesLeft):
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.circle(x, y-1.55, 0.30)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledRectangle(x-0.49,y-1.8,0.8,0.3)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.circle(x,y-1,1)

        stddraw.line(x, y-1.9,x, y-4)

        stddraw.line(x, y-2.1, x+0.5, y-4)
        stddraw.line(x, y-2.1, x-0.5, y-4)

        stddraw.line(x,y-4,x+0.5, y-6)
        stddraw.line(x,y-4,x-0.5, y-6)

        stddraw.line(x-0.75,y-1, x-0.25, y-0.5)
        stddraw.line(x-0.75,y-0.5, x-0.25, y-1)
        stddraw.line(x+0.75,y-1, x+0.25, y-0.5)
        stddraw.line(x+0.75,y-0.5, x+0.25, y-1)

    
HangmanMan(0,0,8)

stddraw.show()