import pygame.font

class score():
    def __init__(self,color_button, color_text,screen,msg):
        self.color_button=color_button
        self.color_text=color_text
        self.screen = screen
        self.rect_button = pygame.Rect(0,0,100,30)
        self.font = pygame.font.SysFont(None,20)
        self.rect_button.x=30
        self.rect_button.y=30
        self.msg=msg
        self.SetScore(self.msg)

    def UpdateScore(self,bonus):
        self.msg+=bonus
        self.SetScore(self.msg)

    def SetScore(self,msg):
        self.image_Score = self.font.render(str(msg),True,self.color_text,self.rect_button)
        self.rect_Score_Image = self.image_Score.get_rect()
        self.rect_Score_Image.center = self.rect_button.center

    def DrawScore(self):
        self.screen.fill(self.rect_button,self.rect_button)
        self.screen.blit(self.image_Score,self.rect_Score_Image)

