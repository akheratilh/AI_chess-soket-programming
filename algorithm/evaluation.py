from algorithm.move import Move

class Evaluation():
    def __init__(self):
        self.board = []
        self.score_board = []
        self.move = Move()

    def get_board(self , Board):
        self.board = Board.board
    
    def set_score(self):
        for x in range (0 , 8):
            for y in range (0 , 8):
                self.move.set_value(self.board[x][y] , [ x , y ] )
                print self.move.is_white


# THIS CLASS DOES NOT COMPLITE YET