global bal
acc_no=input("Enter account number: ")
cust_name=input("Enter customer name: ")
bal=int(input("Enter initial balance: "))

def display():
    print("Customer Nmae:",cust_name)
    print("Account number:",acc_no)
    print("Balnace:",bal)

def deposit(amount):
        global bal
        bal=bal+amount
        print(amount,"deposited succesfully!!")

def withdraw(amount):
        global bal
        if amount>bal:
            print("Insufficient funds!!")
        else:
            bal=bal-amount
            print(amount,"withdrawn from the account")

def bank():
    while(True):
        print("----Menu----")
        print("1) Deposit")
        print("2) Withdraw")
        print("3) Exit")
        
        
        choice=int(input("Enter your choice: "))
        match choice:
            case 1:
                amount=int(input("Enter amount to deposit: "))
                deposit(amount)
            case 2:
                amount=int(input("Enter amount to withdraw: "))
                withdraw(amount)
            
            case 3:
                return
            case _:
                print("Invalid choice!!")

bank()
                
