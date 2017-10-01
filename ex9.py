# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# This is just plain string.

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# to start the month in a new line, type simply /nJan/nFeb/nMar/nApr ...
# \n allows printing the string after \n in a new line.

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# Three double quotes enable to write strings in multiple lines.

# To sum it up, to make a string that goes across multiple lines:
# We can use ("""abcdefg...uvwzyx""") to print a long string in multiple lines
# or seperate short strings by insert \n before the strings

# test escape sequence:
print("I am 6'2\" tall.")
print('I am 6\'2" tall.')
# escape double-quote or single-quote by adding \ before
