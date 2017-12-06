def avoids(str,forbidden):
    list1=[]
    list2=[]
    for i in forbidden:
        for j in strlist:
            if i in j:
                list1.append(j)
            else:
                list2.append(j)

    return len(list2)
str1=raw_input("enter sentence")
strlist=str1.split(' ')
forbidden=['a','e','i','o','u']
#forbidden1=['h','j','l','i','p']
print avoids(strlist,forbidden)
#print avoids(strlist,forbidden1)

