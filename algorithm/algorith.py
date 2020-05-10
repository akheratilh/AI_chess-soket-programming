from Graphic.board import Board
from algorithm.move import Move

class algorithm(Board):
    def __init__(self):
        pass

    def random_move(self):
        m = Move()
        for x in range(0 , 8):
            for y in range(0 , 8):
                value = super(algorithm , self).board[x][y] 
                if value != 0 :
                    print value
                    print x
                    print y
                    m.set_value(value , [x ,y])
                    print m.possible_moves()

