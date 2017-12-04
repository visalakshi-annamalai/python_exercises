'''
Name: visalakshi.annamalai
question no:6
Description:Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.

'''

s=raw_input("string containing decimal numbers separated by commas")
sums=0
mylist=s.split(',')
print mylist
for i in mylist:
   e=float(i)
   sums=sums+e
print sums

