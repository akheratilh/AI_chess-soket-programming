from threading import Thread
from config import *
from time import sleep

class Tim(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
        self.min = 0
        self.sec = 0
        self.text = self.font.render(str(self.min)+':'+str(self.sec), True, BLACK)  

    def run(self): 
        while True:
            sleep(1)
            self.counter()

    def show(self):
        screen.blit(self.text, (width - 250 ,height / 2))
 
    def counter(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
        self.text = self.font.render(str(self.min)+':'+str(self.sec), True, BLACK)  