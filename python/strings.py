#Basics - Strings

#strings - represent text data

#message = "Hello world" #message - is a variable: a variable is container for a value  any ("string") or number

print (message) # here is where we have called our variable

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#advanced concepts - Strings

#You can access individual charecters within a string by using "indexing" it starts from 0 for the first charecter, 1 for the second charecter and -1 for the last charecter


message = " Hello World  "

print(message[0])# output is 'h'
print(message[3])# outputs "l"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#What if we want to find the complete length of our string? 
# For this we use function (len(string goes here))
# It also counts the space or gaps, everything

print (len(message))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Multiple Differnt METHODS to manipulate strings
#Most common built in Methods are : upper, lower, strip, slpit and replace

#1 Strip- Removes leading and trailing white spaces or gaps. E.G:-

print(message.strip())

#------------------------------------------------------------------------------

#2. Lower- Converts all uppper case to lower case

print (message.lower())

#-----------------------------------------------------------------------------

#3. split - splits the one string into two strings base on a comma

print(message.split())

#-----------------------------------------------------------------------------

#4 Upper - Turns the string into upper case

print(message.upper())

#----------------------------------------------------------------------------

#5. Replace - Replaces old value contained in a variable with a new one

message = (" Hello World ")
new_message = message.replace(" Hello World ", "mind games")
print(new_message)


new_message = ("mind games")                                                                                               
new_new_message = new_message.replace ("mind games", "sports games".upper())
print (new_new_message)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

