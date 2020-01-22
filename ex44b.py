class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# anders dan de bij ex44a, waarbij de Child class geen block had, heeft het
# dat hier wel
# de method naam hier is hetzelfde als bij de Parent class, waardoor
# de override() functie, wanneer gecalld de geerfde override, override
# letterlijk eroverheen schrijven
# dit werkt enkel wanneer de namen van de methods hetzelfde zijn
# dit is handig wanneer je sommige attributen wilt gebruiken van de parent
# maar anderen wilt aanpassen 
