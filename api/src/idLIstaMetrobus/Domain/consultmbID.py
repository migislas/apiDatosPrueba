from src.idLIstaMetrobus.Infraestructure.idMetrobus import\
            idMetrobusConsulta

from src.Utils.adquireCursor import adquireConnection

class consultaMannagement():
    

    def __call__(self, db):
        conexion = adquireConnection(db)
        folioGenerator, estatus = idMetrobusConsulta()(conexion)
        return folioGenerator, estatus