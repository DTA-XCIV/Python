# variabele 'types_of_people' met als waarde 10
types_of_people = 10
# variabele met een string die voorafgegaan is door een 'f-functie' zodat de
# waarde van de voorgaande variabele uitgedrukt wordt binnen de string
# dit is de eerste variabele met een string binnen een string
# een string binnen een string kan worden uitgedrukt met de f-functie en door de
# string binnen de string in {} <-- deze haken te zetten
x = f"There are {types_of_people} types of people."
# variabele binary met een string als waarde
binary = "binary"
# variabele do_not met weer een string als waarde
do_not = "don't"
# variabele y die een string bevat met vooraan weer een f-functie, zodat de
# de waardes van de voorgaande toegewezen variabelen uitgedrukt worden
# de tweede variabelen waarin er strings binnen een string geplaatst is
y = f"Those who know {binary} and those who {do_not}."
# print de variabele x
print(x)
# print de variabele y
print(y)
# print een string met f-functie, zodat de waarde van de aangehaalde variabele
# ook geprint wordt, tevens de derde functie waarin een string binnen een string
# staat
print(f"I said: {x}")
# print een string met een de waarde van de aangehaalde variabele door middel
# van de f-functie, de laatste functie met een string binnen een string
print(f"I also said: '{y}'")
# geeft de variabele hilarious een boolean waarde
hilarious = False
# een variabele met een string als waarde, en een lege variabele plaats
# in deze string zitten ook haakjes die aanduiden dat er een string is, maar
# in dit geval is deze leeg, en is het ook aangeduid met een andere kleur
# door Atom, dus ik weet niet zeker wat de functie ervan is, maar wel weet ik
# dat het iets te maken heeft met de print lijn die daarop volgt
# ik verwijderde de tags en probeerde de code opnieuw
# de tag is een open omdat het dan open staat voor meerdere strings
# ik ga dit nog eens testen door eens een andere format aan te halen
joke_evaluation = "Isn't that joke so funny?! {}"
# print de variabele hierboven, gecombineerd met waarde van de variabele hila-
# rious, misschien is dit enkel mogelijk doordat er in de joke_evaluation var
# een lege plek is aangewezen.
# de .format() wordt gebruikt om een lege var-tag op te vullen met welke var dan
# ook, best cool
print(joke_evaluation.format(hilarious))
# een simepele var met string waarde
w = "This is the left side of..."
# weer een simpele var met string waarde
# haakjes voor een string zijn nodig, omdat Python de tekens achter de = gaat lezen
# als code, dus ook andere regels op toepast
e = "a string with a right side"
# print de twee variabelen naast elkaar, dit is anders dan de voorgaande
# voorbeelden, want de twee variabelen worden apart van elkaar geprint
# doordat beide strings apart van elkaar geprint worden, en naast elkaar toe-
# gevoegd door het plusteken, is de combinatie ervan langer dan elk van de strings
# apart
print(w+e)
