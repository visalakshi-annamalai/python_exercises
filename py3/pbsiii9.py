def is_sorted(list1):

    for i in list1:

        J=0

        if list1[J]<=list1[J+1]:

            J=J+1

            return True

        else:
 
           return False

    
str=raw_input("enter string")

list1=[]

for i in str:

    list1.append(i)

print is_sorted(list1)

