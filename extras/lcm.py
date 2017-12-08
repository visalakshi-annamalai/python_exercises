def test_functn(): 
  """ this module is a test function to test lcm """
  m=60
  n=36
  result=lcm(m,n)
  print result
  m=0
  n=2
  result=lcm(m,n)
  print result
  m=6
  n=9
  result=lcm(m,n)
  print result
  
    
def lcm(m, n):
  """ this modules takes two integers m and n and compute lcm  """
  if m>n:
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
m=12
n=16
result=lcm(m,n)
print result
test_functn()