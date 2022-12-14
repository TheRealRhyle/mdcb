import random, math

class Armorsmith(): pass

class Weaponsmith():
    def __init__(self):
        with open('chatgame\\names.txt','r') as f:
            nms = f.readlines()
        self.name = random.choice(nms).title().strip('\n')
        self.race = 'Elf'
        self.markup = random.randint(1, 26)
        self.stock = []
        for i in range(5):
            self.stock.append(Weapons().randomWeapon())
        

class Weapons():      
    def __init__(self, **kwargs):
        self.name = f"{kwargs['adjective'] if 'adjective' in kwargs else ''} {kwargs['name'] if 'name' in kwargs else ''}".strip(" ")
        self.damage = kwargs['damage'] if 'damage' in kwargs else 'SB'

    def randomWeapon(self, **kwargs):
        with open("chatgame/adjectives.txt", 'r') as f:
            adj = f.read().strip("\n").split(", ")
        with open("chatgame/weapons.txt", 'r') as f:
            weapons = f.read().strip("\n").split(", ")
        
        adjChance = 25
        wLine = random.choice(weapons)
        weaponName = f"{wLine}".strip(' ').split(':')[0]
        if random.randint(1,101) < 25:
            weaponName = f"{random.choice(adj)} {weaponName}"
        
        self.name=weaponName
        self.price=int(wLine.split(": ")[-1])
        
        return self.name, self.price
        

class Apothecary(): pass

if __name__=="__main__":
    for x in range(1, 10):
        x+=1
        smith = Weaponsmith()
        print(f'{smith.name} {smith.race}, {smith.markup}%')
        for item, price in smith.stock:
            cost = math.ceil(price+(price*int(smith.markup)/100))
            print(f"{str(cost):>5}cn  {item:<15}".split(',')[0])
    
    # x=Weapons()
    # print(x.name, x.damage)
    # y=Weapons(name="Rapier")
    # print(y.name, y.damage)
    # z=Weapons(adjective= "Thirsty", name="Rapier")
    # print(z.name, z.damage)