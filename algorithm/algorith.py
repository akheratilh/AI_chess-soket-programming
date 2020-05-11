from Graphic.board import Board
from algorithm.move import Move
import random
from algorithm.tree import tree

class algorithm(Board):
    check = False
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
                        if super(algorithm , self).board[possible_move[1]][possible_move[0]] == 'b_king':
                            algorithm.check = True
                            print 'check'
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
        
        super(algorithm , self).board[pos[1]][pos[0]] = possible_moves[x].value 
        x , y = possible_moves[x].get_position() 
        super(algorithm , self).board[x][y] = 0 

    def move(self):
        self.random_move()  #i will add new func to move piece with AI



