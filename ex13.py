# import de module (denk 'features', ook wel libraries genoemd) vanuit sys
from sys import argv
# read the WYSS section for how to run this
# geeft de argument variabele(n) namen
# de eerste, script, is altijd de script naam, omdat vanuit de terminal de file
# eerst wordt ingetypt
# first, second, third, (en evt. meer of minder) zijn de variabelennamen
# wanneer men de script start, verwacht de argv module dat er vijf waardes worden
# meegegeven, hier is dat dus de scriptnaam, en nog vier andere waardes
script, first, second, third, fourth = argv
# print een string, en daarna de eerste variabele uit de argv, de scriptnaam
print("The script is called:", script)
# print een string, daarna de tweede variabele, hier heet het first, die werd
# meegegeven bij het starten van de programma
# als de script integers wil gebruiken
# kan de meegegeven string, omgezet worden tijdens het printen naar een integer
# met de int() functie
# op die manier verwacht de script zelfs een cijfer, omdat hij geen letters om
# kan zetten naar integers, zie beneden:
print("Your first variable is:", int(first))
# derde variabele uit de argv
print("Your second variable is:", second)
# vierde variabele uit de argv
print("Your third variable is:", third)
# print de vierde waarde uit de argv
print("Your fourth variable is:", fourth)
# hier komt een nieuwe variabele, de vijfde, die in het begin niet is meegegeven
# of 'aangeduid' in de argv zelf
# de vijfde variabele verwacht een input van de gebruiker
# de prompt "What's the fifth variable? " vraagt hiernaar
fifth = input("What's the fifth variable? ")
# daarna print de script, na de string, de vijfde waarde uit de variabele
# die het programma NA het opstarten, NA de gebruikerinput pas opslaat
print("Your fifth variable is:", fifth)
# de meegegeven variabelen kunnen verandert worden, door simpelweg de vierde
# var weer aan te halen en de gebruiker te vragen voor een nieuwe input
fourth = input("Wil je de vierde variabele veranderen? ")
# print na de string de nieuwe waarde van de var
print("De vierde variabele is nu: ", fourth)
# de lijn hier beneden heeft een simpele prompt, als de gebruiker iets van input
# geeft, verandert de vijfde variabele in de inputwaarde
fifth = input('? ')
