#!/usr/bin/env python3

from email.quoprimime import quote


def my_skull():
    long_string = '''
    ───────█████████████████████
    ────████▀─────────────────▀████
    ──███▀──────Malware V0.1─────▀███
    ─██▀───────────────────────────▀██
    █▀──────────────by───────────────▀█
    █─────────────────────────────────█
    █───────────MiamiHacker───────────█
    █─────────────────────────────────█
    █───█████─────────────────█████───█
    █──██▓▓▓███─────────────███▓▓▓██──█
    █──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█
    █──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
    █▄──████▓▓▓▓██───────██▓▓▓▓████──▄█
    ▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀
    ──█▄────▀█████▀─────▀█████▀────▄█
    ─▄██───────────▄█─█▄───────────██▄
    ─███───────────██─██───────────███
    ─███───────────────────────────███
    ──▀██──██▀██──█──█──█──██▀██──██▀
    ───▀████▀─██──█──█──█──██─▀████▀
    ────▀██▀──██──█──█──█──██──▀██▀
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ──────────██──█──█──█──██
    ───────────█▄▄█▄▄█▄▄█▄▄█
    '''
    print(long_string)
my_skull()


anonymous = "We are Anonymous, we are legion, we do not forgive, we do not forget. \"Expect us\""
print(anonymous)
print("Starts at:", anonymous.find('legion'))
tab_spacing = "\t Tab Spacing: " + anonymous
print(tab_spacing)


system = "Linux"
print(system.replace('Lin', 'T'))
new_system = system.replace('Lin', 'T')
print(new_system)
print(system)
year = 1970
# formatted string
print(f'Hi from {system} in the year {year}')
print(system[4])


# String Indexes
numbers = '0123456789'
# [reverse:]
print(numbers[::-1])
# [start:]
print(numbers[7:])
# [start:stop]
print(numbers[4:7])
# [start:stop:stepover]
print(numbers[0:9:2])


def hidden_password():
    username = input("What is your username?")
    password = input("What is your password?")

    password_length = len(password)
    hidden_password = '*' * password_length

    print(f'{username}, your password, {hidden_password}, is {len(password)} characters long')
hidden_password()


name = "MiamiHacker"
greeting = f"Hello, {name}"
print(greeting)
with_name = greeting.format(name)
print(with_name)