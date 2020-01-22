from sys import exit

class Scene (object):

    def enter(self):
        pass

# de class Engine, een instance werd aangemaakt toen a_game deze callde
# Engine erfde daarbij de eigenschappen/ attributes van Map, inclusief de
# variabele
# de Engine class has-a __init__ en play methods
class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        # set start_game to an instance of CentralCorridor
        # start_game is na de onderstaande lijn een object met een instance
        # van CentralCorridor
        # het object kan nu gebruikt worden om de methods uit de instance
        # te laten runnen, bij het geraamte is mij enter meegegeven
        # deze zal ik moeten laten callen om de room te laten werken
        start_game = CentralCorridor()
        start_game.enter() # ik laat de script hier de method van de start_game
                        # object callen, zodat de kamer geactiveerd word

# de class CentralCorridor is-a Scene, en erft dus eigenschappen hiervan
# CentralCorridor has-a enter method
# de CentralCorridor is een start scene, die direct gerund wordt
# hij bevat tevens een vijand die verslagen moet worden dmv van een grap,
# voordat de speler verder gaat

        if start_game == 'laser':
            armory = LaserWeaponArmory()
            armory.enter()

class Death(Scene):

    def enter(self):
        exit("bruh u died")

class CentralCorridor(Scene):

    def enter(self):
        print("You enter the Central Corridor.")
        print("A Gothon is blocking your way to the Laser Weapon Armory!")
        print("You prepare to fight the Gothon.")

        action = input('[Fight][Flee][Tell A Joke]> ')

        if "fight" in action:
            print("You try to fight the Gothon, but he is too strong.")
            print("The Gothon alien bites your head off.")
            Death.enter(self)
        elif "flee" in action:
            print("You try to flee, but the door behind you is shut.")
            print("The Gothon approaches you and eats you.")
            Death.enter(self)
        elif "joke" in action:
            print("You tell a nice joke and the Gothon rolls over from laughter.")
            print("You can now sneak past him.")
            LaserWeaponArmory.enter(self)
        else:
            print(f"There's no {action} command.")
            CentralCorridor.enter(self)

class LaserWeaponArmory(Scene):

    def enter(self):
        print("You enter the Armory and see a neutron bomb locked away.")
        print("You have to get it.")
        print("The lock requires a code.")

        code = 1234

        action = input('You try to guess the code> ')

        if code == 1234:
            print("You got the bomb. Nice.")
            TheBridge.enter(self)
        else:
            print("The aliens get to you before you get the bomb.")
            Death.enter(self)

class TheBridge(Scene):

    def enter(self):
        print("You enter the Bridge.")
        print("You need to place the bomb here.")

        action = input('> ')

        if "place" or "put" in action:
            print("You place the bomb and go for the escape pod room.")
            EscapePod.enter(self)
        else:
            print("The aliens notice you and draw their blasters.")
            print("It's the last thing you see.")
            Death.enter(self)

class EscapePod(Scene):

    def enter(self):
        print("You get to the Escape Pods.")
        print("There are five of them, which one do you choose?")

        action = input('> ')
        right_pod = 1

        if int(action) == right_pod:
            print("You launch out of the ship and get to safety.")
            print("bruh u win")
        else:
            print("You launch into space but soon notice that the pod")
            print("has no oxygen and fuel tank.")
            Death.enter(self)

# de class Map is-a object en has-a __init__ function die self en start_scene
# parems aanneemt, daarnaast map has-a next_scene en opening_scene functions
# voor de oplossing kan ik opening_scene gebruiken die al meegegeven is, ipv
# die in de engine te zetten
class Map(object):

    def __init__(self, start_scene):
        pass
        # neemt hier de string die meegegeven is wanneer een instance
        # werd gemaakt van Map, en maakt het een attribuut van de class

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# set a_map to an instance of Map with the argument 'central_corridor'
# doordat de class Map has-a opening_scene, moet ik deze denk ik gebruiken
a_map = Map('central_corridor')
# set a_game to an instance of Engine that takes the object a_map
# dit betekent dat a_game een object wordt, met een Engine instance
# deze Engine instance inherit eigenschappen van de object a_map
# omdat a_map ook een instance van Map bevat
# Engine inherit nu de __init__ en overige functies, en ook de meegegeven string
a_game = Engine(a_map)
# vervolgens runt de script de method play van de a_game object (de instance van
# Engine, die weer geerfd heeft van a_map, die een instance is van Map)
# wat play probeert te doen is de game starten, en de game start met de
# corridor, dus die call die, wanneer play wordt gecalled
# de play call op a_game werkt tot het einde van de start_game object,
# daarna eindigt de script
a_game.play()

# ik heb nu een werkend spel gemaakt met de classes die meegegeven zijn
# maar ik merk dat via mijn manier er geen gebruik wordt gemaakt van de
# map en engine, maar dat ik enkel verwijs naar andere classes
# ik ga een nieuwe file maken en proberen te werken met de code
# die meegegeven is 
