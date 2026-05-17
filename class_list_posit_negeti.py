class A:
    def __init__(self,list_1):
        self.list_1=list_1
        
    def fill(self):

        self.positive_list=[]
        self.negetive_list=[]
        self.zero_list=[]

        for i in self.list_1:
            if(i>0):
                self.positive_list.append(i)
            elif(i<0):
                self.negetive_list.append(i)
            else:
                self.zero_list.append(i)

        print("positive:",self.positive_list)
        print("negetive:",self.negetive_list)
        print("zero:",self.zero_list)

c=A([90,99,-89,-67,0,89,0])
c.fill()