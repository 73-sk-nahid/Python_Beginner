# here we will see an example of extending a list
list1 = [1, 2, 3, 4, 5]  # here a list1 of 1 to 5
list2 = [6, 7, 8, 9, 10]   # here a list2 of 6 to 10
print("List 1 is: ", list1)   # checking list1
print("List 2 is: ", list2)   # checking list2
# now we will extend list1 with list2
list1.extend(list2)
print("Extended list1 is: ", list1)     # checking extended list1
