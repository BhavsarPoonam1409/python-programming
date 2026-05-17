class EMP:
    emp_no=0
    def __init__(self):
        self.name=input("enter name:")
        self.sal=int(input("enter salary:"))
        EMP.emp_no=EMP.emp_no+1

    def display(self):
        print("name of employee:",self.name)
        print("salary of employee:",self.sal)
        print("number of employee:",EMP.emp_no)

e1=EMP()
e1.display()
e2=EMP()
e2.display()
e3=EMP()
e3.display()


