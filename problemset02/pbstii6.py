'''
Name: visalakshi.annamalai
question no:6
Description:Implement a function that satisfies the specification. Use a try-except block.
def findAnEven(l):
	"""Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number"""

'''

def findAnEven(l): 
    for i in l: 
        if int(i) % 2 == 0: 
            return i 
    raise ValueError("No even numbers in list!") 

m=raw_input("enter")
l=[]
for i in m:
    l.append(i)
c=findAnEven(l)
print c


