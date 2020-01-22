from sys import exit
from random import randint
from inventory import weapon_swap, index_inventory

def rng(holding):
    if holding == "Boxing Gloves":
        hit = 10
        rng = randint(0,1)
        return hit, rng
    elif holding == "Knife":
        hit = 20
        rng = randint(0,1)
        return hit, rng
    elif holding == "Handgun":
        hit = 25
        rng = randint(0,1)
        return hit, rng
    elif holding == "Shotgun":
        hit = 150
        rng = 0
        return hit, rng
    else:
        print()

def fight_swap(action, inventory, holding):
    if "knife" in action:
        x = weapon_swap(inventory, "Knife", holding)
        return x
    elif "hand" in action:
        x = weapon_swap(inventory, "Handgun", holding)
        return x
    elif "shot" in action:
        x = weapon_swap(inventory, "Shotgun", holding)
        return x
    else:
        print("Swap to what?")
        return holding

def using_ammo(holding, hg_ammo_left, sg_ammo_left):
    if holding == "Handgun":
        hg_ammo_left -= 1
        print("You aim your handgun and fire. Ammo left:", hg_ammo_left)
        return hg_ammo_left, sg_ammo_left
    elif holding == "Shotgun":
        sg_ammo_left -= 1
        print("You aim your shotgun and fire. Ammo left:", sg_ammo_left)
        return hg_ammo_left, sg_ammo_left

def reload(holding, inventory, hg_inv, sg_inv, hp_inv):
    if holding == "Handgun" and hg_inv > 0:
        x = index_inventory(inventory, "mag")
        inventory.pop(x)
        left = hg_inv - 1
        hg_inv -= 1
        inventory.append("Handgun mag(s): {}".format(left))
        print("You reload your weapon.")
        print("You have {} Handgun mag(s) left in your inventory.".format(left))
        return 5, hg_inv, sg_inv
    elif holding == "Shotgun" and sg_inv > 0:
        x = index_inventory(inventory, "shell")
        inventory.pop(x)
        left = sg_inv - 2
        sg_inv -= 2
        inventory.append("Shotgun shell(s): {}".format(left))
        print("You reload your weapon.")
        print("You have {} Shotgun shell(s) left in your inventory.".format(left))
        return 2, hg_inv, sg_inv
    elif holding == "Pack" and hp_inv > 0:
        x = index_inventory(inventory, "pack")
        inventory.pop(x)
        left = hp_inv - 1
        hp_inv -= 1
        inventory.append("Healthpack(s) (30): {}".format(left))
        print("You have {} Healthpack(s) left in your inventory.".format(left))
        return hp_inv
    else:
        print("You go into your inventory but don't find anything, mate.")
