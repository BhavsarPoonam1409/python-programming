n=int(input("enter number:"))
i=1
sum_even=0
sum_odd=0
while(i<=n):
    if(i%2==0):
        sum_even=sum_even+i
    else:
        sum_odd=sum_odd+i
    i=i+1

print("sum of even number is:",sum_even)
print("sum of odd number is:",sum_odd)