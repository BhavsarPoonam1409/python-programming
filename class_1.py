class car:
    def __init__(self,car_name,speed):
        self.name=car_name
        self.speed=speed

    def display(self):
        print("car name:",self.name)
        print("car speed:",self.speed)

car1=car("Nano",100)
car1.display()
car2=car("BMW",200)
car2.display()