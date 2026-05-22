list1=[]
for i in range(1,11):
    list1.append(i)
print(list1)

#convert list to tuple
tup1=tuple(list1)
print(tup1)

#Indexing
print(tup1[1:3])
print(tup1[::2]) #0 to end odd no
print(tup1[2:8:3]) #3 end 3 jump

#del tup11[::2] #will produce error as its immutable data structure
#tup1[0]=100 #will produce error as its immutable data structure
#dosnt chane val and char in tuble

tup2=()
for i in range(1,11):
    tup2+=(i,) #conceniting to value + #a=a+b  // a+=b
    # i new tuple because , 
print(tup2)