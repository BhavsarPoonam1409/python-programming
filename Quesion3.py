n=int(input("Enter number: "))
def  square_no(n):
    for i in range(1,n+1):
        squ=i*i
        cubes=i*i*i
        print("Square of this number is:",squ,"\t","cubes of this number:",cubes)
    return squ
    return cubes     
    
square_no(n)
