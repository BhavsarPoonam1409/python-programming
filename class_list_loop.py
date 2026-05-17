class A:
    def __init__(self,list_1):
        self.list_1=list_1

    def loop(self):
        print(self.list_1)
        for i in self.list_1:
            print(i)

        for i in range(len(self.list_1)):
            print(i,self.list_1[i])

c=A([78,90,67,45])
c.loop()
    