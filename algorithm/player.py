import random
from algorithm.algorith import algorithm
from algorithm.move import Move
from sock.sock import sock

class Player(Move):
    def __init__(self , team ):
        self.team = team
        self.round = self.start_first() 
        self.type = 'AI'
        self.type_list = ['AI' , 'SOCKET']  # AI mean play with computer and -- socket -- use to play with other player -- online --
    def move(self):
        pass

    def set_type(self , type):
        self.type = type

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
            if (self.type == self.type_list[0]):
                x = random.randint(0 , 7)
                y = 1  
                al = algorithm()
                al.move()
                return [y , x]
            else:
                so = sock()
                so.start()
                so.receive() 
                so.close()

        
        
