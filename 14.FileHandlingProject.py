from pathlib import Path
import os

def readFileAndFolder():
    path = Path("")
    items = list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i+1}: {item}")

def createFile():
    try:
        readFileAndFolder()

        name = input("Enter the file name with extension: ") 
        file_path = Path(name)

        if not file_path.exists():
            content = input("Enter the content for the file: ")
            with open(file_path, "w") as file:
                file.write(content)
            print("File created successfully!")
        else:
            print("File already exists.")

    except Exception as e:
        print(f"Error occurred while creating file: {e}")

def readFile():
    try:
        n = input("Enter the name of the file you want to read: ")
        path_file = Path(n)

        if path_file.exists():
            with open(n, "r") as file:
                content = file.read()
                print("File content:\n", content)
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"Error occurred while reading file: {e}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to update: ")
        path_file = Path(name)

        if path_file.exists():
            print("Press 1 for changing the name")
            print("Press 2 for overwriting the content")
            print("Press 3 for appending some content")

            result = int(input("Enter the number of your choice: "))

            if result == 1:
                name2 = input("Enter the new name for the file: ")
                path_file2 = Path(name2)
                path_file.rename(path_file2)
                print("File renamed successfully!")

            elif result == 2:
                with open(name, "w") as file:
                    content = input("Enter new content to overwrite: ")
                    file.write(content)
                print("File overwritten successfully!")

            elif result == 3:
                with open(name, "a") as file:
                    content = input("Enter content to append: ")
                    file.write(content)
                print("Content appended successfully!")

        else:
            print("File does not exist.")

    except Exception as e:
        print(f"Error occurred while updating file: {e}") 

def deleteFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of the file you want to delete: ")
        path_file = Path(name)

        if path_file.exists():
            os.remove(name)
            print("File deleted successfully!")
        else:
            print("File does not exist.")
    except Exception as e:
        print(f"Error occurred while deleting file: {e}")

# Main Program
print("File Handling Project")
print("Press 1 for creating Files")
print("Press 2 for reading Files")
print("Press 3 for updating Files")
print("Press 4 for deleting Files")

check = int(input("Enter your choice: "))

if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    updateFile()
elif check == 4:
    deleteFile()
