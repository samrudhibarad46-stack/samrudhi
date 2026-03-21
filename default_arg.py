def power(num,exp=2):
    return num ** exp
print(power(3)) # 9
print(power(3,3)) # 27  
print(power(2,4)) # 16

def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")
greet("Alice") # Hello, Alice!
greet("Bob", "Hi") # Hi, Bob!

def calculate_area(radius, pi=3.14):

    return pi * radius ** 2
print(calculate_area(5)) # 78.5
print(calculate_area(5, 3.14159)) # 78.53975
print(calculate_area(10)) # 314.0

def study(subject, hours=1):
    print(f"Studying {subject} for {hours} hour(s).")
study("Math") # Studying Math for 1 hour(s).
print(study("Science", 3)) # Studying Science for 3 hour(s). None

def student_info(name, age=18, grade="A"):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
student_info("John") # Name: John, Age: 18, Grade: A
student_info("Emily", 20) # Name: Emily, Age: 20, Grade: A
student_info("Michael", 22, "B") # Name: Michael, Age: