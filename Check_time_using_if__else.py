import time

current_time = time.strftime("%H:%M:%S")
print("The current time is", current_time)

hour = int(time.strftime("%H"))
#print("The current time is", hour)

#minute = int(time.strftime("%M"))
#print("The current time is", minute)

#second = int(time.strftime("%S"))
#print("The current time is", second)

if(hour>=6 and hour<12):
    print("Good Morning")
elif(hour == 12):
        print("Good Noon")
elif(hour>12 and hour<17):
        print("Good Afternoon")
elif(hour>=17 and hour<20):
        print("Good Evening")
else:
    print("Good Night")