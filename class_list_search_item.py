class A:
    def __init__(self,list_1,item):
        self.list_1=list_1
        self.item=item

    def search(self):
        count=0
        for i in range(len(self.list_1)):
            if(self.list_1[i]==self.item):
                count=1
        
        if(count==1):
            print("present")
        else:
            print("Absent")

c=A([89,90,67,66],66)
c.search()