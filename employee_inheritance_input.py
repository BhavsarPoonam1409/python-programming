class Emp:
    def __init__(self):
        self.name=""

    def get_input(self):
        self.name=input("enter employee name:")

class B(Emp):
    def __init__(self):
        self.position=input("enter employee position:")
        self.department=input("enter employee department")

    def show(self):
        print("employee name is:",self.name)
        print("employee position is:",self.position)
        print("employee department:",self.department)

e1=B()
e1.get_input()
e1.show()