# functions are a fundamental way to structure your code in python, they allow you to incapsulatee a piece of code and reuse it through out your program
#  in python you define a function using the "def" keyword, followed by the function name "Cars" and parentheses "()". inside these parentheses you can specify any parameters "("Mac,Bimmer,suzu")" that your function should take...
# ... after the parentheses you can have a colon ":" to start the indented block of code that makes up th block of the function. E.G>...
'''
def greet(name): #greet is the name of the function & "(name)" is a parameter
    print(f"Hello {name}") #
    
# to call this function. function call
greet ("alice")

# functions can also return a value using the "return" keyword. this allows yo to produce a result that you can use elsewhere in your code.abs

def add(a, b):
    return a + b

results = add(2, 5)
print(results)
'''
# functions in python can also handle more complex task, can contain loops, cnditional statements etc.
# for instance condisnder the following functions that calculate the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)  
    
def greet(name, greeting= "Hello"):
    print(f"{greeting}, {name}")
    
greet("bob", "hello goodmorning")