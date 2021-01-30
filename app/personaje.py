import sys, pygame
from .tiles import Sprite
from .db import conexion

class Personaje(Sprite):
    def __init__(self, nombre,position):
        self.hoja='modelo'
        self.tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}
        super().__init__(self.hoja,self.tiles,position)

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

