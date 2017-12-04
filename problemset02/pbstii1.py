'''
Name: visalakshi.annamalai
question no:1
Description:The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder. One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a. Write a function called gcd that takes parameters a and b and returns their greatest common divisor.
'''

a=raw_input("Enter first integer ")
b=raw_input("Enter second integer")
n1=int(a)
n2=int(b)
i=1
if n2>n1:
    for i in range(i,n2):
        if(n1%i==0 and n2%i==0):
            gcd = i
            i=i+1
    print gcd
    
else:
    for i in range(i,n1):
        if(n1%i==0 and n2%i==0):
            gcd = i
            i=i+1
    print gcd
  
