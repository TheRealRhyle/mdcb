import unittest
import sys

sys.path.append('f:\\Google Drive\\May 2020\\rhylebot v3')
sys.path.append('f:\\Google Drive\\May 2020\\rhylebot v3\chatgame')

from chatgame import characterController as cc
from chatgame import monsterMaker as mm


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

class MonsterTest(unittest.TestCase):
    def test_monster_creation(self):
        test_monster = mm.Monster("Slavering Ghoul")
        self.assertEqual(test_monster.name, "Slavering Ghoul")
        self.assertEqual(test_monster.maxHp, 100)
        self.assertEqual(test_monster.currentHp, 100)
        self.assertEqual(test_monster.armorHead, 0)
        self.assertEqual(test_monster.armorTorso, 0)
        self.assertEqual(test_monster.armorArms, 0)
        self.assertEqual(test_monster.armorLegs, 0)

if __name__ == '__main__':
    unittest.main()