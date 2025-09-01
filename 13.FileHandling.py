# File Handling in Python means working with files to read, write, and manipulate data stored in them.
# It allows you to perform operations like creating, opening, reading, writing, and deleting files.
# There are multiple modes for opening files:
# 1. Read ('r'): Opens a file for reading (default mode).
# 2. Write ('w'): Opens a file for writing (creates a new file or truncates an existing file).
# 3. Append ('a'): Opens a file for appending (creates a new file if it doesn't exist).
# 4. Read and Write ('r+'): Opens a file for both reading and writing.


f = open("demofile.txt", "w")
f.write("Hello, World!")
f.close()

# Now, let's read the content of the file
f = open("demofile.txt", "r")
print(f.read())
f.close()

# now lets append in the file
f = open("demofile.txt", "a")
f.write("Appending a new line.")
f.close()

# Let's read the updated content of the file
f = open("demofile.txt", "r")
print(f.read())
f.close()

#