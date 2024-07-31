import pygame
from pygame.sprite import  Sprite
class bullet(Sprite):

    def __init__(self,screen,shipRect,bullet_width=3, bullet_height=15,bullet_color=(5,5,255),bullet_speed_factor=1):
        super().__init__()
        self.screen=screen
        self.ShipRect = shipRect
        self.color = bullet_color
        self.speed = bullet_speed_factor
        self.rect = pygame.Rect(0,0,bullet_width, bullet_height)
        self.rect.centerx=shipRect.centerx
        self.rect.top=shipRect.top
        self.y=float(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        self.y-=self.speed
        self.rect.y=self.y






