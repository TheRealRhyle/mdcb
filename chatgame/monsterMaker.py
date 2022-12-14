import random
import gc
import pickle
from characterController import Fighter

class Monster(Fighter):
    def __init__(self):
        with open('chatgame\monster.txt', 'r') as m:
            monsters = m.read().strip('\n').split(', ')
        
        super().__init__(random.choice(monsters))

    def saveStatus(self):
        with open(self.name, 'wbpsa') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        # pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        # f.close()

    def loadStatus(self):
        pass

