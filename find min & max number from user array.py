a = int(input("Enter range of number: "))
num = []
sum = 0
for i in range(0,a):
    print("Enter ",i+1," numbers:")
    j = int(input())
    num.append(j)
print("Listed numbers: " ,num)
"""
#find maximum & minimum number using sort method

num.sort()
print("Minimum number is: ", num[0])
print("Maximum number is: ", num[-1]) """
max = num[0]
min = num[0]
for x in num:
    if x>max:
        max = x
    elif x < min:
        min = x
print("Minimum number is: ", min)
print("Maximum number is: ", max)