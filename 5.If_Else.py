# If-Else Statements, so the concept of this is to allow the program to make decisions based on certain conditions.

age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# We can also make Nested if-Else statements

age = 29
if age > 25:
    if age == 30:
        print("You are 30 years old.")
        if age >= 31:
            print("You are older than 30.")
    else:
        print("You are older than 25 but not 30.")
else:
    print("You are not older than 25.")

# here first we checked the condition if age > 25:
# if it is True then we checked the next condition if age == 30:
# Since age is 29, this condition is False, so we go to the else block
# In the else block, we print "You are older than 25 but not 30."


## there is another thing called indentation, it is very important in python as it 
# defines the blocks of code. In the above example, the code inside the if statements
# is indented, which means it belongs to that particular if block. If we don't indent
# the code properly, we might get unexpected results or errors.


money = 15

if money == 10: # if this condition is True it will print "I will buy a chocolate bar" if this condition is false then it will move to the next block
    print ("I will buy a chocolate bar")

elif money < 10: # if this condition is True it will print "I dont have enough money" if not met move towards the next block
    print ("I dont have enough money")

else: 
    print ("I will buy a gum")


#################################################################################
#QUESTION NO 1: COMPARING TWO NUMBERS AND FINDING THE GREATER ONE

num_1 = int(input("Enter no 1: "))
num_2 = int(input("Enter no 2: "))

# HERE I HAVE USED LOGICAL OPERATORS WITH IF ELSE STATEMENTS
if num_1 > num_2 or num_1 < num_2:
    if num_1 > num_2:
        print(f"{num_1} is greater than {num_2}")
    elif num_1 < num_2:
        print(f"{num_2} is greater than {num_1}")
else:
    print(f"{num_1} is equal to {num_2}")

# QUESTION NO 2: CHECKING IF A NUMBER IS EVEN OR ODD

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# QUESTION NO 3: ACCEPTING GENDER AND PRINTING GREETING

gender = input("Enter the gender: ")

if gender == "male" or gender == "Male":
    print ("Good Morning Sir")
elif gender == "female" or gender == "Female":
    print ("Good Morning Ma'am")

# QUESTION NO 4: CHECKING VOTING ELIGIBILITY BASED ON AGE

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
    print(f"Hello, {name} you are not eligible to vote.")
elif age >= 18:
    print (f"Hello, {name} you are eligible to vote.")

#QUESTION NO 5: CHECKING IF THE YEAR IS LEAP YEAR OR NOT

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")