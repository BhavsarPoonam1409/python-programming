base=int(input("Enter base:"))
exp=int(input("Enter exponent:"))
ans=1
for i in range(1,exp+1):
    ans=ans*base
print("Answer:",ans)

