from src.Utils.adquireCursor import OnlyConection
import psycopg2
from shapely import wkt
import os
import geopandas as gp
from shapely.wkb import dumps as wkb_dumps


class alcaldiasNombres():
    def __init__(self):
       self.lista = []
        
    def nombresAlcaldiasconMetrobus(self):
        os.system("bash alcaldias.sh")
        directorio = os.getcwd()
        archivo = directorio + '/alcaldiasm/limite_de_las_alcaldias/limite_de_las_alcaldias.shp'
        df = gp.read_file(archivo)
        df["geom_wkb"] = df["geometry"].apply(lambda x: wkb_dumps(x))
        self.lista = [[valor+1,df['nomgeo'].iloc[valor],df["geom_wkb"].iloc[valor]] for valor in range(len(df))]
        


    def insertAlcaldiaInformation(self,db):
        try:
            cursor = db.cursor()
            self.nombresAlcaldiasconMetrobus()
            cursor.execute("TRUNCATE alcaldias")
            cursor.executemany("INSERT INTO alcaldias  (idAlcaldia,nombreAlcaldia,geometryAlcaldia) VALUES(%s,%s,ST_GeomFromWKB(%s))", self.lista)
            db.commit()
            print("Lista de alcaldias actualizadas")
        except psycopg2.OperationalError as e:
            errorObj, = e.args
            print("Error Code:", errorObj.code)
            print("Error mssg:",  errorObj.message)
            self.__message = 'FAILED with error:' + errorObj.message 
            self.estatus = None, False


    async def alcaldias(self,db):
        cursor = OnlyConection(db)
        with cursor as db:
            self.insertAlcaldiaInformation(db)
        