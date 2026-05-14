class car:
    def __init__(self):
        self.name=""
        self.speed=0

    def get_input(self):
        self.name=input("enter car name:")
        self.speed=int(input("enter car speed:"))

    def display(self):
        print("car name:",self.name)
        print("car spped:",self.speed)

car1=car()
car2=car()
car1.get_input()
car2.get_input()
car1.display()
car2.display()     