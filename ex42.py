## Animal is-a object
class Animal(object):
    print("I've created a class named Animal.")

# Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name
        print(name)

# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # 通过调用super实现父类实例的初始化函数，从而实现父类的功能
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

#Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# halibut is-a Fish
class Halibut(Fish):
    pass


# Rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# mary is- a Person
mary = Person("Mary")

# mary has-a Pet Satan
mary.pet = satan

# Employee has-a frank whose salary is 120000
frank = Employee("Frank", 120000)

# frank has-a pet Rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
