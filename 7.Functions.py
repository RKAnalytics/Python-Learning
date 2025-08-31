# so there are two types of functions in Python
# 1. Built-in functions: These are functions that are already defined in Python, such as print(), len(), and range().
# 2. User-defined functions: These are functions that you create yourself using the def keyword.

# Lets say we want to make a add function in which we are doing sum

def add(a, b):
    return a + b

# now here i will call the function

sum = add(4,5) 
print(sum)

# now lets make a function which will check if the number is even or odd

def even_odd(num): #here the num is a parameter because it is listed in the function definition
    # the thing you accept are parameters
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = even_odd(number) # here the number is an argument because it is the value passed to the function
# the thing you provide to parameters are arguments 
print(result)

# there are two things parameters and arguments
# parameters are the variables listed inside the parentheses in the function definition
# arguments are the values passed to the function when it is called

## Arguments are of 3 types
# 1. Positional arguments: These are arguments that are passed to the function in the correct positional order.
# 2. Keyword arguments: These are arguments that are passed to the function by explicitly specifying the parameter name.
# they are also known as named arguments.
# 3. Default arguments: These are arguments that take a default value if no value is provided.

# example

def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Good morning") #this is the example of positional arguments
greet(message="Good morning", name="Alice") #this is the example of keyword arguments
# greet("Bob") #this will give an error because the message parameter is missing


def greet(message="Hello"): #this is the example of default arguments
    print(f"{message}, World!")

greet() # this will take the default value for message as provided in the parameter
greet("Hi there!") # this will use the provided message


def palindrome_check(name):
    b = ""

    for i in range(len(name)-1,-1,-1):
        b += name[i]

    if name == b:
        print(f"{name} is a palindrome")
    else:
        print(f"{name} is not a palindrome")

palindrome_check(input("Enter a name: "))