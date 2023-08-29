#functions

def welcome_message():
 print("Welcome Python!")

welcome_message()


def sum(a, b):
    c = a + b
    return c
result=sum(10, 20)
 

print(result)

def mul(a, b):
    d=a * b
    return d
result=mul(10, 5)
print(result)


def add():
    a=int(input("enter1st no"))
    b=int(input("enter2nd no"))
    c= a + b
    print("addition=",c)
add()


def sub(p, t):
   print(p-t)
sub(12,30)
  
import os
print(os.name)
