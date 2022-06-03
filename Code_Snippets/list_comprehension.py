#!/usr/bin/env python3

numbers = [5, 10, 20]
doubled = []

for num in numbers:
    doubled.append(num * 2)
print(doubled)

# or this way 
tripled = [x * 3 for x in numbers]
print(tripled)



friends = ['Bob', "Anne", "Adam", "Angela", "Tom"]
starts_a = []

for friend in friends:
    if friend.startswith("A"):
        starts_a.append(friend)
print(starts_a)

#or this way 
another_starts_a = [friend for friend in friends if friend.startswith("A")]
print(another_starts_a)