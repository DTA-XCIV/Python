fruit = ["Banaan", "Appel", "Sinaasappel", "Kiwi", "Druif"]

print(f"In de fruitmand zit: {fruit}")
print("Waar heb je zin in?")

while len(fruit) >= 0:
    nemen = input('> ')

    if "banaan" in nemen:
        b = fruit.index("Banaan")
        fruit.pop(b)
        print("Je eet de banaan.")
    elif "appel" in nemen:
        a = fruit.index("Appel")
        fruit.pop(a)
        print("Je eet de appel.")
    elif "sinaas" in nemen:
        s = fruit.index("Sinaasappel")
        fruit.pop(s)
        print("Je eet de sinaasappel.")
    elif "kiwi" in nemen:
        k = fruit.index("Kiwi")
        fruit.pop(k)
        print("Je eet de kiwi.")
    elif "druif" in nemen:
        d = fruit.index("Druif")
        fruit.pop(d)
        print("Je eet de kiwi.")
    else:
        print("De fruitmand is leeg!")
