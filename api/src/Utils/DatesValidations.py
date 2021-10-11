from pydantic import BaseModel, validator, PydanticValueError
from datetime import date, datetime,timedelta
from pydantic import BaseModel
from pydantic.datetime_parse import parse_date
import re
date_expr = r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})'
date_re = re.compile(f'{date_expr}$')

class DateError(PydanticValueError):
    code = 'date'
    msg_template = 'invalid date'

def validate_date(v) -> date:
    if isinstance(v, (int, float)):
        raise DateError()
    if date_re.match(v) is None:
        raise DateError()
    fecha =  datetime.strptime(v, "%Y-%m-%d")
    if not datetime(year=1980, month=1, day=1) <= fecha <= datetime(year=2500, month=12, day=31):
            raise DateError()
    return fecha


class StrictDate(date):
    @classmethod
    def __get_validators__(cls):
        yield validate_date



class DateErrorTwoDays(PydanticValueError):
    code = 'dateCancel'
    msg_template = 'invalid date'

def validatetwodays(v) -> date:
    if isinstance(v, (int, float)):
        raise DateError()
    if date_re.match(v) is None:
        raise DateError()
    fecha =  datetime.strptime(v, "%Y-%m-%d")
    fechaHoymasDosDias = datetime.today() + timedelta(2)
    if not fechaHoymasDosDias <= fecha:
            raise DateErrorTwoDays()
    return fecha


class twoDaysValidation(date):
    @classmethod
    def __get_validators__(cls):
        yield validatetwodays


    
    
   
