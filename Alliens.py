import pygame
from pygame.sprite import  Sprite

class allien(Sprite):

    def __init__(self,init,scale):
        super().__init__()
        self.init=init
        self.InfoNlo=init.LoadImage('B:\Рабочий СТОЛ\ggh.png',scale)
        self.InfoNlo[1].x=self.InfoNlo[1].width
        self.InfoNlo[1].y = self.InfoNlo[1].height
        self.rect=self.InfoNlo[1]
        self.x=float(self.InfoNlo[1].x)
        self.y=float(self.InfoNlo[1].y)


    def Draw_Nlo(self):

        self.init.AddImage(self.InfoNlo[0],self.InfoNlo[1])

    def update(self,speed):
        self.InfoNlo[1].x+= speed/2
        self.rect = self.InfoNlo[1]
        if self.InfoNlo[1].x>1200:

            self.InfoNlo[1].y += self.y
            self.InfoNlo[1].x=0
            self.rect = self.InfoNlo[1]




