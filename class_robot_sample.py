# coding = UTF-8

class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Initializing {self.name}")
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1

    def say_hi(self):
        print(f"Greetings, my master call me {self.name}.")

    @classmethod
    def how_many(cls):
        print(f"We have {cls.population} robots")


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.die()
Robot.how_many()
