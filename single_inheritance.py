class A:
    def display(self):
        print("inside class A")

class B(A):
    def show(self):
        print("Hey from B!!")

obj1=B()
obj1.display()
obj1.show()