#!/usr/bin/env python3

my_set = {1, 2, 3, 4, 5, 5, 4, 3}
your_set = {2, 4, 14, 6, 7, 8, 11, 12}

# it is only showing the difference 
print(f'LOG: difference_update before my_set{my_set}')
print(f'LOG: difference_update before your_set{your_set}')
# difference_update
print(f'LOG: Show the difference_update: {my_set.difference_update(your_set)}')
print(f'LOG: difference_update after my_set{my_set}')
print(f'LOG: difference_update after your_set{your_set}')
update_set = my_set.difference(your_set)
print(update_set) # my_set == update_set (so need needed to create a new variable)