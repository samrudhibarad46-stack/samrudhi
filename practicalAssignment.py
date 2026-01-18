Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Simple Interest Calculator

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))

si = (p * r * t) / 100
... 
... print("Simple Interest is:", si)
... a = int(input("Enter first number: "))
... b = int(input("Enter second number: "))
... 
... if a > b:
...     print("Maximum number is:", a)
... else:
...     print("Maximum number is:", b)
... for i in range(1, 6):
...     print(i)
... s = input("Enter a string: ")
... length = len(s)
... print("Length of the string is:", length)
... print("Welcome to Python!")
... s = input("Enter a string: ")
... 
... print("First character is:", s[0])
... s = input("Enter a string: ")
... 
... print("Last character is:", s[-1])
... num = int(input("Enter a number: "))
... 
... if num > 0:
...     print("Positive number")
... elif num < 0:
...     print("Negative number")
... else:
...     print("Zero")
... # Input three numbers
... num1 = float(input("Enter first number: "))
... num2 = float(input("Enter second number: "))
... num3 = float(input("Enter third number: "))
... 
... # Calculate sum
... total = num1 + num2 + num3
... 
... # Display result
... print("The sum of three numbers is:", total)
... name = input("Enter your name: ")
... print("Hello,", name)
