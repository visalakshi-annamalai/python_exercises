'''
Name: visalakshi.annamalai
question no:3
Description:
Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.
'''
mylist=[]
list2=[]
count=0
while count<10 :
    num=raw_input("enter 10 numbers  or q to quit")
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
    print "no odd numbers"
