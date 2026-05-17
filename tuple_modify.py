list_1=[]
for i in range(1,11):
    list_1.append(i)

print(list_1)
tuple_1=tuple(list_1)
print(tuple_1)
#indexing
print(tuple_1[1:3])
print(tuple_1[::2])
print(tuple_1[2:8:3])
#del tuple_1 [::2]#will produce error as it s immutable data structure
#tuple_1[0] #will priduce error as it s immutable data structure
tuple_2=()
for i in range(1,11):
    tuple_2=tuple_2+(i,)
print(tuple_2)

