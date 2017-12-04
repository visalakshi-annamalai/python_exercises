'''
Name: visalakshi.annamalai
question no:5
Description:Implement a function that meets the specification below. Use a try-except block.

def sumDigits(s):
	"""Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5"""

'''

def sumDigits(a):
    try:
        list1=[]
        sum=0
        for i in a:
            list1.append(i)
            if  i.isdigit():
                sum=sum+int(i)
        return sum
    except Exception as E:
        print E
a=raw_input("enter string along with numbers")
c=sumDigits(a)
print c


