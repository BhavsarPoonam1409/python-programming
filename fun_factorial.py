num=int(input("enter number:"))
def factorial_no(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
    
result=factorial_no(num)
print("factorial is:",result)