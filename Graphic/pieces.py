from config import *

class Pieces():
    def __init__(self):
        self.path = ''
        self.img = None

    def set_model(self , name):
        self.path = 'pieces/' + name + '.png'
        load_img = pygame.image.load(self.path)
        scale = (100 , 100)     #width and height are 100px
        self.img = pygame.transform.scale(load_img , scale)
    
    def set_background(self , name):
        self.path = 'background/' + name + '.png'
        load_img = pygame.image.load(self.path)
        scale = (101 , 101)     #width and height are 100px
        self.img = pygame.transform.scale(load_img , scale)        

    def draw_model(self , position):    #position = (x_pos , y_pos)
        screen.blit(self.img , position)
