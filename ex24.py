# print een string
print("Let's practice everything.")
# print een string met escape sequences; de backslash maakt het mogelijk om
# een enkele aanhalingsteken te gebruiken in een string die omsloten is door
# enkele aanhalingstekens; laat ook zien dat een backslash geprint kan worden
print('You\'d need to know \'bout escapes with \\ that do:')
# print een string, met escape sequences, hier een extra line break, bovenop
# de linebreak die een print normaalgezien uitvoert, en een tab
print('\n newlines and \t tabs.')
# hier een variabele met een string die formatting behoudt, omdat het omsloten
# is door drie """ .. """ aanhalingstekens
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# print een lijn voor de sier
print("--------------")
# print een variabele, dus de waarde binnen de variabele
print(poem)
# print een lijn voor de sier
print("--------------")

# variabele met een integer als waarde die uit een wiskundesom komt
five = 10 - 2 + 3 - 6
# print een f"" string; variabelen kunnen in {} haken aangehaald worden en
# de print() functie weergeeft de waarde van de variabele
print(f"This should be five:{five}")
# een function die secret_formule heet, en een enkele argument aanneemt
# hier neemt het een integer, en verwerkt het driemaal, elke volgende variabele
# afhankelijk van de waarde van de vorige, maar uiteindelijk zijn er wel
# drie afzondelijke variabelen die een waarde bevatten
# return geeft de waardes in deze variabelen terug (returnt), als een soort
# van output naar de lijn die de function callde
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# variabele met een integer, hier als waarde voor de function
start_point = 10000
# omdat de function drie waardes returnt, kunnen drie variabelen op een lijn
# deze waardes aannemen voor gebruik buiten de function
# de drie variabelen staan dus open voor voor waardes
# deze krijgen zij door de function secret_formula te callen, en de variabele
# mee te geven die eerder al aangeduid werd
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
# een string met een open plek voor aanvulling wordt aangeduid met een {}
# een format functie erachter vult deze plek aan
print("With a starting point of {}".format(start_point))
# it's just like with an f"" string
# de waardes uit de function zijn opgeslagen in variabelen die buiten de function
# staan, en dus nu ook bekend in het algemeen, zodat de print functie
# deze kan printen met de f "" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
# deelt de voorgaande waarde door 10
start_point = start_point / 10
# print een string
print("We can also do that this way:")
# de drie returnde waarde van de function kunnen ook opgeslagen worden in
# een variabele
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# om die waardes te printen (ze staan al in een bepaalde volgorde,
# de volgorde die de variabele binnen de function ook hebben),
# kan de script lege {} haken gebruiken, die tevens niet in een f "" string
# staan, omdat ze anders niet gebruikt kunnen worden door de format functie
# de drie waardes kunnen vervolgens op de opgeslagen volgorde ingevuld worden
# in de onderstaande string met de format functie die als waarde *formula,
# om op die manier aan te duiden dat deze meerdere waardes bevat
# de variabele formula slaat de waardes op als volgt:
# formula = 500000, 500, 5; dat maakt het gemakkelijker om te zien hoe de
# waardes opgeslagen worden
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
