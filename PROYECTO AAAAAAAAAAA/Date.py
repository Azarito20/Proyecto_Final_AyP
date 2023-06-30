import typing
from datetime import date
from datetime import datetime

class Date:
    """
    Definición de la clase Date
    """
    def date_format(date):
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        messsage = f"{day} de {month} del {year}"

        return messsage

    now = datetime.now()
    print(date_format(now))
