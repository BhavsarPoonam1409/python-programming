def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multipy(x,y):
    return x * y
def divide(x,y):
    return x / y
def modulo(x,y):
    return x % y



no1=float(input("Enter first number: "))
no2=float(input("Enter second number : "))
op = input("Enter operator (+, -, *, /, %): ")

if op =="+":
    print("Result:", add(no1,no2))
elif op == "-":
    print("Result ", subtract(no1,no2))
elif op == "*":
    print("Result ", multipy(no1,no2))
elif op == "/":
    print("Result ", divide(no1,no2))
elif op == "%":
    print("Result ", modulo(no1,no2))

else:
    print("Invalid operator")








