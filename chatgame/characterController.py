import random
class Fighter():
    def __init__(self, name):
        self.name=name
        self.maxHp=100
        self.currentHp=100
        self.armorHead=0
        self.armorTorso=0
        self.armorArms=0
        self.armorLegs=0
        self.inventory=[]
        self.damage = 1
        self.mainhand=''
        self.offhand=''
        self.isAlive=True
        self.experience = 0
        self.purse = 0
        self.inventory.append(random.choice(["Pocket Lint", "A frayed knot", "Thoughts and Prayers", "Hopes and Dreams", "POCKET SAND!"]))

    def take_damage(self, amount):
        self.currentHp -= amount
        if self.currentHp <= 0:
            self.currentHp = 0
            self.isAlive = False

    def heal_damage(self, amount):

        currentHP = self.currentHp
        if (currentHP + amount) > self.maxHp:
            self.currentHp = self.maxHp
        else:
            self.currentHp += amount

    def equip_armor(self, slot, points):
        match slot.lower():
            case 'head':
                self.armorHead += points
            case 'torso':
                self.armorTorso += points
            case 'arms':
                self.armorArms += points
            case 'legs':
                self.armorLegs += points
            case 'all':
                self.armorHead += points
                self.armorTorso += points
                self.armorArms += points
                self.armorLegs += points

    def remove_armor(self, slot, points):
        match slot.lower():
            case 'head':
                self.armorHead -= points
            case 'torso':
                self.armorTorso -= points
            case 'arms':
                self.armorArms -= points
            case 'legs':
                self.armorLegs -= points
            case 'all':
                if self.armorHead - points >= 0:
                    self.armorHead -= points
                
                if self.armorTorso - points >= 0:
                    self.armorTorso -= points
                
                if self.armorArms - points >= 0:
                    self.armorArms -= points
                
                if self.armorLegs - points >= 0:
                    self.armorLegs -= points

    def equip_weapon(self, name, wtype, damage):
        self.weapon = [name, wtype, damage]

    def remove_weapon(self, name):
        if len(self.weapon) and self.weapon[0] == name:
            self.weapon = []
        else:
            print("Not wielding that weapon")
            
    def myInventory(self):
        pass

if __name__=="__main__":
    p1 = Fighter("Rhyle")
    print(p1.__dict__)