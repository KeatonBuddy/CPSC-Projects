import math
import random
import stddraw
import stdaudio
import sys
import stdstats

xlist = []
ylist = []
blendlist = []

stddraw.setYscale(-1,1)
white = []
audiolist = []

def blend(f,t,r):
    s = (  math.sin( ((math.pi ) * (f) * (t) / (r)) )  )**6
    return s

def brown(list1,list2,x1, y1, x2, y2, variance, scale):
    if (x2 - x1) < 1:
        return
    middlex = (x1+x2)/2.0
    middley = (y1+y2)/2.0

    sd = math.sqrt(variance)

    delta = random.normalvariate(0, sd)
    middley = middley + delta


    
    if list1 == []:
        list1.append(x1)
        list1.append(x2)
    list1.insert( ((len(list1))-1) , middlex )

    if list2 == []:
        list2.append(y1)
        list2.append(y2)

    list2.insert( ((len(list2))-1) , middley )


    brown(list1,list2,x1, y1, middlex, middley, variance / scale, scale)

    brown(  list1,list2,middlex, middley, x2, y2, variance / scale, scale)


    
def ocean(blendfactor,brownnoise,whitenoise):
    y = ( (( 1 - (blendfactor) ) * (brownnoise)) + ((blendfactor) * (whitenoise) ))
    return y
    



h = float(sys.argv[1])
scale = 2 ** (2*h)

for i in range(20):
    brown(xlist,ylist,0.0, 0.0, 44100, 0.0, 0.05, scale)


for i in range(len(xlist)):
    rand = random.uniform(-0.25, 0.25)
    white.append(rand)
    
for i in range(len(xlist)):
    v = blend(0.25,i,44100)
    blendlist.append(v)

for i in range(len(xlist)):
    k = ocean( blendlist[i], ylist[i], white[i] )
    audiolist.append(k)

    
print("play")
stdaudio.playSamples(audiolist)
