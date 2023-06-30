import typing

class Client:
    """
    Definición de la clase Client con sus getter y setter
    """
    def __init__(self, name: str, status: str, ci: str, email: str, adress: str, phone: str):
        self.__name = name
        self.__status = status
        self.__ci = ci
        self.__email = email
        self.__adress = adress
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def get_status(self):
        return self.__status
    
    def get_ci(self):
        return self.__ci
    
    def get_email(self):
        return self.__email
    
    def get_adress(self):
        return self.__adress
    
    def get_phone(self):
        return self.__phone
    
    def set_name(self, name):
        self.__name = name

    def set_status(self, status):
        self.__status = status

    def set_ci(self, ci):
        self.__ci = ci

    def set_email(self, email):
        self.__email = email

    def set_adress(self, adress):
        self.__adress = adress

    def set_phone(self, phone):
        self.__phone = phone

    def show(self):
        return f"""
        Nombre: {self.__name}
        Tipo de cliente: {self.__status}
        Cédula/RIF: {self.__ci}
        Correo electrónico: {self.__email}
        Dirección de envío: {self.__adress}
        Teléfono: {self.__phone}
        """
    