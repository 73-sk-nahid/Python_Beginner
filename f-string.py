# here we will know about format string vs normal string printing
sentence = 'Hi your name is {}. You are from {}.'
name = input("Enter name: ")
country = input("Enter country: ")
print(sentence.format(name, country))

# now we will know how all these part can be done by formatting method

print(f"Hi your name is {name}. You are from {country}.")  # printing using format method (f" ")

# using this we can print any types of variables like float
price = 999.9999
print(f"Price of the earphone is {price:.2f} taka.")