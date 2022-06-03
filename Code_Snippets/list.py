#!/usr/bin/env python3

#list slicing
shopping_list = [
    'coffee',
    'water',
    'coding books'
]
shopping_list[2] = 'beer'
print(f'It\'s weekend so we need {shopping_list}')


random_words = [
    ["fork", "beginning", "grandfather", "marble", "coalition"],
    ["loyalty", "frame", "lid", "dirty", "monster"],
]
print (random_words[1][4])
random_words.append("yoga")
new_random_words = random_words
print(random_words)
print(new_random_words)
print (random_words[2][0:4])

# insert
numbers = [0,1,2,3,4,5,6,7,8,9, 100]
numbers.insert(6, 4)
print(numbers)

# remove
numbers.pop(0)
print(numbers)
numbers.remove(100)
print(numbers)
numbers.clear()
print(numbers)

#index
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'g']
print('d' in letters)
print(letters.index('d', 2, 6)) #start indexing from 2 to 6 in list
letters.sort()
print(letters)
letters.reverse()
print(letters)
join = ' '.join(['i', 'am', 'on', 'python'])
print(join)

