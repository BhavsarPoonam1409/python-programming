class Car:
    def __init__(self):
        self.name=""
    
    def get_input(self):
        self.name=input("enter car name:")
    
class B(Car):
    def __init__(self):
        self.speed=int(input("enter speed:"))
        self.price=int(input("enter car price:"))

    def show(self):
        print("car name is:",self.name)
        print("car speed is:",self.speed)
        print("car price is:",self.price)

c1=B()
c1.get_input()
c1.show()