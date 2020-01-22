# this one is like your scripts with argv
# def geeft aan dat de functie begint, met de naam ervan erachter
# de functie hieronder heeft tussen de haakjes ()
# een argument dat meerdere waardes kan bevatten
# hier zijn dat er twee
# vervolgens print het de twee waarden
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
# hetzelfde als hierboven, maar hieronder zijn de twee argumenten al
# in de functie zelf geplaatst, in plaats van dat ze namen van de waardes
# nog in een extra lijn worden aangegeven (en het aantal)
# binnen de function is er nog een print-functie die de waardes uitprint
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
# hetzelfde als hierboven, maar dit keer maar een argument
# de script is telkens hetzelfde, hier print hij ook weer het argument in
# een string
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
# deze functie heeft geen argumenten, maar bevat wel nog een print-functie lijn
def print_none():
    print("I got nothing'.")
# door de naam van de function te typen, met tussen haakjes de arguments
# als strings mee te geven, roept de script de function aan en runt deze
# hieronder worden de vier functions gecalled
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
