n = int(input("Enter a number 1:"))

i = 1
while i <= n:
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "odd")
    i +=1
    