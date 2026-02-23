## here i am gonna learn about the strings and their manipulation in python

#  print("hello world") ## this is a string and it is enclosed in double quotes
#  but this shows and error becasuse if the indendation is not correct then it will show an error
print ("Hello" + " " + "world") ## this is a string concatenation and it will print hello world
print ("Hello" * 3) ## this will print hello three times    

#######################################################################################################
a = input ("What is your name?\n") ## this will take input from the user and it will print what is your name
print (a)
# print ("What is your name? ") ## this will print what is your name but it will not take input from the user

print (f"Hello {a}!") ## this will print hello and the name of the user that is stored in the variable a

#######################################################################################################
name = "Rafay"
print (name)

name = "Hadi"
print (name) ## this will print Hadi because we have reassigned the value of the variable name to Hadi

print (len(name)) ## this will print the length of the string Hadi which is 4 we will get a string length

name = len(input("What is your name? ")) ## this will take input from the user and it will print the length of the string that the user has entered
print (name) 

#######################################################################################################

# naming convention in python
# 1. variable names should be in lowercase letters and words should be separated by underscores
# 2. variable names should not start with a number
# 3. variable names should not be a reserved keyword in python

