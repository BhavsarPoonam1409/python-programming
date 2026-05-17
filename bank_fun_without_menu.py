global bal
acct_no=int(input("enter account nimber:"))
cust_name=input("enter custemer name:")
bal=int(input("enter balance:"))


def display():
    print("account number:",acct_no)
    print("custemer name:",cust_name)
    print("curant blance:",bal)

amount=int(input("enter amount"))
def deposite(amount):
    global bal
    bal=bal+amount
    print("deposite amount:",amount)

with_amount=int(input("enter amount:"))
def withdraw(with_amount):
    global bal
    if(with_amount>bal):
        print("insuffiant blance")
    else:
        bal=bal-with_amount
    print("withdraw amount:",with_amount)

deposite(amount)
withdraw(with_amount)
display()

