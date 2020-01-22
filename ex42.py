## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    def __init(self, size):
        self.size = None

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name attribute
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name attribute
        self.name = name

## Person is-a Object
class Person(object):

    def __init__(self, name):
        ## Person has-a name attribute
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a super attribute?
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is-a Object
class Fish(object):
    def __init__(self, color):
        self.color = color

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary's pet is-a Satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank's pet is-a rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish("White")

## crouse is-a Salmon
crouse = Salmon("White")

## harry is-a Halibut
harry = Halibut("Iksnaphet")

class Book(object):

    def __init__(self, cover):
        self.cover = cover

class Popscience(Book):

    def __init__(self, cover, chapters):
        self.chapters = chapters
        super(Popscience, self).__init__(cover)

class Stories(Book):

    def __init__(self, chapters):
        self.chapters = chapters

si_chapters = ([1, 2, 3])

social_intelligence = Popscience("soft cover", si_chapters)

print(social_intelligence.cover)

#print(social_intelligence.chapters)

ms_chapters = ({'1': 'inleiding',
                '2': 'middenstuk',
                '3': 'slot'})

misdaad_en_straf = Stories(ms_chapters)

#print(misdaad_en_straf.chapters)
