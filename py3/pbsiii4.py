def has_no_e(strlist):
    with_e=[]
    without_e=[]
    for i in strlist:
        if 'e' in i:
            with_e.append(i)
        elif 'E' in i:
            with_e.append(i)
        else:
            without_e.append(i)
    original_len=float(len(strlist))
    len_without_e=len(without_e)
    percentage=(len_without_e/original_len)*100
    print percentage
str=raw_input("str")
strlist=str.split(' ')
has_no_e(strlist)
