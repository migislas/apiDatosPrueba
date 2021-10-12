from src.Utils.adquireCursor import OnlyConection
import psycopg2
from shapely.geometry import Point
import os
import geopandas as gp

class alcaldiasNombres():
    def __init__(self):
        self.listaAlcaldiasnorpetidas = []
        self.alcaldiasTotales = []

    def listaPuntos(self):
        
        self.listaTotalPuntos = [[Point(float(x[0].split(',')[1]),float(x[0].split(',')[0]))] 
                                            for x in self.respuesta]

    def estaDentroDelPoligon(self, punto:Point, 
                        numeroAlcaldia:int)->str:
        
        estaDentro = punto.within(self.listaAlcaldias[numeroAlcaldia][0])

        if estaDentro == True:
            nombre = self.listaAlcaldias[numeroAlcaldia][1]
            if nombre not in self.listaAlcaldiasnorpetidas:
                self.listaAlcaldiasnorpetidas.append(nombre)
                self.alcaldiasTotales.append([nombre])
        else:
            if numeroAlcaldia -1 < 0:
                return None
            numeroAlcaldia = numeroAlcaldia -1
            self.estaDentroDelPoligon(punto, numeroAlcaldia)

        

        
    def nombresAlcaldiasconMetrobus(self):
        os.system("bash alcaldias.sh")
        directorio = os.getcwd()
        archivo = directorio + '/alcaldiasm/limite_de_las_alcaldias/limite_de_las_alcaldias.shp'
        df = gp.read_file(archivo)
        self.listaAlcaldias = [[df["geometry"].iloc[valor],df["nomgeo"][valor]] 
                                    for valor in range(16)]
        self.numeroAlcaldias = len(self.listaAlcaldias) -1
        self.listaPuntos()
        alcaldias = list(map(lambda x: self.estaDentroDelPoligon(x[0],self.numeroAlcaldias),
                                         self.listaTotalPuntos  ))
        print(self.alcaldiasTotales)
        


    def lista(self,db):
        try:
            cursor = db.cursor()
            cursor.callproc('Coordenadas')
            self.respuesta =  cursor.fetchall()
            print(len(self.respuesta))
            if self.respuesta:
                self.nombresAlcaldiasconMetrobus()
                print("Lista de alcaldias obtenida")
                cursor.execute("TRUNCATE alcaldias")
                cursor.executemany("INSERT INTO alcaldias  (nombreAlcaldia) VALUES(%s)", self.alcaldiasTotales)
                db.commit()
                print("Lista de alcaldias actualizadas")

            else:
                diccionarioRespuesta = {"Respuesta":
                    "No se encontro información para estos parametros"}
                self.estatus = True
                return diccionarioRespuesta, self.estatus
        except psycopg2.OperationalError as e:
            errorObj, = e.args
            print("Error Code:", errorObj.code)
            print("Error mssg:",  errorObj.message)
            self.__message = 'FAILED with error:' + errorObj.message 
            self.estatus = None, False


    async def alcaldias(self,db):
        cursor = OnlyConection(db)
        with cursor as db:
            self.lista(db)
        