import pygame
import sys
class InitUpdate():

    def __init__(self,scale,Color):
        pygame.init()
        self.color=Color
        self.screen=pygame.display.set_mode(scale)
        pygame.display.set_caption('Aliens')
        self.CentreX=self.screen.get_rect().centerx
        self.Right= self.screen.get_rect().right
        self.Bottom=self.screen.get_rect().bottom
        self.screen.fill(Color)

    def UpdateWindown(self):
        self.screen.fill(self.color)

    def UpdateBul(self,bullets,alliens,scoreSet):
        bullets.update()
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        collosions = pygame.sprite.groupcollide(bullets,alliens, True, True)
        if collosions:
            scoreSet.UpdateScore(10)
        for bullet in bullets.copy():
            if bullet.rect.bottom<=110:
                bullets.remove(bullet)

    def UpdateAliens(self,aliens,rect):
        aliens.update(1)
        for Alliens in aliens.sprites():
            Alliens.Draw_Nlo()
            if  (Alliens.rect.y > rect.top) and (Alliens.rect.x > rect.centerx) :
                sys.exit()
    def UpdateAliensMot(self,aliens,rect):
        for Alliens in aliens.sprites():
            Alliens.Draw_Nlo()
            if  (Alliens.rect.y > rect.top) and (Alliens.rect.x > rect.centerx) :
                sys.exit()


    def LoadImage(self, path, scale=(250, 260)):
        image=pygame.image.load(path)
        image=pygame.transform.scale(image,scale)
        rect=image.get_rect()
        rect.centerx=self.CentreX
        rect.bottom=self.Bottom
        return image,rect

    def AddImage(self,image,rect):
        self.screen.blit(image,rect)











