people = 60
cars = 15
trucks = 40

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide.")



if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")



if people > trucks:
    print("All right, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# What happens if multiple elif blocks are true?
# Python starts at the top and runs the first block that is true, so it will run only the first one.
