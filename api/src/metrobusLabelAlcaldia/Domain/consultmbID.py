from src.metrobusLabelAlcaldia.Infraestructure.idAlcaldia import\
            idMetrobusConsulta

from src.Utils.adquireCursor import adquireConnection

class consultaMannagement():
    

    def __call__(self, db,datos):
        print(datos['idAlcaldia'])
        conexion = adquireConnection(db)
        response, estatus = idMetrobusConsulta(datos['idAlcaldia'])(conexion)
        return response, estatus