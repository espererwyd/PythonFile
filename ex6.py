types_of_people = 10
# define number of types

x = f"There are {types_of_people} types of people."
# format strings with a variable types_of_people inside

binary = "binary"
# define binary

do_not = "don't"
# define do_not

y = f"Those who know {binary} and those who {do_not}."
# format a string with two variables inside.

print(x)
print(y)
# Just print it!

print(f"I said: {x}")
# format string with variable x

print(f"I also said: '{y}'")
# format string with variable y

hilarious = False
# define hilarious

joke_evaluation = "Isn't that joke so funny?! {}"
# define joke_evaluation as a string with an undefined variable

print(joke_evaluation.format(hilarious))
# format the undefined variable with command format().

w = "This is the left side of..."
e = "a string with a right side."
# two variables of strings

print(w + e)
# print the combination of strings

# Four strings with strings inside:
# Line 13
# Line 20
# Line 23
# Line 32
