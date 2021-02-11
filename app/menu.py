import sys, pygame
from .db import config,conexion
from .tiles import Botones,Panel,Input,BotonesCambiaTexto


class Menu():
    def __init__(self,ventana,ancho,alto,x,y,color):
        self.ventana=ventana
        self.ancho=ancho
        self.alto=alto
        self.x=x
        self.y=y
        self.color=color
        self.superficie=Panel(self.ancho,self.alto,self.x,self.y,self.color)
        #FORMATO BOTONES
        #{'boton':'','nombre':'','funcion':miFuncion(),'value':'valor','estado':False,'x':0,'y':0}
        #FORMATO INPUT
        #{'input':'','nombre':'','value':'valor','estado':False,'x':0,'y':0,'ancho':0,'alto':0,'color':(0,0,0)}
        self.botones=[]
        self.input_box=[]
        self.estado=True

        self.retorno=(0,0)

    def getEstado(self):
        return self.estado

    def getRetorno(self):
        return self.retorno
    
    def crearInput(self):
        for inp in self.input_box:
            inp['input']=Input(self.superficie,inp['ancho'],inp['alto'],inp['x'],inp['y'],inp['color'])

    def crearBotones(self):
        for btn in self.botones:
            btn['boton']=btn['boton'](btn['nombre'],self.superficie,btn['x'],btn['y'])

    def update(self,event,cursor):
        self.event=event
        self.cursor=cursor
        self.updateBotones()
        self.updateInput()
        self.show()
    
    def selfUpdate(self):
        pass

    def updateBotones(self):
        self.check()
        for btn in self.botones:
            btn['boton'].update(self.event,self.cursor)
            if self.clickBoton(btn):
                try:
                    btn['funcion']()
                except:
                    try:
                        btn['funcion'](btn['value'])
                    except:
                        btn['funcion']
                btn['funcion']
                self.falseAllBotones()
                btn['estado']=True

    def falseAllBotones(self):
        for btn in self.botones:
            btn['estado']=False

    def clickBoton(self,btn):
        estado=btn['boton'].clic
        return estado

    def updateInput(self):
        for inp in self.input_box:
            inp['input'].update(self.event,self.cursor)

    def check(self):
        for btn in self.botones:
            try:
                b=btn['funcion'].getAccion()
                retorno=btn['funcion'].getDatosPersonaje()
            except:
                b=True
                retorno=(0,0)
            if b==False:
                self.retorno=retorno
                self.estado=False

    def show(self):
        self.superficie.dibujarPanel(self.ventana)
        self.showBotones()
        self.showInputs()

    def showBotones(self):
        for btn in self.botones:
            btn['boton'].draw()
                    
    def showInputs(self):
        for inp in self.input_box:
            inp['input'].draw()


class MenuPrincipal(Menu):
    def __init__(self):
        super().__init__(config.ventana,config.pantallaAncho,config.pantallaAlto,0,0,(63,59,64))
        self.botones=[
            {'boton':Botones,'nombre':'Nuevo','funcion':opcion_nuevo(),'value':'valor','estado':False,'x':20,'y':200},
            {'boton':Botones,'nombre':'Cargar','funcion':opcion_cargar(),'value':'valor','estado':False,'x':20,'y':260},
            {'boton':Botones,'nombre':'Configuracion','funcion':opcion_config(),'value':'valor','estado':False,'x':20,'y':320},
            {'boton':Botones,'nombre':'Salir','funcion':opcion_salir(),'value':'valor','estado':False,'x':20,'y':380}
        ]
        self.crearBotones()

    def destroy(self):
        self=None

    def selfUpdate(self,event,cursor):
        self.update(event,cursor)
        for btn in self.botones:
            if btn['estado']:
                btn['funcion'].update(event,cursor)
                btn['funcion'].show()
                    


class Opciones(Menu):
    def __init__(self):
        self.x=250
        self.y=180
        self.width=600
        self.height=350
        self.color=(136,121,140)
        super().__init__(config.ventana,self.width,self.height,self.x,self.y,self.color)
        self.accion=True
        self.datosPersonaje=(0,0)
    
    def getAccion(self):
        return self.accion

    def getDatosPersonaje(self):
        return self.datosPersonaje

class opcion_nuevo(Opciones):
    def __init__(self):
        super().__init__()
        self.value=''
        self.input_box=[
            {'input':'','nombre':'nombrePJ','value':self.value,'estado':False,'x':20,'y':20,'ancho':560,'alto':40,'color':(92,122,147)}
        ]
        self.botones=[
            {'boton':Botones,'nombre':'Crear','funcion':self.crear,'value':self.value,'estado':False,'x':225,'y':80}
        ]
        self.crearInput()
        self.crearBotones()

    def crear(self):
        nuevo=conexion.CrearPartida(self.value)
        self.datosPersonaje=nuevo.getPartida()
        self.accion=False

    def selfUpdate(self):
        self.value=self.input_box[0]['input'].texto
        
class opcion_cargar(Opciones):
    def __init__(self):
        self.saves=conexion.CargarPartida()
        super().__init__()
        y=20
        for datos in self.saves.partidas:
            self.botones.append({'boton':Botones,'nombre':datos,'funcion':self.cargar,'value':datos,'estado':False,'x':20,'y':y})
            y+=60
        self.crearBotones()
    
    def cargar(self,nombre):
        self.datosPersonaje=self.saves.Cargar(nombre)
        print(self.datosPersonaje)
        self.accion=False

class opcion_config(Opciones):
    def __init__(self):
        super().__init__()
        self.resolucionList=['640 x 480','960 x 540','1200 x 600','1.280 x 720']
        self.botones=[
            {'boton':BotonesCambiaTexto,'nombre':self.resolucionList,'funcion':self.resolucion,'value':'valor','estado':False,'x':20,'y':20},
            {'boton':Botones,'nombre':'Volumen','funcion':self.volumen,'value':'valor','estado':False,'x':20,'y':80},
            {'boton':Botones,'nombre':'Idioma','funcion':self.idioma,'value':'valor','estado':False,'x':20,'y':140},
            {'boton':Botones,'nombre':'Guardar','funcion':self.guardar,'value':'valor','estado':False,'x':190,'y':290}
        ]
        self.crearBotones()


    def resolucion(self):
        for btn in self.botones:
            if btn['boton'].getClick():
                if type(btn['boton'].texto) is list:
                    btn['boton'].CambiarTexto()

    def volumen(self):
        print('volumen')

    def idioma(self):
        print('idioma')

    def guardar(self):
        print('Guardar')

class opcion_guardar_partida(Opciones):
    def __init__(self):
        super().__init__()
        self.botones=[
            {'boton':Botones,'nombre':'Guardar','funcion':self.guardar,'value':'valor','estado':False,'x':225,'y':80}
        ]
        self.crearBotones()

    def guardar(self):
        print('Guardar')

class opcion_salir(Opciones):
    def __init__(self):
        super().__init__()
        self.botones=[
            {'boton':Botones,'nombre':'SI','funcion':self.close,'value':'valor','estado':False,'x':20,'y':20},
            {'boton':Botones,'nombre':'NO','funcion':self.continuar,'value':'valor','estado':False,'x':190,'y':20}
        ]
        self.crearBotones()
    
    def close(self):
        pygame.quit()
        sys.exit()

    def continuar(self):
        pass