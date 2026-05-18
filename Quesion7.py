n1=int(input("enter a number: "))
def sum_digit(n1):
    sum=0
    while(n1>0):
        rem=n1%10
        sum=sum+rem
        n1=n1//10
    return sum
result=sum_digit(n1)
print("sum of digits is: ",sum_digit(n1))
