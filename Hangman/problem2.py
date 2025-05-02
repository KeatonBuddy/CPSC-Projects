import stddraw
import math
import time
time_aggregate = time.localtime()
hour = time_aggregate.tm_hour
minute = time_aggregate.tm_min
second = time_aggregate.tm_sec

stddraw.setPenColor(stddraw.BOOK_RED)
stddraw.filledRectangle(0,0,1,1)
stddraw.setPenColor(stddraw.LIGHT_GRAY)
stddraw.filledCircle(0.5, 0.5, 0.45)



stddraw.setPenColor(stddraw.BLACK)
for i in range(12):
    theta = math.radians(i * 30 +30)
    stddraw.setFontSize(25)
    stddraw.setFontFamily("Times New Roman")
    stddraw.text(0.5 + 0.40 * math.sin(theta), 0.5 + 0.40 * math.cos(theta), str(i+1))
for i in range(60):
    theta = math.radians(i * 6)
    stddraw.setPenRadius(0.003)
    stddraw.line(0.5 + 0.44 * math.sin(theta), 0.5 + 0.44 * math.cos(theta), 0.5 + 0.448 * math.sin(theta), 0.5 + 0.448 * math.cos(theta))
for i in range(12):
    theta = math.radians(i * 30)
    stddraw.setPenRadius(0.009)
    stddraw.line(0.5 + 0.435 * math.sin(theta), 0.5 + 0.435 * math.cos(theta), 0.5 + 0.445 * math.sin(theta), 0.5 + 0.445 * math.cos(theta))


stddraw.setPenRadius(.005)
stddraw.setPenColor(stddraw.RED)
secondangle = math.radians(6 * second)
stddraw.line(0.5, 0.5, 0.5 + 0.4 * math.sin(secondangle), 0.5 + 0.4 * math.cos(secondangle))


stddraw.setPenRadius(.015)
stddraw.setPenColor(stddraw.GRAY)
minuteangle = math.radians(6 * minute)
stddraw.line(0.5, 0.5, 0.5 + 0.3 * math.sin(minuteangle), 0.5 + 0.3 * math.cos(minuteangle))



stddraw.setPenRadius(.01)
stddraw.setPenColor(stddraw.BLACK)
hourangle = math.radians((30 * hour)+((minute/60)*30))

stddraw.line(0.5, 0.5, 0.5 + 0.2 * math.sin(hourangle), 0.5 + 0.2 * math.cos(hourangle))


stddraw.show()
