import typing
from Date import Date

class Shipment:
    """
    Definición de la clase Shipment con sus getter y setter
    """
    def __init__(self, code: str, date: Date, service: str, delivery, cost: float):
        self.__code = code
        self.__date = date
        self.__service = service
        self.__delivery = delivery
        self.__cost = cost

    def get_code(self):
        return self.__code
    
    def get_date(self):
        return self.__date
    
    def get_service(self):
        return self.__service
    
    def get_delivery(self):
        return self.__delivery
    
    def get_cost(self):
        return self.__cost
    
    def set_code(self, code):
        self.__code = code
    
    def set_date(self, date):
        self.__date = date

    def set_service(self, service):
        self.__service = service

    def set_delivery(self, delivery):
        self.__delivery = delivery

    def set_cost(self, cost):
        self.__cost = cost
    
    def show(self):
        return f"""
        Orden de compra: {self.__code}
        Fecha de la compra: {self.__date}
        Servicio del envío: {self.__service}
        Datos del motorizado: {self.__delivery}
        Costo del servicio: {self.__cost}
        """
