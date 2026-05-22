def simple_intrest():
    if age > 60:
        r = principal_amount * 7.25 / 100 * year_loan
    else:
        r = principal_amount * 7 / 100 * year_loan
    return r

age = int(input("enter age: "))
principal_amount = int(input("enter p: "))
year_loan = int(input("enter year of loan: "))

result = simple_intrest()
print(result)