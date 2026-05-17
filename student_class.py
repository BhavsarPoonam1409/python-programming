class Student:
    def __init__(self):
        self.name=input("enter student name:")
        self.rollno=int(input("enter student roll number:"))
        self.n1=int(input("enter number 1:"))
        self.n2=int(input("enter number 2:"))
        self.n3=int(input("enter number 3:"))

    def show(self):
        print("student name:",self.name)
        print("student roll number:",self.rollno)
        print("subject 1 marks:",self.n1)
        print("subject 2 marks:",self.n2)
        print("subject 3 marks:",self.n3)

    def total(self):
        self.t=self.n1+self.n2+self.n3
        print("all subject total:",self.t)

    def percentage(self):
        self.per=self.t/3
        print("percentage marks:",self.per)

    def grade(self):
        percentage=self.per
        if(percentage>80):
            print("A grade")
        elif(percentage>70 and percentage<=80):
            print("B grade")
        elif(percentage>60 and percentage<=70):
            print("pass")
        else:
            print("Fail")

s1=Student()
s1.show()
s1.total()
s1.percentage()
s1.grade()