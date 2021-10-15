import csv
import timeit
from typing import (IO,
                    Iterator,
                    List, 
                    Text)
from src.schema import valores
import requests


def rowIterator(source: IO)->Iterator[List[Text]]:
    return csv.reader(source.splitlines(), delimiter=",")


def headerSpliter(
    row_iter:Iterator[List[Text]]
    )->List :
    columnsName = next(row_iter)
    return [row_iter, columnsName]

def singleRowValidation(rowInformation:List, 
                        ColumnName:List)->List:
    dictionary = {
            ColumnName[valor]:rowInformation[valor]
                for valor in range(len(ColumnName))}
    proccesedDictionary = valores.parse_obj(dictionary)
    proccesedList = [ elements for elements in
                     proccesedDictionary.dict().values()]
    return proccesedList

def validatingRows(rowsList:Iterator[List[Text]],
        columnsName:List[Text])->List:
    allDataValidated = list(map(lambda x:
        singleRowValidation(x,columnsName), rowsList))
    return allDataValidated

def dataExtraction():
    html = 'https://datos.cdmx.gob.mx/dataset/32b08754-ae92-4fbd-86d3-261cc64b6ca8/resource/ad360a0e-b42f-482c-af12-1fd72140032e/download/prueba_fetchdata_metrobus.csv'

    #nombre = "prueba_fetchdata_metrobus.csv"
    with requests.Session() as s:
        file = s.get(html)
        decoded_content = file.content.decode('utf-8')
        datos, columnsName = headerSpliter(rowIterator(decoded_content))
        listtoDB = validatingRows(datos, columnsName)
    return listtoDB, columnsName


