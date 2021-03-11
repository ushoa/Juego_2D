import sys, pygame

from .db import conexion
from .tiles import Tiles
from .personaje import Npc,Enemigo

from .mapas import fuerte_no,afueras_fuerte_no,plaza_olvidada,afueras_fuerte_ne,fuerte_ne
from .mapas import masmorras,entrada_masmorras,detras_del_castillo,campo,esquina_externa_ne
from .mapas import entrada_principal,patio_castillo_o,castillo,granja,pasillo_este_externo_B
from .mapas import afueras_entrada,patio_castillo_so,patio_castillo_s,patio_castillo_se,pasillo_este_externo_A
from .mapas import esquina_externa_so,pasillo_sur_externo_A,pasillo_sur_externo_B,pasillo_sur_externo_C,esquina_externa_se


class MapaMundy():
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__tabla='mapamundi'
        self.__mapaMundi=[
        [fuerte_no,afueras_fuerte_no,plaza_olvidada,afueras_fuerte_ne,fuerte_ne],
        [masmorras,entrada_masmorras,detras_del_castillo,campo,esquina_externa_ne],
        [entrada_principal,patio_castillo_o,castillo,granja,pasillo_este_externo_B],
        [afueras_entrada,patio_castillo_so,patio_castillo_s,patio_castillo_se,pasillo_este_externo_A],
        [esquina_externa_so,pasillo_sur_externo_A,pasillo_sur_externo_B,pasillo_sur_externo_C,esquina_externa_se]
        ]
        self.mapa=self.__mapaMundi[self.__y][self.__x].mapa
        self.nombre=self.__mapaMundi[self.__y][self.__x].nombre
        self.npc=self.__mapaMundi[self.__y][self.__x].npc
        self.enemigo=self.__mapaMundi[self.__y][self.__x].enemigo
        self.mundi=self.__mapaMundi[self.__y][self.__x].mundi

class Mapa(MapaMundy):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__hoja='TILES'
        self.setMapa()
        self.setNPC()
        self.setEnemigo()

    def setMapa(self):
        for f in range(len(self.mapa)):
            for c in range(len(self.mapa[f])):
                con=conexion.Conexion()
                id=con.getDatosById(self.__hoja,self.mapa[f][c])
                tile=Tiles(self.__hoja,id)
                tile.rect.x=c*25
                tile.rect.y=f*25
                self.mapa[f][c]=tile

    def dibujarMapa(self,ventana):
        for f in range(len(self.mapa)):
            for c in range(len(self.mapa[f])):
                ventana.blit(self.mapa[f][c].image,(self.mapa[f][c].rect.x,self.mapa[f][c].rect.y))
                self.mapa[f][c].rect.x
                self.mapa[f][c].rect.y

    def update(self,x,y):
        self.mapa.rect.x+=x

    def setNPC(self):
        for npc in self.npc:
            npc[0]['npc']=Npc(npc[0]['nombre'],1,npc[0]['hoja'],npc[0]['position'],npc[0]['tile'])
            #print(npc[0]['npc'].sprite)

    def dibujarNPC(self,ventana):
        for npc in self.npc:
            ventana.blit(npc[0]['npc'].sprite.image,npc[0]['npc'].sprite.rect)

    def setEnemigo(self):
        for enemigo in self.enemigo:
            enemigo[0]['npc']=Enemigo(enemigo[0]['nombre'],enemigo[0]['hoja'],enemigo[0]['position'],enemigo[0]['tile'])

    def dibujarEnemigo(self,ventana):
        for enemigo in self.enemigo:
            ventana.blit(enemigo[0]['npc'].image,enemigo[0]['npc'].rect)

    def dibujarTodo(self,ventana):
        self.dibujarMapa(ventana)
        self.dibujarNPC(ventana)
        self.dibujarEnemigo(ventana)

