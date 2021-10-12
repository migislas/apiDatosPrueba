from fastapi import APIRouter, Request

from src.posicionID.Domain.consultmbID import\
                consultaMannagement

from src.posicionID.Domain.schemaConsult import\
                InputConsulta

from src.Utils.ResponseSchemas.responseSchema import\
                    ResponseBaseResult
from src.Utils.ErrorHandler.ErrorMannaging import\
                    NotFoundException
from src.Utils.ResponseSchemas.exceptionSchema import (
                        ExceptionsNotFound,
                        ExceptionsBadData)
                  
router = APIRouter() 

responses = {
    '404': {"model": ExceptionsNotFound},
    '400': {"model": ExceptionsBadData},
}



@router.post("/ConsultaPosicionID", 
             response_model=ResponseBaseResult, 
             responses={**responses},
             tags=["Consulta"])
async def consultaMetrobusID(request: Request, 
                        datosentrada:InputConsulta):
    
    Response, estatus = consultaMannagement()(
                        request.app.state.db.pool,
                        datosentrada.dict())
    if estatus:
        return ResponseBaseResult(codigo=1,
                            mensaje='Consulta Exitosa', 
                            resultado = Response)
    else:
        raise NotFoundException(detail={
            'mensaje':'Error consulta',
                                    'codigo':-1})
    
 