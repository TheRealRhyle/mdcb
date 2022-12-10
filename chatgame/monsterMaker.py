import random
import gc
import pickle
from characterController import Fighter

class Monster(Fighter):
    def __init__(self, name):
        super().__init__(name)

    def saveStatus(self):
        with open(self.name, 'wbpsa') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        # pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        # f.close()

    def loadStatus(self):
        pass

