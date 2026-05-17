class A:
    def __init__(self,list_1):
        self.list_1=list_1
    
        
    def operator(self):
        print(type(self.list_1))
        print(max(self.list_1))
        print(min(self.list_1))
        print(sum(self.list_1))
        print(sorted(self.list_1))
        print(len(self.list_1))
        self.list_1.index(45)
        print(self.list_1)
        self.list_1.pop()
        print(self.list_1)
        

c=A([12,67,45,12,56,90])
c.operator()