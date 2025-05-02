from karel import *
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def movewith_beeper():
    put_beeper()
    move()
def diagonal_beeper():
    move()
    put_beeper()
    turn_left()
    move()
    turn_right()
def diagonal_beeper2():
    move()
    put_beeper()
    turn_right()
    move()
    turn_left()
def triangle():
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_left()

begin_karel_program()

move()
put_beeper()
turn_left()
while front_is_clear():
    movewith_beeper()
put_beeper()
turn_around()
for i in range(20):
    move()
turn_left()
for i in range(20):
    diagonal_beeper()
move()
put_beeper()
turn_right()

for i in range(20):
    move()
turn_right()
for i in range(21):
    move()
turn_around()
for i in range(19):
    diagonal_beeper2()
move()
movewith_beeper()

move()
move()


turn_left()
while front_is_clear():
    movewith_beeper()
turn_right()
for i in range(10):
    movewith_beeper()


turn_right()
move()
turn_left()

triangle()

move()
turn_right()
move()
turn_left()
triangle()
turn_right()
move()
put_beeper()

turn_left()
triangle()
turn_right()
for i in range(4):
    movewith_beeper()
put_beeper()
turn_right()

move()
put_beeper()
turn_left()
move()
put_beeper()
move()
put_beeper()
turn_right()
move()
put_beeper()
turn_left()

move()
turn_right()
move()

put_beeper()
turn_left()
move()
put_beeper()
turn_right()
move()
put_beeper()
turn_left()

move()
turn_right()
move()

for i in range(10):
    movewith_beeper()

turn_left()
move()
turn_left()
move()
move()
for i in range(12):
    movewith_beeper()

turn_right()
move()
turn_left()
triangle()

move()
turn_right()
move()

for i in range(18):
    movewith_beeper()
    
turn_right()
move()
put_beeper()
turn_left()
move()
put_beeper()
turn_right()
move()
put_beeper()
move()
turn_left()
move()
turn_right()
for i in range(11):
    movewith_beeper()

end_karel_program()
