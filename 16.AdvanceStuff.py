# Decorators

class Animals:

    def __init__(self):
        pass
    
    @property # This makes the method callable without parentheses
    def show(self):
        print("I am an animal")


obj = Animals()
obj.show

# decorator funcion [@decorate] captures the original function [display()] and wrapper captuers every argument 
# and parameters we are giving to the function
def decorate(func): # so whenever we create function on the name of decorator so its its *** function display() will pass as an argument
    # it menas the func is pointing the display function
    def wrapper(a, b):
        print("Something is happening before the function is called.")
        func(a, b)
        print("Something is happening after the function is called.")
    return wrapper


@decorate # ***
def display(a, b): # these are the arguments we are giving
    print(f"the addition is {a + b}")

display(5, 10)

## so now the problem is like if someone is trying to give more than two arguments we
# cant just keep on changing the wrapper function and adding parameters so in this case ther is another
# thing named as *args and **kwargs --> basically they are * and ** and you can use anything after them
# so what are those, they are special keywords in python that used in function defention to accept multiple arguments

def decorate(func): # so whenever we create function on the name of decorator so its its *** function display() will pass as an argument
    # it menas the func is pointing the display function
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper


@decorate # ***
def display(a, b, c, d): # these are the arguments we are giving
    print(f"the addition is {a + b + c + d}")

display(5, 10, 15, 20)


#######################################################################################################

def addition(*args): # this is use for positional arguments
    total = 0
    for num in args:
        total += num
    print(f"the addition is {total}")


addition(5, 10, 15, 20, 12, 12, 43, 53, 435, 63)

def addition(**kwargs): # for keyword arguments
    total = 0
    for num in kwargs.values():
        total += num
    print(f"the addition is {total}")


addition(a=5, b=10, c=15, d=20, e=12, f=12, g=43, h=53, i=435, j=63)


#############################################################################################################

## now list, dic, set comprehension
# multiple lines of code in a single line

## list comprehension
l = [i for i in range(1, 11) if i % 2 == 0] # this is list comprehension
print(l)

dic = {i: i**2 for i in range(1, 11) } # this is dictionary comprehension
print(dic)

s = {i for i in range(1, 11) if i % 2 != 0} # this is set comprehension
print(s)

###################################################################################################################



a = [1,2,3,4,5,6,7]

# result = lambda x : x * 2 # so here we dont know the type of x means what kind of values x accepts 

# print (result) # this will print the memory location of the lambda function because it does not have a value inside 

# so for that i will use maps


# we are providing list on which we want to map the function
result = map(lambda x: x * 2, a) # so maps does two things one is taht it accpets a lambda function and
# it accpts the iterable means list, dic, set

print(list(result)) # so here we are converting the map object to list