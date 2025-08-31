# Tuple is also a data structure used in Python to store a collection of items.
# Unlike lists, tuples are immutable, meaning their elements cannot be changed once they are assigned.
# they are defined using parentheses instead of square brackets.
# they are heterogeneous, meaning they can store elements of different data types.
# they can have a fixed size, meaning once they are created, their size cannot be changed.
# they can have a duplicate values

tuple = (1, 2, 3, 4, 5, 5)
print(tuple)

# Tuple have only two methods
# 1. count() - returns the number of occurrences of a specific element in the tuple
print(tuple.count(5))

# 2. index() - returns the index of the first occurrence of a specific element in the tuple
print(tuple.index(3))