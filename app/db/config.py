import sys, pygame

pygame.init()
#CARACTERISTICAS DEL JUEGO
exp=1
drop=1
expMax=5
#NOMBRE DDBB
nombreDB="JuegoDB"
#LVL MAXIMO
lvlMax=80

#DIMENSION PANTALLA
pantallaAncho=1200
pantallaAlto=600

ventana=pygame.display.set_mode((pantallaAncho,pantallaAlto))

#DIRECTORIO DE LAS TABLAS
dirTablas="./app/db/tablas/"
#DIRECTORIO DE LOS DATOS
dirDatos="./app/db/datos/"
#DIRECTORIO DE LAS TABLAS CUSTOM
dirTablasCustom="./app/db/tablas/custom/"
#DIRECTORIO DE LOS DATOS CUSTOM
dirDatosCustom="./app/db/datos/custom/"
#DIRECTORIO DE LOS MAPAS
dirMapas="./app/mapas/"
#DIRECTORIO DE TABLA NUEVO USUARIO
dirUserTabla="./app/db/tablaUser/"
#DIRECTORIO DE PARTIDAS GUARDADAS
dirSave="./app/db/save/"

#SPRITES
#DIRECTORIO DE LAS ARMADURAS
dirArmaduras="./app/sprites/armaduras/"
#DIRECTORIO DE LAS ARMAS
dirArmas="./app/sprites/armas/"
#DIRECTORIO DE LOS ICONOS
dirIconos="./app/sprites/iconos/"
