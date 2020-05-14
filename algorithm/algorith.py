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
        self.bestmove_pos = []
        self.bestmove_val = ''
        self.bestmove_des = []


    def get_possible_moves(self):
        m = Move()
        possible_tree = []
        for x in range(0 , 8):
            for y in range(0 , 8):
                value = super(algorithm , self).board[x][y] 
                
                if value != 0 and value[0] == Move.player_team: 
                    m.set_value(value , [x ,y])  
                    t = tree(value , [x ,y])
                    for possible_move in m.possible_moves():
                        t.append(possible_move)
                        if super(algorithm , self).board[possible_move[1]][possible_move[0]] ==  'b_king':
                            #algorithm.check = True 
                            algorithm.king_X_pos ,algorithm.king_Y_pos  = possible_move[0] ,possible_move[1]
                    if (len(t.get_children()) > 0): 
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
        
        self.mov(possible_moves[x].value  , possible_moves[x].get_position() ,pos)
    
    def AI(self):
        self.minimax( 2 , True) 
        self.mov(self.bestmove_val , self.bestmove_pos ,self.bestmove_des) 

    def move(self): 
        self.AI() 

    def mov(self , value , position ,dest_position ):
        x , y = position
        dx , dy = dest_position
        Board.board[dy][dx] = value
        Board.board[x][y] = 0 
        
    def minimax(self , depth , ismaxing ):
        possible_moves = self.get_possible_moves()      
        temp_board = []

        for x in range (0 , 8):
            temp_board.append([])
            for y in range (0 , 8):
                temp_board[x].append(y) 

        for x in range (0 , 8):
            for y in range (0 , 8):
                temp_board[x][y] = Board.board[x][y] 

        if (depth == 0):
            e = Evaluation() 
            e.set_score()
            print e.get_score()
            return e.get_score()

        for pieces in possible_moves: 
            if (ismaxing):
                bestmove = -99999 
                for possible_move in pieces.get_children():
                    self.mov(pieces.value ,pieces.get_position() , possible_move )                    
                    bm = self.minimax(depth -1 , False ) 
                    if bestmove < bm:
                        bestmove = bm
                        self.bestmove_val = pieces.value
                        self.bestmove_pos = pieces.get_position()
                        self.bestmove_des = possible_move
                    for x in range (0 , 8):
                        for y in range (0 , 8):
                            Board.board[x][y] = temp_board[x][y]                
                    
            elif(not ismaxing):
                bestmove = 99999 
                for possible_move in pieces.get_children():
                    self.mov(pieces.value ,pieces.get_position() , possible_move )  
                    bm = self.minimax( depth -1 , True )
                    if bestmove < bm:
                        bestmove = bm
                        self.bestmove_val = pieces.value
                        self.bestmove_pos = pieces.get_position()
                        self.bestmove_des = possible_move                 
                    for x in range (0 , 8):
                        for y in range (0 , 8):
                            Board.board[x][y] = temp_board[x][y]  
        
            for x in range (0 , 8):
                for y in range (0 , 8):
                    Board.board[x][y] = temp_board[x][y]

        return bestmove

