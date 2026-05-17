class Book:
    def __init__(self):
        self.name=""

    def get_input(self):
        self.name=input("enter book name:")

class B(Book):
    def __init__(self):
        self.a_name=input("enter book author name:")
        self.price=int(input("enter book price:"))

    def show(self):
        print("book name is:",self.name)
        print("book author name is:",self.a_name)
        print("book price:",self.price)

b1=B()
b1.get_input()
b1.show()