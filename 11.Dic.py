# In python dictionaries are know as hash maps
# They are mutable (can be changed after creation)
# They store key-value pairs, where each key is unique.
# Values can be of any data type and can be duplicated.
# Dictionaries are defined using curly braces with key-value pairs separated by colons.
# Dic are ordered
# keys must be unique and hashable but the values can be of any data type and can be duplicated.


dic1 ={1: "one", 2: "two", 3: "three"}
print(dic1.items()) # this will print all the key value pairs in the form of tuples inside a list

# if we only want to print the keys then
print(dic1.keys())

#if we only want to print values 
print(dic1.values())

# here we are changing the value of key 1
dic1[1] = "Rafay"
print(dic1)

dic2 = {"Name": "Rafay", "Age": 20, "City": "Karachi", dic1[1]: dic1[2]} # here we can also use another dic's key value pair as a key value pair in this dic
# by using dic1's key-value pairs

print (dic2)

# we can also perform CRUD operation
dic2["Country"] = "Pakistan" # Create operation
dic2["Name"] # Read operation
dic2["Age"] = 21 # Update operation
del dic2["City"] # Delete operation

print("LOOPS")
d = {1: 100, 2: 200, 3: 300}

for i in d:
    print(d[i]) # here the value of key i is printed