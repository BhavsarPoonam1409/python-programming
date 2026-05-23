no1 = int(input("Enter a frist subject marks: "))
no2 = int(input("Enter a second subject marks: "))
no3 = int(input("Enter a thired subject marks: "))




sum = no1+no2+no3
percentage = sum * 100 / 300
marks = percentage

print("Display The Total Marks ",sum)
print("Display The Total percentage ",percentage)

if(marks>=90 and marks<=100):
    print("your grade is A")
elif(marks>=80 and marks<=89):
    print("your grade is B")
elif(marks>=70 and marks<=79):
    print("your grade is C")
elif(marks>=60 and marks<=69):
    print("your grade is D")
else:
    print("your grade is F")



