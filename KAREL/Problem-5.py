from karel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()

def square():
    if front_is_clear():
        put_beeper()
        move()
        turn_left()
        if front_is_clear():
            move()
            put_beeper()
            turn_left()
            if front_is_clear():
                move()
                turn_right()
                if front_is_clear():
                    move()
                    turn_right()

                else:
                    if front_is_clear():
                        turn_right()
                    else:
                        turn_right()
                        move()
                        turn_right()
                        while front_is_clear():
                           move()
                        turn_left()
                        if front_is_clear():
                            move()
            else:
                turn_right()
                move()
        else:
            turn_around()
            while front_is_clear():
                move()
            turn_left()
            move()
            
    else:
        put_beeper()
        turn_left()
        if front_is_clear():
            move()
            turn_right()
            if not front_is_clear():
                turn_left()
                move()
                turn_right()
        else:
            turn_around()
            while front_is_clear():
                move()
begin_karel_program()

while not beepers_present():
    square()


end_karel_program()
