


# de inventory heeft plaats voor 2 items, dus een lijst met maximaal
# twee waarden
# oppakken van items en in de inventory stoppen
# de items moeten in de lijst terecht komen, in de lijst zijn variabelen
# die bijhouden wat het is







print("You find 10 handgun bullets.")
print(f"Right now you have {handgun_ammo} handgun ammo.")

action = input("> ")



# als ik wil herladen, dan moet de handgun_ammo buiten de functions
# aangevuld worden, dus ik moet die variabele gebruiken




print(inventory)
print("handgun ammo:", handgun_ammo)
print("reload?")

add_ammo = input()

if "y" in add_ammo:
    handgun_ammo = reload(inventory, handgun_ammo)
else:
    print("no reload")

print(inventory)
print("handgun ammo:", handgun_ammo)
