def tst_functn():
    """ this is a TEST function to check lcm """
    a=15
    b=20
    Least_common_factor=lcm(a,b)
    print("LCM is: ")
    print(Least_common_factor)

    a=0
    b=51
    Least_common_factor=lcm(a,b)
    print("LCM is: ")
    print(Least_common_factor)

    a=12
    b=0
    Least_common_factor=lcm(a,b)
    print("LCM is: ")
    print(Least_common_factor)

def gcd(a,b):
    """ this is a helper function to calculate gcd to find lcm using the formula lcm=a*b/gcd """
    try:
        if(b==0):
            return a
        else:
            return gcd(b,a%b)
    except Exception as e:
        print e
def lcm(a,b):
    """ this module takes two integers a and b , calculates lcm of those """
    if a==0:
        return b
    if b==0:
        return a
    c=gcd(a,b)
    lcm=a*b/c
    return lcm
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
Least_common_factor=lcm(a,b)
print("LCM is: ")
print(Least_common_factor)
tst_functn()

