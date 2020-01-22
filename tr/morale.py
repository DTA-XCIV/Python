from textwrap import dedent


class Death(object):


    def entrance_death(self):

        exit(
            dedent("""
            The riddle sealing the entrance appeared to be too hard.
            Having no morale left, you head back home.
            """)
            )

    def water_death(self):

        exit(
            dedent("""
            From all these years of raiding tombs,
            Harrison still hasn't learned not to drink from
            deceptively tempting looking water.

            The water was poisened, and Harrison slowly chokes to death,
            joining the other skeletons in the room.
            """)
            )

    def maze_death(self):

        exit(
            dedent("""
            You get hopelessly lost in the dark maze.
            Still not knowing which way to go, you panick
            and run into a wall, cracking open your skull.

            You collapse and bleed to death.
            """)
            )

    def blast_death(self):

        exit(
            dedent("""
            The air blast was too much for Harrison.
            Your eyes got blinded by the sand.

            Blinded and unnable to find a way out, you starve to death.
            """)
            )


class Morale(object):


    def __init__(self, morale):

        self.mo_lvl = morale

    def fatigue(self, room):

        self.room = room
        self.mo_lvl -= 10

        if self.mo_lvl <= 0 and self.room == 'entrance':
            Death.entrance_death(self)
        elif self.mo_lvl <= 0 and self.room == 'maze':
            Death.maze_death(self)

    def air_blast(self):

        self.mo_lvl -= 50
        if self.mo_lvl <= 0:
            Death.blast_death(self)

jones = Morale(100)
