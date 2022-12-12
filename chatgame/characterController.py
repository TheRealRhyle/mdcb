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
        self.weapon=[]

    def take_damage(self, amount):
        self.currentHp -= amount

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