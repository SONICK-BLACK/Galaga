import pygame.font
class buttonSet():
    def __init__(self,color_button,color_text,screen,msg):
        self.color_button=color_button
        self.screen=screen
        self.color_text=color_text
        self.rect_button = pygame.Rect(0,0,200,50)
        self.rect_button.center=screen.get_rect().center
        self.rect=self.rect_button
        self.font= pygame.font.SysFont(None,48)
        self.SetMsgbutton(msg)

    def SetMsgbutton(self,msg):
        self.msg_image=self.font.render(msg,True,self.color_text,self.color_button)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect_button.center

    def DrawButton(self):
        self.screen.fill(self.color_button,self.rect_button)
        self.screen.blit(self.msg_image,self.msg_image_rect)
