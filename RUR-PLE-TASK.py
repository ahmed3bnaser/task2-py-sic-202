def turn_right():
    turn_left()
    turn_left()

    turn_left()


def go_back():
    turn_left()

    turn_left()


def play():
    if front_is_clear():
        move()

    if left_is_clear():
        turn_left()

    if right_is_clear() and not front_is_clear():
        turn_right()

    if not front_is_clear():
        go_back()

    if on_beeper():
        turn_off()

    play()


play()
