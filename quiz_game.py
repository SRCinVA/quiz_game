print("Welcome to my computer quiz!")

playing = input("Do you want to play? ") # he drops it into a variable
score = 0

if playing.lower() != "yes": # .lower() converts everything to lower regardless of original case. The input still has to be y,e, and s.
    quit() # quit() is a built-in method

print("OK! Then let's play.")

# Question 1
answer1 = input("What does CPU stand for? ") # *could* have done .lower() up here instead
if answer1.lower() == "central processing unit": 
    print("Nice job!")
    score += 1
else:
    print("Incorrect!")

# Question 2
# Best practice is to not re-use variables, but in this case, you could do that.
answer2 = input("What does GPU stand for? ")
if answer2.lower() == "graphics processing unit":
    print("Nice job!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer3 = input("what does RAM stand for? ")
if answer3.lower() == "random access memory":
    print("Nice job!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer4 = input("What does PSU stand for? ")
if answer4.lower() == "power supply":
    print("Nice job!")
    score += 1
else:
    print("Incorrect!")

if score == 1:
    print("You made " + str(score) + " point. Not too bad.")
else:
    print("You made " + str(score) + " points. Not too bad.") 