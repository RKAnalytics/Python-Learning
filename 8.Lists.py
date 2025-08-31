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

######################################################################################

# there are some of the methods that we can use with lists
# 1. append() - adds an element to the end of the list
l = [1, 2, 3, 4, 5]
l.append(6)
print(l)

# 2. extend() - adds multiple elements to the end of the list
l.extend([7, 8, 9])
print(l)

# 3. insert() - adds an element at a specific position in the list
l.insert(0, 0) # here 1st 0 is the index and 2nd 0 is the value
print(l)

# 4. remove() - removes the first occurrence of a specific element from the list
l.remove(3)
print(l)

# 5. pop() - removes and returns the element at a specific position in the list
l.pop(0)
print(l)

# 6. clear() - removes all elements from the list
# l.clear()
# print(l)

# 7. index() - returns the index of the first occurrence of a specific element in the list
print(l.index(9))

# 8. count() - returns the number of occurrences of a specific element in the list
print(l.count(2))

# 9. sort() - sorts the elements of the list in ascending order
l.sort()
print(l)

# 10. reverse() - reverses the order of the elements in the list
l.reverse()
print(l)

# there is another thing called nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(nested_list[0][2])


num = int (input("How many elements you want to enter "))

list = []
# add = 0

# counter = 0

for i in range(num):
    element = int(input("Enter the number you want to enter:-"))
    list.append(element)

largest_number = list[0]
sec_largestNum = list[0]
largest_index = 0
second_largest = 0
    
# for j in list:
        
#     add = add + j
#     counter += 1
        
# avg = add / counter

for i in range(len(list)):
    if list[i] > largest_number:
        sec_largestNum = largest_number
        largest_number = list[i]
        second_largest = largest_index
        largest_index = i
    elif list[i] > sec_largestNum and list[i] != largest_number:
        sec_largestNum = list[i]
        second_largest = i
        
        
        

print(f"Greatest number {largest_number} is at position {largest_index} ")
print(f"Second greatest number {sec_largestNum} is at position {second_largest} ")


num = int (input("How many elements you want to enter in the list:- "))

list = []

for i in range(num):
    element = int(input(f"Number{i + 1}:"))
    list.append(element)

for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)






















