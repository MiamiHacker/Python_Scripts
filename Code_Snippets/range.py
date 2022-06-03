#!/usr/bin/env python3

#range object
import enum
from multiprocessing.connection import wait


print(range(5, 10))

for _ in range(1, 10): #3th value like (1, 10, 2) will step over
    print(_, "Email send to target")



#enumerate is useful if you need the index counter of the item
for i,char in enumerate('hacking'):
    print(i, char)

for i,char in enumerate('hacking'):
    #print(i, char)
    if char == 'k':
        print(f'k is on index: {i}')