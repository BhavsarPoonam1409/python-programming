def freq_ctr(str,ch):
    ctr=0
    for i in range(len(str)):
        if str[i]==ch:
            ctr=ctr+1
    return ctr
str=input("Enter string:")
ch=input("Enter character:")
count=freq_ctr(str,ch)
print("count:",count)