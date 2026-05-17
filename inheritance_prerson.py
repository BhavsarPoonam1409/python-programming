class A:
    def __init__(self,name):
        self.name=name

    
class B(A):
    
    def __init__(self,name):
        super().__init__(name)
        self.course=input("enter course:")
        self.semester=int(input("enter semester:"))

    def show(self):
        print("Inside class B")
        print("student name:",self.name)
        print("course name:",self.course)
        print("semester:",self.semester)
        

s1=B('Ekta')
s1.show()