#from .datos import clases,items
from .config import nombreDB,dirTablas,dirDatos
from os.path import basename,splitext
from os import listdir
from io import open
import sqlite3
from .read import  nombreSinExtencion

class Conexion():
    def __init__(self):
        self.__db=nombreDB
        self.__conn=sqlite3.connect(f'app/db/{self.__db}')
        self.__cursor=self.__conn.cursor()

    def close(self): self.__conn.close()

    def instalacionDB(self):
        self.crearTabla()
        self.insetarDatos()
        self.close()

    def crearTablas(self):
        tablas=listdir(dirTablas)
        i=0
        escribir=False
        for inx in tablas:
            sql=open(dirTablas+inx).read()
            try:
                self.__cursor.execute(str(sql))
                tablas[i]=nombreSinExtencion(inx)
                print(f"Se creo la tabla {tablas[i].upper() } exitosamente")
            except Exception as e:
                print(e)
                print(f"Error, no se creo la Tabla: {tablas[i].upper()}")
            finally:
                pass
            i+=1

    def crearTablas(self,tabla):
        sql=open(dirTablasCustom+tabla).read()
        try:
            self.__cursor.execute(str(sql))
            tabla=nombreSinExtencion(tabla)
            print(f"Se creo la tabla {tablas[i].upper() } exitosamente")
        except Exception as e:
            print(e)
            print(f"Error, no se creo la Tabla: {tablas[i].upper()}")
        finally:
    
    def insetarDatos(self):
        datos=listdir(dirDatos)
        i=0
        for inx in datos:
            sql=open(dirDatos+inx).read()
            datos[i]=splitext(basename(inx))[0]
            if datos[i] in tablas :
                print('')
                print(f"_________Creando datos de la tabla: {datos[i].upper()}__________")
                char=''
                for e in sql:
                    if(e=='('):
                        escribir=True
                    if(e==';'):
                        escribir=False
                        try:
                            self.__cursor.execute("INSERT INTO "+datos[i].upper()+" VALUES "+char)
                            self.__conn.commit()
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
        self.__cursor.execute("SELECT * FROM "+tabla)
        datos=self.__cursor.fetchall()
        self.close()
        return self.setiarAll(datos,self.__cursor.description)

    def getDatos(self,tabla,col,valor,condicion='='):
        sql=f"SELECT * FROM {tabla} WHERE {col} {condicion} '{valor}'"
        #print(sql)
        self.__cursor.execute(sql)
        datos=self.__cursor.fetchall()
        #cols=self.__cursor.description
        self.close()
        return self.setiarFila(datos,self.__cursor.description)

    def getDatosById(self,tabla,valor,condicion='='):
        sql=f"SELECT * FROM {tabla} WHERE ID {condicion} '{valor}'"
        #print(sql)
        self.__cursor.execute(sql)
        datos=self.__cursor.fetchall()
        #cols=self.__cursor.description
        self.close()
        return self.setiarFila(datos,self.__cursor.description)

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

class UsuarioDB(Conexion):
    def __init__(user):
        super.__init__():
        self.__db=user
        self.__conn=sqlite3.connect(f'app/db/save/{self.__db}')