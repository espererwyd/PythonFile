# do not run the script
# this is only a review of the previous chapters.

print("This is plain text.")
print(f"This is text and {variable}.")
print(3 + 5 / 10 * 2)
print(current_file.exists())

variable_strings_combined = "This is another format {}."
print(variable_strings_combined.format(Yes))

formatter = "{} {} {} {}"
one_two_three_four = formatter.format(one, two, three, four)
print(one_two_three_four)

days = "Mon Tue Wed Thu Fri Sat Sun"

# \n = linefeed
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug\nsep\noct\nnov\ndec"

# \t = tabbed
print("""
Here are some food:
\t *Fish
\t *Meat
\t *Rice
\t *Vegetable
""")


# backslash, single-quote, double-quote
print("I'am \\ a \\ fat \\ cat.")
print('I\'m six feet tall.')
print("Tom said:\"Ok, I'll be  there.\"")


# request user's input
print("Saisir votre nom, s'il vous plait.", end = ' ')
input_stored_here = input()
# or
input_stored_here = input("Saisir votre nom, s'il vous plait.")

# import module from system
from sys import argv
arg1, arg2, arg3 = argv

# print text from a specific file, default read only mode.
file_object = open(current_file)
print(file_object.read())
# or
open(current_file).read()

# open file in other modes
target_file = open(current_file, 'w')
# remove contents
target_file.truncate()
# add text to file
add_text = "This is the text that I want to add to the file."
target_file.write(add_text)
# close opened file
target_file.close()

# exists function returns boolean TRUE or FALSE
from sys import exists

def new_function(a, b, c, d):
    x = a + b
    y = a - b
    z = a * b
    d = a / b
    return (x + y) * z - d

def read_a_line(f):
    print(f.readline())

read_a_line(open(input_file))
