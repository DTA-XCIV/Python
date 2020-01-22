class Scene (object):

    def enter(self):
        pass

# de class moet tegen de engine zeggen welke kamer er volgt
# maar als ik return doe in de class (van de room) dan blijft die steken
# waar ik hem callde, in de Map
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # de manier die ik hier gebruik, is bijna hetzelfde als die van zed
        # alleen geef ik hier direct de naam van de class terug
        # en laat ik de next_scene niks verwerken
        # echter merk ik nu dat wanneer ik de speler door alle maps wil
        # laten lopen veel herhalende code is die de kamers met elkaar verbind
        # daarom gebruikt zed ook een loop en zet hij het ook in de class Engine
        # zodat het duidelijk is wat er gebeurd
        # het verloop van een spel, of van een programma (mits die een lijn van
        # procedures bevat, kan het best worden geschreven als een loop die
        # de verschillende classes overloopt en de loop verbreekt wanneer
        # er afgeweken wordt van het verwachte verloop)
        
        open = self.scene_map.opening_scene()
        laserterug = open.enter()
        brug = self.scene_map.next_scene(laserterug)
        brugterug = brug.enter()
        vlucht = self.scene_map.next_scene(brugterug)
        vluchtterug = vlucht.enter()
        eind = self.scene_map.next_scene(vluchtterug)
        eindterug = eind.enter()
        gewonnen = eindterug.enter()

class Death(Scene):

    def enter(self):
        exit("dead bruh")

class CentralCorridor(Scene):

    def enter(self):
        print("CC scene; win or lose")

        action = input('> ')

        if action == "win":
            return LaserWeaponArmory()
        else:
            return Death()

class LaserWeaponArmory(Scene):

    def enter(self):
        print("Je bent in de armory.")
        return TheBridge()

class TheBridge(Scene):

    def enter(self):
        print("Je bent op de brug.")
        return EscapePod()

class EscapePod(Scene):

    def enter(self):
        print("Je bent op de vlucht.")
        return Finished()

class Finished(Scene):

    def enter(self):
        print("Je hebt gewonnen")

# Map is-a object that has-a __init__, next_scene, and opening_scene methods
class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return scene_name
# de opening_scene, die waarschijnlijk de eerste room gaat bevatten
# moet gecalled worden
    def opening_scene(self):
        return CentralCorridor()

# set a_map to an instance of Map with the argument 'central_corridor'
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
