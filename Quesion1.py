str=input("enter name:")
if(str.isdigit()):
    print("this is a number")
elif(str.isalpha()):
    print("this is character")
    
    if(str.islower()):
        print("this is a lowercase letter")
    else:
        print("this is a uppercase letter")
