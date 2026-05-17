class Student:
    def __init__(self,name):
        self.name=name

class B(Student):
    stu_id=0
    def __init__(self,name,age,m1,m2,m3,m4,m5,m6,m7):
        super().__init__(name)
        self.age=age
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.m6=m6
        self.m7=m7
        B.stu_id=B.stu_id+1

    def total(self):
        self.t=self.m1+self.m2+self.m3+self.m4+self.m5+self.m6+self.m7

    def per(self):
        self.p=self.t/7

    def show(self):
        print("student name is:",self.name)
        print("student id is:",B.stu_id)
        print("student age is:",self.age)
        print("student subject 1 marks is:",self.m1)
        print("student subject 2 marks is:",self.m2)
        print("student subject 3 marks is:",self.m3)
        print("student subject 4 marks is:",self.m4)
        print("student subject 5 marks is:",self.m5)
        print("student subject 6 marks is:",self.m6)
        print("student subject 7 marks is:",self.m7)
        print("student total marks is:",self.t)
        print("student percentage is:",self.p)

    
class C(B):
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
            print("Pass")
        else:
            print("fail")

    
s1=C("ekta",19,90,90,95,93,93,64,86)
s1.total()
s1.per()
s1.show()
s1.grade()
        