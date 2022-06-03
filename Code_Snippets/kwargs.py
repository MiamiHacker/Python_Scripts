#!/usr/bin/env python3

def named(**kwargs):
    print(kwargs)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
print_nicely(name="MiamiHacker", age=19)


def both(*args, **kwargs):
    print(args)
    print(kwargs)
both(5, 12, 21, 74, name="MiamiHacker", age=19)