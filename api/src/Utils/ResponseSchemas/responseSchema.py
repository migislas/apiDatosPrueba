from typing import Generic, TypeVar, Optional, List, Union, Any, Tuple, Dict
from pydantic import (BaseModel, 
                      Field
                      )
from pydantic.generics import GenericModel
from src.Utils.DatesValidations import StrictDate
from datetime import datetime
generic = TypeVar('generic')

date = f'{datetime.today().year}-'\
            f'{datetime.today().month}-'\
            f'{datetime.today().day}'


class Responsetype(BaseModel):
    statusCode: int
    descriptionCode: str
    fechaOperacion = date



class ResponseBaseOnlyMessage(GenericModel, Generic[generic]):
    """
    Este es el esquema de respuesta:\n
        \n Mensaje: contiene un mensaje
        \n Resultado: Contiene el resultado de la consulta u operación
    """
    codigo: str
    resultado: Responsetype
    fechaOperacion = date

class ResponseBaseResult(GenericModel, Generic[generic]):
    """
    Este es el esquema de respuesta:\n
        \n Mensaje: contiene un mensaje
        \n Resultado: Contiene el resultado de la consulta u operación
    """
    codigo: str
    mensaje: str
    resultado: Union[Dict,List]
    fechaOperacion = date