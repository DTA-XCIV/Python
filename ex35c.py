from sys import exit
from random import randint

def game_room(key, points):
    print("You are in the game room")
    print("There's only one game here.")
    print("In the corner is a prize store")
    print("(Play) the game, go to prize (store) or (leave)")
    action = input("> ")

    if "play" in action:
        while True:
            print("Insert coin or leave. (c)")
            play = input("> ")
            if "c" in play:
                win = randint(0, 1)
                if win == 1:
                    print("You play the game and win.")
                    points += 1
                    print(f"You have {points} point(s).")
                else:
                    print("You lose. Better luck next time.")
            else:
                print("You decide to head back.")
                game_room(key, points)
    elif "store" in action:
        print("You head over to the prize store. ")
        print("You can buy a key here for 3 points!")
        print("Do you want to buy the key?")

        buy = input("> ")

        if "y" in buy and points >= 3:
            key = True
            print("You have a key and head back out.")
            start()
        elif "y" in buy and points < 3:
            print("You don't have enough points.")
            game_room(key, points)
        else:
            print("You leave the store.")
            game_room(key, points)
    else:
        print("You decide to head back.")
        start(key, points)


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = int(input("> "))

    if choice >= 50:
        exit("You greedy bastard!")
    elif choice < 50:
        exit("Nice, you're not greedy, you win!")
    else:
        exit("Man, learn to type a number.")

def bear_room(key):
    print(f"{key}")
    print("There is a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        choice = input("> ")

        if "honey" in choice:
            exit("The bear looks at you then slaps your face off.")
        elif "taunt" in choice and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif "taunt" in choice and bear_moved:
            exit("The bear gets pissed off and chews your leg off.")
        elif "door" in choice and bear_moved and not key:
            print("The door is locked.")
            print("Do you want to head back?")
            back = input(" > ")
            if "y" in back:
                start(key, points)
            else:
                print("You decide to stay in the room")
        elif "door" in choice and bear_moved and key:
            print("You use the key to unlock the door.")
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil C'thulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input('> ')

    if "flee" in choice:
        start(key, points)
    elif "head" in choice:
        exit("Well that was tasty!")
    else:
        cthulhu_room()

def start(key, points):
    print("You are in a dark room.")
    print("There is a door to your right, left and front.")
    print("Which one do you take?")

    choice = input('> ')

    if choice == "left":
        bear_room(key)
    elif choice == "right":
        cthulhu_room()
    elif choice == "front":
        game_room(key, points)
    else:
        exit("You stumble around the room until you starve.")

key = False
points = 0

start(key, points)
