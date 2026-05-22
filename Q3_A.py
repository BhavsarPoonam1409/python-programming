class person:  
    def __init__(self,name):
        self.name=name

class Student(person):
    def __init__(self,name):
        super().__init__(name)
        
        self.age=int(input("Enter age:"))

    def display(self):
        print("name: ",self.name)
        print("age:",self.age)
        
s1=Student('Poonam')
s1.display()















     
        
        


        
        
        


