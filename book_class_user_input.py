class Book:
    count_book=0
    total_price=0
    def __init__(self):
        self.name=""
        self.a_name=""
        self.price=0

    def get_input(self):
        self.name=input("enter book name:")
        self.a_name=input("enter author name is:")
        self.price=int(input("enter book price:"))
        if(self.name=="ABC"):
            Book.count_book=Book.count_book+1
        Book.total_price=Book.total_price+self.price

    def show(self):
        print("book name is:",self.name)
        print("book author name is:",self.a_name)
        print("book price is:",self.price)


b1=Book()
b1.get_input()
b1.show()
b2=Book()
b2.get_input()
b2.show()

print("total price book:",Book.total_price)
print(Book.count_book,"books name is ABC")

    