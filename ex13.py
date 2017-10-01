from sys import argv
# read the WYSS section for how to run this
# Import is how we add "features" (modules) into our script from the python system feature set.
# as there is a whole bunch of features.

# argv is the argument variable.
# the variable holds the argument you pass to python script when running it.


script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("Who are the three most important people in your life? Tell me:")

person_one = input()
person_two = input()
person_three = input()

print("So they are:", person_one, person_two, person_three)
