mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

mystuff['apple'] # get apple from dict

# Original module code:
def apple():
    print("I AM THE APPLES!")

# this is just a variable
import mystuff
# mystuff.apple() # get apple from module >mystuff.py
mystuff.apple()
# mystuff.tangerine # same thing, it's just a variable
print(mystuff.tangerine)

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM A CLASSY APPLE!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I will stop right here"])

bulls_on_a_parade = Song(["They rally around the family",
                          "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_a_parade.sing_me_a_song()
