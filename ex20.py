# importeert module argv van de sys package
from sys import argv
# argv unpacked twee argumenten
script, input_file = argv
# function print_all met een argument
# functie print de tekst uit het bestand(argument)
def print_all(f):
    print(f.read())
# function rewind met een argument voor bestand
# gaat naar het begin van het bestand (doorgegeven via argument)
def rewind(f):
    f.seek(0)
# function print_a_line met twee argumenten
# print een waarde, en runt de .readline() functie, deze print gewoon de lijn
# die de functie tegenkomt in de tekst, en daarna eindigt hij met een \n
def print_a_line(line_count, f):
    print(line_count, f.readline())
# variabele waaronder een file object wordt geopend
current_file = open(input_file)
# print een string
print("First let's print the whole file:\n")
# callt de print_all function, met meegegeven de file object, zodat binnen de
# print_all function de .read() functie daarop kan werken
print_all(current_file)
# print een string
print("Now let's rewind, kind of like a tape.")
# callt de rewind function, meegegeven een file object, zodat er binnen de
# gecallde function .seek(0) werkt
rewind(current_file)
# print een string
print("Let's print three lines:")
# variabele met waarde 1
current_line = 1
# callt de print_a_line function
# geeft waarde 1 en de file object door
# hier is de current_line gelijk aan 1
print_a_line(current_line, current_file)
# verandert de variabele in het vorige cijfer + 1
current_line += 1
# callt weer de print_a_line function
# hier is de current_line gelijk aan 2
print_a_line(current_line, current_file)
# verandert de current_line in een + 1 cijfer
current_line += 1
# callt de print_a_line function weer eens
# hier is de current_line waarde gelijk aan 3
# wanneer de script een function callt, geeft het de laatste waardes van de
# variabelen door, let goed op hoe ze veranderen zoals in dit voorbeeld
print_a_line(current_line, current_file)
