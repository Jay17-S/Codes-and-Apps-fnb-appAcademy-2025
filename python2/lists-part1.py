# lists part 1
# - In python a list is a built in data structure that can hold a collection of items these items can be various types, such as intergers, strings and other lists.
# - lists are orderd and changable and even allow duplicates. By changable we mean values on the list can be changed. by duplicate we mean you can use the same value many times.

# When using list, we use sqare brackets []

### fruits = ["apple", "banana", "cherry"] # here the variable fruits is a list, that has contains 3 strings of fruits.
# you can access items in this list by refering to their item number. REMEMBER python starts counting from 0 and the last item will be -1

### print(fruits[0]) # the output displays apple as the first item on index.

# list are changable/mutable

### fruits[1] = "blueberry" #here we are changing the "banana" item which is in index [1] of the list of fruits, to Blueberry
### print(fruits) # in the output, the "banana" string has been replaced by "blueberry"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -------------- LISTS PART 2-------------- LISTS PART 2 ----------------------- LISTS PART 2 --------------------------- LISTS PART 2 ------------------ LISTS PART 2 --------------

# ADDING AND REMOVING ITEMS IN A LIST

#1. APPEND METHOD - To add item an extra item/items to the end of our list we use .append method 

fruits = ["apple", "banana", "cherry"]

fruits.append("kiwi")
print(fruits)

#2. ADDING VALUE TO SPECIFIC POSITION - 

fruits.insert(1, "orange") # this adds orange in the 1st position, moving banana to number 2 in our list.
print(fruits)

#3. REMOVE METHOD -
# - REMEMBER - if there's two duplicate values, python remove method will remove one instant/ item/ value.

fruits.remove("banana")
print(fruits)

#4. SORT METHOD - for sorting alphabetically or numerical in ascending order

fruits.sort()
print(fruits)

# SORTING IN REVERSE OR DESCENDING ORDER - YOU PASS AN ARGUEMENT IN PARENTHESES (reverse=true)

fruits.sort(reverse=True)
print(fruits)

