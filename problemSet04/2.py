'''
Name:visalakshi annamalai
date:12-12-17
Description:gender
'''
class person():
    def getGender(self):
        pass
class male(person):
    def getGender(self):
        print "male"
class female(person):
    def getGender(self):
        print "female"
m=male()
m.getGender()
f=female()
f.getGender()