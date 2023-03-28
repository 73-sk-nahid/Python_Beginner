try:
    a = [2, 0, 1, 9, 0, 2, 0, 7, 3]
    i = int(input("Enter the index (1-9): "))
    print(a[i])
except:
    print("Some error here or maybe index number error")
finally:   # here finally will execute every time
    print("Wow! I am always executable")

# another example below with commentline
"""try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")"""