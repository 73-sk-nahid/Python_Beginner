#using continue we can skip any particular part using condition
#here an example for skipping the odd values
for i in [1,2,3,4,5,6,7,8,9]:
    if( i % 2 != 0):
        continue
    print(i)