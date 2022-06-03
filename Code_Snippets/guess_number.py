#!/usr/bin/env python3
import random

while True:
    number = random.randint(1, 10)
    user_input_play = input("Enter 'y' if you would like to play: ").lower()
    if user_input_play in ("y", "yeah", "yes"):
        user_input_number = int(input("Guess the number between 1 - 10: "))
        if user_input_number == number or user_input_number == 000: # 000 is a cheat
            print(f"Well done it's number {number}")
        elif abs(number - user_input_number) == 1:
            print(f"That was pretty close, the number is {number}")
        else:
            print(f"Wrong it was number {number}, Game Over!!")
    else:
        break