'''
Name: visalakshi.annamalai
question no:7
Description:Write a function isIn() that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.

'''

def isIn(s1,s2):
    if s1.find(s2)>=0:
        return True
    else:
        return False
s1=raw_input("enter the string")
s2=raw_input("enter the string to be searched")
c=isIn(s1,s2)
print c


