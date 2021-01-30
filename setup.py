import sys, pygame
from app.db import conexion,read,config
from app import tiles,mapa_mundi,personaje

pygame.init()
ventana=pygame.display.set_mode((1200,600))
fps=pygame.time.Clock()
###################
# CONEXION CON DB #
###################
#con=conexion.Conexion()
#con.instalacionDB()

lugarMapa=pygame.Surface((800,525))
barraInfoPj=pygame.Surface((800,55))

mapaMundi=mapa_mundi.Mapa(2,2)
mapa=mapaMundi.getMapa()

pj=personaje.Personaje('Ivan',(100,200))
#pj2=personaje.Test((500,200))

velocidad=50
while True:
    ventana.fill((50,50,100))
    #mapa.draw(ventana)
    ventana.blit(lugarMapa,(200,20))
    ventana.blit(barraInfoPj,(200,545))
    mapaMundi.dibujarMapa(lugarMapa)
    lugarMapa.blit(pj.image,pj.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pj.handle_event(event)
            

    fps.tick(120)
    pygame.display.set_caption(f'Juego en "2D"{fps}')
    pygame.display.flip()
    pygame.display.update()