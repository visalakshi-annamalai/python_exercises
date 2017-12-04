'''
Name: visalakshi.annamalai
question no:4
Description:Write a program that computes the decimal equivalent of the binary number 10011?
'''

number = raw_input('enter a number: ')
decimal = 0
for i in number:
    decimal = decimal*2 + int(i)
print decimal


