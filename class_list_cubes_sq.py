class A:
    def __init__(self,list_1):
        self.list_1=list_1

    def fill(self):
        self.sq_list=[]
        self.cubes_list=[]
        for i in self.list_1:
            sq=i*i
            cubes=i*i*i
            self.sq_list.append(sq)
            self.cubes_list.append(cubes)

        print("sq list:",self.sq_list)
        print("cubes list:",self.cubes_list)

c=A([1,2,3,4])
c.fill()


    
