import pygame
from pygame.sprite import  Sprite
class ColShip(Sprite):
    def __init__(self):
        super().__init__()
        self.rect=0

    def SetRect(self,rect):
        self.rect=rect