# here we will know about which one can be tuple and which one can't be tuple
tuple1 = ( 1 )  # here we use just one element in tuple(as wish) but is it actually a tuple?
# let's check
print("------Is tuple1 (", tuple1, ") tuple or not?")
print(type(tuple1))

print("=Yes this is not a tuple. It's consider it ", tuple1, " like a int")
tuple2 = (1,)   # is it consider as a tuple ? let's check
print("------Is tuple2 (", tuple2, ") tuple or not?")
print(type(tuple2))
print("=Yes this is a tuple", tuple2)
tuple3 = (1,2,3, "Sheikh", "Nahid")     # yes, tuple can contains multiple datatype
print(type(tuple3))
print("------Is tuple3 ", tuple3, " tuple or not?")
print("=Yes this is also a tuple", tuple3)