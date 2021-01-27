from io import open
from os import listdir
from os.path import basename,splitext

def getTexto(dir,arc):
    archivo=open(dir+"/"+arc,"r")
    contenido=archivo.read()
    archivo.close()
    return contenido

def getArchivosEnDirectorio(dir):
    return listdir(dir)

def getTablas():
    return listdir("./app/db/tablas")

def getDatos():
    return listdir("./app/db/datos")

def nombreSinExtencion(archivo):
    return splitext(basename(archivo))[0]
    
def extencionArchivo(archivo):
    return splitext(basename(archivo))[1]
