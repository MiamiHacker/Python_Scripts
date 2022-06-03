#!/usr/bin/env python3

def hidden_password():
    username = input("What is your username?")
    password = input("What is your password?")

    password_length = len(password)
    hidden_password = '*' * password_length

    print(f'{username}, your password, {hidden_password}, is {len(password)} characters long')
hidden_password()