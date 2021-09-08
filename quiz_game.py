print("Welcome to my computer quiz!")

playing = input("Do you want to play? ") # he drops it into a variable

if playing != "yes":
    quit() # quit() is a built-in method

print("OK! Then let's play.")

answer = input("What does CPU stand for? ")

if answer == central processing unit:
    print("Nice job!")
