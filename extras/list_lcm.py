def test_functn():
""" this module is a test function to test lcm """
    
    list2=[4,8,12,16]
    result=reduce(lcm,list2)
    print result
    list1=[3,6,8,0]
    result=reduce(lcm,list1)
    print result
    
    
def lcm(m, n):
  """ this modules takes list of integers and compute lcm in pairs """
    if m > n:
        max = m
    else:
        max = n
    try:
        while(True):
            if((max % m == 0) and (max % n == 0)):
                lcm = max
                return lcm
                break
            max=max+1
    except Exception as e:
        print e

listt=[12,16,8,9]
result=reduce(lcm,listt)
print result
test_functn()