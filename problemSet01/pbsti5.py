'''
Name: visalakshi.annamalai
question no:5
Description:Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.

'''
num = int(raw_input('Enter a positive integer: '))
pwr = 2
root = 1
flag=False
while pwr < 6:
    while root**pwr <= num:
        if root**pwr == num:       
            print root
            print pwr
            flag = True
        root =root+ 1        
    pwr =pwr+ 1
    root = 1
if flag != True:
    print'No such pair exist'