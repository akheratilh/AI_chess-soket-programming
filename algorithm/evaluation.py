from Graphic.board import Board
#king 1000
#queen 100
#rook 40
#knight 20
#bishop 30
#pawn 10

class Evaluation(Board):
    board = [[0,-10,-10,-10,-10,-10,-10,0],
            [-10,-10,-20,-30,-30,-20,-10,-10],
            [-20,-10,-20,-10,-10,-20,-10,-20],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [20,10,20,10,10,20,10,20],
            [10,10,20,30,30,20,10,10],
            [0,10,10,10,10,10,10,0]
            ]    
    def __init__(self):
        self.temp = Evaluation.board

    def get_board(self):
        return self.temp
    
    def set_score(self):
        value = 0   
        self.temp = Evaluation.board
        for x in range (0 , 8):
            for y in range (0 , 8):
                self.temp[x][y] = 0
        for x in range (0 , 8):
            for y in range (0 , 8):
                if super(Evaluation , self).board[x][y] != 0:
                    pieces = super(Evaluation , self).board[x][y]
                    if(pieces[2:] == 'pawn'):
                        value = 10
                    elif(pieces[2:] == 'knight'):
                        value = 20                    
                    elif(pieces[2:] == 'bishop'):
                        value = 30
                    elif(pieces[2:] == 'rook'):
                        value = 40
                    elif(pieces[2:] == 'queen'):
                        value = 100
                    elif(pieces[2:] == 'king'):
                        value = 1000    
                                                        
                    if pieces[0] == 'w':
                        value *= -1
                        
                    self.temp[x][y] += value
    def get_score(self):
        value = 0
        for x in range(0,8):
            for y in range (0 , 8):
                value += self.temp[x][y]
        return value


# THIS CLASS DOES NOT COMPLITE YET