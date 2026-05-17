uname=input("enter user name:")
password=int(input("enter password:"))

def login(uname,password):

    if uname=="ekta" and password==123:
        return"welcome user"
    else:
        return"invalid credentials"
    

result=login(uname,password)
print(result)
