import pygame
from threading import Thread 

class Sound(Thread):
    mute = False

    def __init__(self, path):
        Thread.__init__(self)
        self.path = path
        
    def run(self):
        pygame.mixer.music.load(self.path)  

    def load(self):
        pygame.mixer.music.load(self.path)      

    def play(self): 
        if not Sound.mute:
            pygame.mixer.music.play(1)          
    