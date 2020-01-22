from fight import monster, cont
from sys import exit
from inventory import open_inventory

def entrance(args):
    print("Welcome to Dr. Booms dungeon!")
    print("Go through the dungeon  and kill the End Boss.")
    cleared1 = False
    while True:
        inventory = args[7]
        tier = args[6]
        print("There's one door to your left and a store.")
        print("[Door] [Store] [Inventory]")
        open = input('> ')
        if "door" in open and cleared1 == False:
            fight, inventory, cleared1 = room1(args, cleared1)
            player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv = fight
            args = player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv, tier, inventory
            inventory = inventory
        #elif "store" in open:
            #store(args)
        elif "door" in open and cleared1 == True:
            room1(args, cleared1)
        elif "inv" in open:
            open_inventory(inventory)

        else:
            print("I can't do that.")

def room1(args, cleared1):
    inventory = args[7]
    tier = args[6]
    print("You enter a strange room.")
    print("It has a tier 1 monster.")
    if cleared1 == False:
        fight = monster(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv = fight
        tier = 2
        args = player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv, tier, inventory
        print("You can continue or go back.")
        cleared2 = False
        while True:
            print("[Door] [Back]")
            open = input('> ')
            if "door" in open:
                fight, inventory, cleared2 = room2(args)

            elif "back" in open:
                cleared1 = True
                return fight, inventory, cleared1
                break
            else:
                print("I can't do that.")
    else:
        print("Continue or go back. (The room is cleared)")
        cleared2 = False
        while True:
            print("[Door] [Back]")
            open = input('> ')
            if "door" in open and cleared2 == True:
                room2(args)
                return fight, inventory, cleared2
            elif "back" in open:
                cleared1 = True
                break
            else:
                print("I can't do that.")

def room2(args, cleared2):
    inventory = args[7]
    tier = args[6]
    cleared2 = False
    print("You enter a strange room.")
    print("It has a tier 2 monster.")
    if cleared2 == False:
        fight = monster(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv = fight
        tier = 3
        args = player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv, tier, inventory
        print("You can continue or go back.")
        while True:
            print("[Door] [Back]")
            open = input('> ')
            if "door" in open:
                room3(args)
            elif "back" in open:
                cleared2 = True
                return fight, inventory, cleared2
                break
            else:
                print("I can't do that.")
    else:
        print("Continue or go back. (The room is cleared)")
        while True:
            print("[Door] [Back]")
            open = input('> ')
            if "door" in open:
                room3(args)
            elif "back" in open:
                cleared1 = True
                break
            else:
                print("I can't do that.")


def room3(args, cleared2):
    print("You enter a room full with plants.")
    print("The room is empty except for some door(s).")
    if cleared2 == False:
        print("A large monster appears from behind the plants.")
        fight = monster(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        cleared2 = True
        return fight, clared2
    else:
        print("The green monster is decaying.")
        print("There's only one way out of this room.")

    while True:
        print("[Door] [Back]")
        open = input('> ')
        if open == "door":
            break
        elif open == "back":
            room3()
        else:
            print("I can't do that.")

def room4(args):
    print("You enter a hell-forged room.")
    print("The devil himself is standing in front of you.")
    fight = monster(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
    return fight
