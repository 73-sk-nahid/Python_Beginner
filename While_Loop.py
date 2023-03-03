#-----Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5.---------
i = 50
sum = 0
while i <= 101:
    if i % 3 == 0 and i % 5 != 0:
        sum = sum + i
    i = i + 1
print("Sum", sum)