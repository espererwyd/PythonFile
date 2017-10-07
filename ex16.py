from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
# keyboardInterrupt
# terminate the script
print("If you don't want this, hit CTRL-C (^C).")
print("If you do want this, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("Now I'm going to write this to the file.")

target.write(f"{line1} \n{line2} \n{line3}")
# original code below
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

# Study Drills
print("Which file do you want me to read?")
file_read = input("> ")
target2 = open(file_read, "r")
print(target2.read())

print("Ok, you got want you want.")
print("I'm closing it, hit RETURN to confirm.")
input("?")

target2.close()
