import random, pickle, sys

class GameSystem():
    def __init__(self, name='System Undefined', dice='Undefined', publisher='Undefined', edition='Undefined'):
        if len(sys.argv)==0:
            self.name = ""
            self.dice = ""
            self.publisher = ""
            self.edition = ""
        else:
            self.name = name
            self.dice = dice
            self.publisher = publisher
            self.edition = edition
        
    def pick_system(self):
        pass
    
if __name__=="__main__":
    g1 = GameSystem()
    print(g1.__dict__)
