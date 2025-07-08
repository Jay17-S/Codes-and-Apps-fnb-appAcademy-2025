# SETS - A set in python is an unborthered collection of unique elements.
# - unlike list or tuples, sets do not allow duplicate data
# - sets are useful when you want to perform operations like 1.union, 2.intersection and 3. the difference between a collection of elements

# sets are un-ordered and immutible. But can add and remove but dont allow for duplicates

# IN SETS WE USE CURLY BRACKETS {}

my_set = {1,2,3,4,5}
print(my_set)

# ---------------- ADDING TO SETS --------------

my_set.add(6)
print(my_set)

# ---------------- REMOVING FROM SETS -------------

my_set.remove(3)
print(my_set)

#------------- OPERATIONS IN SETS -------------- OPERATIONS IN SETS --------------------- OPERATIONS IN SETS ------------------------- OPERATIONS IN SETS ------------------

# Sets supports various operations that allow you to manipulate and compare colletions of elements, we can use

# 1. Union - Combines two sets and removes any duplicate data

set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

# 2. Intersection - Finds the common element between two sets 
set1 = {1,2,3}
set2 = {3,4,5}
inter_set = set1.intersection(set2)
print(inter_set)

# 3. Difference -  Finds elements that are present in one but not the other

diff_set = set1.difference(set2)
print(diff_set)

# sets are Useful when working with collections of unique elements and perform eoperations like finding differences, intersections or union between sets.
# - some common use include, 1. removing duplicate data form list or collection.
#                              2. Checking memberships efficiently 