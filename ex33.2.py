# de while loop in een function
# hier zijn de waardes die de while loop begrenzen door te geven via
# de arguments van de function
# daarnaast staat er ook een clear() functie in om de lijst die wordt
# doorgegeven te wissen
# wanneer de while nog runt, voegt de append functie de cijfer toe als waarde
# aan de lijst numbers, en voegt het de increment toe die is doorgegeven
def loop(i, o, x, numbers):
    numbers.clear()
    while i < o:
        numbers.append(i)

        i += x


numbers = []

loop(0, 10, 2, numbers)

for num in numbers:
    print(num)

loop(3, 12, 4, numbers)

for num in numbers:
    print(num)
