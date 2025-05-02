import math
import stdstats
import stddraw
import random
import sys


stddraw.setXscale(0, 129)
stddraw.setYscale(-1, 1)
stddraw.setPenRadius(0.01)

xlist = []
ylist = []

def brown(xlist,ylist,x1, y1, x2, y2, variance, scale):
    
    if (x2 - x1) < 1:
        stddraw.line(x1, y1, x2, y2)
        return
    middlex = (x1+x2)/2.0
    middley = (y1+y2)/2.0

    sd = math.sqrt(variance)

    delta = random.normalvariate(0, sd)
    middley = middley + delta


    
    if xlist == []:
        xlist.append(x1)
        xlist.append(x2)
    xlist.insert( ((len(xlist))-1) , middlex )

    if ylist == []:
        ylist.append(y1)
        ylist.append(y2)

    ylist.insert( ((len(ylist))-1) , middley )


    brown(xlist,ylist,x1, y1, middlex, middley, variance / scale, scale)

    brown(xlist,ylist,middlex, middley, x2, y2, variance / scale, scale)


    

    



h = float(sys.argv[1])
scale = 2 ** (2*h)
brown(xlist,ylist,0.0, 0.0, 129, 0.0, 0.05, scale)
print(xlist)
print(ylist)
stddraw.show()
