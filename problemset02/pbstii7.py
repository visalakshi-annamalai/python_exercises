'''
Name: visalakshi.annamalai
question no:7
Description:def isPalindrome(s):
	"""Assumes s is a str
	Returns True if s is a palindrome; False otherwise.
	Punctuation marks, blanks, and capitalization are
	ignored."""
'''

def ispalindrome(my_str):
    letters = []
    for c in my_str:
        if c.isalpha():
            letters.append(c)
    return letters == letters[::-1]
str=raw_input("string")
c=ispalindrome(str)
print c
