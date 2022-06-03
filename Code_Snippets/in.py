#!/usr/bin/env python3


letters = {"a", "b", "c", "e", "x"}
letter_input = input("Type in a letter (a / z)").lower()

is_letter_in = letter_input in letters
print(is_letter_in)


if letter_input in letters:
    print(f"The letter {letter_input} is in the list")
else:
    print(f"The letter {letter_input} is not in the list")