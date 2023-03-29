a = 5
b = 3
# One line if else statement, with 3 conditions
print("A") if a > b else print("=") if a == b else print("B")
# this syntax is equivalent to
if a>b:
    print("A")
elif a == b:
    print("=")
else:
    print("B")

# here another example of Short-hand if else with assign
c = 9 if a>b else 0
print(f"a is greater then b so, c = {c}")