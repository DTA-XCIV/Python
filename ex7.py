# print een string
# wat je wilt 'printen' moet altijd tussen () haakjes
print("Mary had a little lamb.")
# print een string met een open var-tag, deze kan in dezelfde lijn gevuld worden
# met de .format functie, die hier weer een string als waarde bevat
# een lege var-plek, wordt gevuld door '.format()' <-- syntax is altijd zo
print("Its fleece was white as {}.".format('snow'))
# print een string
print("And everywhere that Mary went.")
# print een string, en vermenigvuldigt deze tien maal, en plakt ze achter elkaar
print("." * 10) #what'd that do --> de string gewoon tien maal achter elkaar
# Opmerking: een string kan enkel vermenigvuldigt worden met een cijfer, niet delen
# niet aftrekken, enkel vermenigvuldigen
# alle ends zijn variabeles, hier zijn het er twaalf en bevatten ze elke letter
# van het woord Cheeseburger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# de end = ' ' geeft aan het einde van de print een spatie, en plakt de volgende
# string er direct achter

# print de variabelen met de letters van cheeseburger achter elkaar, op deze lijn
# zijn het de eerste zes letters, end betekent dus ook gewoon het einde.
# de end betekent dus eigenlijk ook het einde van een lijn; wat betekent dat erachter
# nog iets volgt, deze wordt voorafgegaan door een ',' want het is een keyword binnen
# de print functie om de 'line-break' aan te duiden
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
# de laatste zes letters van het woord Cheeseburger
print(end7 + end8 + end9 + end10 + end11 + end12)
