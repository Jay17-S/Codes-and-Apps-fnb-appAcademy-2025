# Tuples - a tuple in python is a collection of ordered elements, similar to lists, but
# Unlike list, tuples cannot be changed, added or removed.
# they are ordered, unchangable but they allow duplicates.

my_tuple = (1,2,3,4,5)
print(my_tuple)

# ACCESSING ELEMENTS IN A TUPLE - you can access elements in a tuple just like in lists

print(my_tuple[3]) # it  prints out 4 in the console.

# You can also use negative/minus [-1] indexing to print out the last tuple

print(my_tuple[-1]) # prints out 5

# DIFFERENT OPERATIONS THAT CAN BE USED WITH TUPLES -------------------------------------------

# 1. CONCATINATION - adding two or more tuples together with addition operator (+)

tuple1 = (1,2,3)
tuple2 = (4,5,6)

print( tuple1 + tuple2) # outputs (123456) in a single line

# or wecan use

conc_tuple = tuple1 + tuple2
print(conc_tuple) 


# 2. REPITITION - having 1 tuple and using multiplication operator (*) to multiply that tuple 

rep_tuple = tuple1 * 4
print(rep_tuple)

# WHEN DO WE USED TUPLES? 

# tuples are suitable for a situation where you wanna store a collection of elements that should not be changed towards your programs execusions.
# When dealing with data such as, cor-ordinates, rgb codes, database records etc. 