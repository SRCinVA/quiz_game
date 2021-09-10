print("Welcome to my computer quiz!")

playing = input("Do you want to play? ") # he drops it into a variable

if playing != "yes":
    quit() # quit() is a built-in method

print("OK! Then let's play.")

# Question 1
answer1 = input("What does CPU stand for? ")
if answer1 == "central processing unit":
    print("Nice job!")
else:
    print("Incorrect!")

# Question 2
# Best practice is to not re-use variables, but in this case, you could do that.
answer2 = input("What does GPU stand for? ")
if answer2 == "graphics processing unit":
    print("Nice job!")
else:
    print("Incorrect!")

# Question 3
answer3 = input("what does RAM stand for? ")
if answer3 == "random access memory":
    print("Nice job!")
else:
    print("Incorrect!")

# Question 4
answer4 = input("What does PSU stand for? ")
if answer4 == "power supply":
    print("Nice job!")
else:
    print("Incorrect!")