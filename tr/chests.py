from textwrap import dedent
import morale


def open():

    action = input('Chest # > ')
    if action == '2':
        print(
            dedent("""
            You open the chest to find a golden key inside of it.
            Quickly you take the key and head towards the big door.
            """)
             )
        return 'treasure_room'
    else:
        print(
            dedent("""
            You open a false chest, and air explodes out of it,
            knocking you over and blowing sand in your eyes.
            """)
             )
        morale.jones.air_blast()
        print(f"Your morale levels dropped to:{morale.jones.mo_lvl}")
