# importeert een module ('features', ookwel libraries van sys)
from sys import argv
# geeft aan dat argv twee variabelen moet openen/unpacken
# de eerste is altijd de scriptnaam
# de tweede hier is de naam van het tekst bestand dat we willen openen
script, filename = argv
# variabele met de functie open, hier opent hij de tekst file die we
# in de commandline hebben meegegeven
# een open file betekent dat hij dat gewoon is, geopend, op de achtergrond
# dat betekent dat er vervolgens dingen mee gedaan kunnen worden, zoals
# de script doet op de lijn die daarop volgt
# de functie opent het bestand niet echt, dus de inhoud is nog niet bekend
# maar creeert als het ware een framework rondom het bestand, wat een
# file object genoemd wordt
txt = open(filename)
# print hier een simpele string met variabele
print(f"Here's your file {filename}:")
# print de uitkomt van de functie .read op variabele txt
# txt voorheen bevat een geopende file
# en nu kunnen we daar een functie op laten werken, .read()
# de uitkomst van de functie printen de script
print(txt.read())
# sluit het bestand binnen de variabele
txt = close(filename)
