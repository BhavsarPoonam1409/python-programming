empty_tuple=()
print(type(empty_tuple))
no_tuple=(12,45,78,89,500)
print(no_tuple)
mixed_tuple=(34,'A',"python",466,"hello")
print(mixed_tuple)
for i in no_tuple:
    print(i)

for i in range(len(mixed_tuple)):
    print(i,mixed_tuple[i])