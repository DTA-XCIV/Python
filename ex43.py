# importeert exit vanuit de sys, is handig voor errors en wanneer je
# de script manueel wilt laten stoppen
from sys import exit
# importeert de randint uit de package random, is handig voor rng functies
from random import randint
# importeert de dedent functie uit package textwrap, zodat de output formatting
# beter overkomt
from textwrap import dedent
# een class object met (has-a) enter functie, de prints is voor wanneer
# scene nog niet gecodeerd is

# een gevecht start wanneer de speler een alien tegenkomt
# de speler krijgt de mogelijkheid om te slaan, waarbij schade wordt gedaan bij de Alien
# daarna slaat de Alien, en doet schade bij de Player
# wanneer de speler beneden nul raakt, verliest hij het spel
# wanneer de alien dood gaat, kan de speler verder

class Entity(object):

    def __init(self, health, dmg):
        self.health = health
        self.dmg = dmg

class Player(Entity):

    def __init__(self, health, dmg):
        self.health = health
        self.dmg = dmg


class Alien(Entity):

    def __init__(self, health, dmg):
        self.health = health
        self.dmg = dmg

class Fight(object):

    def start_fight(self):
        self.speler = Player(100, 10)
        self.ali = Alien(50, 5)

    def combat_system(self):
        spelerhp = self.speler.health
        alihp = self.ali.health

        while spelerhp > 0:
            spelerhp -= self.ali.dmg
            alihp -= self.speler.dmg

        print("You won the battle.")

class Scene (object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

# wat Zed hier doet is alvast twee variabelen vaststellen
# eentje waarmee de loop begint, en de laatste die de loop verbreekt
# in de while-loop begint de loop met de eerste kamer te verlopen
# de verkregen waarde wordt gebruikt om de current_scene variabele
# te herschrijven dmv een call naar de parentclass Map
# (in de parent class zorgt de next_scene method ervoor dat er uit de
# dict de juiste class naam wordt teruggegeven)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
    "You died. You kinda suck at this.",
    "Your mom would be proud... if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this.",
    "You're worse than your Dad's jokes."

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("Central Corridor scene with Gothon")

        gevecht = Fight()
        gevecht.start_fight()
        gevecht.combat_system()

        action = input('> ')

        if action == "shoot!":
            print("gothon kills you")
            return 'death'
        elif action == "dodge!":
            print("slips")
            return 'death'
        elif action == "tell a joke":
            print("tells joke")
            return 'laser_weapon_armory'
        else:
            print("does not compute")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print("room with keypad")

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")

        if guess == "111":
            print("you got it")
            return 'the_bridge'
        else:
            print("you die")
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print("bridge scene")

        action = input("> ")

        if action == "throw the bomb":
            print("throw bomb, you die")
            return 'death'
        elif action == "slowly place the bomb":
            print("you get to the escape pod")
            return 'escape_pod'
        else:
            print("does not compute")
            return "the_bridge"

class EscapePod(Scene):

    def enter(self):
        print("pod scene: which one?")

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod #]")


        if int(guess) != good_pod:
            print("bad pod: you die")
            return 'death'
        else:
            print("good pod: you win!")

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("you win!")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
