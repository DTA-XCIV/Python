# argv wordt geimporteerd vanuit sys
from sys import argv
# argv unpacked twee variabelen, waarvan de eerste altijd de scriptnaam is
script, user_name, day = argv
# variabele 'prompt' met als waarde een string
prompt = "Answer: "
# print de meegegeven waardes van de argv-functie in een string
print(f"Hi {user_name}, I'm the {script} script.")
print(f"It is {day} today!")
# print een string
print("I'd like to as you a few questions.")
# print een string met de argv variabele dmv de f-functie aan het begin van string
print(f"Do you like me {user_name}?")
# variabele met gebruiker input, de eerder aangeduide variabele (met de string
# als waarde wordt geprompt)
likes = input(prompt)
# print een string met een variabele
print(f"Where do you live {user_name}?")
# variabele waarbij de gebruiker de waarde bepaald door de input-functie, die
# de eerdere variabele prompt-var prompt
lives = input(prompt)
# print een string
print("What kind of computer do you have?")
# gebruiker input voor variabele waarde
computer = input(prompt)
# print een stuk tekst met variabelen, die door de gebruiker aan de andere kant
# bepaald zijn
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
