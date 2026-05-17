students=[("Ekta",89,),("poonam",88),("dhavni",89),("mona",56)]
for name,marks in students:
    print(name,':',marks)

highest=max(marks for name,marks in students)
for name,marks in students:
    if(highest==marks):
        print("higest marks is:",name,':',marks)

search=input("enter name:")
for name,marks in students:
    if(search==name):
        print(name,':',marks)
total=0
for name,marks in students:
    total=total+marks

average=total/len(students)
print("average is:",average)