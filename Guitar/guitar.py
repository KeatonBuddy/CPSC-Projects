import collections
import random
import math



class GuitarString:
    def __init__(self,f):
        self.freq = f
        self.wavetable = collections.deque()
        self.p = math.ceil(44100 / f)
        for i in range(self.p):
            self.wavetable.append(0.0)

    def pluck(self):
        self.wavetable.clear()
        for i in range(self.p):
            rand = random.uniform(-0.5, 0.5)
            self.wavetable.append(rand)

    def tick(self):
        y = 0.996 * 0.5 * (self.wavetable[0]+ self.wavetable[1])
        self.wavetable.append(y)
        self.wavetable.popleft()
        return y

 