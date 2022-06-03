#!/usr/bin/env python3
import random

what_day = input("What day is it today? ").lower()

if what_day == "saturday" or what_day == "sunday":
    print("It's weekend!")
elif what_day == "friday":
    print("It's allmost weekend!")
else:
    number = random.randint(1, 3)
    if number == 1:
        print("I wish your luck till the weekend.")
    elif number == 2:
        print('Are you kidding me?')
    else:
        print("Feels like it will be never weekend again.")