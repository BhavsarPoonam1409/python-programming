class Book:
    def __init__(self,name):
        self.name=name

class B(Book):
    def __init__(self,name,a_name,price):
        super().__init__(name)
        self.a_name=a_name
        self.price=price

    def show(self):
        print("book name is:",self.name)
        print("book author name is:",self.a_name)
        print("book price is:",self.price)

b1=B("ABc","Ram",700)
b1.show()