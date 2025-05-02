from karel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()

        
begin_karel_program()

turn_left()
move()
turn_right()
while front_is_clear():
    move()

for i in range(4): 
    while not front_is_clear():
        if not beepers_present():
            put_beeper()
        if not front_is_clear():
            turn_left()
        if front_is_clear():
            move()
            turn_right()
    move()
    turn_right()
    move()
    turn_right()

end_karel_program()

