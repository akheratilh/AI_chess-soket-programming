from pieces import *
from sound.sound import Sound
from threading import Thread

class Anime(): 
    def __init__(self , Board):
        self.S = Sound('sound/move.mp3')
        self.boardClass = Board
        self.position = None
        self.type = None
        self.next_position = None
        
    def move(self ,speed):
        if speed ==0 :
            self.boardClass.board[0][0] =0
        p = Pieces()
        p.set_model(self.type) 
        p.draw_model([1 * speed ,1 * speed])
    
    def set_pos(self , position):
        self.position = position
    
    def set_pos_digit(self , position):
        x , y = position
        x = int(round(x/100))
        y = int(round(y/100))
        self.position = [x , y] 
    
    def get_type(self): 
        self.type = self.boardClass.board[self.position[0]][self.position[1]]
        self.boardClass.board[self.position[0]][self.position[1]] = 0

    def drag_init(self):
        x , y = pygame.mouse.get_pos()
        self.set_pos_digit([y , x])
        self.get_type() 

    def drag(self , position):
        if (self.type):
            p = Pieces()
            p.set_model(self.type)
            p.draw_model([position[0] -50, position[1] -50 ])

    def drag_done(self , possible_moves):
        x , y = pygame.mouse.get_pos()
        x = int(round(x/100))
        y = int(round(y/100))        
        for possible_move in possible_moves: 
            if x == possible_move[0] and y == possible_move[1]: 
                self.S.play()
                self.boardClass.board[y][x] = self.type 
                return True
        self.drag_succed()
        return False
    
    def drag_succed(self): 
        self.boardClass.board[self.position[0]][self.position[1]] = self.type

    def highlight(self , position):
        x , y = position
        x = int(round(x/100))
        y = int(round(y/100))
        pygame.draw.rect(screen, GREEN, (100 * x, 100 * y, 100, 100), 5)
        
    def highlight_possible_move(self , possible_move):
        for move in possible_move:
            pygame.draw.rect(screen, BLUE, (100 * move[0], 100 * move[1], 100 , 100))
