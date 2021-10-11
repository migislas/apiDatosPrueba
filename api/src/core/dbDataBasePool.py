import psycopg2
from psycopg2 import pool
from .config import  DATABASE, USER, PASSWORD, HOST, PORT


class Database:
    def __init__(self) -> None:
        self.pool = None
        self.con = None
    
    async def connect(self):
        if not self.pool:
            try:
                print("Haciendo el Pool de conexiones")
                self.pool = psycopg2.pool.SimpleConnectionPool(
                    1,
                    3,
                    user=USER,
                    password=PASSWORD,
                    host=HOST,
                    port=PORT,
                    database=DATABASE
        
                    )
                print(self.pool)
                return self.pool

            except Exception as e:
                raise e
  