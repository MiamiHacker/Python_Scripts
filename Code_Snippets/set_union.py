#!/usr/bin/env python3

my_set = {1, 2, 3, 4, 5, 5, 4, 3}
your_set = {2, 4, 14, 6, 7, 8, 11, 12}

# it is union the sets   
print(f'LOG: difference_of my_set{my_set}')
print(f'LOG: difference of your_set{your_set}')
#print(f'LOG: Show the difference: {my_set.difference(your_set)}')
print(my_set.union(your_set))

#or use 
print(my_set | your_set)