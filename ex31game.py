lines = "-" * 12

def traproom():
    print(lines)
    print("You go through the door and find out it's a traproom...")
    print("The floor opens up and you fall down a traphole.")
    print(lines)
    print("Better luck next time!")

def idle():
    print(lines)
    print("You can't decide on which door to choose and starve to death.")

def new_room(doors):
    print(lines)
    print("You enter a new room.")
    new_room = "The new room has {} door(s).".format(doors)
    print(new_room)

def left():
    print("There's one to the left.")

def front():
    print("One infront of you.")

def right():
    print("There's one to the right.")

def go():
    print(lines)
    print("Through which one do you go?")

print(lines)
print("You wake up in a strange room.")
print("You stand up and look around you...")
print("The room you're in has two doors")

left()
right()
go()

room1 = input('> ')


if room1 == "left":
    new_room("one")
    right()
    go()

    room2 = input('> ')

    if room2 == "right":
        new_room("two")
        front()
        right()
        go()

        room3 = input('> ')

        if room3 == "right":
            new_room("two")
            left()
            front()
            go()

            room4 = input('> ')

            if room4 == "left":
                new_room("three")
                left()
                front()
                right()
                go()

                room5 = input('> ')

                if room5 == "front":
                    print(lines)
                    print("You safely made it out of the maze!")
                elif room5 == "left":
                    traproom()
                elif room5 == "right":
                    traproom()
                else:
                    idle()

            elif room4 == "front":
                traproom()

        elif room3 == "front":
            traproom()
        else:
            idle()
    else:
        idle()
elif room1 == "right":
    traproom()
else:
    idle()
