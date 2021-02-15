import sys, pygame
from app.db import conexion,read,config
from app import stage
#from app import tiles,mapa_mundi,personaje,menu,stage

#pygame.init()
#ventana=pygame.display.set_mode((config.pantallaAncho,config.pantallaAlto))
fps=pygame.time.Clock()
###################
# CONEXION CON DB #
###################
#con=conexion.Conexion()
#con.instalacionDB()

stage=stage.Stage()


velocidad=50
config.ventana.fill((50,50,100))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        evento=event
    stage.update(evento)

    fps.tick(60)
    pygame.display.set_caption(f'Juego en "2D"{fps}')
    pygame.display.flip()
    pygame.display.update()