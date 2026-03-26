# multiplication table of 5 using while loop
i=1
while i<=10:
    print("5 x",i,"=",5*i)
    i+=1

# break statement in while loop
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1

#array of 5 elements using while loop
arr=[1,2,3,4,5]
print("original Array:", arr)

# add element
arr.append(6)

# insert element
arr.insert(2,10)

# update element
arr[0]=100

# remove element
arr.remove(3)

#display array
print("Updated Array:", arr)

#traverse array
print("array elements:")
for i in arr:
    print(i)

# length
# print("length of array:", len(arr))    

# slicing array

from array import array
from unittest import result 
# create 
arr=array('i',[1,2,3,4,5])
# slicing
sliced_arr=arr[1:4] 
print("Sliced Array:", sliced_arr)

# types of functions

# positional arguments
def add(a,b):
    print("Sum:", a+b)
add(5,10)

# keyword arguments
def greet(name, message):
    print(f"{message}, {name}!")
greet(name="Alice", message="Hello")

# default arguments
def power(base, exponent=2):
    print(f"{base} raised to the power of {exponent} is {base**exponent}.")
power(5)    
power(5,3)

# *args
def sum_all(*args):
    result=sum(args)
    print("Sum of all numbers:", result)    
sum_all(1,2,3,4,5)

# **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
print_info(name="Alice", age=30, city="New York")

info={"name":"Alice", "age":30, "city":"New York"}
print_info(**info)