import sys, pygame
from .tiles import Sprite
from .db import conexion

class Personaje(Sprite):
    def __init__(self, nombre,position):
        self.hoja='modelo'
        self.tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}
        super().__init__(self.hoja,self.tiles,position)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pressed())
            pass

    def mochila(self):
        pass

class Equipamiento():
    def __init__(self):
        self.hoja='modelo'
        tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}

        self.sheet = pygame.image.load(f"./app/sprite/{self.hoja}.png")
        self.sheet.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        
        self.sheet2 = pygame.image.load(f"./app/img/{self.hoja2}.png")
        self.sheet2.set_clip(pygame.Rect(tiles['X'], tiles['Y'], tiles['WIDTH'], tiles['HEIGHT']))
        self.image2 = self.sheet2.subsurface(self.sheet2.get_clip())
        self.rect2 = self.image.get_rect()


