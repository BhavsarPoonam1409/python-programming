str=input("enter string:")
chr=input("enter charecter:")
def frequancy(str,chr):
    count=0
    for i in range(len(str)):
        if(str[i]==chr):
            count=count+1
    return count

result=frequancy(str,chr)
print(result)