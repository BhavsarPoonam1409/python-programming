class A:
    def __init__(self):
        self.name=""
        self.speed=0
        self.price=0
        self.model=0

    def get_input(self):
        self.name=input("enter car name:")
        self.speed=int(input("enter car speed:"))
        self.price=int(input("enter car price:"))
        self.model=int(input("enter car model:"))

    def show(self):
        print()
        print("car name is:",self.name)
        print("car speed:",self.speed)
        print("car price:",self.price)
        print("car model:",self.model)


c1=A()
c1.get_input()
c1.show()
c2=A()
c1.get_input()
c2.show()
