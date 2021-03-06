from fastapi import APIRouter, Request

from src.listaDelegaciones.Domain.consultmbID import\
                consultaMannagement

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


@router.get("/listaDelegaciones", 
             response_model=ResponseBaseResult, 
             responses={**responses},
             tags=["Consulta"])
async def listaDelegaciones(request: Request):
    
    Response, estatus = consultaMannagement()(
                        request.app.state.db.pool)
    if estatus:
        return ResponseBaseResult(codigo=1,
                            mensaje='Consulta Exitosa', 
                            resultado = Response)
    else:
        raise NotFoundException(detail={
            'mensaje':'Error de consulta',
                                    'codigo':-1})
    
 