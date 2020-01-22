class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

like_the_angel = Song(["Like the angel you are",
                       "You laugh, creating",
                       "A lightness in my chest",
                       "Your eyes they penetrate me",
                       "Your answer's always maybe",
                       "That's when I got up and left"])

eternal_flame_lyrics = (["Close your eyes",
                         "Give me your hand, darling",
                         "Do you feel my heart beating",
                         "Do you understand",
                         "Do you feel the same",
                         "Or am I only dreaming"])

eternal_flame = Song(eternal_flame_lyrics)

eternal_flame.sing_me_a_song()
