age=int(input("enter age"))
principle_amt=int(input("enter principle amount:"))
loan_year=int(input("enter year of loan:"))

def simple_intrest(age,principle_amt,loan_year):
    if(age>60):
        si=principle_amt*7.25/100*loan_year
    else:
        si=principle_amt*7/100*loan_year
    return si

result=simple_intrest(age,principle_amt,loan_year)
print("simple intrest is:",result)