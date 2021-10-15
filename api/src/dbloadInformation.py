import psycopg2

import csv
import timeit
import requests


from src.Utils.adquireCursor import OnlyConection
from src.lecturaCSV import dataExtraction


async def datatoDb(db):
    conexion = OnlyConection(db)
    with conexion as db:
        print("conexion Iniciada del Pool")
        cursor = db.cursor()
        listatoDB,_ = dataExtraction()
        cursor.execute("TRUNCATE informacion")
        cursor.executemany("INSERT INTO informacion  (id, date_updated,vehicle_id,vehicle_label,vehicle_current_status,position_latitude,position_longitude,geographic_point,position_speed,position_odometer, trip_schedule_relationship,trip_id,trip_start_date,trip_route_id) VALUES(%s, %s, %s,%s,%s,%s, %s, ST_GeomFromText(%s),%s,%s,%s,%s,%s,%s)", listatoDB)
        db.commit()
        print("Datos actualizatos en tabla informacion")
