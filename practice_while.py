i=1
while i <= 5:
    print(i)
    i += 1

n=int(input("Enter a number: "))
factorial=1
for i in range(1,n+1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")

num=int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1.")
else:
    factorial=1
    for i in range(2,num+1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")


n=20
factorial=1
for i in range(1,n+1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")
    

i=1
while i <= 5:
    print(i)
    i += 1  
