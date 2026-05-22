stu_marks={
    'Poonam':[50,60,87],
    'Sakshi':[60,90,80],
    'Jiya':[50,50,50]

}

for sname,marks in stu_marks.items():
    print(sname,":","Total marks:",sum(marks))