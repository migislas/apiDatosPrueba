import psycopg2

import csv
import timeit
import requests
from typing import (IO,
                    Iterator,
                    List, 
                    Text,
                    Union,
                    Iterable)

from src.Utils.adquireCursor import OnlyConection


def row_iter(source)->Iterator[List[Text]]:
    return csv.reader(source.splitlines(), delimiter=",")


def head_split_fixed(
    row_iter:Iterator[List[Text]]
    ) -> Iterator[List[Text]]:
    headersMetrobus = next(row_iter)
    print(headersMetrobus)
    columns = next(row_iter)
    return row_iter

def readingCSV(html:str)->List:
    with requests.Session() as s:
            file = s.get(html)
            decoded_content = file.content.decode('utf-8')
            datos = head_split_fixed(row_iter(decoded_content))
            lista  = list(datos)
    return lista


async def datatoDb(db):
    conexion = OnlyConection(db)
    with conexion as db:
        print("conexion Iniiciada del Pool")
        cursor = db.cursor()
        html = 'https://datos.cdmx.gob.mx/dataset/32b08754-ae92-4fbd-86d3-261cc64b6ca8/resource/ad360a0e-b42f-482c-af12-1fd72140032e/download/prueba_fetchdata_metrobus.csv'
        lista = readingCSV(html)
        cursor.execute("TRUNCATE informacion")
        cursor.executemany("INSERT INTO informacion  (idMetrobus, date_updated,vehicle_id,vehicle_label,vehicle_current_status,position_latitude,position_longitude,posicionPunto,position_speed,position_odometer, trip_schedule_relationship,trip_id,tstartDate,trip_route_id) VALUES(%s, %s, %s,%s,%s,%s, %s, %s,%s,%s,%s,%s,%s,%s)", lista)
        db.commit()
        print("Datos actualizatos en tabla informacion")
