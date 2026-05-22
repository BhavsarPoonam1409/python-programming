n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0
i = 1

while i <= n:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1

print("Even numbers sum =", even_sum)
print("Odd numbers sum  =", odd_sum)