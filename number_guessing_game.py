import random

#r = random.randrange(-1, 10) # prints a random number with range parameters (exclusive of last number)
                                # (last number alone is the stop)
# print(r)

top_of_range = input("Type a number: ")

# we need to validate the input.
# because it will be entered as a string, it has to be cast as a string.
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:

else:
    print("Need an actual number, my friend.")

s = random.randint(11) # the same as above, but this time it goes to 11 : )

