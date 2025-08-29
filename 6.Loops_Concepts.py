# LOOPS IN PYTHON

# 1. FOR LOOP -----> IT WORKS WITHOUT USING A COUNTER VARIABLE IT MEANS WE CAN ITERATE OVER A SEQUENCE (LIKE A LIST OR STRING) DIRECTLY WITHOUT 
# ANY CONDITION

# 2. WHILE LOOP -----> IT REPEATS A BLOCK OF CODE AS LONG AS A CONDITION IS TRUE

# now the other is range() function which is used to generate a sequence of numbers and is used in FOR LOOPS

a = range(1,11,1) # so here it will generate numbers from 1 to 10 range(start(included), stop(not included), step)

# for i in a:
#     print(i)

# for i in range(11, 21, 1):
#     print(i)

for i in range (20, 0, -1): # here the step is -1, so it will count downwards if we write 1 then it will count upwards 
    print(i)

## Lets print a table using range() function

num = int(input("Enter a number to print its table: "))

for i in range (1, 11):
    print (num, "x", i, "=", num*i)

## we can also use the range() function to print the table

num = int(input("Enter a number to print its table: "))

for i in range(num, (num*10)+1, num):
    print(f"{num} x {i//num} = {i}") # here i//num is used to get the multiplier

################################################################################################


# LOOPS FOR STRINGS
# in string the loop iterates over the indices

name = "RAFAY KHAN"

for i in range (0,10, 1):
    print (name[i])

# we can also iterates over the characters directly

for char in name:
    print(char)


## there is another thing called break and continue statements

num = int(input("Number: "))

for i in range(1, (num + 1)):
    if i == 5:
        break
    else:   
        print(i)

num = int(input("Number: "))

for i in range(1,(num + 1)):
    if i == 5:
        continue
    print(i)