#!/usr/bin/env python3

#input is always a string => set var to int 
money_input = input("How much money you want to borrow?")
months_input = input("In how many months you want to pay it back?")
money_int = int(money_input)
months_int = int(months_input)
interest = 1.07 
monthly_payment = (money_int * interest) / months_int
print(f"Your monthly payment is {monthly_payment:.2f}") # 2 decimals 

# or do it like this with int
user_age = int(input("Enter your age: "))
months = user_age * 12
days = user_age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"Your age {user_age}, is equal to {months} months, or {days} days, or {hours} hours, or {minutes} minutes, or {seconds} seconds")