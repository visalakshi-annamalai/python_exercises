'''
Name: visalakshi.annamalai
question no:3
Description:check whether the string has e
'''
def has_no_e(str):
    for i in str:
        if 'e' in str:
            return False
        elif 'E'in str:
            return False
    return True
str=raw_input("str")
c=has_no_e(str)
print c
    
