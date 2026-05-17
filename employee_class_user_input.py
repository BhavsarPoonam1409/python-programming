class EMP:
    emp_id=0
    emp_count=0
    emp_department=0
    total_salary=0
    def __init__(self):
        self.name=""
        self.position=""
        self.department=""
        self.salary=0
        EMP.emp_id=EMP.emp_id+1
        EMP.emp_count=EMP.emp_count+1

    def get_input(self):
        self.name=input("enter employee name:")
        self.position=input("enter employee position:")
        self.department=input("enter employee department:")
        self.salary=int(input("enter emplyee salary:"))
        if(self.department=="sales"):
            EMP.emp_department=EMP.emp_department+1
        EMP.total_salary=EMP.total_salary+self.salary

    def show(self):
        print("employee name is:",self.name)
        print("employee id is:",EMP.emp_id)
        print("employee position is:",self.position)
        print("emplyee department is:",self.department)
        print("employee salary is:",self.salary)

e1=EMP()
e1.get_input()
e1.show()
e2=EMP()
e2.get_input()
e2.show()
e3=EMP()
e3.get_input()
e3.show()

average=EMP.total_salary/EMP.emp_count
print("total salry of employee is:",EMP.total_salary)
print("employee salary average is:",average)
print(EMP.emp_department,"employee are from sales department")
