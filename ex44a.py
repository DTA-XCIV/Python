# class Parent is-a object and has-a implicit method that prints a string
# class Child is-a Parent, thus inherits from object Parent
# set dad to an instance of Parent
# set son to an instance of Child
# call the method implicit on object dad
# call the method implicit on object son
# de implicit call op object dad is logisch, omdat er gemakkelijk gezien kan
# worden dat de Parent class een implicit method bevat
# de tweede call van implicit op son is iets gedetailleerder
# als de programmeur goed op let ziet hij dat Child de attributes, en dus
# ook de methods van Parent inherit, letterlijk erft
# dat betekent dat de Child, letterlijk dus een afstammeling van Parent
# de implicit method bevat die gecalld kan worden 

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
