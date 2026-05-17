str=input("enter string:")
def revers(str):
    revers_string=""
    for i in range(len(str)-1,-1,-1):
        revers_string=revers_string+str[i]
    return revers_string

result=revers(str)
print(result)