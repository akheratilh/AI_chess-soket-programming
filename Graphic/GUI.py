from pieces import *
from board import Board
from move import Move , Thread
from anime import Anime 

class GUI():
    def __init__(self):    
        game_exit = False
        drag = False
        chess_board = Board()
         
        chess_board.set_template('wood')
        m = Move()
        m.start()

        animation = Anime(chess_board)
        animation.start() 
        flag_move = 0 

        history = [] 
        possible_move = []

        while not game_exit:  
            chess_board.draw_board()
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
                    animation.drag_init()  
                    m.set_value(str(animation.type) ,animation.position )
                    # argument are fake and used for test
                    possible_move = m.possible_moves(chess_board , animation)
                    animation.highlight_possible_move(possible_move)   
                    drag = True
                elif event.type == pygame.MOUSEBUTTONUP: 
                    animation.drag_done(possible_move )   #TO DO : check if is it possible to move 
                    possible_move = []
                    drag = False
            if drag:
                animation.highlight_possible_move(possible_move)
                     
            if not drag:
                animation.highlight(pygame.mouse.get_pos())
            
            chess_board.draw_piece()

            if drag:                                        # i check drag two time beacuse if i merge them then in the result the draged piece show under enemy solder
                animation.drag(pygame.mouse.get_pos())              # in the other hand if i create piece first the highlight will stay on piece so player cant see piece

            pygame.display.flip()
            clock.tick(60)     
        pygame.quit()