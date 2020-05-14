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
                            algorithm.check = True 
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
        self.minimax( 1 , True , 0)
        print self.bestmove_val , self.bestmove_pos ,self.bestmove_des
        self.mov(self.bestmove_val , self.bestmove_pos ,self.bestmove_des)
        #for a in self.get_possible_moves():
        #    print a.value
        #    print a.get_children()

    def move(self):
        self.e.set_score()
        print '--------------'
        eval = self.e.get_board()
        #for ev in eval:
         #   print ev 
        #self.random_move()  #i will add new func to move piece with AI
        self.AI()
        #print self.minimax(1 ,self.get_possible_moves() , True) 

    def mov(self , value , position ,dest_position ):
        x , y = position
        dx , dy = dest_position
        Board.board[dy][dx] = value
        Board.board[x][y] = 0 
        


    def minimax(self , depth , ismaxing , i):
        possible_moves = self.get_possible_moves()      
        temp_board = []

        for x in range (0 , 8):
            temp_board.append([])
            for y in range (0 , 8):
                temp_board[x].append(y) 

        for x in range (0 , 8):
            for y in range (0 , 8):
                temp_board[x][y] = Board.board[x][y]
        for tem in temp_board:
            print tem 
        print 'i : ' , i
        if (depth == 0):
            e = Evaluation() 
            print 'score : ' ,e.get_score()
            return e.get_score()
        for pieces in possible_moves:

            print pieces.value
            if (ismaxing):
                bestmove = -99999 
                for possible_move in pieces.get_children():
                    print possible_move , 'end'
                    self.mov(pieces.value ,pieces.get_position() , possible_move )                    
                    bm = self.minimax(depth -1 , False ,i+10) 
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
                    bm = self.minimax( depth -1 , True ,i+5)
                    if bestmove > bm:
                        bestmove = bm                    
                    for x in range (0 , 8):
                        for y in range (0 , 8):
                            Board.board[x][y] = temp_board[x][y] 
                
            print '----------------end pieces ---------------------'
        
            for x in range (0 , 8):
                for y in range (0 , 8):
                    Board.board[x][y] = temp_board[x][y]

        return bestmove

