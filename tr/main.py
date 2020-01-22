from sys import exit
from textwrap import dedent
import morale
import random
import maze
import chests


class Begin(object):


    def enter(self):

        print(dedent("""
            Welcome to Treasure Run!

            You are Harrison Jones, a widely-known treasure hunter who
            is looking for a last big score before he retires.

            Having decided you are going to raid Moonjabi, you prepare
            the essentials and head off to the jungle where the
            catacomb is located.
            """))

        input("Continue > ")

        return 'entrance'


class Entrance(object):


    def enter(self):

        print(
            dedent("""
            After a long search through the jungle,
            you arrive at the Moonjabi catacomb.
            With the surroundings clear, you head towards the entrance.
            It seems the entrance is sealed with a riddle:

            "Feed it - it lives. Give it something to drink - it dies."

            The entrance requires a correct answer to open.
            """)
             )

        while True:
            guess = input('> ')

            if guess != 'fire':
                print(f"You shout {guess} at the door, but it remains sealed.")
                morale.jones.fatigue('entrance')
                print(f"Your morale drops to: {morale.jones.mo_lvl}")
            else:
                print(
                    dedent("""
                    The stone door starts to move and reveals
                    a dark entrance. You can't see anything through the
                    darkness, but knowing there's a treasure inside,
                    you tell yourself it's worth the risk. You make your
                    way through the entrance. You still can't see anything.
                    You think to yourself that you should have brought
                    your lantern.

                    Fumbling around, you walk into a wall. The only way onward
                    is to continue to the left...
                    """)
                     )
                return 'cata_one'


class CataOne(object):


    def enter(self):

        going_in = maze.MazePosition('c3')
        in_maze = maze.MazeEngine(going_in)
        in_maze.start()
        return 'cata_two'


class CataTwo(object):


    def enter(self):

        print(
            dedent("""
            Coming out of the maze, you see that this room is lit from
            a crack from the ceiling. Rays of light fall upon a shrine.
            Moving closer you see that the shrine is filled with clear water.

            The water looks tempting, as you are thirsty.
            """)
             )
        action = input('> ')
        if "drink" in action:
            morale.Death.water_death(self)
        else:
            print(
                dedent("""
                You have enough experience to tell that the water is
                probably poisened. As you look around you see that the
                room is actually filled with skeletons.
                Searching through the corpses on the ground,
                you find a cellar door that leads further underground.
                """)
                 )
            return 'cata_three'


class CataThree(object):


    def enter(self):

        print(
            dedent("""
            You now enter a richly decorated room.
            It only has one door and it is huge. You are pretty sure
            it is the door to the treasure room.

            Again the door is sealed, but this time with a lock.
            You look around the room and find there are three chests.
            They look like they can be opened without much effort.

            You walk over to the chests...
            """)
             )
        chest_key = random.randint(0,2)
        while morale.jones.mo_lvl > 0:
            key = chests.open()
            return key

class TreasureRoom(object):


    def enter(self):

        print(
            dedent("""
            The room you walk into is filled with treasure.
            You found enough gold to live the rest of your live comfortably.

            The end.
            """)
             )
        return 'finish'


class Maps(object):


    rooms = {
        'begin': Begin(),
        'entrance': Entrance(),
        'cata_one': CataOne(),
        'cata_two': CataTwo(),
        'cata_three': CataThree(),
        'treasure_room': TreasureRoom(),
            }

    def __init__(self, starting_room):

        self.start = starting_room


class Engine(object):


    def __init__(self, maps):

        self.maps = maps

    def start_game(self):

        next = self.maps.start
        while next != 'finish':
            now = self.maps.rooms.get(next)
            next = now.enter()


mapping = Maps('begin')
play = Engine(mapping)
play.start_game()
