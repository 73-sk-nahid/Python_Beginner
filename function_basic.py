#here we will see some basic function
#actually we use functions for doing the task for single time which will use for multiple time.
#here we will watch a calculation part as an example
def addition(a,b):
    s = a + b
    print("The addition is: ", s)

def multiplication(a,b):
    m = a * b
    print("The multiplication is: ", m)
a = int(input("Enter a positive number: "))
b = int(input("Enter a positive number: "))
addition(a,b)
multiplication(a,b)