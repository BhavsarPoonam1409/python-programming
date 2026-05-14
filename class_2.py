class student:
    def __init__(self,sname,m1,m2,m3):
        self.sname=sname
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.total=self.m1+self.m2+self.m3
        
    def display(self):
        print("student name:",self.sname)
        print("marks 1:",self.m1)
        print("marks 2:",self.m2)
        print("marks 3:",self.m3)
        print("total marks:",self.total)
        per=self.total/3
        print("prrcentage:",per)


s1=student("Ekta",89,90,95)
s2=student("Archita",45,67,56)
s3=student("Tanu",78,77,85)
s1.display()
s2.display()
s3.display()