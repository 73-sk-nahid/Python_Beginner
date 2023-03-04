a = int(input("Enter max number: "))
list = []
sum = 0
for i in range(0,a):
    print("Enter ",i+1," numbers:")
    j = int(input())
    sum = sum + j
    list.append(j)
print("Listed numbers: " ,list)
list.sort()
print("After sorted: ", list)
print("Sum of the numbers: ", sum)