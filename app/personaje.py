import sys, pygame
from math import floor,ceil

from .tiles import SpriteMobile,SpriteStand,Botones,Panel
from .db import conexion,config


class Ente():
    def __init__(self,nombre,clase_id):

        self.tiles={'X':18,'Y':588,'WIDTH':46,'HEIGHT':47}
        self.nombre=nombre
        self.clase=clase_id

        self.LVL=1
        self.EXP=0

        self.MOD=self.LVL*0.1
        
        self.STR=0
        self.DEF=0
        self.CON=0
        self.DEX=0

        self.HPMAX=0
        self.HP=0
        self.ENEMAX=0
        self.ENE=0
        self.DMG=0
        self.PDEF=0
        self.BLO=0
        self.AGI=0
        self.SPE=0
        self.CRIT=0
        self.PCRIT=0

        self.statsPrincipales={
            'STR' : self.STR,
            'DEF' : self.DEF,
            'CON' : self.CON,
            'DEX' : self.DEX
        }
        
        self.getClaseStats()
        self.setStatsPrincipales()
        self.setStatSecundarios()

    def getClaseStats(self):
        con=conexion.Conexion()
        self.statsClase=con.getDatosById('clases',self.clase)

    def setStatsPrincipales(self):
        self.setModificador()
        for stats in self.statsClase:
            try:
                self.statsPrincipales[stats]
                self.statsPrincipales[stats]=self.statsClase[stats]
            except :
                pass

    def setStatSecundarios(self):
        self.setModificador()
        self.statsSecundarios={
            'HPMAX' : ceil(self.HPMAX+(self.statsPrincipales['CON']*self.MOD)),
            'HP' : ceil(self.HP),
            'ENEMAX' : ceil(self.ENEMAX+(self.statsPrincipales['DEX']*self.MOD)),
            'ENE' : ceil(self.ENE),
            'DMG' : ceil(self.DMG+(self.statsPrincipales['STR']*self.MOD)),
            'PDEF' : ceil(self.PDEF+(self.statsPrincipales['DEF']*self.MOD)),
            'BLO' : ceil(self.BLO),
            'AGI' : ceil(self.AGI+(((self.statsPrincipales['DEX']+self.statsPrincipales['STR'])/2)*self.MOD)),
            'SPE' : ceil(self.SPE+(self.statsPrincipales['DEX']*self.MOD)),
            'CRIT' : ceil(self.CRIT+(self.DMG*(1+self.MOD))),
            'PCRIT' : ceil(self.PCRIT+(self.statsPrincipales['DEX']*self.MOD))
        }
    
    def setModificador(self):
        self.MOD=self.LVL*0.1


class Npc(Ente):
    def __init__(self,nombre,clase_id,hoja,position,tile):
        self.hoja='npc/'+hoja
        self.nombre=nombre
        super().__init__(nombre,clase_id)
        self.tabla='npc'
        self.tile=tile
        self.sprite=SpriteStand(self.hoja,self.tile,position)

    def interaccion(self):
        print('Mensaje de prueba para corroborar coliciones')

class Enemigo(Ente):
    def __init__(self,nombre,hoja,clase_id,lvl,position):
        self.hoja=hoja
        super().__init__(nombre,clase_id)
        self.tabla='npc'
        self.LVL=lvl
        self.spriteEnemigo=SpriteMobile(self.hoja,self.tiles,position)


