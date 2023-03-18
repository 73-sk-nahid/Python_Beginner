a = int(input("How many numbers you want to enter: "))
list = []
odd_sum = 0
even_sum = 0
for i in range(0, a):
    num = int(input("Enter numbers: "))
    list.append(num)
for i in range(0,a):
    if(list[i] % 2 == 0):
        even_sum = even_sum + list[i]
    else:
        odd_sum = odd_sum + list[i]
print("Sum of odd numbers: ", odd_sum)
print("Sum of even numbers: ", even_sum)