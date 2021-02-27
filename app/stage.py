import sys, pygame
from app.db import conexion,read,config
from app import tiles,mapa_mundi,personaje,menu,personaje


class Stage():
    def __init__(self):
        self.cursor=tiles.Cursor()
        self.mp=menu.MenuPrincipal()
        self.load_Map=False
        self.jugar=False
        self.load_pj=False

    def menuPrincipal(self,event):
        self.cursor.update()
        self.mp.selfUpdate(event,self.cursor)
        self.datos=self.mp.getRetorno()

    def pantallaCarga(self):
        if self.jugar==False:
            self.carga=tiles.PanelConTexto(config.pantallaAncho,config.pantallaAlto,0,0,(0,0,0),'Cargando...',(255,255,255),config.pantallaAncho/2,config.pantallaAlto/2)
        else:
            self.carga=tiles.Panel(config.pantallaAncho,config.pantallaAlto,0,0,(0,0,0))

        self.carga.dibujarPanel(config.ventana)

    def juego(self):
        if self.jugar==False:
            self.lugarMapa=tiles.Panel(800,525,200,0,(0,0,0))
            self.barraInfoPj=tiles.Panel(800,75,200,255,(0,0,0))
            self.mapaMundi=mapa_mundi.Mapa(2,2)
            self.mapa=self.mapaMundi.getMapa()
            self.jugar=True
        self.lugarMapa.dibujarPanel(config.ventana)
        self.barraInfoPj.dibujarPanel(self.lugarMapa.getPanel())
        self.mapaMundi.dibujarMapa(self.lugarMapa.getPanel())

    def loadMap(self):
        if self.load_Map==False:
            self.mapaMundi=mapa_mundi.Mapa(2,2)
            self.mapa=self.mapaMundi.getMapa()
            self.load_Map==True

    def personaje(self):
        if self.load_pj==False:
            self.datosPj=self.datos[0]
            self.datosInv=self.datos[1]
            self.pj=personaje.Personaje(self.datosPj[0]['NOMBRE'],self.datosPj[0]['ID_CLASE'],self.datosPj[0]['EXP'],self.datosPj[0]['LVL'],self.datosPj[0]['HP'],self.datosPj[0]['ENE'],(self.datosPj[0]['X'],self.datosPj[0]['Y']))
            self.load_pj=True
        self.lugarMapa.getPanel().blit(self.pj.image,self.pj.rect)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.mp.getEstado():
                self.menuPrincipal(event)
            else:
                self.pantallaCarga()
                self.juego()

                self.personaje()
                self.pj.handle_event(event)
    