def square_no(n):
    square_sum=0
    for i in range(1,n+1):
        squ=i*i
        square_sum=square_sum+squ
    return square_sum
n=int(input("Enter no:"))
ans=square_no(n)
print("Square sum is:",ans)
