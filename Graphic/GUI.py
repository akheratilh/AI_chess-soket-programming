from pieces import *
from board import Board
from anime import Anime
from sound.sound import Sound
from algorithm.move import Move , Thread
import threading
from algorithm.algorith import algorithm
from contentText.tim import Tim 
from algorithm.player import Player 
import sys
from sock.sock import sock

class GUI():
    def __init__(self):   
        global game_exit  
        global mute
        team1 = 'black'
        team2 = 'white'
        drag = False

        print len(sys.argv)
        isSockOn = 'AI'
        if len(sys.argv) > 2 :
            isSockOn = sys.argv[2] 
        if len(sys.argv) > 1:
            team2 = sys.argv[1]
            if sys.argv[1] == 'black':
                team1 = 'white'
        chess_board = Board(team2)

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

        chess_board.draw_board()
        
        chess_board.draw_piece()
 

        p1 = Player(team1)
        p2 = Player(team2) 
        p1.set_type(isSockOn) 

        if (team2 == 'black'):
            Move.player_team = 'w'
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
                    if event.key == pygame.K_m:
                        if Sound.mute == False:
                            Sound.mute = True
                        else :
                            Sound.mute = False
                    if event.key == pygame.K_r:
                        chess_board.reset_board(team1) 
                        history = []
                        t.reset()
                        p1.next_round()
                        p2.next_round() 
                        algorithm.check = False
                    elif event.key == pygame.K_q:
                        game_exit = True
                    elif event.key == pygame.K_z and len(history) > 0:
                        pos = history.pop()         #TO DO : this part use to reverse move (undo move)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    possible_move = []
                    animation.set_type()
                    if animation.type and p2.can_move() and p2.team[0] == animation.type[0] :
                        animation.drag_init()  
                        history.append(animation.position)
                        m.set_value(str(animation.type) ,animation.position )
                        if not algorithm.check:
                            possible_move = m.possible_moves()
                        if animation.type == 'b_king':
                            possible_move = m.possible_moves()

                        animation.type = m.name
                        animation.highlight_possible_move(possible_move)   
                        drag = True 
                elif event.type == pygame.MOUSEBUTTONUP: 
                    move_done = animation.drag_done(possible_move)   # check if is it possible to move 
                    if not move_done and len(history) > 0:
                        history.pop()
                    
                    possible_move = []
                    if move_done :
                        algorithm.check = False
                        p1.next_round()
                        p2.next_round()
                        if isSockOn == "SOCKET":
                            so = sock() 
                            so.send()   
                            so.close()    

                    drag = False

            if drag:
                animation.highlight_possible_move(possible_move)
                     
            if not drag:
                animation.highlight(pygame.mouse.get_pos())
                
            if algorithm.check:
                pygame.draw.rect(screen, RED, (100 * algorithm.king_X_pos, 100 * algorithm.king_Y_pos, 100, 100), 5)
             
            chess_board.draw_piece()

            if drag:                                        # i check drag two time beacuse if i merge them then in the result the draged piece show under enemy solder
                animation.drag(pygame.mouse.get_pos())              # in the other hand if i create piece first the highlight will stay on piece so player cant see piece
                   
            if (p1.can_move()):
                threading.Thread(target=p1.move).start()
                #p1.move()
                p1.next_round()
                p2.next_round()       

            #animation.king_check([3 , 0])  use this func as shown kings 

            pygame.display.flip()
            clock.tick(40)     
        pygame.quit()