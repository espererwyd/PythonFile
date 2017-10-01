print("Mary had a little lamb.")
# It's a pretty straightforward print syntax.

print("Its fleece was as white as {}.".format('snow'))
# as there is no format before the string, we should use .format() syntax
# or we can write:
# adjective = "snow"
# sentence = "Its fleece was as white as {}"
# print(sentence.format(adjective))
# or maybe in a more straightforward way:
# print(f."Its fleece was as white as {adjective}")
# so we can try it below:

adjective = 'snow'
sentence = "Its fleece was as white as {}."
print(sentence.format(adjective))
print(f"Its fleece was as white as {adjective}.")

print("And everywhere that Mary went.")
# Again, it's a pretty straightforward print command.

print("." * 10) # What'd that do?
# the purpose of *10 is simply print . 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# define each variable by a single leter

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# error made: f"string", not f."string"
