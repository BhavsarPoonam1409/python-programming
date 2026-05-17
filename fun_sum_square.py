n=int(input("enter number:"))
def sum_square(n):
    sum_sq=0
    for i in range(1,n+1):
        square=i*i
        sum_sq=sum_sq+square
    return sum_sq

result=sum_square(n)
print("sun of square is this number:",result)