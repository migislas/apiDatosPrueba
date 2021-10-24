import unittest
from pandas.core import base
from lecturaCSV import\
                dataExtraction
import pandas as pd
import os
from pathlib import Path
from typing import List

class testCSVoppenning(unittest.TestCase):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows, self.columnsNames = dataExtraction()
        
    def testingColumnsTypes(self):
        assert isinstance(self.columnsNames, List)
    
    def testingColumnsNames(self):
        listaArchivo =  ['id', 
                         'date_updated', 
                         'vehicle_id',
                         'vehicle_label',
                         'vehicle_current_status',
                         'position_latitude',
                         'position_longitude',
                         'geographic_point',
                         'position_speed',
                         'position_odometer',
                         'trip_schedule_relationship',
                         'trip_id',
                         'trip_start_date',
                         'trip_route_id']
        self.assertListEqual(listaArchivo,
                    self.columnsNames)
    
    
    # def testingColumnsNames(self):
    #     valores, _ = dataExtraction()
        
    
   



