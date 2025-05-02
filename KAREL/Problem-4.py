from karel import *
def turn_around():
    turn_left()
    turn_left()
    
def check_front():
        if front_is_clear():
            move()
        if beepers_present():
            turn_around()
            move()
            turn_around()
            pick_beeper()
            move()
        else:
            turn_around()
            if front_is_clear():
                end_karel_program()

          
            
begin_karel_program()


while not beepers_present():
    put_beeper()
    if front_is_clear():
        move()       
turn_around()



while beepers_present():
    check_front()
    move()
    while front_is_clear():
        move()
    turn_around()
    while not beepers_present():
        move()

        



end_karel_program()
