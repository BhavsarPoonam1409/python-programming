class Bank:
    def __init__(self):
        self.acct_no=0
        self.bal=0
        self.cust_name=""

    def accept_input(self):
        self.acct_no=int(input("enter accuont no:"))
        self.bal=int(input("enter balance:"))
        self.cust_name=input("enter custemer name:")

    def display(self):
        print("account number:",self.acct_no)
        print("current balance:",self.bal)
        print("custemer name:",self.cust_name)

    def deposite(self):
        depo_amt=int(input("enter deposited amount:"))
        self.bal=self.bal+depo_amt
        print("account :",self.acct_no,"credited amount:",depo_amt)

    def withdraw(self):
        withdraw_amt=int(input("enter withdraw amount:"))
        if(withdraw_amt<=self.bal):
            self.bal=self.bal-withdraw_amt
        else:
            print("insuffiant balance")
        print("account:",self.acct_no,"debited amount:",withdraw_amt)

cust1=Bank()
cust1.accept_input()
cust1.display()
cust1.deposite()
cust1.display()
cust1.withdraw()
cust1.display()

while(True):
    print("---menu---")
    print("1)deposite")
    print("2)withdraw")
    print("3)Display")
    print("4)exite")
    choice=int(input("enter choice:"))
    match choice:
        case 1:
            cust1.deposite()
        case 2:
            cust1.withdraw()
        case 3:
            cust1.display()
        case 4:
            break
        case _:
            print("invalide choice")



