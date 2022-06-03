#!/usr/bin/env python3

from colorama import Fore
import random

#parameters 
def panel_login(user_name, user_level):
    '''
    This functions prints in console a username and userlevel when they log in into the panel.
    '''
    print(Fore.YELLOW + f'[LOG:] User {user_name} is logged in on level {user_level} in the panel' + Fore.RESET)

#arguments 
print(panel_login.__doc__)
panel_login('MiamiHacker', 3)

#return in function
def easy_sum(num1, num2):
    return num1 + num2
total = easy_sum(10, 20)
print(total)

#nested function with return 
def my_sum(num1, num2):
    def my_nested_sum(n1, n2):
        return n1 + n2
        # after return it exits the function
        print('This will not be printed')
    return my_nested_sum(num1, num2)
my_total = easy_sum(6, 20) # change the sum(6, 20) for function is_even()
print(my_total)

def is_even(my_total):
    return my_total % 2 == 0 
print(is_even(my_total))

def super_function(*args, **kwargs):
    randomlist_total = 0
    randomlist = random.sample(range(1, 10), 8)
#    for random_items in kwargs.values():
#        randomlist_total += random_items
#    sum(randomlist)
    total_evens = 0
    evens = []
    for number in randomlist:
        if number %2 == 0:
            evens.append(number)
    print(f'sum_randomlist {randomlist_total}')
    print(f'random list: {randomlist}:')
    print(evens)
    # total_evens += evens
    # print(total_evens)

    # TODO = randomlist_total not working yet
    # print(randomlist)
    # print(randomlist_total)
    # print(random_items)
    total = 0
    for items in kwargs.values():
        total += items
    # print(args)
    # print(kwargs)
    return sum(args) + total + randomlist_total
print(super_function(1,2,3,4,5, num1=5, num2=10))

print("------------------------------------")

def my_age_in_seconds():
    age = int(input("Enter your age: "))
    age_in_seconds = age * 365 * 24 * 60 * 60
    print(f"You're {age_in_seconds} seconds old.")
my_age_in_seconds()

def my_name(name, surname):
    print(f"I am {name} {surname}")
my_name("Miami", "Hacker")

def divide(dividend, divisor):
    if dividend != 0:
        print(dividend / divisor)
    else:
        print("You can't divide with 0")
# the proper way to make it clear in python 
divide(dividend=15,divisor=2)