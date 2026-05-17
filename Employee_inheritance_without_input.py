class Emp:
    def __init__(self,name):
        self.name=name

class B(Emp):
    emp_id=0
    count_department=0
    total_salary=0
    def __init__(self,name,position,department,salary):
        super().__init__(name)
        self.position=position
        self.department=department
        self.salary=salary
        B.emp_id=B.emp_id+1
        if(self.department=="sales"):
            B.count_department=B.count_department+1
        B.total_salary=B.total_salary+self.salary

    def show(self):
        print("employee name is:",self.name)
        print("employee id:",B.emp_id)
        print("employee position is:",self.position)
        print("employee department is:",self.department)
        print("employee salary is:",self.salary)

e1=B("ekta","jr","sales",10000)
e1.show()
e2=B("poonam","jr","sales",10000)
e2.show()

print("total of salary:",B.total_salary)
print("count department is:",B.count_department)