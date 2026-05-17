import math
from math import sqrt,pi
class A:
    def __init__(self):
        self.a=16

    def display(self):
        print("Inside class A")
        print(math.sqrt(self.a))

class B(A):
    def show(self):
        print("Inside class B:")
        print(sqrt(25))
        print("value of a:",self.a)
        print("value of pi:",pi)
        
class C(B):
    pass

c=C()
c.show()
c.display()