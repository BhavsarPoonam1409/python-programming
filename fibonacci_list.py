a=[0,1]
for i in range(2,11):
    t=a[i-1]+a[i-2]
    a.append(t)

print(a)