'''
Name:visalakshi annamalai
date:12-12-17
Description:area
'''
class shape():
    def area(self):
        print "parent class"
class square(shape):
    def __init__(self,length=0):
        self.length=length
        
    def area(self):
        return self.length*self.length
s=square(6)
c=s.area()
print c
