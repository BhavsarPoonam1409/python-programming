class Bank:
    def __init__(self):
        self.cust_name=""
        self.acct_no=0
        self.balance=0

    def get_input(self):
        self.cust_name=input("enter custemer name:")
        self.acct_no=int(input("enter account number:"))
        self.balance=int(input("enter custemer balance:"))

    def display(self):
        print("custemer name is:",self.cust_name)
        print("custemer account no is:",self.acct_no)
        print("custemer currant balance is:",self.balance)

    def deposite(self):
        depo_amt=int(input("enter deposite amount"))
        self.balance=self.balance+depo_amt
        print(depo_amt,"deposite successfully!!")

    def withdraw(self):
        with_amt=int(input("enter withdraW amt:"))
        if(with_amt>self.balance):
            print("insufiant balance")
        else:
            self.balance=self.balance-with_amt
            print(with_amt,"withdraw successfully!!")

    
c1=Bank()
c1.get_input()
while(True):
    print("---menu-----")
    print("1)display")
    print("2)deposite")
    print("3)withdraw")
    print("exite")
    choice=int(input("enter choice:"))
    if(choice==1):
        c1.display()
    elif(choice==2):
        c1.deposite()
    elif(choice==3):
        c1.withdraw()
    elif(choice==4):
        break
    else:
        print("invalid choice")

        