def merge(left,right):

    """ accepts two lists from mergesort function after sorting merges the list """

    result=[]

    i=0

    j=0

    while i<len(left) and j<len(right) :

        if(left[i] < right[j]) :

            result.append(left[i])

            i=i+1

        else:

            result.append(right[j])

            j=j+1

    result=result+left[i:]

    result=result+right[j:]

    return result

def mergesort(lst):

    """ it takes a list as input and divides the list into half recursively until the lsit is left with single element on left and right lists and then passes to the merge """

    if(len(lst) <= 1):

        return lst

    mid=int(len(lst)/2)

    left=mergesort(lst[:mid])

    right=mergesort(lst[mid:])

    return merge(left,right)

    
arr=[2,4,1,7]

print mergesort(arr)
