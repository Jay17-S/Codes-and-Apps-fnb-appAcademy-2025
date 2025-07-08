# CONTROL STATEMENTS - are a fundamental component of programing langauges that allow us to control the flow of execusion based on certain conditions.

# In python we Primaraly use 3 types of control statements:- 1. if > 2. elsif > 3. elsestatement

# E.G:: WHAT IF WE HAD A DESTINATION, AND WE HAD TWO ROUTES TO THAT DESTINATION THE FIRST ROUTE IS TAR ROAD WHICH IS SAFE AND 5KM LONG
#    :: AND THE SECOND ROUTE IS A GROVEL ROAD 1KM LONG, IN A SUNNY DAY YOU WILL USE THE GROVEL BUT IN A RAINY DAY YOU WILL TAKE THE LONG ROUTE
#    :: WHICH IS SAFER. > THIS IS 

# ESSENTIALY THE CONTROL STATEMENT, IS CHOOSING THE CORRECT ROUTE BASED ON A CERTAIN CONNDITION

#1. if > STATEMENT

 num = 10
 if num > 0:
    print("The number is positve")

    
# BUT WHAT IF WE SAID

 num = -5
  if num > 0:
     print("The number is positve")
  else:
     print("This number is either 0 or negative")

#-----------------------------------------------------------------------------------------------------------

#2. elseif > STATEMENT

# IF WE WANTED TO CHECK MULTIPLE CONDITIONS, WE USE THE elseif STATEMENT. IT ALLOWS US TO CHECK FOR MULTIPLE CONDITIONS, 1 AFTER THE OTHER

#elseif E.G = (elif
# )

num = 0
if num > 0:
    print("The number is positve")
elif num == 0:
    print("This number is zero")
else:
    
    print("This number is negative")