import sys, pygame
from app.db import conexion,read,config
from app import tiles,mapa_mundi,personaje,menu

pygame.init()
ventana=pygame.display.set_mode((config.pantallaAncho,config.pantallaAlto))
fps=pygame.time.Clock()
###################
# CONEXION CON DB #
###################
#con=conexion.Conexion()
#con.instalacionDB()

cursor=tiles.Cursor()

#lugarMapa=pygame.Surface((800,525))
#barraInfoPj=pygame.Surface((800,75))

mp=menu.MenuPrincipal(ventana)
op=menu.opcion_config()
#mapaMundi=mapa_mundi.Mapa(2,2)
#mapa=mapaMundi.getMapa()

#pj=personaje.Personaje('Ivan',(100,200))

velocidad=50
ventana.fill((50,50,100))
while True:
    #mapa.draw(ventana)
    #ventana.blit(lugarMapa,(200,0))
    #ventana.blit(barraInfoPj,(200,525))

    #mapaMundi.dibujarMapa(lugarMapa)
    #lugarMapa.blit(pj.image,pj.rect)
    #lugarMapa.blit(pj2.image,pj2.rect)
    cursor.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        mp.show(event,cursor)

    #pj.handle_event(event)
    #pj2.handle_event()
            

    fps.tick(60)
    pygame.display.set_caption(f'Juego en "2D"{fps}')
    pygame.display.flip()
    pygame.display.update()