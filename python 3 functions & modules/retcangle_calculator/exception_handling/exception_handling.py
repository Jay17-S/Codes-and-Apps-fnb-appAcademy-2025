#  in python exception handling allows a programmer to deal with run time error or exception.
# an exception is a event that occurs during the excecution of a program, disrupting the normal program flow or execution.
# Python "try" amd "accept" blocks are used for exception handling. the 
# try block - contains the code that may raise and exception
# except block - contains the code that will execute if an exception occurs
'''
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("an exception occured")
''' 
'''
# the finally block
try: 
    print(x)
finally:
    print("the 'try except' is finished")
''' 

# the else block in exception handling

# the else block - will excecute if only no exceptions are raised in the try block
'''
try:
    print(x)
except NameError:
    print("variable x is not defined")
else:
    print("Everything went wrong")
''' 
x = -1

if x < 0:
    raise Exception("sorry no numbers less than zero")