questions = ["What is the capital of Bangladesh?",
             "Who is present Prime Minister?",
             "Who is the father of nation?",
             "When Bangladesh won their victory"]
options = ["a) Khulna \n b) Barishal \n c) Dhaka \n d) Sylhet",
           "a) Sheikh Hasina \n b) Begun Khaleda Zia \n c) Sheikh Mujibur Rahman \n d) Rowson Ara Ersad",
           "a) Ziaur Rahman \n b) Hussain Muhammad Ershad \n c) Sheikh Mujibur Rahman \n d) Dr. Anisur Rahman",
           "a) 26 March, 1971 \n b) 14 December, 1971 \n c) 16 December, 1971 \n d) 21 February, 1971"]
s = 0
name = input("Enter your name: ")
script = name + " please enter the answer(a/b/c/d):"
print("-------Ok!", name, "Let's play-------")
prizemoney = [1000, 1500, 2000, 2500]
print(questions[0])
print(options[0])
answer1 = input(script)
if (answer1.lower() == "c"):
    print("Congratulation!", name, "You won", prizemoney[0],  "tk")
    s = s + prizemoney[0]
else:
    print("Sorry! Wrong answer. Still you have 3 questions")
print(questions[1])
print(options[1])
answer2 = input(script)
if (answer2.lower() == "a"):
    print("Congratulation!", name, " You won", prizemoney[1],  "tk")
    s = s + prizemoney[1]
else:
    print("Sorry! Wrong answer. Still you have 2 questions")
print(questions[2])
print(options[2])
answer3 = input(script)
if (answer3.lower() == "c"):
    print("Congratulation!", name, " You won", prizemoney[2],  "tk")
    s = s + prizemoney[2]
else:
    print("Sorry! Wrong answer. Still you have 1 questions")
print(questions[3])
print(options[3])
answer4 = input(script)
if (answer4.lower() == "c"):
    print("Congratulation!", name, " You won", prizemoney[3],  "tk")
    s = s + prizemoney[3]
else:
    print("Sorry!", name, " Wrong answer. Game end")
total = sum(prizemoney)
print("Congratulations!", name, " Finally you won total of", s, "Tk out of", total, "tk")