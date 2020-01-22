# geeft aan dat het aantal auto's 100 is.
cars = 100
# geeft aan hoeveel plaats er in een auto is.
space_in_a_car = 4
# geeft de variabele 'drivers' een cijfer
drivers = 30
# geeft aan in een variabele hoeveel passagiers er zijn.
passengers = 90
# deze variabele bestaat uit een combinatie (in een aftreksom) hoeveel auto's er
# niet in gebruik zijn
cars_not_driven = cars - drivers
# het aantal auto's is hetzelfde als het aantal chauffeurs
cars_driven = drivers
# deze variabele bestaat uit een multiplicatie van voorheen aangeduidde variabeles
carpool_capacity = cars_driven * space_in_a_car
# hetzelfde als de vorige, maar dan een deelsom
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# De NameError geeft aan dat een variabele niet aangeduid is (wanneer men de
# variabele wel probeert te gebruiken.)
# een voorbeeld is bijvoorbeeld:
# getal1 = 1
# print(getal1 * getal2) <-- python zal een error aangeven, omdat de variabele
# 'getal2' geen waard heeft; niet is aangeduid.
