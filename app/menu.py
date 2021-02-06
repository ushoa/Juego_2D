import sys, pygame
from .db import config
from .tiles import Botones,Panel

class MenuPrincipal():
    def __init__(self):
        super().__init__()
        self.superficie=Panel(config.pantallaAncho,config.pantallaAlto,0,0,(67,57,70))
        
        self.listaBtns=[
            ['Nuevo',opcion_nuevo],
            ['Cargar',opcion_cargar],
            ['Configuracion',opcion_config],
            ['Salir',opcion_salir]
        ]
        self.y=200
        for btn in range(len(self.listaBtns)):
            print(self.listaBtns[btn][0])
            self.listaBtns[btn][0]=Botones(self.listaBtns[btn][0],self.superficie,70,self.y)
            self.y+=60

    def seleccion(self,event,cursor):
        for btn in self.listaBtns:
                btn[0].update(event,cursor)

    def opcion_nuevo(self):
        print('opcion_nuevo')

    def opcion_cargar(self):
        print('opcion_cargar')
        
    def opcion_config(self):
        print('opcion_config')
        
    def opcion_salir(self):
        print('opcion_salir')
        

