def rev_str(text):
    reversed_string=""
    for i in range(len(text)-1,-1,
        -1):
        reversed_string=reversed_string+text[i]
    return reversed_string
user_input=input("enter a string:")
result=rev_str(user_input)
print("result:",result)