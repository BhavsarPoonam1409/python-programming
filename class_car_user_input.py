class Car:
    total_price=0
    count_name=0
    car_count=0
    def __init__(self):
        self.name=""
        self.speed=0
        self.model=0
        self.price=0
        

    def get_input(self):
        self.name=input("enter car name:")
        self.speed=int(input("enter car speed is:"))
        self.model=int(input("enter car model:"))
        self.price=int(input("enter car price:"))
        Car.car_count=Car.car_count+1
        Car.total_price=Car.total_price+self.price
        if(self.name=="BMW"):
            Car.count_name=Car.count_name+1

    def show(self):
        print("car name is:",self.name)
        print("car speed is:",self.speed)
        print("car model is:",self.model)
        print("car price is:",self.price)

    
c1=Car()
c1.get_input()
c1.show()
c2=Car()
c2.get_input()
c2.show()

average=Car.total_price/Car.car_count
print("total price of car is:",Car.total_price)
print("average of car is:",average)
print(Car.count_name,"car is BMW name")