#######     printing name using for loop
name = input("Enter your name: ")
for i in name:
    print(i)
    if (i == "b"):
        print("This is something special!")


########    print from array using for loop
colors = ["Red", "Green", "Blue", "Yellow"]
for i in colors: #here "i" can be any string
    print(i)


######  print 1 to 9 using range
for j in range(1, 9):
    print(j + 1)
######  print 1 to 8 using range
for j in range(1,9):
    print(j) #just remove the +1 which was adding 1

######  print 1 to 9 using range with increment of 2
for i in range(1,10,2):
    print(i)
