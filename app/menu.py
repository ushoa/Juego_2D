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
        #{'items':'','nombre':'','funcion':miFuncion(),'value':'valor','estado':False,'x':0,'y':0,'ancho':150,'alto':40,'color':(0,95,136)}
        self.items=[]
        self.estado=True

        self.retorno=(0,0)

    def getEstado(self):
        return self.estado

    def getRetorno(self):
        return self.retorno

    def crearItems(self):
        for btn in self.items:
            btn['items']=btn['items'](btn['nombre'],self.superficie,btn['x'],btn['y'],btn['ancho'],btn['alto'],btn['color'])

    def update(self,event,cursor):
        self.show()
        self.updateItems(event,cursor)
    
    def selfUpdate(self):
        pass

    def updateItems(self,event,cursor):
        pygame.event.pump()
        for btn in self.items:
            btn['items'].update(event,cursor)
            mouse_buttons = pygame.mouse.get_pressed()
            if cursor.colliderect(btn['items'].rectangulo):
                if mouse_buttons[0] and btn['items'].action==1:
                    try:
                        btn['funcion']()
                    except:
                        try:
                            btn['funcion'](btn['value'])
                        except:
                            btn['funcion']
                    #self.check()
                    self.falseAllItems()
                    btn['estado']=True

    def falseAllItems(self):
        for btn in self.items:
            btn['estado']=False

    def check(self):
        for btn in self.items:
            try:
                self.estado=btn['funcion'].getEstado()
                self.retorno=btn['funcion'].getDatosPersonaje()
                print(self.estado,self.retorno)
            except:
                pass


    def show(self):
        self.superficie.dibujarPanel(self.ventana)
        self.showItems()

    def showItems(self):
        for btn in self.items:
            btn['items'].draw()


class MenuPrincipal(Menu):
    def __init__(self):
        super().__init__(config.ventana,config.pantallaAncho,config.pantallaAlto,0,0,(63,59,64))
        self.items=[
            {'items':Botones,'nombre':'Nuevo','funcion':opcion_nuevo(),'value':'valor','estado':False,'x':20,'y':200,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'Cargar','funcion':opcion_cargar(),'value':'valor','estado':False,'x':20,'y':260,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'Configuracion','funcion':opcion_config(),'value':'valor','estado':False,'x':20,'y':320,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'Salir','funcion':opcion_salir(),'value':'valor','estado':False,'x':20,'y':380,'ancho':150,'alto':40,'color':(0,95,136)}
        ]
        self.crearItems()

    def selfUpdate(self,event,cursor):
        self.update(event,cursor)
        for btn in self.items:
            if btn['estado']:
                btn['funcion'].update(event,cursor)
                btn['funcion'].show()
                    
    def getEstado(self):
        for item in self.items:
            if item['funcion'].estado==False:
                self.estado=False
                return self.estado
        return True

    def getRetorno(self):
        for item in self.items:
            if item['funcion'].datosPersonaje!=(0,0):
                return item['funcion'].datosPersonaje
        return (0,0)

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
        self.items=[
            {'items':Input,'nombre':'nombrePJ','funcion':'','value':self.value,'estado':False,'x':20,'y':20,'ancho':560,'alto':40,'color':(92,122,147)},
            {'items':Botones,'nombre':'Crear','funcion':self.crear,'value':self.value,'estado':False,'x':225,'y':80,'ancho':150,'alto':40,'color':(0,95,136)}
        ]
        self.crearItems()

    def crear(self):
        nuevo=conexion.CrearPartida(self.items[0]['items'].texto)
        self.datosPersonaje=nuevo.getPartida()
        self.estado=False

    def selfUpdate(self):
        self.value=self.items[0]['items'].texto
        
class opcion_cargar(Opciones):
    def __init__(self):
        self.saves=conexion.CargarPartida()
        super().__init__()
        y=20
        for datos in self.saves.partidas:
            self.items.append({'items':Botones,'nombre':datos,'funcion':self.cargar,'value':datos,'estado':False,'x':20,'y':y,'ancho':150,'alto':40,'color':(0,95,136)})
            y+=60
        self.crearItems()
    
    def cargar(self,nombre):
        self.datosPersonaje=self.saves.Cargar(nombre)
        self.estado=False

class opcion_config(Opciones):
    def __init__(self):
        super().__init__()
        self.resolucionList=['640 x 480','960 x 540','1200 x 600','1.280 x 720']
        self.items=[
            {'items':BotonesCambiaTexto,'nombre':self.resolucionList,'funcion':self.resolucion,'value':'valor','estado':False,'x':20,'y':20,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'Volumen','funcion':self.volumen,'value':'valor','estado':False,'x':20,'y':80,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'Idioma','funcion':self.idioma,'value':'valor','estado':False,'x':20,'y':140,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'Guardar','funcion':self.guardar,'value':'valor','estado':False,'x':190,'y':290,'ancho':150,'alto':40,'color':(0,95,136)}
        ]
        self.crearItems()


    def resolucion(self):
        for btn in self.items:
            if btn['items'].getClick():
                if type(btn['items'].texto) is list:
                    btn['items'].CambiarTexto()

    def volumen(self):
        print('volumen')

    def idioma(self):
        print('idioma')

    def guardar(self):
        print('Guardar')

class opcion_guardar_partida(Opciones):
    def __init__(self):
        super().__init__()
        self.items=[
            {'items':Botones,'nombre':'Guardar','funcion':self.guardar,'value':'valor','estado':False,'x':225,'y':80,'ancho':150,'alto':40,'color':(0,95,136)}
        ]
        self.crearItems()

    def guardar(self):
        print('Guardar')

class opcion_salir(Opciones):
    def __init__(self):
        super().__init__()
        self.items=[
            {'items':Botones,'nombre':'SI','funcion':self.close,'value':'valor','estado':False,'x':20,'y':20,'ancho':150,'alto':40,'color':(0,95,136)},
            {'items':Botones,'nombre':'NO','funcion':self.continuar,'value':'valor','estado':False,'x':190,'y':20,'ancho':150,'alto':40,'color':(0,95,136)}
        ]
        self.crearItems()
    
    def close(self):
        pygame.quit()
        sys.exit()

    def continuar(self):
        pass