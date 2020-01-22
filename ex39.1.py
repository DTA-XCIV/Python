# create a mapping of state to abbreviation
# een dict is net als een lijst, waarin de items gescheiden zijn met een komma
# anders dan een lijst, waar de waardes aan indexen, oftewel nummers gebonden
# zijn, kunnen items in een dict aan een andere waarde verbonden zijn, die tevens
# gebruikt kunnen worden om de waarde te callen
# in een dict heten zij de key en value
# de key is een string, en de value kan een string zijn, of integer, andersom
# kan natuurlijk ook
# de format van een dict lijkt op die van een blok
# waarbij items onder de naam van de dict met een ingetabde format geschreven
# wordt
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# add some more cities
# items kunnen toegevoegd worden aan een dict door eerst een nieuwe key
# door te geven door de dict te callen, met een nieuwe key
# en daaraan een nieuwe waarde te verbinden
# zie de code hieronder
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
# de values van een dict kunnen bereikt worden door de dict samen met de key
# te callen
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
# dicts kunnen met elkaar worden verbonden, zolang de waardes van een dict
# overeen komt met de keys van een andere, zodat wanneer de code een value aanvraagt
# deze gebruikt kan worden als key voor een andere dict
# zie hieronder
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
# om zowel de key en value uit een dict te halen, gebruikt men de method
# items(), Zed plaatst deze nog eens in een list()-functie, maar ik kan niet
# verklaren waarom, want states.items() werkt ook
# key en value kunnen geprint worden in een loop
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both as the same time
print('-' * 10)
for state, abbrev in list(states.items()):
  print(f"{state} state is abbreviated {abbrev}")
  print(f"and has the city {cities[abbrev]}")

print('-' * 10)
# om een waarde uit een dict te halen, gebruikt men ook de key
# de get() method callen op de dict met de key als argument
# als de key niet bestaat, dan 'returnt' de dict niks
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

# get a city with a default value
# om een eigen waarde door te geven wanneer niks terugkomt, plaatst men
# de waarde, gescheiden door een komma, achter de key
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
