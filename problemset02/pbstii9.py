'''
Name: visalakshi.annamalai
question no:1
Description:comparing newton square root and normal square root
'''

import math
def newtonSqrt(a,x):
    y = (x + a/x) / 2
    print y
def tst_sqrt(a):
    y=math.sqrt(a)
    print y
for a in range(1,9):
    x=2.0
    newtonSqrt(a,x)
    x=x+1
for a in range(1,9):    
    tst_sqrt(a)

