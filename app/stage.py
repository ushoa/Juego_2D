import sys, pygame
from app.db import conexion,read,config
from app import tiles,mapa_mundi,personaje,menu,personaje


class Stage():
    def __init__(self):
        self.cursor=tiles.Cursor()
        self.mp=menu.MenuPrincipal()
        self.load_Map=False
        self.jugar=False

    def menuPrincipal(self,event):
        self.cursor.update()
        self.mp.selfUpdate(event,self.cursor)
        self.nombrePJ=self.mp.getRetorno()

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
            self.pj=personaje.Jugador(self.nombrePJ)
            coordenadas=self.pj.mapaActual
            self.mapa=mapa_mundi.Mapa(coordenadas[0],coordenadas[1])
            
            self.jugar=True
            
        self.lugarMapa.dibujarPanel(config.ventana)
        self.barraInfoPj.dibujarPanel(self.lugarMapa.getPanel())
        self.mapa.dibujarTodo(self.lugarMapa.getPanel())
        self.pj.dibujarJugador(self.lugarMapa.getPanel())
        self.pj.inventario.mostrar()

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

                self.pj.handle_event(event)
    