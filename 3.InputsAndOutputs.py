# There are two types of strings
# formatted strings
# raw strings

name = "Rafay"
age = 19
print ("Hello, my name is", name, "and I am", age, "years old.") # this is called string concatenation
# now the formatted string is where we use only one string and in which we can directly embed variables containing integer values
print(f"Hello, my name is {name} and I am {age} years old.") # this is called f-string formatting
# now the raw string is where we use a string as it is without any formatting
print(r"C:\Users\Alice\Documents")# this is called raw string formatting
# r-string treats backslashes as literal characters instead of escape characters