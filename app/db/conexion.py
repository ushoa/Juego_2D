#from .datos import clases,items
from .config import nombreDB,dirTablas,dirDatos,dirUserTabla,dirSave
from os.path import basename,splitext
from os import listdir
from io import open
import sqlite3
from .read import  nombreSinExtencion

class Conexion():
    def __init__(self):
        self.__db=nombreDB
        self._conn=sqlite3.connect(f'app/db/{self.__db}')
        self._cursor=self._conn.cursor()

    def close(self): self._conn.close()

    def instalacionDB(self):
        self.crearTablas(dirTablas)
        self.insetarDatos()
        self.close()

    def crearTablas(self,Tablas):
        self.__tablas=listdir(Tablas)
        i=0
        for inx in self.__tablas:
            sql=open(Tablas+inx).read()
            try:
                self._cursor.execute(str(sql))
                self.__tablas[i]=nombreSinExtencion(inx)
                print(f"Se creo la tabla {self.__tablas[i].upper() } exitosamente")
            except Exception as e:
                print(e)
                print(f"Error, no se creo la Tabla: {self.__tablas[i].upper()}")
            finally:
                pass
            i+=1
    
    def insetarDatos(self):
        datos=listdir(dirDatos)
        i=0
        escribir=False
        for inx in datos:
            sql=open(dirDatos+inx).read()
            datos[i]=splitext(basename(inx))[0]
            if datos[i] in self.__tablas :
                print('')
                print(f"_________Creando datos de la tabla: {datos[i].upper()}__________")
                char=''
                for e in sql:
                    if(e=='('):
                        escribir=True
                    if(e==';'):
                        escribir=False
                        try:
                            self._cursor.execute("INSERT INTO "+datos[i].upper()+" VALUES "+char)
                            self._conn.commit()
                            print(f'Se agrego: {char}')
                        except Exception as e:
                            print(e)
                            print("Error en el registro: "+char)
                        finally:
                            pass
                        char=''
                    if(escribir):
                        char+=e
            i+=1

    def getAll(self,tabla):
        self._cursor.execute("SELECT * FROM "+tabla)
        datos=self._cursor.fetchall()
        self.close()
        return self.setiarAll(datos,self._cursor.description)

    def getDatos(self,tabla,col,valor,condicion='='):
        sql=f"SELECT * FROM {tabla} WHERE {col} {condicion} '{valor}'"
        #print(sql)
        self._cursor.execute(sql)
        datos=self._cursor.fetchall()
        #cols=self._cursor.description
        self.close()
        return self.setiarFila(datos,self._cursor.description)

    def getDatosById(self,tabla,valor,condicion='='):
        sql=f"SELECT * FROM {tabla} WHERE ID {condicion} {valor}"
        #print(sql)
        try:
            self._cursor.execute(sql)
        except:
            pass
        datos=self._cursor.fetchall()
        #cols=self._cursor.description
        self.close()
        return self.setiarFila(datos,self._cursor.description)


    def setiarFila(self,datos,cols):
        fila={}
        i=0
        for c in cols:
            #print(f'{str(c[0])} = {datos[0][i]}')
            fila[str(c[0])] = datos[0][i]
            i+=1
        return fila

    def setiarAll(self,datos,cols):
        array=[]
        fila={}
        i=0
        for d in datos:
            for c in cols:
                #print(f'{str(c[0])} = {d[i]}')
                fila[str(c[0])] = d[i]
                i+=1
            i=0
            array.append(fila)
            fila={}
        return array

class CargarPartida(Conexion):
    def __init__(self):
        super().__init__()
        self.partidas=[]
        for save in listdir(dirSave):
            self.partidas.append(nombreSinExtencion(save))
    
    def Cargar(self,nombre):
        self._conn=sqlite3.connect(f'app/db/save/{nombre}')
        self._cursor=self._conn.cursor()
        p=self.getAll('PERSONAJE')
        self._conn=sqlite3.connect(f'app/db/save/{nombre}')
        self._cursor=self._conn.cursor()
        i=self.getAll('INVENTARIO')
        self.close()
        return (p,i)

class CrearPartida(Conexion):
    def __init__(self,nombre):
        super().__init__()
        self.nombre=nombre
        self._conn=sqlite3.connect(f'app/db/save/{nombre}')
        self._cursor=self._conn.cursor()
        self.crearTablas(dirUserTabla)
        self._cursor.execute(f"INSERT OR IGNORE INTO PERSONAJE VALUES ('{nombre}',1,0,1,0,0,400,212,'castillo')")
        self._cursor.execute("INSERT OR IGNORE INTO INVENTARIO VALUES (0,200,0,0)")
        self._conn.commit()
    
    def getPartida(self):
        p=self.getAll('PERSONAJE')
        self._conn=sqlite3.connect(f'app/db/save/{self.nombre}')
        self._cursor=self._conn.cursor()
        i=self.getAll('INVENTARIO')
        self.close()
        return (p,i)