import typing

class Receipt:
    """
    Definición de la clase Receipt con sus getter y setter
    """
    def __init__(self, subtotal, discount, iva, igtf, total):
        self.__subtotal = subtotal
        self.__discount = discount
        self.__iva = iva
        self.__igtf = igtf
        self.__total = total

    def get_subtotal(self):
        return self.__subtotal
    
    def get_discount(self):
        return self.__discount
    
    def get_iva(self):
        return self.__iva
    
    def get_igtf(self):
        return self.__igtf
    
    def get_total(self):
        return self.__total
    
    def set_subtotal(self, subtotal):
        self.__subtotal = subtotal

    def set_discount(self, discount):
        self.__discount = discount

    def set_iva(self, iva):
        self.__iva = iva
    
    def set_igtf(self, igtf):
        self.__igtf = igtf
    
    def set_total(self, total):
        self.__total = total
    
    def show(self):
        return f"""
        Subtotal: {self.__subtotal}
        Dscuento: {self.__discount}
        IVA: {self.__iva}
        IGTF: {self.__igtf}
        Total: {self.__total}
        """
