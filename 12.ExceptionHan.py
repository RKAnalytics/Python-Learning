# Exceptional Handling is used to manage errors gracefully

try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handling the specific exception
    print("Error: Division by zero is not allowed.")
except Exception as e:
    # Handling any other exceptions
    print("Error:", e)
else:
    # Code to execute if no exceptions were raised
    print("Result:", result)
finally:
    # Code to execute regardless of whether an exception occurred
    print("Execution complete.")


# there is another way like in that way we can create custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print("Caught a custom error:", e)

# but mostly we will use try and except blocks for error handling