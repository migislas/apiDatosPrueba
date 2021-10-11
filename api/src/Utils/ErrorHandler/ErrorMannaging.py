from __future__ import annotations
from fastapi import (Request,
                    HTTPException,
                    status)
from fastapi.responses import JSONResponse
from typing import Optional, Dict, Any,Union
import json
from fastapi.exceptions import (
                            RequestValidationError, 
                            ValidationError,
                            HTTPException)

from src.Utils.ResponseSchemas.exceptionSchema import (ExceptionsNotFound,
                    ExceptionsBadData,
                    PageNotFound)
class BadRequestException(RequestValidationError, ValidationError):
    ...

   
class NotFoundException(HTTPException):
    def __init__(
            self,
            status_code: int = status.HTTP_404_NOT_FOUND,
            detail: Any = None,
            headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(status_code=status_code, detail=detail)
        self.headers = headers

async def not_found_error_handler(
        _: Request,
        exc: HTTPException,
        msg: str = ''
    ) -> JSONResponse:
    detalles = exc.detail if exc.detail else constants.HTTP_404_NOT_FOUND
    if isinstance(detalles, Dict):
        content = ExceptionsNotFound(
            codigoError=detalles['codigo'],
            codigo=status.HTTP_404_NOT_FOUND,
            descriptionCode=detalles['mensaje']
            )
        content = json.loads(content.json())
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, 
                        content=content)
    else:
        content = PageNotFound(
            detalles='Recurso No Encontrado',
            codigo=status.HTTP_404_NOT_FOUND,
            )
        content = json.loads(content.json())
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, 
                        content=content)




def add_exception_handlers(app:FastAPI)->None:
    """
        Esta Funcion agrega ecepciones para mostrar a los usuarios
        
    """
    
 
    app.add_exception_handler(NotFoundException,
                              not_found_error_handler)
    
    app.add_exception_handler(404,
                              not_found_error_handler)
