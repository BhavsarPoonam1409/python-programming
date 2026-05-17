def fact_recursion(no):
    if(no==1):
        return 1
    return no*fact_recursion(no-1)

no=int(input("enter no:"))
result=fact_recursion(no)
print("factorial is:",result)