# print een soort van prompt
print("Type in the filename: ")
# variabele voor gebruiker input
file_name = input('> ')
# variabele met open() functie op de variabele met bestandsnaam, opent een
# bestand binnen de variabele
txt = open(file_name)
# print de uitkomst van de .read()-functie op de txt variabele
print(txt.read())
# sluit het bestand binnen de txt variabele
txt = close(file_name)
