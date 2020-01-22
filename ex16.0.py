# importeert argv vanuit de package sys
from sys import argv
# geeft argv twee variabelen die aangenomen moeten worden
# standaard eerst de script naam
# daarna, voor deze script, de filename
script, filename = argv
# print een simpele string met een de uitdrukking van waarde van de var
print(f"We're going to erase {filename}.")
# geeft aan dat de script gestopt kan worden met CNTRL-C
print("If you don't want that hit CNTRL-C (^C).")
# geeft aan dat een ENTER / RETURN genoeg input is om de script verder te laten
# werken
print("If you do want that, hit RETURN.")
# vraagt om input, hier slaat hij niks op, maar een soort stop voor de gebruiker
# voor besluit of het script verder gaat of niet
input("?")
# print een string zodat de gebruiker weet wat er gebeurd
print("Opening the file...")
# opent een file onder de var target, en zegt dat wij erin willen schrijven
# de write-functie, aangegeven door 'w', is een voorzorgsmaatregel om ervoor
# te zorgen dat de programmeur weet in welke modus het bestand geopend wordt
# anders kan men per ongeluk de inhoud van het bestand wissen met de truncate()
# functie
# zoals ik bij het testen ook al opmerkte, werkt de .truncate()-functie niet
# wanneer het bestand niet in de write-mode geopend is
target = open(filename, 'w')
# print een string die verteld dat de file leeggemaakt wordt
print("Truncating the file. Goodbye!")
# de .truncate()-functie maakt de file object binnen de var target leeg
# bij het openen van een file in de write-mode wordt er automatisch
# getruncate, dus de onderstaande lijn is niet echt nodig
target.truncate()
# print een prompt die verteld wat er gaat gebeuren
print("Now I'm going to ask you for three lines.")
# drie variabelen voor waardes van de gebruiker
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# print een string die verteld wat er gaat gebeuren
print("I'm going to write these to the file.")
# de .write() functie schrijft lijnen in de het bestand, die open staat onder
# de 'w'/schrijf mode (eerder aangegeven). Het bestand is geopend in de variabele
# target
# de linebreak is een format, een ignore sequence die werkt als string, dus
# staat ie hier tussen aanhalingstekens
target.write(f"{line1}\n{line2}\n{line3}\n")
# print wat er gaat gebeuren
print("And finally, we close it.")
# .close()-functie sluit het bestand/ file object in de var target
target.close()
