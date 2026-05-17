n=int(input("enter number:"))
sum_digit=0
while(n>0):
    rem=n%10
    sum_digit=sum_digit+rem
    n=n//10
print("the sum of digit is:",sum_digit)