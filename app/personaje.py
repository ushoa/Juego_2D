import sys, pygame
from .tiles import Sprite
from .db import conexion

class Personaje(Sprite):
    def __init__(self, nombre,position):
        self.hoja='BODY_male'
        self.tiles={'X':1,'Y':55,'WIDTH':23,'HEIGHT':53}
        super().__init__(self.hoja,self.tiles,position)
        self.left_states = {0:(1,55,21,53),1:(23,57,24,51),2:(49,57,23,50),3:(72,58,24,48),4:(96,57,25,51),5:(121,57,28,51),6:(149,56,25,52),7:(174,56,24,52),8:(197,56,24,52),}
        self.right_states = {}
        #self.up_states = {0:(1,1,30,52),1:(31,1,30,52),2:(61,0,30,53),3:(91,0,30,53),4:(120,0,30,53),5:(150,0,30,52),6:(180,0,30,53),7:(210,0,29,53),8:(239,0,30,53)}
        self.down_states = {0:(7,109,30,55),1:(71,109,30,55),2:(135,109,30,54),3:(200,110,29,53),4:(263,109,33,55),5:(328,109,29,55),6:(391,109,30,54),7:(455,110,29,53),8:(519,109,30,55),}

class Test():
    def __init__(self, position):
        self.hoja='BODY_male'
        self.hoja2='HEAD_chain_armor_helmet'
        tiles={'X':17,'Y':15,'WIDTH':30,'HEIGHT':46}

        self.sheet = pygame.image.load(f"./app/img/{self.hoja}.png")
        self.sheet.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        
        self.sheet2 = pygame.image.load(f"./app/img/{self.hoja2}.png")
        self.sheet2.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image2 = self.sheet2.subsurface(self.sheet2.get_clip())
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = position
        
        self.rect.x=position[0]
        self.rect.y=position[1]

