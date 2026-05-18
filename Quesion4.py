n=int(input("Enter number:"))

def sum_sq_even(n):
    even_sq_list=[]
    sum_sq=0
    for i in range(1,n+1):
        if i%2==0:
            sq=i*i
            sum_sq=sum_sq+sq
            even_sq_list.append(sum_sq)
    print(even_sq_list)
    return sum_sq
print(sum_sq_even(n)) 