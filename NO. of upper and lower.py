def no_of_upperlower(str1):
    upper_count=0
    lower_count=0
    n=len(str1)
    for i in range(0,n):
        if str1[i].isupper():
            upper_count+=1
        elif str1[i].islower():
            lower_count+=1
        else:
            pass
    print('No. of uppercase characters: ',upper_count)
    print('No. of lowercase characters: ',lower_count)
no_of_upperlower('The quick Brow Fox')