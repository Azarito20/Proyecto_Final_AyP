import typing

class Product:
    """
    Definición de la clase Product con sus getter y setter
    """
    def __init__(self, name: str, description: str, price: int, category: str, availability: int):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__availability = availability

    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def get_price(self):
        return self.__price
    
    def get_category(self):
        return self.__category
    
    def get_availability(self):
        return self.__availability
    
    def set_name(self, name):
        self.__name = name

    def set_description(self, description):
        self.__description = description
    
    def set_price(self, price):
        self.__price = price
    
    def set_category(self, category):
        self.__category = category

    def set_availability(self, availability):
        self.__availability = availability

    def show(self):
        return f"""
        Nombre: {self.__name}
        Descripción {self.__description}
        Precio: {self.__price}
        Categoría: {self.__category}
        Inventario disponible: {self.__availability}
        """
