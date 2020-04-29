import pygame

class Sound():
    def __init__(self, path):
        self.path = path
        pygame.mixer.music.load(self.path)  
        
    def load(self):
        pygame.mixer.music.load(self.path)      
    
    def play(self):
        pygame.mixer.music.play(1)          
    