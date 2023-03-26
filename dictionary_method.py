ant = {
    1 : 10,
    2 : 20,
    3 : 30,
    "Name" : "Nahid"
}

bee = {
    4 : 40,
    5 : 50,
    6 : 60
}
print(ant)
ant.update(bee)   # update ant dictionary with bee dictionary
print(ant)
ant.pop(1)  # pop selected key from ant dictionary using pop()
print(ant)
ant.popitem()  # pop the last item from the dictionary using popitem()
print(ant)
# del bee  # use for deleting any dictionary
del ant["Name"]   # use for delete any specific value from dictionary
print(ant)