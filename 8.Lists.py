# Data structures are used to store collections of data.
# In Python, the most commonly used data structures are lists, tuples, sets, and dictionaries.

# like 
a = 50
c = 89
e = 13
h = 90

# so i am storing these values in their respective variables
# so data structures is a way to organize and store data so that it can be accessed and modified efficiently in a single variable

list = [50, 89, 13, 90]
print (list)

# we can also access elements in the list using their index
print(list[0]) # prints the first element
print(list[1]) # prints the second element
print(list[2]) # prints the third element
print(list[3]) # prints the fourth element

# we can also slice the list 
print (list[:3:1]) # list[start(included):end(not included):step(how many steps we want to skip)]

def sum(a, b):
    return (a + b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    return (a / b)

def subtract(a, b):
    return (a - b)

arithmetic_operations = [sum(2, 3), multiply(2, 3), divide(2, 3), subtract(2, 3)]

print (arithmetic_operations[0:2])
