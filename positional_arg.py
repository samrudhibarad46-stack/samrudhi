def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result= add(2,5)
print("sum=",result)

def student_info(name,roll,marks):
    print("name:",name)
    print("roll:",roll)
    print("marks:",marks)

student_info("samrudhi",101,84)

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple inetrest:",si)
simple_interest(10000,2,2)
simple_interest(50000,1,2)

def ar_circle(r):
    ar_circle=3.14*r*r
    print("area of circle:",ar_circle)
ar_circle(1.5)
ar_circle(4)   

def cheak_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
cheak_value(0)
cheak_value(90)
cheak_value(-45)     

def odd_even(no):
    if(no%2==0):
        print("value is even")
    else:
        print("valuen is odd")
odd_even(50)
odd_even(15)            