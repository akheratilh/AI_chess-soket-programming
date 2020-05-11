from Graphic.board import Board
from algorithm.move import Move
import random
class tree():
    def __init__(self , value , position):
        self.children = []
        self.value = value
        self.X_position , self.Y_position = position
    
    def append(self , child):
        self.children.append(child)
    
    def get_children(self):
        return self.children

    def get_position(self):
        return [self.X_position , self.Y_position]


class algorithm(Board):
    def __init__(self):
        pass

    def get_possible_moves(self):
        m = Move()
        possible_tree = []
        for x in range(0 , 8):
            for y in range(0 , 8):
                value = super(algorithm , self).board[x][y] 
                if value != 0 and value[0] != 'b': 
                    m.set_value(value , [x ,y]) 
                    m.possible_moves()
                    t = tree(value , [x ,y])
                    for possible_move in m.possible_moves():
                        t.append(possible_move)
                    possible_tree.append(t)

        return possible_tree
        
    def random_move(self):
        possible_moves = self.get_possible_moves()
        x = random.randint(0 , len(possible_moves) -1 )
        child = possible_moves[x].get_children()
        
        while(len(child) == 0):
            x = random.randint(0 , len(possible_moves) - 1)
            print len(possible_moves)
            child = possible_moves[x].get_children()
        pos = child[0]
        print possible_moves[x].value 
        print pos
        
        super(algorithm , self).board[pos[1]][pos[0]] = possible_moves[x].value 
        x , y = possible_moves[x].get_position()
        print x 
        print y 
        super(algorithm , self).board[x][y] = 0 

    def move(self):
        self.random_move()


