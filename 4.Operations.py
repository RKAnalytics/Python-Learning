# Operators
# there are following operators

# Arithimatic Operators 
# 1. + (Addition)
# 2. - (Subtraction)        
# 3. * (Multiplication)

# 4. / (Division) it always return float value
# example: 5/2 = 2.5

# 5. % (Modulus) it gives remainder
# example: 5%2 = 1

# 6. ** (Exponentiation) its like power example 2**3 = 2*2*2 = 8
""" 
But when we use this with strings it works like this
example: "Hello" * 3 = HelloHelloHello

"""
# 7. // (Floor Division) always return integer value
# example: 5//2 = 2

# Python also follws BODMAS rule
# B - Brackets  
# O - Order (i.e. powers and square roots, etc.)
# D - Division
# M - Multiplication
# A - Addition
# S - Subtraction
# example: 2 + 3 * 5 - 6 / 2
# here 3*5 = 15 and 6/2 = 3
# so now the equation becomes 2 + 15 - 3
# now 2 + 15 = 17   
# so now the equation becomes 17 - 3 = 14
# so the final answer is 14 

#############################################################################################

# Assignment Operators

# 1. = (Assign) it assigns value to a variable
a = 5
b = 10
c = 8
# here 5 and 10 is assigned to the variables a and b respectively

# 2. += (Add and Assign) it adds the value to the variable and assigns the new value to the variable
a += 3
# here what is happening is a = a + 3 so the value of a was 5 and here it means first add 3 in the previous value of a and then assign it to a
# so now the value of a is 8
print(a)

#3. -= (Subtract and Assign) it subtracts the value from the variable and assigns the new value to the variable
b -= 2
# here what is happening is b = b - 2 so the value of b was 10 and here it means first subtract 2 from the previous value of b and then assign it to b
# so now the value of b is 8
print(b)

# 4. *= (Multiply and Assign) it multiplies the value to the variable and assigns the new value to the variable
c *= 2 
# here what is happening is c = c * 2 so the value of c was 8 and here it means first multiply 2 to the previous value of c and then assign it to c
# so now the value of c is 16   
print(c)

# 5. /= (Divide and Assign) it divides the value from the variable and assigns the new value to the variable
a /= 4
# here what is happening is a = a / 4 so the value of a was 8 and here it means first divide 4 from the previous value of a and then assign it to a
# so now the value of a is 2.0
print(a)

# 6. %= (Modulus and Assign) it gives remainder and assigns the new value to the variable
b %= 3
# here what is happening is b = b % 3 so the value of b was 8 and here it means first divide 3 from the previous value of b and then assign the remainder to b
# so now the value of b is 2
print(b)

#7. **= (Exponent and Assign) it gives power and assigns the new value to the variable
c **= 2
# here what is happening is c = c ** 2 so the value of c was 16 and here it means first power 2 to the previous value of c and then assign it to c
# so now the value of c is 256  
print(c)

# 8. //= (Floor Divide and Assign) it gives integer value and assigns the new value to the variable
a //= 2 
# here what is happening is a = a // 2 so the value of a was 2.0 and here it means first floor divide 2 from the previous value of a and then assign it to a
# so now the value of a is 1.0  
print(a)

#############################################################################################

# Comparison Operators
# 1. == (Equal to) it checks whether the two values are equal or not if equal then it returns True otherwise False
print("==")
print("5 == 5",5 == 5) # True
print("5 == 3",5 == 3) # False

# 2. != (Not Equal to) it checks whether the two values are not equal or not if not equal then it returns True otherwise False
print("!=")
print("5 != 3",5 != 3) # True    
print("5 != 5",5 != 5) # False

# 3. > (Greater than) it checks whether the first value is greater than the second value or not if greater then it returns True otherwise False
print(">")
print("5 > 3",5 > 3) # True 
print("3 > 5",3 > 5) # False

# 4. < (Less than) it checks whether the first value is less than the second value or not if less then it returns True otherwise False
print("<")
print("3 < 5",3 < 5) # True
print("5 < 3",5 < 3) # False

# 5. >= (Greater than or Equal to) it checks whether the first value is greater than or equal to the second value or not if greater than or equal then it returns True otherwise False
print(">=")
print("5 >= 3",5 >= 3) # True
print("5 >= 5",5 >= 5) # True
print("3 >= 5",3 >= 5) # False

# 6. <= (Less than or Equal to) it checks whether the first value is less than or equal to the second value or not if less than or equal then it returns True otherwise False
print("<=")
print("3 <= 5",3 <= 5) # True
print("3 <= 3",3 <= 3) # True
print("5 <= 3",5 <= 3) # False

#############################################################################################

# Logical Operators
# 1. and it returns True if both the conditions are True otherwise it returns False
# example: (5 > 3) and (3 < 5) it returns True because both the conditions are True
# 2. or it returns True if at least one of the conditions is True otherwise it returns False
# example: (5 > 3) or (3 > 5) it returns True       \
# 3. not it returns True if the condition is False and returns False if the condition is True
# example: not(5 > 3) it returns False because the condition is True