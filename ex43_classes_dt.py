class Scene (object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass
        
class Death(Scene):

    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

# Map is-a object that has-a __init__, next_scene, and opening_scene methods
class Map(object):

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        pass
# de opening_scene, die waarschijnlijk de eerste room gaat bevatten
# moet gecalled worden
    def opening_scene(self):


# set a_map to an instance of Map with the argument 'central_corridor'
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
