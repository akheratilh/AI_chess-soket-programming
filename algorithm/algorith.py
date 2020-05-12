from Graphic.board import Board
from algorithm.move import Move
import random
from algorithm.tree import tree
from algorithm.evaluation import Evaluation 
import math

class algorithm(Board):
    check = False
    king_X_pos ,king_Y_pos = 0 , 0
    def __init__(self):
        self.e = Evaluation()


    def get_possible_moves(self):
        m = Move()
        possible_tree = []
        for x in range(0 , 8):
            for y in range(0 , 8):
                value = super(algorithm , self).board[x][y] 
                
                if value != 0 and value[0] != 'b': 
                    m.set_value(value , [x ,y])  
                    t = tree(value , [x ,y])
                    for possible_move in m.possible_moves():
                        t.append(possible_move)
                        if super(algorithm , self).board[possible_move[1]][possible_move[0]] == 'b_king':
                            algorithm.check = True 
                            algorithm.king_X_pos ,algorithm.king_Y_pos  = possible_move[0] ,possible_move[1]
                    possible_tree.append(t)

        return possible_tree
        
    def random_move(self):
        possible_moves = self.get_possible_moves()
        x = random.randint(0 , len(possible_moves) -1 )
        child = possible_moves[x].get_children()
        
        while(len(child) == 0):
            x = random.randint(0 , len(possible_moves) - 1) 
            child = possible_moves[x].get_children()
        pos = child[0] 
        
        super(algorithm , self).board[pos[1]][pos[0]] = possible_moves[x].value 
        x , y = possible_moves[x].get_position() 
        super(algorithm , self).board[x][y] = 0 

    def move(self):
        self.e.set_score()
        print '--------------'
        eval = self.e.get_board()
        for ev in eval:
            print ev 
        self.random_move()  #i will add new func to move piece with AI
        #print self.minimax(1 ,self.get_possible_moves() , True) 

    def mov(self , value , position ,dest_position ):
        x , y = position
        dx , dy = dest_position
        super(algorithm , self).board[dy][dx] = value
        super(algorithm , self).board[y][x] = 0 
        


    def minimax(self , depth , node , ismaxing):
        m = Move()
        x , y = node    
        value = super(algorithm , self).board[x][y]

        if (depth == 0):
            return evaluation.board[node[0]][node[1]]
            
        if (ismaxing):
            bestmove = -99999
            m.set_value(value , [x ,y])  
            for posible_move in m.possible_moves():
                bm = self.minimax(self , depth -1 , posible_move , False)
                bestmove = math.max(bestmove , bm)
            return bestmove

        elif(not ismaxing):
            bestmove = 99999
            m.set_value(value , [x , y]) 
            for posible_move in m.possible_moves():
                bm = self.minimax(self , depth -1 , posible_move , True)
                bestmove = math.min(bestmove , bm)
            return bestmove



