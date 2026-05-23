def swap(a, b):
    return b, a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Before swapping:", x, y)

x, y = swap(x, y)

print("After swapping:", x, y)