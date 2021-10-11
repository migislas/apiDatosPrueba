from typing import Generic, TypeVar, List, Union, Any, Tuple, Dict
from pydantic import (BaseModel, 
                      )

from datetime import datetime
generic = TypeVar('generic')

date = f'{datetime.today().year}-'\
            f'{datetime.today().month}-'\
            f'{datetime.today().day}'


class ExceptionsNotFound(BaseModel):
    codigoError: int
    descriptionCode: str
    fechaOperacion = date
    codigo:str

class PageNotFound(BaseModel):
    detalles: str
    codigo: str
    fechaOperacion = date


class ExceptionsBadData(BaseModel):
    codigo = '-'
    descriptionCode = 'Campo faltante o valores incorrectos'
    fechaOperacion = date
    datosIncorrectos: Union[Dict,str]