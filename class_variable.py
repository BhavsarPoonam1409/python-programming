class Emp:
    no_emp=0 #class variable
    def __init__(self):
        self.name=input("Enter Name: ")
        self.sal=int(input("Enter Salary: "))
        Emp.no_emp=Emp.no_emp+1

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.sal)
        print("Total no. of employees:",Emp.no_emp)

e1=Emp()
e1.display()
e2=Emp()
e2.display()
e3=Emp()
e3.display()

    


    


