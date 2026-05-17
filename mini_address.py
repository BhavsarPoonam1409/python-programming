mini=[("Ekta",3908),("Archita",6789),("Diya",6754)]
contact=("tina",7890)
mini.append(contact)
print(mini)

search=input("enter name:")
for name,contact in mini:
    if(search==name):
        print(name,":",contact)

for name,contact in mini:
    if(search==name):
        del contact
    print(name,":",contact)


for name,contact in mini:
    print(name,":",contact)


