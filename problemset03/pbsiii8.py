'''
Name: visalakshi.annamalai
question no:8
Description:check whether the string is in alphabetical order
''' 
def is_abcderaian(strlist,d):

    lis1=[]

    strlist.sort()

    for i in strlist:

        lis1.append(i)


    print lis1

    c=(''.join(lis1))

    print c

    if c==d :

        return True


    else:

        return False

str1=raw_input("enter STRING 1")

list=[]

for i in str1:

    list.append(i)


d=(''.join(list))

print is_abcderaian(list,d)