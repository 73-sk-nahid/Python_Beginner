# here we will use try for handling the error
a = input("Enter a number: ")  # here we have to input an int number
print(f"The multiplication table of {a} is")
try:  # if we input any string then it will call for error and will print the except part
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a) * i}")
except ValueError:  # ValueError will search for the input value is the actual type or not
    # there are many except also available like IndexError which will check that is the index value have or not
    print("Number entered is not an integer")
print("Program finished")
