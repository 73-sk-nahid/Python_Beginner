# creating dictionary with duplicate key-value pairs (ID)
my_dict = {"Name": "Sk. Nahid",
           "ID": "201902073",
           "user_id": "201902073",
           "Email": "nahidsheikh2001@gmail.com",
           "Batch": "201"}
print("Viewing previous dictionary--", my_dict)  # displaying my_dict the old one
new_dict = {}  # Create an empty dictionary to store unique key-value pairs
for key, value in my_dict.items():
    if value not in new_dict.values():  # Check if the current value already exists in the new dictionary
        new_dict[key] = value  # If not, add the key-value pair to the new dictionary
print("\n \nViewing new dictionary--", new_dict)  # displaying new-dict the new one with no duplicate value
for x in new_dict:
    print(new_dict[x])
