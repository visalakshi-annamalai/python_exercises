def test_func():
    """   this module is a test function to test our reverse function with few inputs """
    a=' '
    b='madam'
    d='moon'
    test1=reverse(a)
    test2=reverse(b)
    test3=reverse(d)
    if test1==a:
        print True
    else:
        print False
    if test2==b:
        print True
    if test3==d:
        print True
    else:
        print False
    
 
    
def reverse(string):
    """ this module takes an input  string and finds the reverse of the string """
    rev_strings = []
    i = len(string)
    while i:
        i=i- 1                       
        rev_strings.append(string[i])
    rev= ''.join(rev_strings)
    return rev
    
test_func()
a=raw_input("enter the string to be reversed")
c=reverse(a)
if (a==c):
    print True
else :
   print False
   
