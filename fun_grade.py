stu_name=input("enter student name:")
s1=int(input("enter subject 1:"))
s2=int(input("enter subject 2:"))
s3=int(input("enter subject 3:"))
s4=int(input("enter subject 4:"))
s5=int(input("enter subject 5:"))
def total(s1,s2,s3,s4,s5):
    return s1+s2+s3+s4+s5

def per(s1,s2,s3,s4,s5):
    return total(s1,s2,s3,s4,s5)/5

def grade():
    percentage=per(s1,s2,s3,s4,s5)
    grade=""
    if percentage>85:
        grade="A"
    elif percentage>=75 and percentage<85:
        grade="B"
    elif percentage>=50 and percentage<75:
        grade="C"
    elif percentage>30 and percentage<=50:
        grade="D"
    else:
        grade="Reappear"
    return grade


print("total is:",total(s1,s2,s3,s4,s5))
print("percentage is :",per(s1,s2,s3,s4,s5))
print("grade is:",grade())
    