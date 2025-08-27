print("\nHello, my name is rafay its my first day leaning Python\n")

## comments are some thing python ignores like
# this is a comment
#so comments are something that cant be executed by python

# doc string """ it is a multiline comment when we  have to comment multiple line so we use multiline comments"""

""" helloooo my name is dragon whats
your name? """


#################################################################################################################

# variables are used to store information it can be any data type int, float, string, boolean 
name = "rafay"
age = 20
is_student = True

# 1name wrong (will give an error)
# space not allowed before the variable name
# dont use special characters like @, #, $, %, ^, &, *, (, )

#################################################################################################################

# naming conventions
# 1. variable names should be descriptive
# 2. use underscores to separate words (e.g. first_name)
# 3. start variable names with a lowercase letter
# 4. avoid using reserved keywords (e.g. if, else, for)
# 5. keep variable names concise but meaningful
# there are following types of writing variable names
# 1. camelCase (e.g. firstName)
# 2. snake_case (e.g. first_name)
# 3. PascalCase (e.g. FirstName)

#################################################################################################################


# Data Types
# 1. int (integer)
# 2. float (floating-point number)
# 3. str (string)
# 4. bool (boolean)
# so basically what this means is that variables can hold different types of data in simple words what kind of data is being stored in the variable

print("DATA TYPES")
a = 5
b = 3.14
c = "Hello"
d = True

# There is a function name type() in Python that is used to determine the data type of a variable.
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>
print(type(d))  # Output: <class 'bool'>

#There is another data type called complex (e.g. 1 + 2j)

complex_num = 1 + 2j
print(type(complex_num))  # Output: <class 'complex'>