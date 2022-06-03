#!/usr/bin/env python3

my_set = {1, 2, 3, 4, 5, 5, 4, 3}
print(my_set) #it's only showing the unique items
my_set.add(2)
my_set.add(6)
print(my_set)
print(5 in my_set)
print(len(my_set))


# create a set from list
my_list = [1, 2, 3, 4, 5, 4, 3, 6]
print(my_list)
my_newset = (set(my_list)) # set to list 
print(my_newset)
my_newset.add(7)
print(my_newset)
my_newlist = (list(my_newset)) # list to set
print(my_newlist)

your_set = {2, 4, 14, 6, 7, 8, 11, 12}
print(my_set.difference(your_set)) # your_set doesn't have 1 and 3
print(your_set)
your_set.discard(11) # removes 11 in the set
print(your_set)

#difference between 2 sets 
friends = {"Bob", "MH", "Anne"}
at_home = {"Bob", "Anne"}
family = friends.difference(at_home)
print(family)

#make into 1 set 
shopping_list = {"fruit", "bread"}
shopping_list_on_phone = {"coffee"}
shopping = shopping_list.union(shopping_list_on_phone)
print(shopping)

#intersection
math = {"Bob", "Anne", "MH"}
science = {"Bob", "MH", "Adam", "Hassan"}
both = math.intersection(science)
print(both)
