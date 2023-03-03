lang = input("What's the programming language you want to learn? \n 1.JavaScript \n2.Python \n3.PHP \n4.Solidity \n5.Java \n6._ (press uderscore if you have no choice) \n ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")

    case "Python":
        print("You can become a Data Scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a Blockchain developer")

    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")