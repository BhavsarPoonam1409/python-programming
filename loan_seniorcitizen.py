def simple_interest():
    return

principal = float(input("Enter the principle amount:"))
time = float(input("Enter year:"))
age = float(input("Enter age:"))
rate=0

if(age>60):
    rate = 7.25
else:
    rate = 7
    
si=(principal*rate*time)/100
print("simple Interest :",si)