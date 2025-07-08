#LOOP CONTrol STATEments

fruits = ["apples", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break # break exits the loop if cherry is found (or any loop). so it doesn't continue to anything after that.
    print(fruit)
    
print()

fruits = ["apples", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        continue # continue will skip cherry and to the iteration
    print(fruit)
    
print()

fruits = ["apples", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        pass # pass is a place-holder, no action is needed for cherry(when changing or replacing data, we saying when it reaches this value to leave it as it is)
    print(fruit)
    
#------------------------------------------------------------------------------------------------------------------------------

#while loops in Control Statements

count = 0

while count < 5:
    print(count)
    count += 1
    if count ==3:
        break # exit loop when the count is reached, which is 3 (the code will start counting from 0 and stop at 2, because after two its 3 therfore it wont show it in output)
    
    