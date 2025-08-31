# Sets are also a data structure used in Python to store a collection of unique items.
# Unlike lists and tuples, sets are unordered (means they cannot be indexed) and do not allow duplicate elements.
# They are defined using curly braces instead of square brackets.
# Sets are mutable (can be changed after creation)
# they are semi-heterogeneous, meaning they can store elements of different data types.
# values are stored in hashing form


set = {1, 2, 3, 4, 5}
print(set)

# Sets have several useful methods
# 1. add() - adds an element to the set
set.add(6)
print(set)

# 2. update() - adds multiple elements to the set
set.update([7, 8, 9])
print(set)

# 3. remove() - removes a specific element from the set. it will search for the elements hash value and then remove it from the memory
set.remove(3)
print(set)

# 4. discard() - removes a specific element from the set if it exists
set.discard(4)
print(set)

# 5. pop() - removes and returns an arbitrary element from the set
print(set.pop())
print(set)

# 6. clear() - removes all elements from the set
set.clear()
print(set)

# 7. union() - returns a new set with all elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1 | set2)  # another way to do union

# 8. intersection() - returns a new set with elements common to both sets
print(set1.intersection(set2))
print(set1 & set2)  # another way to do intersection

# 9. difference() - returns a new set with elements in the first set but not in the second
print(set1.difference(set2))
print(set1 - set2)  # another way to do difference

# 10. symmetric_difference() - returns a new set with elements in either set but not in both
print(set1.symmetric_difference(set2))
print(set1 ^ set2)  # another way to do symmetric_difference

# so there is another concept known as hash
# Hashing is the process of converting an input (or 'message') into a fixed-size string of bytes.
# The output is typically a 'digest' that is unique to each unique input.
# Hashing is commonly used in data structures like sets and dictionaries to quickly locate a data record.

# Relation between hashing and sets
# In Python, sets use hashing to store their elements.
# When you add an element to a set, Python computes a hash value for that element.
# This hash value is then used to determine where to store the element in memory.
# Because sets are unordered, the elements are not stored in any particular order.
# Hashing allows for fast membership testing, meaning you can quickly check if an element is in a set.
# when we print a set, we see the elements in an arbitrary order because of the way hashing works.

set3 = {10, 20, 30,"hello", 40, 50, 10, 20}
for i in set3:
  print(hash(i))

# so here the hash values for the elements in set3 are printed and the values are printed as integers. and why is that?
# This is because the hash function in Python returns an integer value that represents the hash of the object.
# but strings are also hashed to integers, so why do we see different hash values for the same string?
# This is because the hash value of a string is based on its content, and different strings will have different hash values.

# some of the integers values are stored in the hash but at the end they are returned as an integer.
# hash depends on the system architecture and the specific implementation of the hash function how it stores the values in memory.

# hash() always gives an integer, no matter the input type.

# Strings are converted into integers by hashing their characters.

# Sets use these integers to place elements in memory, which is why they look unordered. 