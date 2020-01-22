# hier is de functie vervangen door een for loop, die de range() functie gebruikt
# opvallend is dat de script veel korter is
# dit komt omdat de increment functie al in de range () functie zit
def loop (i, o, x, numbers):
    for num in range(i, o, x):
        numbers.append(num)


numbers = []

loop(0, 11, 2, numbers)

for num in numbers:
    print(num)
