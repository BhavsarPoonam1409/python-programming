name=input("enter name:")
vowel_list=[]
consonant_list=[]
for i in range(len(name)):
    if name[i] in 'aioue':
        vowel_list.append(name[i])
    else:
        consonant_list.append(name[i])

print(vowel_list)
print(consonant_list)
       