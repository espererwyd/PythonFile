print("How old are you?", end=' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weight?", end = ' ')
weight = input()
# We put a end = " " at the end of eacch print line.
# This tells print to not end the line with a newline character and go to the next line.

print(f"So, you are {age} old, {height} tall and {weight} heavy")

print("What is your name?", end = ' ')
my_name = input()
sentence = "Thus your name is {}."
print(sentence.format(my_name))
