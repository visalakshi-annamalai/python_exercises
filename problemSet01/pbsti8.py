'''
Name: visalakshi.annamalai
question no:8
Description:Implement a function that satisfies the specification. Use a try-except block.

def getRatios(vect1, vect2):
	"""Assumes: vect1 and vect2 are lists of equal length of numbers
	Returns: a list containing the meaningful values of
	vect1[i]/vect2[i]"""
'''
def getRatios(vect1, vect2):
#			find ratio of two list 		
    ratios=[]
    for i in range(len(vect1)):
        vectt1=float(vect1[i])
        vectt2=float(vect2[i])
        ratios.append(vectt1/vectt2)
    return ratios
vect1=[4,6,8,10]
vect2=[9,6,8,10]

c=getRatios(vect1,vect2)
print c
