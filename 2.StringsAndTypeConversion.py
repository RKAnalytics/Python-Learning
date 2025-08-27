# every character has its own unicode code point
# for example, the unicode code point for 'A' is U+0041
# and for 'a' it is U+0061 or 97 in decimal
# and unicode for A is U+0041 or 65 in decimal
# string takes more space than any other data type because it stores each char with its unicode code point
# every value has its special unicode code point

a = "A"
print(ord(a))  # Output: 65 here ord() function gives the unicode code point of a character

num = 65
print(chr(num))  # Output: A here chr() function gives the character corresponding to a unicode code point

#################################################################################################

# INDEXING

# in python indexing starts from 0
# for example, in the string "Hello", H is at index 0, e is at index 1, and so on.
""" H E L L O
    | | | | |
    0 1 2 3 4 """
# this is called positive indexing

""" H  E  L  L  O
    |  |  |  |  |
   -5 -4 -3 -2 -1 """

# this is called negative indexing

# we can also access each character using negative indexing as well as positive indexing.

a = "hello world"
print (a[2]) # this will gonna print 'l'

####################################################################################################

# Indexing slicing

# Slicing allows you to extract a portion of a string by specifying a start and end index.

a = "hello world"
print(a[0:5])  # Output: hello
print(a[6:])   # Output: world
print(a[:5])   # Output: hello
print(a[-5:])  # Output: world

#  a[start(included):stop(not included):steps]
#  a[0:] it will print 'hello world' because if we dont give the stop index it will take the length of the string and print the whole word
#  a[::-1] it will reverse the string and print 'dlrow olleh'
#  a[::2] it will print every second character 'hlowrd'

# TYPE CONVERSION
# there are some falsy values that evaluate to False in a boolean context.
# these include:
# - None
# - False
# - 0 (zero)
# - "" (empty string)
# - [] (empty list)
# - () (empty tuple)
# - {} (empty dictionary)
# all other values are considered truthy.