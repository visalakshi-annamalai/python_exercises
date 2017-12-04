'''
Name: visalakshi.annamalai
question no:2
Description:A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.
'''

def is_power(n1,n2):
    try:
        if n1%n2==0 and n1/n2%n2==0 :
            return True
        else:
            return False
    except Exception as e :
        print e
      
a=raw_input("Enter a ")
b=raw_input("Enter b")
n1=int(a)
n2=int(b)
c=is_power(n1,n2)
print c

