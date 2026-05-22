def vowels_cnt(str):
     
    count = 0
    for i in range(len(str)):
        if str[i] in "aeiou":
            count = count+1
    return count
s = input("Enter a string: ")
count = vowels_cnt(str)
print("count:",count)
