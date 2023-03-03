#here a simple example using if else
#---------check a number is even or odd------------
a = int(input("Enter a number: "))

if a % 2 == 0:
    print(a, "is even number")
else:
    print(a, "is odd number")

#check where the number is equal or which one is greater
a = 330
b = 330

print("A is greater then B") if a > b else print("They both are equal") if a == b else print("B is greater than A")