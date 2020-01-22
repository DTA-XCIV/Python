# function met ruimte voor twee arguments
# deze print eerst een string; daarna telt hij waardes a en b bij elkaar op
# en returnt deze terug naar de variabele die hem callde
# return geeft ook een linebreak \n
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
# function substract met plaats voor twee arguments
# print eerste een lijn die aangeeft dat de twee waardes van elkaar worden
# afgetrokken, en returnt daarna de waarde van a - b naar de variabele
# die deze function callde
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
# een vermeningvuldig function, met ruimte voor twee waardes, hier cijfers
# print een string die verteld dat de twee waardes met elkaar vermenigvuldigt
# worden, en returnt daarna de waarde van de som naar de variabele die hem callde
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
# deel function, met ruimte voor twee waardes (cijfers)
# print een string die zegt wat de wiskundesom in de function doet
# returnt daarna met de return-functie de waarde van de som naar de variabele
# wat betekent dat de variabele, die tevens de function callde, een waarde
# terug krijgt van de function
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# print een string
print("Let's do some math with just function!")
# hier wordt in de eerste variabele age de optel function gecalld, de variabele
# geeft twee waardes mee: 30 en 5, en krijgt via de return in de function
# de waarde uit de optelsom terug, en age verandert direct van waarde
age = add(30, 5)
# hetzelfde gebeurt bij height, de function voor aftrekken wordt gecalld,
# waarbij de function twee arguments meekrijgt, hier 78 en 4, de function
# trekt deze van elkaar af en geeft het terug (return) aan de variabele
# de variabele neemt deze waarde over
height = subtract(78, 4)
# een variabele die de multiply-function callt en twee cijfers meegeeft voor
# de som in de function, de function returnt een waarde voor de variabele
weight = multiply(90, 2)
# callt een function en geeft twee waardes(arguments) mee, de function
# verwerkt deze en returnt een waarde voor de variabele
iq = divide(100, 2)
# print een string met de waardes van de variabelen met aangepaste waardes
# van de functions
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway
# print een string, let goed op de syntax
print("Here is a puzzle.")
# een variabele die de functions callt, maar dan binnen haakjes, dus een function
# hier kan een waarde zijn voor een andere function
# als ik kijk naar wat er geprint wordt, door de lijn later, zie ik dat de
# alhoewel python van links naar rechts lees, de meest genestelde function
# als eerste wordt gecallt, hier is dat divide
# de divide heeft al twee bekende waardes, iq (die al een waarde heeft door
# een voorgaande return) en twee
# de waarde op die plek heeft geen variabele om 'opgeslagen' te worden, maar
# wordt direct gebruikt als waarde voor de multiply function,
# die weer een bekende waarde uit een variabele neemt samen met de returnde waarde
# uit de divide function
# de multiply function returnt weer een waarde, die weer een waarde vormt,
# samen met de bekende waarde van height, voor de function subtract
# de subtract returnt weer een waarde, die samen met de var age uiteindelijk
# bij elkaar opgeteld worden door de function age, en uiteindelijk wordt
# de waarde van de var what de returnde waarde uit de add function
what2 = 35 + 74 - 180 * 50 / 2
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# print twee strings, met ertussen de what var, die de returnde waarde van de add
# function bevat, die weer uit genestelde waardes en functions komt
print("That becomes:", what, " Can you do it by hand?")
print(what2)
