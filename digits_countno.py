no=int(input("Enter number:"))
digit=0
while(no>0):
    rem=no%10
    digit=digit+1
    no=no//10
print("Total number of digits:",digit)

