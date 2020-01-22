lines = "-" * 12
print(lines)
print("You enter a dark room with three doors.")
print("There's a knife on the ground.")
print(lines)
print("Do you want to pick it up?")

knife = input('y/n? > ')

if knife == 'y':
    print(lines)
    print("You pick up the knife. It's very sharp.")
    print(lines)
else:
    print("-" * 12)
    print("Better leave the knife on the ground. It isn't yours.\n")
    print(lines)

print("""You now have to decide through which door you go.
You hear munching noises coming from door #1.
A strange aura emits through the cracks of door #2.
Door #3 seems very attractive to go through.\n
Do you go through door #1, #2 or #3?""")
print(lines)

door = input("> ")

bearroom = """What do you do?
1. Take the cake.
2. Scream at the bear.
3. Nothing."""


if door == "1":
    print(bearroom)
    if knife == 'y':
        print("4. Fight the bear.")
    print(lines)
    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    elif bear == "4":
        print(lines)
        print("You kill the bear and claim the delicious cake for yourself.")

    else:
        print("The bear sees you and charges at you, it's the last thing you see.")


elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survived powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("You come into a room with a naked lady.")
    input('> ')
    print("\"Hello gorgeous,\" she says.")
    input('> ')
    print("\"Why don't you come over here?\"")
    input('> ')
    print("You hesitate for a moment...")
    input('> ')
    print("""You could either:
    1. Go over to her.
    2. Approach more carefully.""")

    walk = input("What do you do? > ")

    if walk == "1":
        print(lines)
        print("She's a succubus!")
        print("The creature sucks out your soul and drags you down to hell.")

    elif walk == "2" and knife == 'y':
        print(lines)
        print("As you approach her carefully, you see she's a succubus.")
        print("Not falling for her tricks, you stab her when you get near.")
        print("She dies, and leaves behind the truth of the universe.")

    else:
        print(lines)
        print("As you approach, you see she's a succubus!")
        print("But it's too late...")

else:
    print("You stumble around and fall on a knife and die. Good job!")
