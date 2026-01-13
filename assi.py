#1 print mess
print("hello world")

#2 add two number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}")

# 3 even or odd
# Program to check if a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# 4 cheak leap year cheak whether a year is a leap year
# Program to check leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#5 print PI value
# Print PI value using math module
import math

print("PI value is:", math.pi)

#6 store and print constant value

# Store and print constants (use UPPERCASE by convention)
PI = 3.141592653589793
SPEED_OF_LIGHT = 299792458  # m/s
MAX_VALUE = 100

print("PI:", PI)
print("Speed of Light:", SPEED_OF_LIGHT)
print("Max Value:", MAX_VALUE)

# 7 square of a number 

# Program to calculate square of a number
num = float(input("Enter a number: "))
square = num ** 2
print(f"The square of {num} is {square}")


# 8 area of circle
# Program to calculate area of circle
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area of circle with radius {radius} is {area:.2f}")


# 9 cheak data type 
# Program to check data types
num = 42
name = "Alice"
price = 19.99
numbers = [1, 2, 3]
is_active = True

print(f"num type: {type(num)}")
print(f"name type: {type(name)}")
print(f"price type: {type(price)}")
print(f"numbers type: {type(numbers)}")
print(f"is_active type: {type(is_active)}")


#10 use maths fun..

# Using Python math module functions
import math

num = 16.7
print(f"sqrt({num}): {math.sqrt(num):.2f}")
print(f"ceil({num}): {math.ceil(num)}")
print(f"floor({num}): {math.floor(num)}")
print(f"PI: {math.pi}")
print(f"sin(1.57): {math.sin(1.57):.2f}")
print(f"cos(1.57): {math.cos(1.57):.2f}")
print(f"factorial(5): {math.factorial(5)}")


# 1 find power
# Program to find power of a number
base = float(input("Enter base number: "))
exponent = float(input("Enter exponent: "))

# Method 1: ** operator (simplest)
power1 = base ** exponent

# Method 2: pow() built-in function
power2 = pow(base, exponent)

# Method 3: math.pow() function
import math
power3 = math.pow(base, exponent)

print(f"{base}^{exponent} = {power1:.2f}")
print(f"Using pow(): {power2:.2f}")
print(f"Using math.pow(): {power3:.2f}")


# cheak posi t nega

# Program to check positive, negative, or zero
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("Number is Zero")
