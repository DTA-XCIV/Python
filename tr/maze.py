from textwrap import dedent
import morale


class A1(object):


    def enter(self):

        morale.jones.fatigue('maze')

        print(
            dedent(""""
            Even though you had a bad feeling about this passageway,
            you decided to walk into this one.

            It's a dead end.
            """)
             )
        print(f"Your morale levels drop to {morale.jones.mo_lvl}")
        print("You can only head back from here.")
        return 'a2'


class A2(object):

    def enter(self):

        print(
            dedent("""
            As you walk forward, you come into another clearing which has
            two passageways. It seems like you are getting deeper into the
            maze.

            You ponder on whether to take passageway #1, #2, or head [back].
            """)
             )
        while True:
            action = input('> ')
            if action == '1':
                return 'a1'
            elif action == '2':
                return 'a1'
            elif action == 'back':
                return 'b2'
            else:
                print("The maze confuses you.")
                morale.jones.fatigue('maze')
                print(f"Your morale levels drop to:{morale.jones.mo_lvl}")
                return 'a2'


class B1(object):


    def enter(self):

        print(
            dedent("""
            You continue into the darkness and the tunnel keeps
            going forward. You don't encounter any new passageways...
            """)
             )
        input('> ')
        return 'c1'


class B2(object):


    def enter(self):

        print(
            dedent("""
            As you keep fumbling forward, you come into a clearing.

            A dimly lit torch shows three passageways you can walk into.
            It seems like you walked into a maze...

            You ponder on whether to take passageway #1, #2, or #3.
            """)
             )
        while True:
            action = input('> ')
            if action == '1':
                return 'b3'
            elif action == '2':
                return 'a2'
            elif action == '3':
                return'b1'
            else:
                print("The maze confuses you.")
                morale.jones.fatigue('maze')
                print(f"Your morale levels drop to: {morale.jones.mo_lvl}")


class B3(object):


    def enter(self):

        print("You walk into a dead-end, it demoralizes you.")
        morale.jones.fatigue('maze')
        print(f"Your morale level drops to: {morale.jones.mo_lvl}")
        print("From here you can only head back.")
        input('> ')
        return 'b2'


class C1(object):


    def enter(self):

        print("As you stumble foward, you see light coming out of the end.")
        print("You quickly walk over.\n")
        input('> ')
        return 'finished'


class C2(object):


    def enter(self):

        print("You appear to be in some kind of tunnel.")
        print("You follow it alongside the wall, heading east this time.")
        input('> ')
        return 'b2'


class C3(object):


    def enter(self):

        print("You fumble ahead and walk into another wall.")
        print("The only way forward is north.")
        input('> ')
        return 'c2'


class MazePosition(object):


    maze_rooms = {
        'a1': A1(),
        'a2': A2(),
        'b1': B1(),
        'b2': B2(),
        'b3': B3(),
        'c1': C1(),
        'c2': C2(),
        'c3': C3(),
               }

    def __init__(self, position):

        self.position = position

    def move(self, next_room):

        next = self.maze_rooms.get(next_room)
        return next


class MazeEngine(object):


    def __init__(self, grid):

        self.grid = grid

    def start(self):

        next_room = self.grid.position

        while next_room != 'finished':
            current_room = self.grid.move(next_room)
            next_room = current_room.enter()
