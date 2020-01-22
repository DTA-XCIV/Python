# de break_words function; gebruikt de split functie om woorden in een string
# uit elkaar te halen en in enkele aanhalingstekens te zetten
# de splitfuncti heeft plaats voor input van de script
# dus wanneer er split(' ') wordt gebruikt, neemt python de spaties eruit en
# zet alle woorden apart
# via een test met "y" merkte ik op dat python de y van mijn de zin:
# "hallo ik ben danny" de y wegneemt :
# 'hallo ik ben dann', ''
# de split functie leest de string van links naar rechts en verwijdert alles
# wat meegegeven is, en laat een gefragmenteerde string achter zonder de
# meegegeven waardes, zoals bijv. het wegknippen van het wit bij een rood witte
# lint
# split(' ') --> split de spaties
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

# function sort_words is best simpel; de function krijgt een waarde binnen
# een string, en de sorted() functie neemt deze string, leest de woorden
# die erin staan en sorteert ze op alfabetische volgorde en geeft ze terug
# via de return functie
# belangrijk om te onthouden is dat een string wel daadwerkelijk meerdere
# waarden / woorden moet bevatten voordat ze gesorteerd kunnen worden
# daarom is het noodzakelijk dat wanneer men deze functie gebruikt
# de zin in een string eerst door de break_words function gehaald word
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# function print_first_word; neemt het woord bij byte 0 en haalt deze van de
# string af; hier slaat de function het op in een variabele
# zodat deze geprint kan worden
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

# function print_last_word; hetzelfde als hierboven, maar een andere positie
# als de string als een ronde cirkel / spectrum / loop beschouwd kan worden
# dan is een stap terug van 0 natuurlijk het laatste woord wat in de string
# voorkomt
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

# function sort_sentence
# gebruikt een combinatie van voorgaande functions, wat voorheen apart door
# de twee gebruikte functions gehaald moesten worden
# hier neemt de function een volledige zin in een string, haalt deze door
# de break_words, terwijl het de waarde opslaat in words, en gebruikt deze
# variabele vervolgens om te gebruiken in de sort_words
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# function print_first_and_last; ook hier is het belangrijk dat een zin in
# een string eerst door de break_words wordt gehaald, zodat de variabele meerdere
# waardes heeft om de opvolgende functions te laten werken
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# function print_first_and_last_sorted; ik was hier in de war omdat ik dacht
# dat de sort function geen break nodig had om woorden te sorteren
# maar toen ik verder keek dan mijn neus lang was, zag ik dat de sort_sentence
# function, die als eerste wordt gecalld in de laatste function, al een
# break_words bevat, dus het is toch wel nodig, maar het staat gewoon in een
# verbonden function
# qua functie is deze hetzelfde als de vorige, maar haalt het de string nog
# een keer extra door de sorteer function
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
