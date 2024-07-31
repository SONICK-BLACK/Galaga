import Update
import pygame
from ShipRect import  ColShip
from Bullet import bullet
from Alliens import allien
from pygame.sprite import Group
import Buttons
from Scores import score
import sys
class GameRun():
    def __init__(self, scale, color):
        self.scale=scale
        self.init=Update.InitUpdate(scale,color)
        self.InfoObject = self.init.LoadImage('B:\Рабочий СТОЛ\ship.png')
        self.init.AddImage(self.InfoObject[0],self.InfoObject[1])
        self.bullets = Group()
        self.alliens = Group()
        self.RectShip=ColShip()
        self.buttons=Buttons.buttonSet((0,255,0),(255,255,255),self.init.screen,'Play')
        self.Score = score((0,255,0),(255,255,255),self.init.screen,0)

    def initWindowGame(self):
        self.init.UpdateWindown()
        self.init.UpdateBul(self.bullets,self.alliens,self.Score)
        self.init.AddImage(self.InfoObject[0], self.InfoObject[1])
        self.init.UpdateAliens(self.alliens,self.InfoObject[1])
        self.Score.DrawScore()
        pygame.display.flip()

    def Fleet(self,shipHeight,width=50,height=65):

        space_x=self.scale[0]-width
        number_space=int(space_x/(2*width))
        number_row=self.GetHeightFleet(shipHeight)
        print(number_row)

        for numberRow in range(number_row):
            for number in range(number_space):
                allien_s=allien(self.init,(width,height))
                allien_s.x=allien_s.InfoNlo[1].width+2*allien_s.InfoNlo[1].width*number
                allien_s.InfoNlo[1].x=allien_s.x
                allien_s.InfoNlo[1].y=allien_s.InfoNlo[1].height+2*allien_s.InfoNlo[1].height*numberRow
                allien_s.y=height
                allien_s.Draw_Nlo()
                self.alliens.add(allien_s)
    def GetHeightFleet(self,shipHeight,height=65):
        space_y=self.scale[1]-shipHeight
        print(space_y)
        number_space_y=int(space_y/(height*2))
        return number_space_y

    def SetGame(self,rect):
        for all in self.alliens.copy():
            if all.rect.y == rect.y and all.rect.x == rect.x:
                sys.exit()
    def PlayGame(self):
        status=True
        while(status):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(9999)
                    mouse_x,mouse_y=pygame.mouse.get_pos()
                    if self.buttons.rect_button.collidepoint(mouse_x,mouse_y):
                        status=False
            self.init.UpdateWindown()
            self.init.UpdateBul(self.bullets, self.alliens,self.Score)
            self.init.AddImage(self.InfoObject[0], self.InfoObject[1])
            self.init.UpdateAliensMot(self.alliens, self.InfoObject[1])
            self.buttons.DrawButton()
            pygame.display.flip()




    def Control(self, speed):
        self.Fleet(shipHeight=260)
        self.PlayGame()
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        if not(self.InfoObject[1].centerx+100 >= self.init.Right):
                            self.InfoObject[1].centerx+=1*speed
                            self.init.UpdateWindown()
                            self.init.AddImage(self.InfoObject[0], self.InfoObject[1])
                    if event.key==pygame.K_LEFT:
                            if not(self.InfoObject[1].centerx<=0):
                                self.InfoObject[1].centerx -= 1 * speed
                                self.init.UpdateWindown()
                                self.init.AddImage(self.InfoObject[0], self.InfoObject[1])
                    if event.key==pygame.K_SPACE:
                        bul=bullet(self.init.screen,self.InfoObject[1])
                        self.bullets.add(bul)

            self.initWindowGame()








