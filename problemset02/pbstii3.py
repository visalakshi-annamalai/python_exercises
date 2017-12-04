'''
Name: visalakshi.annamalai
question no:3
Description:def factI(n):
	"""Assumes that n is an int > 0
	Returns n!
	Uses Iterative Implementation"""
	
def factR(n):
	"""Assumes that n is an int > 0
	Returns n!
	Uses Recursive Implementation"""

'''
#recursion
def factR(n):
    if n == 1:
        return n
    else:
       return n*factR(n-1)
num1 =raw_input("number to find factorial")
num=int(num1)
if num < 0:
    print(" negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    c=factR(num)
    print c


#iteration
def factI(n):
    num=1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
num1=raw_input("number")
num2=int(num1)
c=factI(num2)
print c
