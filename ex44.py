# Implicit inheritance
class Parent(object):

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Explicit override
class Parent(object):

    def parent_print(self):
        print("Parent override()")

class Child(Parent):

    #对parent_print()进行了重新定义，达到override作用
    def parent_print(self):
        pass

dad = Parent()
son = Child()

dad.parent_print()
son.parent_print()

# Alter before or after
class Parent(object):

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# all three combined
class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.override()
dad.implicit()
dad.altered()

son.override()
son.implicit()
son.altered()

# using super() with __init__

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        # complete the initialization in the Parent
        super(Child, self).__init__()

# composition
class Other(object):

    def implicit(self):
        print("OTHER implicit()")

    def override(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER altered()")

# no inheritance here, Child and Other are two different classes
class Child(object):

    def __init__(self):
        self.composition = Other()

    def implicit(self):
        # equals to calling Other.implicit()
        self.composition.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.composition.altered()
        print("CHILD, AFTER OTHER altered()")

other = Other()
child = Child()

other.implicit()
child.implicit()

other.override()
child.override()

other.altered()
child.altered()
