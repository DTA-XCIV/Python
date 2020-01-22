# enkele variabelen met integers als waarde
people = 30
cars = 40
trucks = 15

# deze blok vergelijkt in totaal 2 variabelen: cars en people
# de if-functie komt als eerste en kijkt of er meer auto's zijn dan mensen
# de waarde is True, dus print de script de lijn die onder de if staat
# mocht het zijn dat de waarde not true was, dan zou Python de elif testen
# en zien of er minder cars zijn dan mensen, als DIE waarde true zou zijn
# dan print Python de lijn die daar onderstaan
# mochten beide waardes False geven, in deze situatie enkel mogelijk wanneer
# het aantal auto's gelijk is aan het aantal mensen
# dan gaat Python naar de else-functie, die standaard werkt wanneer de if en
# elif allebei False zijn
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
# de principes van deze blok zijn hetzelfde als die van erboven
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide.")
# deze blok heeft geen elif, dus test het enkel de if, en anders is het de
# else
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's just stay home then.")
