class A:
    def __init__(self,list_1):
        self.list_1=list_1
        
    def fill(self):
        self.even_list=[]
        self.odd_list=[]

        for i in self.list_1:
            if(i%2==0):
                self.even_list.append(i)
            else:
                self.odd_list.append(i)

        print("even list:",self.even_list)
        print("odd list:",self.odd_list)

c=A([67,90,89,56,45])
c.fill()