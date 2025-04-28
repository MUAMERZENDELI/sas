from microbit import *
import random

secret = random.randint(1, 6)
choice = 1
display.show(choice)

while True:
    if button_a.was_pressed():
        choice += 1
        if choice > 6:
            choice = 1
        display.show(choice)
    if button_b.was_pressed():
        if choice == secret:
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
        sleep(2000)
        # Reset game
        secret = random.randint(1, 6)
        choice = 1
        display.show(choice)
