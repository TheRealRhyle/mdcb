import pickle

class Weapon():
    def __init__(self):
        # weaponType = melee or ranged
        self.weaponType = ''
        # Basic, Calvary, Fencing....
        self.weaponClass = ''
        self.name = ''
        self.price = ''
        self.enc = ''
        self.availability = ''
        self.reach = ''
        self.damage = ''
        self.qualititesAndFlaws = ''
    
    def createWeapon(self):
        pass
    
    def weapon_out(self):
        x = f'{self.name} [{self.weaponClass}/{self.weaponType}]\n'
        x = x + f'{self.damage} damage. Range: {self.reach} Qualities: {self.qualititesAndFlaws}\n'
        x = x + f''
        return x
        
        

if __name__ == "__main__":
    w1 = Weapon()
    w1.weaponType = "melee"
    w1.weaponClass = "basic"
    w1.name = 'Hand Weapon'
    w1.price = 1
    w1.enc = 1
    w1.availability = 'Common'
    w1.reach = 'Average'
    w1.damage = '+SB+4'
    w1.qualititesAndFlaws = '--'
    
    with open('outtest', 'wb') as f:
        pickle.dump(w1, f)
    
    print(w1.weapon_out())
        