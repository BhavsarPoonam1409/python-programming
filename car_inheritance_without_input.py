class Car:
    def __init__(self,name):
        self.name=name

class B(Car):
    def __init__(self,name,speed,price,model):
        super().__init__(name)
        self.speed=speed
        self.price=price
        self.model=model

    def show(self):
        print("car name is:",self.name)
        print("car speed is:",self.speed)
        print("car model is:",self.model)
        print("car price is:",self.price)

    
c1=B("BMW",200,2020,10000)
c1.show()
c2=B("nano",700,2019,800000)
c2.show()
        