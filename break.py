#using of break in python for discontinue the loop
#for example here a loop
n = int(input("Enter range>10: "))
for i in range(1,n):
    print("5 x", i, "=", 5*i)
    if(i == 10):
        break
print("Loop breaks when i reach to 10")

