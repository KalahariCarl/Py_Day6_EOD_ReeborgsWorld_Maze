# main.py - my own code
# main_coursefile.py - answer as given by the udemy course

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right() and not wall_in_front():
        move()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif not wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()
        
