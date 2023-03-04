mydictionary = { "Name": "Sk. Nahid", "ID": "201902073", "Batch": 201,
                 "Section": "B", "Course Name" : "Artificial "
                                 "intelligence"}
#here name is key & Sk. Nahid is the value (key : value)
print(mydictionary) #print full dictionary
print(mydictionary["Course Name"]) #print specific value
mydictionary["Course Name"] = "Artificial Intelligence Lab" #changing the value of specific key
print(mydictionary["Course Name"]) #checking that is the value changed or not
mydictionary["Uploaded by"] = "Nahid Sheikh"  #adding new value
print(mydictionary["Uploaded by"]) #check the value added or not