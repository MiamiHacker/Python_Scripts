#!/usr/bin/env python3

my_set = {1, 2, 3, 4, 5, 5, 4, 3}
your_set = {2, 4, 14, 6, 7, 8, 11, 12}

# it is only showing the intersection 
print(my_set.intersection(your_set))

# intersection_update works same like set_difference_update.py

#or use 
print(my_set & your_set)