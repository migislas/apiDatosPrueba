from src.posicionID.Infraestructure.idMetrobus import\
            idMetrobusConsulta

from src.Utils.adquireCursor import adquireConnection

class consultaMannagement():
    

    def __call__(self, db,datos):
        print(datos['idMetrobus'])
        conexion = adquireConnection(db)
        response, estatus = idMetrobusConsulta(datos['idMetrobus'])(conexion)
        return response, estatus