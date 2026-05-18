string=input("enter string:")
digit=0
letter=0
for i in range(len(string)):
    
    if(string[i].isdigit()):
        digit=digit+1   
    else:
        letter=letter+1
print("the digit is:",digit)
print("the letter is:",letter)