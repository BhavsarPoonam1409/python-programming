class Bank:
    def __init__(self): #Constructor
        self.acc_no=0
        self.cust_name="" 
        self.bal = 0

    def accept_input(self):
        self.acct_no=int(input("Enter account number"))
        self.cust_name=input("Enter customer name: ")
        self.bal=int(input("Enter initial balance: "))

    def display(self):
        print("Account no.:",self.acc_no)
        print("Customer Name:",self.cust_name)
        print("Current Balance:",self.bal)

    def deposit(self):
        dep_amt=int(input("Enter amount to be depositeed: "))
        self.bal=self.bal+dep_amt
        print("Account",self.acc_no,"credited with amount",dep_amt)

    def withdraw(self):
        withdraw_amt=int(input("Enter amount to be withdrawn:"))
        if withdraw_amt<=self.bal:
            self.bal=self.bal-withdraw_amt
            print("Account",self.acct_no,"debited with amount",withdraw_amt)
        else:
            print("Insufficient Balance!!")
cust_1=Bank() 
cust_1.accept_input()
while True:
    print("---Menu---")
    print("1) Deposit")
    print("2) withdraw")
    print("3) Display")
    print("4) Exit")
    choice=int(input("enter choice: "))
    match choice:
        case 1:
            cust_1.deposit()
        case 2:
            cust_1.withdraw()
        case 3:
            cust_1.display()
        case 4:
            break
        case _:
            print("Invalid choice!!")

        
        
        

