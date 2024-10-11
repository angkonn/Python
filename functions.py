def area(height,base):
    area=0.5*height*base
    return area


print(area(5,10))

# Prime Checker function:
def is_prime(number):

    if number <= 1:
        print ("Not a prime number")

    for i in range (2,number):
        if number % i == 0:
            print("It's not a prime Number")
            return
        
    print("It is a prime number")

is_prime(59)

# Different types of functions: 
# . Built-in functions
# . User Defined functions
# . Lambda Functions
# . Recursive functions

# Built in functions:
# 1. print()
# 2. input() :
# print("Enter value of a") 
# a = input()
# print("a =",a)

# 3. len()
# 4. type()
# 5. max() ... etc

# lambda functions:
# function name = lambda parameters: function body (everything in one line)

calculate_areea = lambda height,base: 0.5*height*base
print(calculate_areea(10,2))

# Recursive functions: 
# factorial:
def factorial(n):
    if n==1:
        return 1
    ans=n*factorial(n-1)
    return ans
print(factorial(5))
# factorial of 5 means 5*4*3*2*1 (1 ashar por ar function call hobe na, karon tokhon 0 multiply hoye ans 0 hoye zabe, tai tokhon 1 return korbe)

# exception handling:

def division(a,b):
    ans=a/b
    return ans
try:
 a=int(input("Enter the value of a: "))
 b=int(input("Enter the value of b: "))
 print("The answer is: ",division(a,b))
except:
 print("Cannot divide by zero (0)")
else:
 print(division(a,b))
finally:
 print("End of program") 

# built in modules: Math, numpy, pandas, matplotlib, os, time etc
import math
print(math.sqrt(100))
