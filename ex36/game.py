from rooms import entrance, room2, room3, room4
from fight import cont
player_hp = 100
points = 0
hg_ammo_left = 5
sg_ammo_left = 2
holding = "Boxing Gloves"

tier = 1

hg_inv = 1
sg_inv = 4
hp_inv = 1

ammo_inv = hg_inv, sg_inv, hp_inv

inventory = ["Handgun mag(s): 1", "Shotgun shell(s): 6", "Healthpack(s) (30): 1",
"Knife", "Handgun", "Shotgun"]

args = [player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv, tier, inventory]

entrance(args)

player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv, tier, inventory = args

def fight2(args):
    tier = 2
    cleared2 = False
    fight, cleared2 = room3(args, cleared2)
    player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv = fight
    room3(args, cleared2)

tier = "boss"
cleared3 = False
fight = (room4(args, cleared3))
player_hp, points, hg_ammo_left, sg_ammo_left, holding, ammo_inv = fight

print(f"""
Summary:
Player hp: {player_hp}
Weapon: {holding}
Points: {points}
Handgun ammo: {hg_ammo_left}
Shotgun ammo: {sg_ammo_left}
Inventory: {inventory}
""")
