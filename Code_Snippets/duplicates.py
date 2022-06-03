#!/usr/bin/env python3

#not in a set 
my_list = ['m', 'i', 'a', 'm', 'i', 'h', 'a', 'c', 'k', 'e', 'r']

dupli = []
for value in my_list:
    if my_list.count(value) > 1:
        if value not in dupli:
            dupli.append(value)
print(f'The duplicated letters are {dupli}')