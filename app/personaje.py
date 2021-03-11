import sys, pygame
from .tiles import SpriteMobile,SpriteStand
from .db import conexion


class Ente():
    def __init__(self,nombre,clase_id):
        self.tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}
        self.nombre=nombre
        self.__ID=0
        self.__clase=clase_id
        self.__STR=0
        self.__DEF=0
        self.__CON=0
        self.__DEX=0
        self.__MOD=0
        self.__LVLmin=0
        self.__LVL=1
        self.__hpMax=0
        self.__hp=0
        self.__eneMax=10
        self.__ene=0
        self.__dmg=0
        self.__pdef=0
        self.__agi=0
        self.__spe=0
        self.__crit=0
        self.__pCrit=0
        self.__exp=0

    def setStatsPrincipales(self):
        pass

    def setStatSecundarios(self):
        pass


class Npc(Ente):
    def __init__(self,nombre,clase_id,hoja,position,tile):
        self.hoja='/npc/'+hoja
        self.nombre=nombre
        super().__init__(nombre,clase_id)
        self.tile=tile
        self.sprite=SpriteStand(self.hoja,self.tile,position)

    def interaccion(self):
        print('Mensaje de prueba para corroborar coliciones')

class Enemigo(Ente):
    def __init__(self,nombre,hoja,clase_id,lvl,position):
        self.hoja=hoja
        super().__init__(nombre,clase_id)
        self.__LVL=lvl
        self.spriteEnemigo=SpriteMobile(self.hoja,self.tiles,position)


class Jugador(Ente):
    def __init__(self,nombre):
        self.hoja='modelo'
        self.hoja='cuerpo/'
        con=conexion.CargarPartida()
        self.datosPersonaje=con.Cargar(nombre)
        self.position=(self.datosPersonaje[0]['MAPA_X'],self.datosPersonaje[0]['MAPA_Y'],)
        self.inventario=inventario
        super().__init__(nombre,clase_id)
        self.spriteCuerpo=SpriteMobile(self.hoja+'modelo',self.tiles,self.position)
        self.armadura=[
            { 'CASCO' : SpriteMobile(self.hoja,self.tiles,self.position) },
            { 'PECHERA' : SpriteMobile(self.hoja,self.tiles,self.position) },
            { 'GUANTES' : SpriteMobile(self.hoja,self.tiles,self.position) },
            { 'BOTAS' : SpriteMobile(self.hoja,self.tiles,self.position) },
            { 'PANTALON' : SpriteMobile(self.hoja,self.tiles,self.position) }
        ]
        self.spriteCabeza=SpriteMobile(self.hoja,self.tiles,self.position)
        self.spriteTorso=SpriteMobile(self.hoja,self.tiles,self.position)
        self.spriteBrazos=SpriteMobile(self.hoja,self.tiles,self.position)
        self.spritePiernas=SpriteMobile(self.hoja,self.tiles,self.position)
        self.spritePantalon=SpriteMobile(self.hoja+'pantalon_cuero',self.tiles,self.position)
        self.__tabla='CLASES'
        self.__columna='CLASE'

    def itemsInventario(self):
        pass

    def dibujarJugador(self,ventana):
        ventana.blit(self.spriteCabeza.image,self.spriteCabeza.rect)
        ventana.blit(self.spriteTorso.image,self.spriteTorso.rect)
        ventana.blit(self.spriteBrazos.image,self.spriteBrazos.rect)
        ventana.blit(self.spritePiernas.image,self.spritePiernas.rect)
        ventana.blit(self.spritePantalon.image,self.spritePantalon.rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.spriteCabeza.update('left')
                self.spriteTorso.update('left')
                self.spriteBrazos.update('left')
                self.spritePiernas.update('left')
                self.spritePantalon.update('left')
            if event.key == pygame.K_RIGHT:
                self.spriteCabeza.update('right')
                self.spriteTorso.update('right')
                self.spriteBrazos.update('right')
                self.spritePiernas.update('right')
                self.spritePantalon.update('right')
            if event.key == pygame.K_UP:
                self.spriteCabeza.update('up')
                self.spriteTorso.update('up')
                self.spriteBrazos.update('up')
                self.spritePiernas.update('up')
                self.spritePantalon.update('up')
            if event.key == pygame.K_DOWN:
                #self.update('down')
                self.spriteCabeza.update('down')
                self.spriteTorso.update('down')
                self.spriteBrazos.update('down')
                self.spritePiernas.update('down')
                self.spritePantalon.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                #self.update('stand_left')
                self.spriteCabeza.update('stand_left')
                self.spriteTorso.update('stand_left')
                self.spriteBrazos.update('stand_left')
                self.spritePiernas.update('stand_left')
                self.spritePantalon.update('stand_left')       
            if event.key == pygame.K_RIGHT:
                self.spriteCabeza.update('stand_right')
                self.spriteTorso.update('stand_right')
                self.spriteBrazos.update('stand_right')
                self.spritePiernas.update('stand_right')
                self.spritePantalon.update('stand_right')
            if event.key == pygame.K_UP:
                self.spriteCabeza.update('stand_up')
                self.spriteTorso.update('stand_up')
                self.spriteBrazos.update('stand_up')
                self.spritePiernas.update('stand_up')
                self.spritePantalon.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.spriteCabeza.update('stand_up')
                self.spriteTorso.update('stand_up')
                self.spriteBrazos.update('stand_up')
                self.spritePiernas.update('stand_up')
                self.spritePantalon.update('stand_up')
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pressed())
            pass

    def mochila(self):
        pass



