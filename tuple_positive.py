list_1=[12,23,67,-78,-45,8,-2,4,-89,0]
positive_tuple=()
negetive_tuple=()
zero_tuple=()
for i in list_1:
    if i>0:
        positive_tuple=positive_tuple+(i,)
    elif i<0:
        negetive_tuple=negetive_tuple+(i,)
    else:
        zero_tuple=zero_tuple+(i,)

print(positive_tuple)
print(negetive_tuple)
print(zero_tuple)