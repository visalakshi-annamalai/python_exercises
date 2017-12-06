
'''
Name: visalakshi.annamalai
question no:7
Description:check whether the word uses only the specified letters
''' 
def using_only(str1,str2):

    i=0

    while i<len(str1):

        if str1[i] in str2:

            i=i+1

        else:

            return False

    return True



str1=raw_input("enter the string")

str2=raw_input("enter the use_only letters")

c=print using_only(str1,str2)

print c