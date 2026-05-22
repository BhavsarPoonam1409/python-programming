n=int(input("Enter n:"))
circle={}
for radius in range(1,n+1):
    circumference=2*3.14*radius
    circle[radius]=circumference

print(circle)

for radius,circumference in circle.items():
    print(radius,":",circumference)