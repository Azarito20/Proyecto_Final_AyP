import typing
from Client import Client

class Payment:
    """
    Definición de la clase Payment con sus getter y setter
    """
    def __init__(self, client: Client, total: float, coin: str, kind, date):
        self.__client = client
        self.__total = total
        self.__coin = coin
        self.__kind = kind
        self.__date = date

    def get_client(self):
        return self.__client
    
    def get_total(self):
        return self.__total
    
    def get_change(self):
        return self.__coin
    
    def get_kind(self):
        return self.__kind
    
    def get_date(self):
        return self.__date
    
    def set_client(self, client):
        self.__client = client

    def set_total(self, total):
        self.__total = total

    def set_change(self, coin):
        self.__coin = coin

    def set_kind(self, kind):
        self.__kind = kind

    def set_date(self, date):
        self.__date = date

    def show(self):
        return f"""
        Cliente: {self.__client}
        Monto total: {self.__total}
        Moneda del pago: {self.__coin}
        Tipo de pago: {self.__kind}
        Fecha del pago: {self.__date}
        """
