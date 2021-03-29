import sys, pygame
from app.db import conexion,read,config
from app import stage
from app import tiles,mapa_mundi,personaje,menu,stage

#pygame.init()
#ventana=pygame.display.set_mode((config.pantallaAncho,config.pantallaAlto))
fps=pygame.time.Clock()
###################
# CONEXION CON DB #
###################
#con=conexion.Conexion()
#con.instalacionDB()

stage=stage.Stage()

cursor=tiles.Cursor()
pj=personaje.Jugador('Ushoa')

while True:
    config.ventana.fill((50,50,100))
    pj.dibujarJugador(config.ventana)
    for event in pygame.event.get():
        pass
#        stage.update(event)
    pj.handle_event(event,cursor)

    fps.tick(60)
    pygame.display.set_caption(f'Juego en "2D"{fps}')
    pygame.display.flip()
    pygame.display.update()