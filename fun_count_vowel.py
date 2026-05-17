str=input("enter string:")

def vowel(str):
    count=0
    for i in range(len(str)):
        if str[i] in 'aioue':
            count=count+1
    return count

result=vowel(str)
print(result)