from threading import Thread

class Move(Thread):
    def __init__(self): 
        Thread.__init__(self)
        self.X_position ,self.Y_position = None , None
        self.name = None
        self.is_white = None
        self.type = None

    def run(self):
        pass

    def set_value(self , type_name , position):
        self.Y_position ,self.X_position = position
        self.name = type_name
        self.is_white = self.isWhite()  
        self.type = self.name[2:]
 
    def possible_moves(self , Board , Anime):
        all_model = ['pawn','rook','knight','bishop','queen','king']
        temp = []
        possible_move = []  # all moves which valid for pieces to do
        revers_move = -1       #black : -1
        if self.is_white:   
            revers_move *= -1   #white : +1

        if self.type == all_model[1] or self.type == all_model[4]:  #rook or queen moves : 
            for x in range (1 , self.X_position + 1):          #left 
                possible_move.append([self.X_position - x  , self.Y_position]) 
                if Board.board[self.Y_position][self.X_position - x] != 0:
                    break
            for x in range (1 , self.Y_position + 1):           #up
                possible_move.append([self.X_position      , self.Y_position - x]) 
                if Board.board[self.Y_position - x][self.X_position] != 0:
                    break
            for x in range (1 , 8 - self.X_position ):       #right
                possible_move.append([self.X_position + x  , self.Y_position]) 
                if Board.board[self.Y_position][self.X_position + x] != 0:
                    break                
            for x in range (1 , 8 - self.Y_position ):   #down
                possible_move.append([self.X_position      , self.Y_position + x])            
                if Board.board[self.Y_position + x][self.X_position] != 0:
                    break    

        if self.type == all_model[3] or self.type == all_model[4]: #bishop or queen moves 
            for x in range (1 , 8): 
                possible_move.append([self.X_position - x  , self.Y_position - x])  
                if self.Y_position - x < 0 or self.X_position - x < 0 or Board.board[self.Y_position - x][self.X_position - x] != 0:
                    break     
            for x in range (1 , 8): 
                possible_move.append([self.X_position - x  , self.Y_position + x])
                if self.Y_position + x > 7 or self.X_position - x < 0 or Board.board[self.Y_position + x][self.X_position - x] != 0:
                    break                  
            for x in range (1 , 8): 
                possible_move.append([self.X_position + x  , self.Y_position - x])
                if self.Y_position - x < 0 or self.X_position + x > 7 or Board.board[self.Y_position - x][self.X_position + x] != 0:
                    break                  
            for x in range (1 , 8): 
                possible_move.append([self.X_position + x  , self.Y_position + x]) 
                if self.Y_position + x > 7 or self.X_position + x > 7 or Board.board[self.Y_position + x][self.X_position + x] != 0:
                    break                  

        if self.type == all_model[0]: #pawn moves :
            if (self.Y_position == 0):  #exchange black pawn to queen at the end 
                self.name = 'b_queen' 
                Anime.type = 'b_queen'
                Board.board[self.Y_position][self.X_position] = 'b_queen' 
            if self.Y_position == 7 :  #exchange white pawn to queen at the end 
                self.name = 'w_queen' 
                Anime.type = 'w_queen'
                Board.board[self.Y_position][self.X_position] = 'w_queen'  
            
            value = Board.board[self.Y_position + revers_move][self.X_position + 1]
            
            if (value != 0 and value[0] != self.name[0] ):
                possible_move.append([ self.X_position + 1 , self.Y_position + revers_move]) 
            
            value = Board.board[self.Y_position + revers_move][self.X_position - 1]
            
            if (value != 0 and value[0] != self.name[0] ):
                possible_move.append([ self.X_position - 1 , self.Y_position + revers_move]) 

            if Board.board[self.Y_position + revers_move][self.X_position] == 0:
                if(self.Y_position == 6 and revers_move == -1 ): #check if pawn doesnt move yet 
                    possible_move.append([ self.X_position , self.Y_position + (2 * revers_move)]) 
                if(self.Y_position == 1 and revers_move == 1 ): #check if pawn doesnt move yet 
                    possible_move.append([ self.X_position , self.Y_position + (2 * revers_move)]) 
                possible_move.append([ self.X_position , self.Y_position + revers_move])    
            
        elif self.type == all_model[2]: #knight moves :
            possible_move.append([self.X_position + 1 , self.Y_position - 2])
            possible_move.append([self.X_position + 1 , self.Y_position + 2])
            possible_move.append([self.X_position - 1 , self.Y_position - 2])
            possible_move.append([self.X_position - 1 , self.Y_position + 2])
            possible_move.append([self.X_position + 2 , self.Y_position - 1])
            possible_move.append([self.X_position + 2 , self.Y_position + 1])
            possible_move.append([self.X_position - 2 , self.Y_position + 1])
            possible_move.append([self.X_position - 2 , self.Y_position - 1])

        elif self.type == all_model[5]:  #king moves :
            possible_move.append([self.X_position + 1 , self.Y_position + 1])
            possible_move.append([self.X_position + 1 , self.Y_position - 1])
            possible_move.append([self.X_position - 1 , self.Y_position + 1])
            possible_move.append([self.X_position - 1 , self.Y_position - 1])
            possible_move.append([self.X_position + 1 , self.Y_position])
            possible_move.append([self.X_position - 1 , self.Y_position])
            possible_move.append([self.X_position , self.Y_position - 1])
            possible_move.append([self.X_position , self.Y_position + 1]) 
         

        temp = []
        for possible in possible_move:
            if possible[0] < 8 and possible[0] >= 0 and possible[1] < 8 and possible[1] >= 0:
                team = Board.board[possible[1]][possible[0]]
                if team == 0 or team[0] != self.name[0]: 
                    temp.append(possible)
        
        possible_move = temp
        
        return possible_move

    def isWhite(self):
        if self.name[0] == 'w': 
            return True 
        return False

    def get_team(self):
        return self.is_white