class Jugador(Ente):
    def __init__(self,nombre):
        self.hoja='cuerpo/'
        con=conexion.CargarPartida()
        self.datos=con.Cargar(nombre)
        self.dataPersonaje=self.datos[0]

        super().__init__(nombre,self.dataPersonaje[0]['ID_CLASE'])
        
        for i in range(1,21):
            self.LVL=i
            self.setStatsPrincipales()
            self.setStatSecundarios()
            print('*********************************')
            print(f"lvl: {i}, Mod: {self.MOD}")
            print(self.statsPrincipales)
            print(self.statsSecundarios)

        self.objetos=self.datos[1]
        self.inventario=Inventario(self.objetos)

        self.nombre=self.dataPersonaje[0]['NOMBRE']

        self.x=self.dataPersonaje[0]['X']
        self.y=self.dataPersonaje[0]['Y']
        self.position=(self.x,self.y)

        self.mapaX=self.dataPersonaje[0]['MAPA_X']
        self.mapaY=self.dataPersonaje[0]['MAPA_Y']
        self.mapaActual=(self.mapaX,self.mapaY)

        self.clase_id=self.dataPersonaje[0]['ID_CLASE']
        super().__init__(nombre,self.clase_id)
        self.spriteCuerpo=SpriteMobile(self.hoja+'modelo',self.tiles,self.position)

        self.armadura=[
            { 
                'CASCO' : SpriteMobile(self.hoja+'cabeza',self.tiles,self.position) ,
                'PECHERA' : SpriteMobile(self.hoja+'torso',self.tiles,self.position) ,
                'GUANTES' : SpriteMobile(self.hoja+'manos',self.tiles,self.position) ,
                'BOTAS' : SpriteMobile(self.hoja+'pies',self.tiles,self.position) ,
                'PANTALON' : SpriteMobile(self.hoja+'piernas',self.tiles,self.position) 
            }
        ]
        self.sprite=pygame.sprite.Group()
        
        for arm in self.armadura[0]:
            #print(f'Key: {self.armadura[0][arm]}')
            self.sprite.add(self.armadura[0][arm])

        self.__tabla='CLASES'
        self.__columna='CLASE'


    def dibujarJugador(self,ventana):
        self.sprite.draw(ventana)
    
    def movePj(self,direccion):
        for arm in self.armadura[0]:
            self.armadura[0][arm].update(direccion)

    def handle_event(self, event):
        for event in pygame.event.get():
            pass
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.movePj('left')
            if event.key == pygame.K_RIGHT:
                self.movePj('right')
            if event.key == pygame.K_UP:
                self.movePj('up')
            if event.key == pygame.K_DOWN:
                self.movePj('down')

            if event.key == pygame.K_i:
                self.inventario.cambiarEstado()
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.movePj('stand_left')      
            if event.key == pygame.K_RIGHT:
                self.movePj('stand_right')
            if event.key == pygame.K_UP:
                self.movePj('stand_up')
            if event.key == pygame.K_DOWN:
                self.movePj('stand_down')
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pressed())
            pass


        
class Inventario():
    def __init__(self,objetos):
        self.objetos=self.setItemsInventario(objetos)
        self.surface=Panel(200,600,0,0,(29,12,107))
        self.armadura=Armadura(self.objetos,self.surface)
        self.estado=False

    def setItemsInventario(self,objetos):
        for i in objetos:
            con=conexion.Conexion()
            stats=con.getDatosById('items',i['ID_ITEM'])
            i.update(stats)
            #print(i)
        return objetos

    def mostrar(self):
        if self.estado==True:
            self.surface.dibujarPanel(config.ventana)
            self.armadura.dibujarPanel()

    def cambiarEstado(self):
        if self.estado==False:
            self.estado=True
        else:
            self.estado=False

class Mochila():
    def __init__(self,objetos):
        pass

class Armadura():
    def __init__(self,objetos,superficie):
        self.superficie=superficie
        self.objetos=objetos
        self.panelArmaduraStats=Panel(180,200,(self.superficie.width/2)-90,20,(125,125,125))
        self.panelArmadura=Panel(85,200,4,20,(125,125,125))
        self.stats=Panel(85,200,92,20,(125,125,125))
        dim=30
        self.armadura={
            'CASCO' : Panel(dim,dim,27,0,(10,10,10)),
            'PECHERA' : Panel(dim,dim,0,35,(10,10,10)),
            'GUANTES' : Panel(dim,dim,55,35,(10,10,10)),
            'BOTAS' : Panel(dim,dim,0,70,(10,10,10)),
            'PANTALON' : Panel(dim,dim,55,70,(10,10,10)),
            'ARMA' : Panel(dim,dim,0,105,(10,10,10)),
            'ESCUDO' : Panel(dim,dim,55,105,(10,10,10))
        }
        self.setArmadura()

    def setArmadura(self):
        for o in self.objetos:
            if o['EQUIPADO']==1:
                self.armadura[o['EQUIPO']].color=(75,75,75)

    def setItem(self,tipo):
        self.armadura[tipo].color=(10,10,10)


    def dibujarPanel(self):
        self.panelArmaduraStats.dibujarPanel(self.superficie.getPanel())
        self.panelArmadura.dibujarPanel(self.panelArmaduraStats.getPanel())
        for s in self.armadura:
            self.armadura[s].dibujarPanel(self.panelArmadura.getPanel())

        




