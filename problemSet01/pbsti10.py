'''
Name: visalakshi.annamalai
question no:10

'''
z=raw_input("enter the number")
x =abs(z) 
epsilon = 0.01 
numGuesses = 0 
low = 0.0 
high = max(1.0, x) 
ans = (high + low)/2.0 
while abs(ans**3 - x) >= epsilon: 
    print 'low =', low, 'high =', high, 'ans =', ans 
    numGuesses += 1 
    if ans**3 < x: 
        low = ans 
    else: 
        high = ans 
    ans = (high + low)/2.0 
print 'numGuesses =', numGuesses
if z<0: 
    print '-', x 
else: 
    print ans, x 
