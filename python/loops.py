#LOOPS - ARE AN ESSENTIAL CONCEPT IN PROGRAMING, THAT ALLOW US TO EXECUTE A BLOCK OF CODE REPEATEDLY.
#       THEY HELP AUTOMATE REPEATITIVE TASKS AND MAKE OUR PROGRAMS MORE EFFECIENTLY

# IN PYTHON THERE ARE TWO MAIN TYPES OF LOOPS, THE 1. for LOOP, AND THE 2. while LOOP

#1. THE for LOOP

#- USED TO ITERATE OVER A SEQUENCE, SUCH AS A LIST, TOPLE, STRING OR RANGE, AND PERFORM AN ACTION FOR EACH ITEM IN A SEQUENCE.
'''
 fruits = ( "apple", "banana", "cherry")

 for fruit in fruits:
    print (fruit)

 numbers = (1,2,3,4,5,6,7)

 for number in numbers:
    print(number)
    
'''
#2. While LOOP - to count from 1 to 5

#- IN PYTHON IS USED TO EXECUTE A BLOCK OF CODE AS LONG AS A CERTAIN CONDITION IS = TRUE
count = 1 # the count will start from 1

while count <= 5: # the cound will end at 5 and not go to 6 or above
    print(count)
    count += 1 #This increments the count by 1
