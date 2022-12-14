import os
import random
import monsterMaker as mm
import characterController as cc
import shopManager as sm

def characterDisplay(p1):
    os.system('cls')
    disp = "="*15+"\n"
    disp = disp + f"Name: {p1.name}\n"
    disp = disp + f"HP: {p1.currentHp}/{p1.maxHp}\n"
    disp = disp + "="*15+"\n"
    print(disp)

if __name__ == "__main__":
    os.system('cls')
    cname = input("What is your name? ")
    p1 = cc.Fighter(cname)
    if p1.name == "rhyle":
        p1.damage=50
    prep = input(f"Welcome {p1.name}. Are you prepared for the journey before you? ")
    
    if prep.lower() == 'y' or prep.lower() == 'yes':
        prepared = True
    else:
        print("Sorry to see you go so soon.")
        prepared = False

while p1.isAlive:
    x= input(">")
    
    if x == "status":
        characterDisplay(p1)
    if x == "fnd m":
        newmonster = mm.Monster()
        print(f"You've found a {newmonster.name}")
    if x == "fm":
        newmonster.take_damage(p1.damage)
        print(newmonster.currentHp)
    if x == "loot" and newmonster.currentHp <=0:
        try:
            loot=random.choice(newmonster.inventory)
            newmonster.inventory.remove(loot)
            print(f"You reach into the monster and pull out {loot}")
            print(f'{loot} has been added to your inventory.')
            p1.inventory.append(loot)
        except:
            print("There is nothing left in the corpse.")
        
    if x== 'i' or x=='inv' or x=='inventory':
        print(f"You currently have:")
        for itm in p1.inventory:
            print(f'- {itm}')