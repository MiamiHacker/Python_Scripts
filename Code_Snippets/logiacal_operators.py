#!/usr/bin/env python3

is_hacker = True
is_expert = False

if is_expert and is_hacker:
    print("you're a master")
elif is_hacker and not is_expert:
    print("keep on learning")
elif not is_expert:
    print("start hacking today")
else:
    print("You're a expert in something else")