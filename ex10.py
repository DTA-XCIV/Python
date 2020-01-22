# variabele; binnen de string is \t formatting voor een 'tab'
tabby_cat = "\tI'm tabbed in."
# variabele; binnen de string-waarde is \n een linebreak
persian_cat = "I'm split\non a line."
# variabele; de dubbele backslash zorgt ervoor dat de backslash geprint wordt
backslash_cat = "I'm \\ a \\ cat."
# de drie aanhalingstekens zorgt er weer voor dat er grote stukken tekst
# met formatting geprint kunnen worden
# hier zijn er voor het lijstje drie tabs gebruikt, en bij de laatste een line-
# break om de aan te tonen dat het karakter ook binnen de drie aanhalingstekens
# werkt
# drie enkele aanhalingstekens is wellicht handiger, het is gemakkelijker
# te herkennen, EN je kan dubbele aanhalingstekens gebruiken binnen de stuk
# tekst
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# hieronder printen we alle string-waardes van de variabelen
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
# let wel op! een linereak zorgt er enkel voor dat de karakters erna een nieuwe
# lijn krijgen, een enter binnen de format van beneden betekent dan ook een
# volledig nieuwe lijn
# de formfeed is nog een beetje vaag
# in de tekst hieronder zorgt het voor een enter en een tab, de tweede op
# dezelfde lijn geeft een enter en twee tabs
# formfeed maakt van het stukje tekst een paragraaf/alinea
print('''
    \t ingetabd, maar ik tab nog eens.
\t niet ingetabd in het bestand, maar wel in de outp\nut
 de lijn was gebroken, maar ik voegde aan spatie toe aan het begin
 \\ ik print een backslash
 ik kan \" backslash quote gebruiken, maar omdat ik drie enkele aanhalingstekens
 gebruik, kan ik ook zonder """
 python leest snel, dus je hoort een *ding* \a voordat je tot hier bent met lezen
 ik maakte hier een tyy\bp fout, maar dat zie je niet door BS
 \f voor een soort van tab
 \n line-breaks zijn simpel
''')
