# Escape sequence
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# \n stands for ASCII linefeed.

backslash_cat = "I'm \\ a \\ cat."
# \\ symbolieses backslash.

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* catnip\n\t* Grass
"""
# \t symbolises horizontal tab (TAB)

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# test a few escape sequence below:
backslash = "\\ backslash"
single_quote = "\' single-quote"
double_quote = "\" double-quote"
ASCII_bell = "\a ASCII bell"
ASCII_backspace = "\b ASCII backspace"
ASCII_formfeed = "\f ASCII Formfeed"
ASCII_linefeed = "\n ASCII Linefeed"
Carriage_return = "\r Carriage return"
Horizontal_return = "\t Horizontal return"
ASCII_vertical_tab = "\v ASCII vertical tab"

print(backslash)
print(single_quote)
print(double_quote)
print(ASCII_bell)
print(ASCII_backspace)
print(ASCII_formfeed)
print(ASCII_linefeed)
print(Carriage_return)
print(Horizontal_return)
print(ASCII_vertical_tab)
print('''
How will it appear
If I change double-quotes
into single-quotes?
''')
# as far as it appears,
# three single-quotes serve as the same thing as three double-quotes.
# Am I right?

answer = """
\b\"I do not have any apple, but I have other stuff.\"
\t* Pineaplle\n\t* Banana\n\t* Pear\n\t* Orange\n\t* Tomato\r
\"So do you want any of these?\"
"""

print('Mc\'Donalds asked: "How many apples do you have?"')
print(f"Irvin answerd: {answer}")
print("What a sad story!")
