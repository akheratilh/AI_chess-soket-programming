import pygame 
from threading import Thread

pygame.init()
width , height = 800 , 800
screen = pygame.display.set_mode((width, height + 200))
clock = pygame.time.Clock()
BLUE = (0,0,255) 
GREEN = (0,255,0) 
RED = (255,0,0) 
WHITE = (255,255,255)
BLACK = (0,0 ,0)
YELLOW = (255 ,255 , 0)
game_exit = False