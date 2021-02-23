import sys, pygame

from .db import conexion
from .tiles import Tiles

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
        self.__contenedorMapa=self.__mapaMundi[self.__y][self.__x].mapa

    def getContenedorMapa(self):
        return self.__contenedorMapa

class Mapa(MapaMundy):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.__hoja='TILES'
        #self.__mapa=pygame.sprite.Group()
        self.__array=self.getContenedorMapa()
        for f in range(len(self.__array)):
            for c in range(len(self.__array[f])):
                #print(f,'.',c,' = ',self.__array[f][c])
                con=conexion.Conexion()
                id=con.getDatosById(self.__hoja,self.__array[f][c])
                tile=Tiles(self.__hoja,id)
                tile.rect.x=c*25
                tile.rect.y=f*25
                self.__array[f][c]=tile
                #self.__mapa.add(tile)

    def getMapa(self):
        return self.__array

    def dibujarMapa(self,ventana):
        for f in range(len(self.__array)):
            for c in range(len(self.__array[f])):
                ventana.blit(self.__array[f][c].image,(self.__array[f][c].rect.x,self.__array[f][c].rect.y))
                self.__array[f][c].rect.x
                self.__array[f][c].rect.y

    def update(self,x,y):
        self.__array.rect.x+=x
