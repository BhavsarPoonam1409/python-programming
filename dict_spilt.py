sentance=input("enter sentance:")
words=sentance.split()
print(words)
word_dict={}
for i in words:
    word_dict[i]=len(i)

print(word_dict)