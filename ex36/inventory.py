from sys import exit

def index_inventory(inventory, item):
    for i, s in enumerate(inventory):
        if item in s:
            return i
    inventory.append("placeholder")
    return -1

def open_inventory(inventory):
    if inventory:
        print("You open your inventory, it contains:")
        print(inventory)
    else:
        print("You inventory is empty.")

def add_item(action, inventory, inv_a, found):
    if "h" in action:
        item_name = "Handgun mag(s)"
        clips_returned = add_clip_inv(found, inventory, inv_a, item_name)
        return clips_returned
    elif "s" in action:
        item_name = "Shotgun shell"
        clips_returned = add_clip_inv(found, inventory, inv_a, item_name)
        return clips_returned
    elif "black" in action:
        inventory.append("Black Artefact")
    elif "white" in action:
        inventory.append("White Artefact")
    else:
        print("I don't understand.")

def add_clip_inv(found, inventory, inv_a, item_name):
    if item_name == "Handgun mag(s)":
        mag_index = index_inventory(inventory, "mag")
        inventory.pop(mag_index)
        inventory.append("Handgun mag(s): {}".format(inv_a + found))
        inv_a += found
        return inv_a
    else:
        shell_index = index_inventory(inventory, "shell")
        inventory.pop(shell_index)
        inventory.append("Shotgun shell(s): {}".format(inv_a + found))
        inv_a += found
        return inv_a

def ammo_found(*args):
    i_hg, i_sg, hg_inv, sg_inv, inventory = args
    ammo_hg = i_hg
    ammo_sg = i_sg
    hg_taken = False
    sg_taken = False
    while True:

        if hg_taken == False and sg_taken == False:
            print("You encounter {} handgun mag(s).".format(ammo_hg))
            print("You also encounter {} shotgun shell(s).".format(ammo_sg))
        elif hg_taken == True and not sg_taken == True:
            print("There are {} shotgun shell(s) left.".format(ammo_sg))
        elif sg_taken == True and not hg_taken == True:
            print("There is {} handgun mag left.".format(ammo_hg))
        else:
            print("You search the rest of the room.")

        action = input('> ')
        if "h" in action and hg_taken == False:
            hg_inv = add_item(action, inventory, hg_inv, ammo_hg)
            hg_taken = True
            print("You take the handgun mag(s).")
            print(f"--You now have {hg_inv} handgun mag(s).")
        elif "s" in action and sg_taken == False:
            sg_inv = add_item(action, inventory, sg_inv, ammo_sg)
            sg_taken = True
            print("You take the shotgun shell(s).")
            print(f"--You now have {sg_inv} shell(s).")
        else:
            return(hg_inv, sg_inv)
            break

def take_health(action, hp_inv, hp_i, inventory):
        if "y" in action:
            hp_index = index_inventory(inventory, "Health")
            inventory.pop(hp_index)
            inventory.append("Healthpack (30): {}".format(hp_inv + hp_i))
            print("You take the healthpack(s).")
            print("You now have {} healthpack(s).".format(hp_inv + hp_i))
            return hp_inv + hp_i
        else:
            exit("error in take_health")

def add_weapon(weapon):
    inventory.append(weapon)

def weapon_swap(inventory, swap_to, holding):
    inventory.sort()
    if swap_to == "Knife":
        for n in inventory:
            if "Knife" in n:
                swapping = inventory.index(swap_to)
                wield_now = inventory.pop(swapping)
                inventory.append(holding)
                return wield_now

    elif swap_to == "Handgun":
        for n in inventory:
            if "Handgun" in n:
                swapping = inventory.index(swap_to)
                wield_now = inventory.pop(swapping)
                inventory.append(holding)
                return wield_now

    elif swap_to == "Shotgun":
        for n in inventory:
            if "Shotgun" in n:
                swapping = inventory.index(swap_to)
                wield_now = inventory.pop(swapping)
                inventory.append(holding)
                return wield_now

    print(inventory)
