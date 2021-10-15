import psycopg2


class idMetrobusConsulta():
    def __init__(self, idalcaldia):
        self.alcaldia = idalcaldia


    def idLIsta(self):
        try:
            print(self.alcaldia)
            self.cursor.callproc('alcaldiaBusquedaUnidades',[self.alcaldia])
            respuesta =  self.cursor.fetchall()
            
            if respuesta:
                lista = [valorUnidad[0] for valorUnidad in respuesta ]
                self.estatus = True
                diccionarioRespuesta = {'unidades':lista}
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
            





