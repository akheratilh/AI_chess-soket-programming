import random

class Player():
    def __init__(self , team):
        self.team = team
        self.round = self.start_first()

    def move(self):
        pass

    def can_move(self):
        return self.round

    def next_round(self):
        if self.round:
            self.round = False
        else :
            self.round = True
     

    def start_first(self):
        if self.team[0] == 'w':
            return True
        return False
    
    def move(self):
        if self.round:
            x = random.randint(0 , 7)
            y = 1
            print 'hihiihih'
        
        