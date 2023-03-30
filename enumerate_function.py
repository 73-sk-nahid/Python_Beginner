"""enumerate function allows user to auto-detect automatically
 index of list tuple or string in sequentially"""

# look here a list of marks

marks = [33, 41, 52, 82, 67, 58]

index = 0
for mark in marks:
    print(mark)
    if (index == 3):  # checking the index number manually
        # by assigned index = 0
        print("Well done, got A+")
    index += 1  # incrementing index manually by assign index += 1

# this (08 - 14) can be done in a easy way with enumerate
# here it is

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Well done, got A+")
""" It actually count the index automatically by 
 enumerate() built in function"""