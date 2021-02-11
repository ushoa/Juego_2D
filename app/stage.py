import sys, pygame
from app.db import conexion,read,config
from app import tiles,mapa_mundi,personaje,menu,personaje

cursor=tiles.Cursor()
mp=menu.MenuPrincipal()

carga=tiles.PanelConTexto(config.pantallaAncho,config.pantallaAlto,0,0,(0,0,0),'Cargando...',(255,255,255),config.pantallaAncho/2,config.pantallaAlto/2)


def juego(event):
    cursor.update()
    if mp.getEstado():
        mp.selfUpdate(event,cursor)
    else:
        carga.dibujarPanel(config.ventana)

        lugarMapa=tiles.Panel(800,525,200,0,(0,0,0))
        barraInfoPj=tiles.Panel(800,75,200,255,(0,0,0))

        #mapaMundi=mapa_mundi.Mapa(2,2)
        #mapa=mapaMundi.getMapa()
        datos=mp.getRetorno()
        datosPj=datos[0]
        datosInv=datos[1]
        #pj=personaje.Personaje(datosPj[0]['NOMBRE'],datosPj[0]['ID_CLASE'],datosPj[0]['EXP'],datosPj[0]['LVL'],datosPj[0]['HP'],datosPj[0]['ENE'],(datosPj[0]['X'],datosPj[0]['Y']))
        

        lugarMapa.dibujarPanel(config.ventana)
        barraInfoPj.dibujarPanel(lugarMapa.getPanel())

        #lugarMapa.blit(pj.image,pj.rect)
        #mapaMundi.dibujarMapa(lugarMapa)
    