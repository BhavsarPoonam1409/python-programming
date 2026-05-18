string=input("enter string:")
def palindrom(string):
    reversed_string=""
    for i in range(len(string)-1,-1,-1):
        reversed_string=reversed_string+string[i]
    if(reversed_string==string):
        return "string is palindrom"
    else:
        return "string is not palindrom"

print(palindrom(string))