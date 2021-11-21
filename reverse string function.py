def reverse_str(str1):
    rever=''
    n = len(str1)
    for i in range(0,n):
        rever=str1[::-1]
    return(rever)
print(reverse_str('1234abcd'))