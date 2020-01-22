from random import randint
from sys import exit
from weapon import rng, fight_swap, using_ammo, reload

def cont():
    print("[Continue]")
    input('> ')

def monster(player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv, tier, inv):
    hg_inv, sg_inv, hp_inv = ammo_inv
    inventory = inv
    player_strike = 1
    hit = 10
    boss = False
    if tier == 1:
        hp = 50
        dmg = 5
        points = randint(80, 100)
        hit, player_strike = rng(holding)
        print("There is a small monster inside the room.")
        print("Health: 50 -- Damage: 5")
        print("-" * 12)
    elif tier == 2:
        hp = 100
        dmg = 10
        points = randint(120, 150)
        hit, player_strike = rng(holding)
        print("There is a large monster inside the chamber.")
        print("Health: 100 -- Damage: 10")
        print("-" * 12)
    elif tier == 3:
        hp = 150
        dmg = 20
        points = randint(200, 300)
        hit, player_strike = rng(holding)
        print("Inside the chamber you find a Gatekeeper.")
        print("Health: 150 -- Damage: 20")
        print("-" * 12)
    else:
        hp = 500
        dmg = 30
        fire = 50
        points = 1000
        hit, player_strike = rng(holding)
        print("You encounter the end boss.")
        print("Health: 500 -- Damage: 30")
        print("His stone-skin reduces your damage by half.")
        print("-" * 12)
        boss = True

    cont()
    print("A fight ensues.")
    print("-" * 12)
    print(f"Weapon: {holding}, Health: {player_hp}")
    while hp > 0:
        print("[Continue] [Use Healthpack] [Swap Weapon] [Reload]")
        action = input('> ')
        reloadable = False
        while True:
            if 'pack' in action and hp_inv > 0:
                player_hp += 30
                print("You use a Healthpack and regain some health.")
                mechanism = reload("Pack", inventory, hg_inv, sg_inv, hp_inv)
                hp_inv = mechanism
                print("After use:", hp_inv)
                print("Player:", player_hp)
                print("-" * 12)
                cont()
                break
            elif 'pack' in action and hp_inv <= 0:
                print("You're out of Healthpacks.")
                cont()
                break
            elif 'swap' in action:
                temp = fight_swap(action, inventory, holding)
                holding = temp
                print(f"You equip your {holding}.")
                print("-" * 12)
                cont()
                break
            elif 'reload' in action and (((holding == "Handgun" and hg_inv > 0) or (holding == "Shotgun" and sg_inv > 0)) and not (holding == "Boxing Gloves" or holding == "Knife")):
                rel_ammo = 0
                print(f"Reloading: passing {holding}, hg: {hg_inv}, sg: {sg_inv} and hp: {hp_inv} through")
                mechanism = reload(holding, inventory, hg_inv, sg_inv, hp_inv)
                print(f"Reloaded: {mechanism}")
                rel_ammo, hg_inv, sg_inv = mechanism
                reloadable = True
                cont()
                break
            elif 'reload' in action and ((holding == "Handgun" and hg_inv <= 0) or (holding == "Shotgun" and sg_inv <= 0)):
                print(f"You're out of {holding} ammo.")
                cont()
                break
            else:
                break

        if holding == "Handgun" and reloadable == True:
            hg_ammo_left += rel_ammo
        elif holding == "Shotgun" and reloadable == True:
            sg_ammo_left += rel_ammo

        print("The monster lashes out..")

        strike = randint(0,1)

        if strike == 1:
            player_hp -= dmg
            print(f"The monster hits for {dmg} damage.")
        else:
            print("The monster misses!")

        print("[Attack]")
        input('> ')

        hit, player_strike = rng(holding)

        if (holding == "Handgun" and hg_ammo_left > 0) or (holding == "Shotgun" and sg_ammo_left > 0):
            fire = using_ammo(holding, hg_ammo_left, sg_ammo_left)
            hg_ammo_left, sg_ammo_left = fire
        elif (holding == "Handgun" and hg_ammo_left <= 0) or (holding == "Shotgun" and sg_ammo_left <= 0):
            player_strike == 1
            print("You try to fire your weapon, but you're out of ammo.")

        if player_strike == 0 and boss == True:
            hit = hit / 2
            hp -= hit
            print(f"You hit for {hit} damage.")
            print(f"Monster: {hp} <===> Player: {player_hp}")
            print("-" * 12)
        elif player_strike == 0 and not boss == True:
            hp -= hit
            print(f"You hit for {hit} damage.")
            print(f"Monster: {hp} <===> Player: {player_hp}")
            print("-" * 12)
        else:
            print("You try to hit it, but miss.")
            print(f"Monster: {hp} <===> Player: {player_hp}")
            print("-" * 12)


        if hp <= 0 and boss == True:
            print("You managed to kill the final boss!")
            cont()
            print(f"You gain {points} points.")
            print(f"You have {player_hp} health left.")
            ammo_inv = hg_inv, sg_inv, hp_inv
            return player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv
            break
        elif hp <= 0:
            print("The monster dies.")
            cont()
            print(f"You gain {points} points.")
            print(f"You have {player_hp} health left.")
            ammo_inv = hg_inv, sg_inv, hp_inv
            return player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv
            break

        if hg_ammo_left <= 0 and not sg_ammo_left <=0 and holding == "Handgun":
            print("You ran out of handgun ammo mate.")

        elif sg_ammo_left <= 0 and not hg_ammo_left <= 0 and holding == "Shotgun":
            print("You ran out of shotgun shells mate.")

        elif hg_ammo_left <= 0 and sg_ammo_left <= 0 and (holding == "Handgun" or holding == "Shotgun"):
            print("Both weapons out of ammo, running into a problem here...")

        if player_hp <= 0:
            exit("You die in excruciating pain.")
