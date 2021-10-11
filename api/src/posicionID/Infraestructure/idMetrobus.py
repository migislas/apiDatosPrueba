import psycopg2


class idMetrobusConsulta():
    def __init__(self, idMetrobus):
        self.idMetrobus = idMetrobus


    def idLIsta(self):
        try:
            print(self.idMetrobus)
            self.cursor.callproc('idBusqueda',[self.idMetrobus])
            respuesta =  self.cursor.fetchall()
            
            if respuesta:
                fecha = respuesta[0][0]
                fechastr = f'{fecha[0:4]}-{fecha[4:6]}-{fecha[6:8]}'
                punto = respuesta[0][1].split(",")
                Latitud = punto[0]
                Longitud = punto[1]
                self.estatus = True
                diccionarioRespuesta = {'fecha':fechastr, 'posicion':{
                    'latitud':Latitud,
                    'longitud':Longitud}
                    }
                return diccionarioRespuesta, self.estatus

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
            
       
        
    def __call__(self, db):
        with db as self.cursor:

            Respuesta, Bandera = self.idLIsta()
            print(Respuesta)
            if Bandera:
                return Respuesta, self.estatus
            





