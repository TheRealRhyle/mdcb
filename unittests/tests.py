import unittest
import sys

sys.path.append('f:\\Google Drive\\May 2020\\rhylebot v3')
sys.path.append('f:\\Google Drive\\May 2020\\rhylebot v3\chatgame')

from chatgame import characterController as cc
from chatgame import monsterMaker as mm
from chatgame import systemManager as sm

class FighterTest(unittest.TestCase):
    def test_Fighter_creation(self):
        test_Fighter = cc.Fighter("Rhyle")
        self.assertEqual(test_Fighter.name, "Rhyle")
        self.assertEqual(test_Fighter.maxHp, 100)
        self.assertEqual(test_Fighter.currentHp, 100)
        self.assertEqual(test_Fighter.armorHead, 0)
        self.assertEqual(test_Fighter.armorTorso, 0)
        self.assertEqual(test_Fighter.armorArms, 0)
        self.assertEqual(test_Fighter.armorLegs, 0)
    
    def test_Fighter_take_damage(self):
        test_Fighter = cc.Fighter("Rhyle")
        test_Fighter.take_damage(10)
        self.assertEqual(test_Fighter.currentHp, 90)
    
    def test_Fighter_heal_damage(self):
        test_Fighter = cc.Fighter("Rhyle")
        test_Fighter.take_damage(10)
        test_Fighter.heal_damage(10)
        self.assertEqual(test_Fighter.currentHp, 100)
    
    def test_Fighter_equip_armor(self):
        test_Fighter = cc.Fighter("Rhyle")
        test_Fighter.equip_armor('head', points=1)
        self.assertEqual(test_Fighter.armorHead, 1)
        test_Fighter.equip_armor(slot='torso', points=1)
        self.assertEqual(test_Fighter.armorTorso, 1)
        test_Fighter.equip_armor(slot='ARMS', points=1)
        self.assertEqual(test_Fighter.armorArms, 1)
        test_Fighter.equip_armor(slot='LEGS', points=1)
        self.assertEqual(test_Fighter.armorLegs, 1)
        test_Fighter.equip_armor(slot='aLl', points=1)
        self.assertEqual(test_Fighter.armorLegs, 2)
        self.assertEqual(test_Fighter.armorHead, 2)
        self.assertEqual(test_Fighter.armorTorso, 2)
        self.assertEqual(test_Fighter.armorArms, 2)
    
    def test_Fighter_remove_armor(self):
        test_Fighter = cc.Fighter("Rhyle")
        test_Fighter.equip_armor('all', 1)
        test_Fighter.remove_armor('head', points=1)
        self.assertEqual(test_Fighter.armorHead, 0)
        test_Fighter.remove_armor(slot='torso', points=1)
        self.assertEqual(test_Fighter.armorTorso, 0)
        test_Fighter.remove_armor(slot='ARMS', points=1)
        self.assertEqual(test_Fighter.armorArms, 0)
        test_Fighter.remove_armor(slot='LEGS', points=1)
        self.assertEqual(test_Fighter.armorLegs, 0)
        test_Fighter.remove_armor(slot='aLl', points=1)
        self.assertEqual(test_Fighter.armorLegs, 0)
        self.assertEqual(test_Fighter.armorHead, 0)
        self.assertEqual(test_Fighter.armorTorso, 0)
        self.assertEqual(test_Fighter.armorArms, 0)

    def test_Fighter_equip_weapon(self):
        test_Fighter = cc.Fighter("Rhyle")
        test_Fighter.equip_weapon(name="Great Axe", wtype='melee/slashing', damage=5)
        self.assertEqual(test_Fighter.weapon, ["Great Axe", "melee/slashing", 5])
    
    def test_Fighter_remove_weapon(self):
        test_Fighter = cc.Fighter("Rhyle")
        test_Fighter.equip_weapon(name="Great Axe", wtype='melee/slashing', damage=5)
        test_Fighter.remove_weapon("Great Axe")
        self.assertEqual(test_Fighter.weapon, [])
        
class MonsterTest(unittest.TestCase):
    def test_Monster_creation(self):
        test_monster = mm.Monster("Slavering Ghoul")
        self.assertEqual(test_monster.name, "Slavering Ghoul")
        self.assertEqual(test_monster.maxHp, 100)
        self.assertEqual(test_monster.currentHp, 100)
        self.assertEqual(test_monster.armorHead, 0)
        self.assertEqual(test_monster.armorTorso, 0)
        self.assertEqual(test_monster.armorArms, 0)
        self.assertEqual(test_monster.armorLegs, 0)
    def test_Monster_take_damage(self):
        test_monster = mm.Monster("Slavering Ghoul")
        test_monster.take_damage(10)
        self.assertEqual(test_monster.currentHp, 90)


if __name__ == '__main__':
    unittest.main()