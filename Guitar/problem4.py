import math
import random
import stddraw
import stdaudio
from picture import Picture
from guitar import GuitarString

def frequency(n):
     k = 2**(n/12) * (110)
     return k


a1_string = GuitarString(frequency(0))
a1_5_string = GuitarString(frequency(1))
b1_string = GuitarString(frequency(2))
c1_string = GuitarString(frequency(3))
c1_5_string = GuitarString(frequency(4))
d1_string = GuitarString(frequency(7))
d1_5_string = GuitarString(frequency(8))
e1_string = GuitarString(frequency(9))
f1_string = GuitarString(frequency(8))
f1_5_string = GuitarString(frequency(9))
g1_string = GuitarString(frequency(10))
g1_5_string = GuitarString(frequency(11))


a2_string = GuitarString(frequency(12))
a2_5_string = GuitarString(frequency(13))
b2_string = GuitarString(frequency(14))
c2_string = GuitarString(frequency(15))
c2_5_string = GuitarString(frequency(16))
d2_string = GuitarString(frequency(17))
d2_5_string = GuitarString(frequency(18))
e2_string = GuitarString(frequency(19))
f2_string = GuitarString(frequency(20))
f2_5_string = GuitarString(frequency(21))
g2_string = GuitarString(frequency(22))
g2_5_string = GuitarString(frequency(23))


a3_string = GuitarString(frequency(24))
a3_5_string = GuitarString(frequency(25))
b3_string = GuitarString(frequency(26))
c3_string = GuitarString(frequency(27))
c3_5_string = GuitarString(frequency(28))
d3_string = GuitarString(frequency(29))
d3_5_string = GuitarString(frequency(30))
e3_string = GuitarString(frequency(31))
f3_string = GuitarString(frequency(32))
f3_5_string = GuitarString(frequency(33))
g3_string = GuitarString(frequency(34))
g3_5_string = GuitarString(frequency(35))

a4_string = GuitarString(frequency(36))


p = Picture("cpsc231-guitar.png")
stddraw.picture(p)
stddraw.show(0.0)


escape = False
while not escape:
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        elif key == chr(113):
            a1_string.pluck()
        elif key == chr(50):
            a1_5_string.pluck()
        elif key == chr(119):
            b1_string.pluck()
        elif key == chr(101):
            c1_string.pluck()
        elif key == chr(52):
            c1_5_string.pluck()
        elif key == chr(114):
            d1_string.pluck()
        elif key == chr(53):
            d1_5_string.pluck()
        elif key == chr(116):
            e1_string.pluck()
        elif key == chr(121):
            f1_string.pluck()
        elif key == chr(55):
            f1_5_string.pluck()
        elif key == chr(117):
            g1_string.pluck()
        elif key == chr(56):
            g1_5_string.pluck()



        elif key == chr(105):
            a2_string.pluck()
        elif key == chr(57):
            a2_5_string.pluck()
        elif key == chr(111):
            b2_string.pluck()
        elif key == chr(112):
            c2_string.pluck()
        elif key == chr(45):
            c2_5_string.pluck()
        elif key == chr(91):
            d2_string.pluck()
        elif key == chr(61):
            d2_5_string.pluck()
        elif key == chr(122):
            e2_string.pluck()
        elif key == chr(120):
            f2_string.pluck()
        elif key == chr(100):
            f2_5_string.pluck()
        elif key == chr(99):
            g2_string.pluck()
        elif key == chr(102):
            g2_5_string.pluck()




        elif key == chr(118):
            a3_string.pluck()
        elif key == chr(103):
            a3_5_string.pluck()
        elif key == chr(98):
            b3_string.pluck()
        elif key == chr(110):
            c3_string.pluck()
        elif key == chr(106):
            c3_5_string.pluck()
        elif key == chr(109):
            d3_string.pluck()
        elif key == chr(107):
            d3_5_string.pluck()
        elif key == chr(44):
            e3_string.pluck()
        elif key == chr(46):
            f3_string.pluck()
        elif key == chr(59):
            f3_5_string.pluck()
        elif key == chr(47):
            g3_string.pluck()
        elif key == chr(39):
            g3_5_string.pluck()



        elif key == chr(32):
            a4_string.pluck()
        
    y = a1_string.tick()
    y += a1_5_string.tick()
    y += b1_string.tick()
    y += c1_string.tick()
    y += c1_5_string.tick()
    y += d1_string.tick()
    y += d1_5_string.tick()
    y += e1_string.tick()
    y += f1_string.tick()
    y += f1_5_string.tick()
    y += g1_string.tick()
    y += g1_5_string.tick()
    y += a2_string.tick()
    y += a2_5_string.tick()
    y += b2_string.tick()
    y += c2_string.tick()
    y += c2_5_string.tick()
    y += d2_string.tick()
    y += d2_5_string.tick()
    y += e2_string.tick()
    y += f2_string.tick()
    y += f2_5_string.tick()
    y += g2_string.tick()
    y += g2_5_string.tick()
    y += a3_string.tick()
    y += a3_5_string.tick()
    y += b3_string.tick()
    y += c3_string.tick()
    y += c3_5_string.tick()
    y += d3_string.tick()
    y += d3_5_string.tick()
    y += e3_string.tick()
    y += f3_string.tick()
    y += f3_5_string.tick()
    y += g3_string.tick()
    y += g3_5_string.tick()
    y += a4_string.tick()


    stdaudio.playSample(y)