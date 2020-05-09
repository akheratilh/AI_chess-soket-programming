from pieces import *
from board import Board
from anime import Anime 
from algorithm.move import Move , Thread
from contentText.tim import Tim 
from algorithm.player import Player

class GUI():
    def __init__(self):   
        global game_exit  
        drag = False
        chess_board = Board()

        chess_board.set_template('wood')
        m = Move()
        m.start()

        t = Tim()
        t.start()

        animation = Anime(chess_board)
        animation.start() 
        flag_move = 0 

        history = [] 
        possible_move = []      

        p1 = Player('white')
        p2 = Player('black')
        p1.move()
        p1.next_round()
        p2.next_round()
        while not game_exit:  
            chess_board.draw_board()
            t.show()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        chess_board.reset_board() 
                    elif event.key == pygame.K_q:
                        game_exit = True
                    elif event.key == pygame.K_z:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    animation.set_type()
                    if animation.type and p2.can_move() and p2.team[0] == animation.type[0] :
                        animation.drag_init()  
                        m.set_value(str(animation.type) ,animation.position )
                        possible_move = m.possible_moves(chess_board , animation)
                        animation.highlight_possible_move(possible_move)   
                        drag = True 
                elif event.type == pygame.MOUSEBUTTONUP: 
                    animation.drag_done(possible_move )   #TO DO : check if is it possible to move 
                    possible_move = []
                    if drag :
                        p1.next_round()
                        p2.next_round()
                    drag = False
            if drag:
                animation.highlight_possible_move(possible_move)
                     
            if not drag:
                animation.highlight(pygame.mouse.get_pos())
            
            chess_board.draw_piece()

            if drag:                                        # i check drag two time beacuse if i merge them then in the result the draged piece show under enemy solder
                animation.drag(pygame.mouse.get_pos())              # in the other hand if i create piece first the highlight will stay on piece so player cant see piece
                   
            if (p1.can_move()):
                p1.move()
                p1.next_round()
                p2.next_round()
            

            #animation.king_check([3 , 0])  use this func as shown kings 

            pygame.display.flip()
            clock.tick(40)     
        pygame.quit()