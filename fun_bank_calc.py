global bal
acct_no=input("enter account number:")
cust_name=input("enter custmer name:")
bal=int(input("enter balance:"))

def display():
    print("customer name:",cust_name)
    print("account number:",acct_no)
    print("balance:",bal)

def deposit(amount):
    global bal
    bal=bal+amount
    print(amount,"deposited succesfully")

def withdraw(amount):
    global bal
    if amount>bal:
        print("insufficiant funds")
    else:
        bal=bal-amount
        print(amount,"withdrow from the account")

def bank():
    while(True):
        print("----menu----")
        print("1)deposite")
        print("2)withdraw")
        print("3)display")
        print("4)exit")
        choice=int(input("enter choice:"))
        match choice:
            case 1:
                amount=int(input("enter amount to deposit:"))
                deposit(amount)
            case 2:
                amount=int(input("enter amount to withdrow:"))
                withdraw(amount)
            case 3:
                display()
            case 4:
                return 
            case _:
                print("invalid choice")

bank()