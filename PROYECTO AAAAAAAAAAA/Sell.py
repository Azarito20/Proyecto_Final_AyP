import typing
from Client import Client
from Product import Product
from Date import Date

class Sell:
    """
    Definición de la clase Sell con sus getter y setter
    """
    def __init__(self, client: Client, product, quantity, payment: str, shipment: str, date: Date):
        self.__client = client
        self.__product = product
        self.__quantity = quantity
        self.__payment = payment
        self.__shipment = shipment
        self.__date = date

    def get_client(self):
        return self.__client
    
    def get_product(self):
        return self.__product
    
    def get_quantity(self):
        return self.__quantity
    
    def get_payment(self):
        return self.__payment
    
    def get_shipment(self):
        return self.__shipment
    
    def get_date(self):
        return self.__date
    
    def set_client(self, client):
        self.__client = client

    def set_product(self, product):
        self.__product = product

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_payment(self, payment):
        self.__payment = payment

    def set_shipment(self, shipment):
        self.__shipment = shipment

    def set_date(self, date):
        self.__date = date

    def show(self):
        return f"""
        Cliente: {self.__client}
        Producto: {self.__product}
        Cantidad de cada producto: {self.__quantity}
        Método de pago: {self.__payment}
        Método de envío: {self.__shipment}
        Fecha: {self.__date}
        """
