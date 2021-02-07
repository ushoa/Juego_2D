import sys, pygame
from .db import config
from .tiles import Botones,Panel

class MenuPrincipal():
    def __init__(self,ventana):
        self.ventana=ventana
        self.superficie=Panel(config.pantallaAncho,config.pantallaAlto,0,0,(63,59,64))
        
        self.listaBtns=[
            ['Nuevo','opcion_nuevo',False],
            ['Cargar','opcion_cargar',False],
            ['Configuracion',opcion_config(),False],
            ['Salir','opcion_salir',False]
        ]
        self.y=200
        for btn in range(len(self.listaBtns)):
            self.listaBtns[btn][0]=Botones(self.listaBtns[btn][0],self.superficie,70,self.y)
            self.y+=60

    def show(self,event,cursor):
        for btn in self.listaBtns:
            btn[0].update(event,cursor)
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and cursor.colliderect(btn[0].rectangulo):
                if btn[2]==True:
                    btn[2]=False
                else:
                    btn[2]=True
        self.seleccion()

    def seleccion(self):
        self.superficie.dibujarPanel(self.ventana)
        for btn in self.listaBtns:
            btn[0].draw()
            if btn[2]==True:
                btn[1].show(self.ventana)

class Opciones():
    def __init__(self):
        self.x=250
        self.y=180
        self.width=600
        self.height=350
        self.panelOpcion=Panel(self.width,self.height,self.x,self.y,(136,121,140))
        self.listaBtns=[]
        self.btnCancelar=Botones('Cancelar',self.panelOpcion,20,335)
        self.btnGuardar=Botones('Guardar',self.panelOpcion,190,335)
    
    def CrearBotones(self):
        y=20
        for btn in range(len(self.listaBtns)):
            self.listaBtns[btn][0]=Botones(self.listaBtns[btn][0],self.panelOpcion,20,y)
            y+=60

    def show(self,ventana):
        self.panelOpcion.dibujarPanel(ventana)
        self.btnCancelar.draw()
        self.btnGuardar.draw()

class opcion_nuevo(Opciones):
    def Pintar(self):
        print ('A')

class opcion_cargar(Opciones):
    def Pintar(self):
        return 'B'

class opcion_config(Opciones):
    def __init__(self):
        super().__init__()
        self.listaBtns=[
            ['1200x600','dimension',False],
            ['Volumen','volumen',False],
            ['Idioma','opcion_config',False]
        ]
        self.CrearBotones()

class opcion_salir(Opciones):
    def Pintar(self):
        return 'C'