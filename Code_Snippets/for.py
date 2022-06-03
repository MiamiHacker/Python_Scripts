#!/usr/bin/env python3

os = ["Ubuntu", "Linux", "Kali", "Parrot"]
for distro in os:
    print(f"[ + ] {distro}")



numbers = [27, 182, 39, 153, 70, 129]
total = 0 
amount = len(numbers)

for number in numbers:
    total += number
print(total / amount)

# or like this:
numbers = [27, 182, 38, 153, 71, 129]
total = sum(numbers) 
amount = len(numbers)
print(total / amount)