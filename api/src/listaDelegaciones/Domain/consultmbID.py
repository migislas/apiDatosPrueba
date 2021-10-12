from src.listaDelegaciones.Infraestructure.listaDelegaciones import\
            listaDelegaciones

from src.Utils.adquireCursor import adquireConnection

class consultaMannagement():
    

    def __call__(self, db):
        conexion = adquireConnection(db)
        response, estatus = listaDelegaciones()(conexion)
        return response, estatus