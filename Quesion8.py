str=input("enter a string: ")
def calc(str):
    upper=0
    lower=0
    for i in str:
        if(i.isupper()):
            upper=upper+1

        else:
            lower=lower+1
    print(upper)
    print(lower)
    return upper,lower
calc(str)
