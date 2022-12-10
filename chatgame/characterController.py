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

    def take_damage(self, amount):
        self.currentHp -= amount
