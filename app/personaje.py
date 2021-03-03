import sys, pygame
from .tiles import SpriteMobile,SpriteStand
from .db import conexion

class Npc(SpriteStand):
    def __init__(self,nombre,hoja,position):
        self.hoja=hoja
        self.nombre=nombre
        self.tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}
        super().__init__(self.hoja,self.tiles,position)

class Enemigo(SpriteMobile):
    def __init__(self,nombre,hoja,clase,exp,lvl,hp,ene,position):
        self.hoja=hoja
        self.nombre=nombre
        self.tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}
        super().__init__(self.nombre,self.hoja,position)
        self.__ID=0
        self.__clase=clase
        self.__STR=0
        self.__DEF=0
        self.__CON=0
        self.__DEX=0
        self.__MOD=0
        self.__LVLmin=0
        self.__LVL=lvl
        self.__hpMax=0
        self.__hp=hp
        self.__eneMax=10
        self.__ene=ene
        self.__dmg=0
        self.__pdef=0
        self.__agi=0
        self.__spe=0
        self.__crit=0
        self.__pCrit=0
        self.__exp=exp


class Jugador(Enemigo):
    def __init__(self,nombre,clase,exp,lvl,hp,ene,position):
        self.hoja='modelo'
        super().__init__(nombre,self.hoja,clase,exp,lvl,hp,ene,position)
        self.__tabla='CLASES'
        self.__columna='CLASE'

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


