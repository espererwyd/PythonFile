# import argv module from system
from sys import argv

# request two initial inputs: the script and the file that you want to open
script, filename = argv

# open the file by recognizing the second input above
# the returning value of the command is the file object, which include the contents, properties such as creation time, user, etc.
txt = open(filename)

print(f"Here's your file {filename}:")
# print out the text, other commands include write, add, etc.
print(txt.read())

print("Type the filename again:")
# request file name input and store it in a variable
file_again = input("> ")

# store the text by opening the specific file
txt_again = open(file_again)

# print out the contents of file by reading it
print(txt_again.read())

# close both files
txt.close()
txt_again.close()
