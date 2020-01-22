# deze Parent class is-a object en is een block of code
# Parent has-many methods, override, implicit en altered
# elk van deze methods zijn attributen van een standaard object
# omdat dit een parent class is, zijn de methods tevens de 'eerste versie'
class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

# de class Child is-a Parent en erft dus eigenschappen van de Parent class
# Child erft dus methods override(), implicit(), en altered()
# override() wordt herschreven omdat de Child class dezelfde naam gebruikt
# en wanneer deze gecalled wordt in het object, dan zal het de override()
# van de Child gebruiken
# implicit() wordt geerfd, en wordt in de Child class niks mee gedaan,
# en daarmee bedoel ik dat het niet herschreven wordt
# dat betekent dat wanneer implicit() gecalld wordt op Child, of op een
# instance ervan, dat het in feite de Parent method runt
# altered() is hier de interessantse method
# altered() is herschreven in de Child class, en runt de eerste print lijn
# van de Child class
# daarna komt er een super line, en wat dat betekent is:
# call super, en call de altered() method ervan
# achter super staat nog tussen haakjes de de class waarvan de super gecalld
# moet worden, in dit geval Child --> call de super(dus de parent class) Child
# en run de altered() method ervan
# deze lijn print de altered() print lijn van de parent class
# en vervolgens print hij terug de lijn die in de altered() van de Child class
# staat
# de override() van child is een override
# implicit() is geen override, wel geerft
# altered() is een override
# maar binnen altered() van Child is er nog een zogenaamde Alter before or after?
# dit is gewoon een call naar een voorgaande functie die herschreven is, maar
# het werkt wel nog steeds omdat het in de code staat
# de script gaat dan even een class terug voor die ene functie
# maar komt terug naar de code van de Child class
# het is geen override 
class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
