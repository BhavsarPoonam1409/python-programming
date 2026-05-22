class person:  
    def __init__(self,name):
        self.name=name

class Student(person):
    def __init__(self,name):
        super().__init__(name)
        self.course=input("Enter course name: ")
        self.sem=int(input("Enter semester:"))

    def display(self):
        print("Student name: ",self.name)
        print("course:",self.course)
        print("Semster:",self.sem)
s1=Student('Poonam')
s1.display()
