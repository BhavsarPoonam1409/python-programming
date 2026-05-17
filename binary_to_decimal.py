n=int(input("enter number:"))
t=1
dec=0
while(n>0):
    rem=n%10
    dec=dec+rem*t
    t=t*2
    n=n//10
print(dec)
