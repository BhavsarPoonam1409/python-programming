n=int(input("enter number:"))
circle={}
for r in range(1,n+1):
    circumference=2*3.14*r
    circle[r]=circumference

print(circle)
for r,circumference in circle.items():
    print(r,':',circumference)