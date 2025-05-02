from karel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()


begin_karel_program()
for i in range(5):
    move()
while beepers_present():
    pick_beeper()




end_karel_program()
