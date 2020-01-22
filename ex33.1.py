# variabelen die gebruikt zullen worden in de loop
i = 0
numbers = []
# de while loop, lijkt een beetje op de for-loop, maar er is meer vrijheid
# en is in het algemeen moeilijker om te schrijven dan een for loop
# hier is de waarde voor de while-loop i < 6, wat betekent, dat de lijnen
# onder while blijven runnen, opnieuw en opnieuw, totdat i 6 bereikt
# om een grens op te stellen heeft de loop in het midden een
# lijn voor increment --> i = i + 1
# de while loop is geen function, dus een variabele van 'buitenaf' kan aangepast
# worden
# hier wordt er telkens een cijfer toegevoegd, zodat i uiteindelijk een hoog
# genoeg waarde haalt zodat de loop stopt
# er staan tevens ook nog print lijnen in om te laten zien wat de waarde van i
# telkens is
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

# een for loop, print voor elke waarde in de var numbers die een lijst bevat,
# de waarde van de lijst
for num in numbers:
    print(num)
