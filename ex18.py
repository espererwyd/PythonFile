# this one is like your scripts with argv
# First we tell python we want to make a function using def for "define".
# the define command end with a colon ":"
def print_two(*args):
# * tells python to take all the arguments to the function and put them in args as a list
# unpack the arguments
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one arguments
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Function checklist:
# 1. start the function definition with def.
# 2. function name should only contain characters and underscore characters "_"
# 3. put an open parenthesis right after the function name.
# 4. put arguments after the parenthesis and seperate by commas
# 5. each argument should be unique without duplicated names
# 6. put a close parenthesis and a colon after the arguments
# 7. indent all lines of code that you want in a function by four spaces
# 8. end the function by going back to write with no indent

# Run function checklist:
# 1. call funtion by typing its name
# 2. type parenthesis after the function to run it
# 3. put the values that you want into the parenthesis seperated by commas
# 4. end calling the function with a parenthesis
