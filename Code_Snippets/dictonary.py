#!/usr/bin/env python3

'''
Iterable in python:
list, dictonary, tuple, set, string
'''

#Dictionary
dictionary = {
    'a': 1,
    'b': [2,3,4,5],
    'c': 'python'
}
print(dictionary['b'][3])
print(dictionary.get('d')) # none
print('d' in dictionary)

# gives the keys of the dictonary
for item in dictionary:
    print(item)

for item in dictionary.keys():
    print(item)

# key value pair in a tuple
for item in dictionary.items():
    print(item)
for key, value in dictionary.items(): #or use k and v 
    print("=> ", key, value)


# values of the dictonary
for item in dictionary.values():
    print(item)


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for item in my_list:
    count = count + item
print(count)

print("###############################")

friends = [
    {"name": "Anne", "age": 19},
    {"name": "Angela", "age": 20},
    {"name": "Britt", "age": 18},
]

print(friends[1]["name"])

friends_list = {"Anne": 19, "Angela": 20, "Britt": 18}
for list in friends_list:
    print(f"{list}: {friends_list[list]}")
if "Angela" in friends_list:
    print("Party Time!!")
else:
    "Time to study."


# **nums you can use all values in the dictionary 
def add(x,y):
    return x + y
nums = {"x": 10, "y": 20}
print(add(**nums))

def named(name, age):
    print(name, age)
details = {"name": "Anne", "age": 18}
named(**details)