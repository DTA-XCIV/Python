# een function met de naam (aangegeven door def) met als naam cheese_and_crackers
# binnen de function zijn er twee arguments, cheese_count en boxes_of_crackers
# deze nemen een waarde aan die later worden meegegeven wanneer de function
# wordt gecalled/geuset/gerund
# de function hierbeneden print in de eerste twee strings de waardes
# die kunnen worden meegegeven
# en daarna nog twee extra strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print met uitleg
print("We can just give the function numbers directly:")
# de function wordt hier gecalled, hier geeft de script twee integers mee
# als waardes
cheese_and_crackers(20, 30)

# print een string met uitleg
print("OR, we can use variables from our script:")
# hieronder zijn twee variabelen die een integer als waarde aannemen
amount_of_cheese = 10
amount_of_crackers = 50
# deze variabelen kunnen ook gebruikt worden bij het callen van een function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print een string met uitleg
print("We can even do math inside too:")
# de argumenten die de script meegeeft aan de function wanneer deze gecalled wordt
# kan ook wiskunde zijn, net zoals dat kan bij het aanduiden van een waarde
# in een variabele
cheese_and_crackers(10 + 20, 5 + 6)
# print een string met uitleg
print("And we can combine the two, variables and math:")
# de argumenten die meegegeven kunnen worden bij het callen van een function
# kan een combinatie zijn van variabelen en wiskunde 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
