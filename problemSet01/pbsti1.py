'''
Name: visalakshi.annamalai
question no:1
Description:Write a program that examines three variables?x, y, and z? and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.
'''
mylist=[]
list2=[]
count=0
while count<10 :
    num=raw_input("enter number or q to quit")
    if num== 'q':
        break
    else:
        mylist.append(int(num))
        count=count+1
print mylist
for i in mylist:
    if i%2<>0:
        list2.append(i)
    else:
        print "not an odd number "
try:
    print list2
    print max(list2)
except:
    print "empty list"
