from fastapi import FastAPI

#Se agregan las rutas por Dominio

#from src.user.dbAquirePool import get_connection
from src.Utils.ErrorHandler.ErrorMannaging import  add_exception_handlers
from fastapi_utils.tasks import repeat_every
from src.core.dbConectionMannager import database_instance

from src.idLIstaMetrobus.Application import \
                    idLIsta

from src.posicionID.Application import \
                    idPosicion

from src.listaDelegaciones.Application import \
                    delegacionesLista

from src.metrobusLabelAlcaldia.Application import \
                    idmetrobusesalcaldia

from src.dbloadInformation import datatoDb
from src.alcaldias import alcaldiasNombres


import asyncio
                  


def get_app() -> FastAPI:
    app = FastAPI(
        title="Api Consulta de datos Metrobus",
        description="API",
        version="1.0.0",
    )
    add_exception_handlers(app)
    return app

app = get_app()

app.include_router(idLIsta.router)
app.include_router(idPosicion.router)

app.include_router(delegacionesLista.router)
app.include_router(idmetrobusesalcaldia.router)

@app.on_event("startup")
async def startup():
    await database_instance.connect()
    
    print("Pool de conexiones Creado")
    app.state.db = database_instance
    #alcaldias = alcaldiasNombres()
    #await datatoDb(app.state.db.pool)
    #print("Inicio Proceso de insertar a base datos de alcaldias donde hay metrobus")
    #await alcaldias.alcaldias(app.state.db.pool)
    #print("ok")
    
     
    
    
   
@app.on_event("shutdown")
def close_database_connection_pools():
    try:
        app.state.db.pool.close()
        print("Conexion a Base de datos Cerrada")
    except Exception as e:
        print(e)



# @app.on_event("startup")
# @repeat_every(seconds=3600 )  #se actualiza cada 60 segundos
# async def InicioProceso() -> None:
#     print("+++++++++++++++++")
#     print("Inicio Proceso de insertar a base nuvos datos del MB")
#     await datatoDb(app.state.db.pool)
#     print("ok")
    
    

   
    
    
    