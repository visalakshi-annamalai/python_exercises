def is_anagram(lsit,listt):
    lis1=[]
    list2=[]
    lsit.sort()
    listt.sort()
    for i in lsit:
        lis1.append(i)
    for j in listt:
        list2.append(j)
    c=(''.join(lis1))
    d=(''.join(list2))
    if c==d :
        return True
    else:
        return False
str1=raw_input("enter STRING 1")
lsit=[]
for i in str1:
    lsit.append(i)
str2=raw_input("enter STRING 2")
listt=[]
for i in str2:
    listt.append(i)

print is_anagram(lsit,listt)
