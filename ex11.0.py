# print een string, en verteld dat de print eindigt met een leeg karakter
# door na de string ,end = ' ' te gebruiken
# dit zorgt ervoor dat de printlijn niet eindigt en begint bij de volgende
# lijn, hier print hij gewoon een normale vraag
print("How old are you?", end=' ')
# waarop de zogenaamde input op de vraag bij de onderstaande functie
# door de gebruiker aan de andere kant van de software ingevuld kan worden
# door middel van de input()-functie
# de input functie heeft een waarde, en wordt daarom aan een variabele gehecht
age = input()
# hetzelfde principe als de eerste printlijn, een string voor de visuele output
# die de gebruiker aan de andere kant vraagt om input
# de ,end = ' ' zorgt ervoor dat de lijn niet begint op de volgende regel
print("How tall are you?", end=' ')
# een variabele die ingevuld kan worden door de gebruiker aan de andere kant
# door zijn INPUT
height = input()
# hetzelfde als hierboven, print een string, zorg ervoor dat de lijn niet eindigt
print("How much do you weigh?", end=' ')
# variabele die ingevuld wordt door de input van de gebruiker
weight = input()
# een simpele print met f-functie, die de waardes van de voorgaande variabelen
# print
print(f"So you're {age} old, {height} tall and {weight} heavy.")
# een andere manier om de input()-functie te gebruiken is door de
# stimuli/verzoek voor input, in de haakjes te zetten, zoals hieronder is
# weergegeven
# anders dan de eerste paar lijnen, hoeft er nu geen aparte lijn geprint te worden
# die vraagt om input, deze is namelijk al ingebouwd in de functie
name = input ("What's your name? ")
# de print functie hier gebruikt meerdere aanhalingstekens, maar dit kan ook anders
# en ik denk dat ik de functie van Zed handiger vind
print("Nice to meet you " + name + "!")
# ik print het hieronder nog eens, maar dan met de methode die ik handiger vind
# het is wat overzichtelijker
print(f"Nice to meet you {name}!")
# hieronder is dan mijn eigen verzonnen lijn
# hij lijkt heel erg op de tweede lijn die ik gebruikte
vraag = input ("Wat vind je van je MacBook? ")
# hier print ik eerst de input, en daarna met een linebreak een reactie erop
print(vraag, "\nDat vind ik fijn om te horen!")
