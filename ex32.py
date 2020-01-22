# variabele met een lijst, de waardes staan tussen rechte haken
# en zijn gescheiden door komma's
the_count = [1, 2, 3, 4, 5]
# een lijst kan ook strings als waarden bevatten
fruits = ['apples', 'oranges', 'pears', 'apricots']
# of een mix
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# de for-functie, gebruikt voor loops
# hier neemt de for-functie variabele the_count met als waarde
# de lijst 1 tot 5, en geeft elke waarde binnen de lijst
# de tijdelijke naam number, de for-functie gaat elke waarde af
# omdat het er 5 zijn, zal de lijn onder de for-functie
# ook vijf keer werken
for number in the_count:
    print(f"This is count {number}")

# same as above
# ja, hetzelfde als erboven
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
# het maakt niet uit wat je de waardes noemt na de for, maar
# voor onbekenden, en een veelgebruikt teken is i
for i in change:
  print(f"I got {i}")

# we can also build lists, first start with an empty one
# dit is een variabele met een lege lijst
elements = []

# then use the range function to do 0 to 5 counts
# de range()-functie wordt meestal samen gebruikt met de for
# om dingen te laten herhalen
# range(0, 6) telt van 0 tot 5 , begint bij 0 , gaat tot 6, dus niet
# t/m
# herhaalt hier print("string")
# append schrijft een waarde in een lijst die onder een variabele staat
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
