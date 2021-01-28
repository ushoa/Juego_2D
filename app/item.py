from db import conexion
class Item():
    def __init__(self):
        self.conn=conexion.Conecion()
        self.tipo=('CONSUMIBLE','ARMA','ARMADURA')
        self.categoria=('LIVIANA','MEDIANA','PESADA')
        self.equipo=('ESPADA CORTA','ESPADA LARGA','ESPADA DOS MANOS','ARCO','GUANTES','PECHERA','CASCO','BOTAS','PANTALON')
        self.itemsDB=self.conn.getAll('ITEMS')