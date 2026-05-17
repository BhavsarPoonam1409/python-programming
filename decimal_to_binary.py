n=int(input("enter number:"))
reverse=0
while(n>0):
    rem=n%2
    n=n//2
    reverse=reverse*10+rem
binary=0
while(reverse>0):
    rem=reverse%10
    binary=binary*10+rem
    reverse=reverse//10

print(binary)




