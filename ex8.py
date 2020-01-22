# variabele met een string, die vier lege {}-tags bevat
# het is belangrijk dat de .format/aantal {}-tags in een variabele, wanneer
# deze samen worden gebruikt, dezelfde aantallen waardes bevatten, anders is het
# bereik van de .format te klein, of te groot etc.
formatter = "{} {} {} {}"
# print de eerste variabele, en vult de vier lege {}-tags in met de waardes die
# volgen in de .format functie, elk zijn gescheiden door een komma
# de formatter bevat enkel {}-tags, dus ik kan de waarde van de print niet in
# aanhalingstekens zetten, dat zou het een string maken
# als ik enkel formatter in aanhalingstekens zet, neemt print het niet eens aan
# als variabele, wat het wel moet doen
# als ik de volledige .format waardes in aanhalingstekens zet, neemt de functie
# het aan als een enkele waarde, wat dus niet overeenkomt met de regels hierboven
# beschreven
print(formatter.format(1, 2, 3, 4))
# hetzelfde als hierboven, maar hier zijn de waardes omhult met aanhalingstekens
# omdat het strings zijn
# ook belangrijk om de de aanhalingstekens goed af te sluiten met hetzelfde
# karakter, dus niet " ', of andersom.
print(formatter.format('one', 'two', 'three', 'four'))
# hetzelfde als hierboven, die vier lege {}-tags worden hier gevulg met boolean
# waardes
print(formatter.format(True, False, False, True))
# de {}-tags worden gevuld met de waarde van de variabele, dus in totaal zestien
# maal de {}-tags
print(formatter.format(formatter, formatter, formatter, formatter))
# code met Tab formatting, hetzelfde als de tweede print functie, maar dan met
# formatting, de strings zijn ook wat langer
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
