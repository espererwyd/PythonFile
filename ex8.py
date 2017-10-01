formatter = "{} {} {} {}"
# created a formatter function to turn variable into strings

print(formatter.format(1, 2, 3, 4))
# pass to format four arguments, which match up with the four {} in the formatter variable.
# This is like passing arguments to the command line command format.
# Calling format on formatter is a new string that has the {} replaced with four variables.

print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your", "Own text here", "Maybe a poem", "Or a song about fear"))
# Do not forget to check the parentheses.
