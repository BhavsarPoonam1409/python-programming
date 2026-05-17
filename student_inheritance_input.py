class Student:
    def __init__(self):
        self.name=""
        self.age=0

    def get_input(self):
        self.name=input("enter name:")
        self.age=int(input("enter student age:"))


class B(Student):
    def __init__(self):
        self.m1=int(input("enter student subject 1 marks:"))
        self.m2=int(input("enter student subject 2 marks:"))
        self.m3=int(input("enter student subject 3 marks:"))
        self.m4=int(input("enter student subject 4 marks:"))
        self.m5=int(input("enter student subject 5 marks:"))
        self.m6=int(input("enter student subject 6 marks:"))
        self.m7=int(input("enter student subject 7 marks:"))

    def total(self):
        self.t=self.m1+self.m2+self.m3+self.m4+self.m5+self.m6+self.m7

    def per(self):
        self.p=self.t/7


    def show(self):
        print("student name is:",self.name)
        print("student age is:",self.age)
        print("student subject 1 marks:",self.m1)
        print("student subject 2 marks:",self.m2)
        print("student subject 3 marks:",self.m3)
        print("student subject 4 marks:",self.m4)
        print("student subject 5 marks:",self.m5)
        print("student subject 6 marks:",self.m6)
        print("student subject 7 marks:",self.m7)
        print("student total marks:",self.t)
        print("student percentage marks:",self.p)

    def grade(self):
        per=self.p
        if(per>90):
            print("A grade")
        elif(per>80 and per<=90):
            print("B grade")
        elif(per>70 and per<=80):
            print("C grade")
        elif(per>60 and per<=70):
            print("D grade")
        elif(per>50 and per<=60):
            print("pass")
        else:
            print("fail")

s1=B()
s1.get_input()
s1.total()
s1.per()
s1.show()
s1.grade()