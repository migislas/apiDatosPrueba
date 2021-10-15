from pydantic import (BaseModel,
                      validator)
from typing import List
class valores(BaseModel):
    id:int
    date_updated:str
    vehicle_id:int
    vehicle_label:str
    vehicle_current_status:str
    position_latitude:float
    position_longitude:float
    geographic_point: str
    position_speed: float
    position_odometer: int
    trip_schedule_relationship:int
    trip_id: int
    trip_start_date:str
    trip_route_id: int
    
    @validator("geographic_point", pre=True, always=True)
    def geographicpointsChangeValue(cls, v):
        if v == '':
            return "','"
        else:
            try:
                strSpliting = v.split(",")
                valor0 = strSpliting[1]
                valor1 = strSpliting[0]
                cadena = f'point({valor0} {valor1})'
                return cadena
            except:
                return "999,999"
    
    
    @validator("trip_start_date", pre=True, always=True)
    def tripStartDate(cls, v):
        if v == '':
            return "9999/99/99"
        else:
            try:
                year = v[0:4]
                month = v[4:6]
                day = v[6:8]
                return f'{year}-{month}-{day}'
            except:
                return "9999/99/99"
        
    
    @validator('trip_id', pre=True, always=True)
    def tripIDvalidatos(cls, v):
        if v =='':
            return -9999
        else:
            try:
                valor = int(float(v))
                return valor
            except:
                return -9999
    
    @validator('trip_route_id', pre=True, always=True)
    def tripRouteIdvalidatos(cls, v):
        if v =='':
            return -9999
        try:
            valor = int(float(v))
            return valor
        except:
            return -9999
