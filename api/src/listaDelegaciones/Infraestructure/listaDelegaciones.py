import psycopg2

class listaDelegaciones():

    def idLIsta(self):
        try:
            self.cursor.callproc('alcaldiaBusqueda')
            respuesta =  self.cursor.fetchall()
            if respuesta:
                listaID=[elementos[0] for elementos in respuesta]
                self.estatus = True
                diccionarioRespuesta = {'respuesta':listaID}
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
            





