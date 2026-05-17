t1=0
t2=1
nexterm=t1+t2
print(t1)
print(t2)
for i in range(2,11):
    print(nexterm)
    t1=t2
    t2=nexterm
    nexterm=t1+t2
    