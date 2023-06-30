import typing
from Client import Client
from Payment import Payment
from Product import Product
from Sell import Sell
from Shipment import Shipment
from Date import Date
from Recipt import Receipt
import json
from urllib.request import urlopen
import requests
#Hacer funciones de estadisticas
class Store:
    """
    Definición de la clase Store con sus getter y setter
    """
    def __init__(self):
        self.__clients =[]
        self.__payments = []
        self.__products = []
        self.__sells = []
        self.__shipments = []
    
    def get_clients(self):
        return self.__clients
    
    def get_payments(self):
        return self.__payments
    
    def get_products(self):
        return self.__products
    
    def get_sells(self):
        return self.__sells
    
    def get_shipments(self):
        return self.__shipments
    
    def set_clients(self, clients):
        self.__clients = clients

    def set_payments(self, payments):
        self.__payments = payments

    def set_products(self, products):
        self.__products = products

    def set_sells(self, sells):
        self.__sells = sells
    
    def set_shipments(self, shipments):
        self.__shipments = shipments

    def show_products(self):
        """
        Función que retorna un enlistado con código de los productos en la tienda
        """
        for product in self.__products:
            print(product.show())
        while True:
            for code in range(len(self.__products)):
                for object in self.__products:
                    return print(f"{code+1}. {object}")
    
    def show_clients(self):
        """
        Función que retorna un enlistado con código de los clientes en la tienda
        """
        for client in self.__clients:
            print(client.show())
        while True:
            for code in range(len(self.__clients)):
                for object in self.__clients:
                    return print(f"{code+1}. {object}")

    def load_products(self):
        """
        Función para añadir los productos desde la API proporcionada a la lista de productos de la tienda
        """
        payload = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json")
        payload = payload.json()
        for dicc in payload:
            name = dicc["name"]
            description = dicc["description"]
            price = dicc["price"]
            category = dicc["category"]
            availability = dicc["quantity"]
            new_product = Product(name, description, price, category, availability)
            self.__products.append(new_product)

    def add_product(self):
        """
        Función para agregar productos nuevos a la tienda mediante inputs
        """
        name = input("Ingrese el nombre del producto: ")
        description = input("Ingrese la descripción del producto: ")
        price = input("Ingrese el precio del producto: ")
        category = input("Ingrese la categoría del producto: ")
        availability = input("Ingrese la cantidad de productos: ")
        new_product = Product(name, description, price, category, availability)
        self.__products.append(new_product)
    
    def search_product(self):
        """
        Función para filtrar los productos por Nombre, Precio, Categoría y disponibilidad. Retorna los productos filtrados
        """
        filtered_objects = []
        option = input("""
        1. Nombre
        2. Precio
        3. Categoría
        4. Disponibilidad
        Escoja la opción a filtrar: 
        """)
        while True:
            if option == "1":
                name = input("Ingrese el nombre del producto: ")
                for obj in self.__products:
                    if getattr(obj, "name") == name:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen productos con el nombre ingresado")
                        break

            elif option == "2":
                price = input("Ingrese el precio del producto: ")
                for obj in self.__products:
                    if getattr(obj, "price") == price:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen productos con el precio ingresado")
                        break
            
            elif option == "3":
                category = input("Ingrese la categoría del producto: ")
                for obj in self.__products:
                    if getattr(obj, "category") == category:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen productos con la categoría ingresada")
                        break
            
            elif option == "4":
                availability = input("Ingrese la cantidad de productos: ")
                for obj in self.__products:
                    if getattr(obj, "availability") <= int(category):
                        filtered_objects.append(obj)
                    else:
                        print("Error!, no existen productos con la cantidad ingresada")
                        break
            
            else:
                option = input("Error! Seleccione una opción válida")
            
            return print(filtered_objects)

    def edit_product(self):
        """
        Función para editar la información dentro de los objetos Product
        """
        self.show_products()
        code = input("Ingrese el código del producto que desea editar: ")
        for product in self.__products:
            while True:
                if product.code == code - 1:
                    option = input("""
                    1. Nombre
                    2. Descripción
                    3. Precio
                    4. Categoría
                    Elija el código del atributo a cambiar: 
                    """)
                    if option == "1":
                        product.name = input("Ingrese el nuevo nombre: ")
                    elif option == "2":
                        product.description = input("Ingrese la nueva descripción")
                    elif option == "3":
                        product.price = input("Ingrese el nuevo precio: ")
                    elif option == "4":
                        product.category = input("Ingrese la nueva categoría")
                    else:
                        print("Error! código no válido")

    def delete_product(self):
        """
        Función que permite eliminar los productos de la lista de la tienda
        """
        for product in self.__products:
            print(product.show())
        while True:
            for code in range(len(self.__products)):
                for object in self.__products:
                    print(f"{code+1}. {object}")
        
            option = input("Ingrese el número del producto que desea eliminar: ")
            while not option.isnumeric() or (int(option) -1) not in range(len(self.__products)):
                option = input("Error! Ingrese el número del producto que desea eliminar: ")

            if option == code+1:
                self.__products.remove(self.__products[option-1])
    
    def register_sell(self):
        """
        Función para registrar un objeto Sell dentro de la lista de ventas
        """
        client = input("Ingrese el nombre del cliente")
        products = []
        shopcart = []
        payment = input("Ingrese el método de pago")
        shipment = input("Ingrese el método de envío")
        date = input("Ingrese la fecha de la venta: ")
        while True: 
            for code in range(len(self.__products)):
                for product in self.__products:
                    print(f"{code+1}. {product}")
                    option = input("Seleccioné el código del producto que desea seleccionar")
                    if code == option-1:
                        products.append(product[code])
                        option2 = input(f"Ingrese la cantidad de {product} que desea comprar: ")
                        if int(option2) <= product.availability:
                            product.availability - option2
                            shopcart.append(option2)
                        else:
                            print("Error! no se posee la cantidad solicitada")
                    else:
                        print("Error! el código no es válido")
            new_sell = Sell(client, products, shopcart, payment, shipment, date)
            self.__sells.append(new_sell)

    def generate_sell(self): #ayuda
        pass

    def search_sell(self):
        """
        Función para filtrar las ventas por Cliente, Fecha y Monto total. Retorna las ventas filtrados
        """
        filtered_objects = []
        option = input("""
        1. Cliente
        2. Fecha de la venta
        3. Monto total de la venta
        Escoja la opción a filtrar: 
        """)
        while True:
            if option == "1":
                client = input("Ingrese el nombre del cliente: ")
                for obj in self.__sells:
                    if getattr(obj, "client") == client:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen clientes con el nombre ingresado")
                        break

            elif option == "2":
                date = input("Ingrese la fecha de la venta: ")
                for obj in self.__sells:
                    if getattr(obj, "date") == date:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen ventas con la fecha ingresada")
                        break
            
            elif option == "3":
                total = input("Ingrese el monto total de la venta: ")
                for obj in self.__sells:
                    if getattr(obj, "total") == total:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen ventas con el total ingresado")
                        break
            else:
                option = input("Error! Seleccione una opción válida")
            
            return print(filtered_objects)

    def register_client(self):
        """
        Función para registrar un objeto Client dentro de la lista de clientes
        """
        name = input("Ingrese nombre y apellido o razón social del cliente: ")
        status = input("Ingrese si el cliente es Natural o Jurídico: ")
        id = input("Ingrese la cédula o RIF del cliente: ")
        email = input("Ingrese el correo electrónico del cliente: ")
        adress = input("Ingrese la dirección de envío del cliente: ")
        phone = input("Ingrese el número de teléfono del cliente: ")
        new_client = Client(name, status, id, email, adress, phone)
        self.__clients.append(new_client)

    def edit_client(self):
        """
        Función para editar la información dentro de los objetos Client
        """
        self.show_clients()
        name = input("Ingrese el nombre del cliente que desea editar: ")
        for client in self.__products:
            while True:
                if client.name == name:
                    option = input("""
                    1. Nombre
                    2. Tipo de cliente
                    3. Cédula/RIF
                    4. Correo electrónico
                    5. Dirección de envío
                    6. Teléfono
                    Elija el código del atributo a cambiar: 
                    """)
                    if option == "1":
                        client.name = input("Ingrese el nuevo nombre: ")
                    elif option == "2":
                        client.status = input("Ingrese el nuevo tipo de cliente: ")
                    elif option == "3":
                        client.ci = input("Ingrese la nueva cédula: ")
                    elif option == "4":
                        client.email = input("Ingrese el nuevo correo: ")
                    elif option == "5":
                        client.adress = input("Ingrese la nueva dirección")
                    elif option == "6":
                        client.phone = input("Ingrese el nuevo teléfono: ")
                    else:
                        print("Error! código no válido")

    def delete_client(self):
        """
        Función que permite eliminar los clientes de la lista de la tienda
        """
        print(Client.show())
        while True:
            for code in range(len(self.__clients)):
                for client in self.__clients:
                    print(f"{code+1}. {client}")
        
            option = input("Ingrese el número del cliente que desea eliminar: ")
            while not option.isnumeric() or (int(option) -1) not in range(len(filter)):
                option = input("Error! Ingrese el número del cliente que desea eliminar: ")

            if option == code+1:
                self.__products.remove(self.__client[option-1])

    def search_client(self):
        """
        Función para filtrar los clientes por Documento y Correo. Retorna los clientes filtrados
        """
        filtered_objects = []
        option = input("""
        1. Cédula o RIF
        2. Correo electrónico
        Escoja la opción a filtrar: 
        """)
        while True:
            if option == "1":
                ci = input("Ingrese la cédula o RIF del cliente: ")
                for obj in self.__clients:
                    if getattr(obj, "ci") == ci:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen clientes con la cédula o RIF ingresada")
                        break

            elif option == "2":
                email = input("Ingrese el correo electrónico del cliente: ")
                for obj in self.__clients:
                    if getattr(obj, "email") == email:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen clientes con el email ingresado")
                        break
            
            else:
                option = input("Error! Seleccione una opción válida")
            
            return print(filtered_objects)

    def register_payment(self):
        """
        Función para registrar un objeto Payment dentro de la lista de pagos
        """
        name = input("ingrese el nombre del cliente: ")
        total = input("Ingrese el monto total de la compra: ")
        coin = input("Ingrese la moneda de pago(Bolívares/Dólares): ")
        kind = input("Ingrese el método de pago: ")
        date = input("Ingrese la fecha del pago: ")
        new_payment = Payment(name, total, coin, kind, date)
        self.__payments.append(new_payment)

    def search_payment(self):
        """
        Función para filtrar los pagos por Cliente, Fecha, Tipo de Pago y Moneda de pago. Retorna los pagos filtrados
        """
        filtered_objects = []
        option = input("""
        1. Cliente
        2. Fecha
        3. Tipo de pago
        4. Moneda de pago
        Escoja la opción a filtrar: 
        """)
        while True:
            if option == "1":
                name = input("Ingrese el nombre del cliente: ")
                for obj in self.__payments:
                    if getattr(obj, "name") == name:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen pagos con el cliente ingresado")
                        break

            elif option == "2":
                date = input("Ingrese la fecha del pago: ")
                for obj in self.__payments:
                    if getattr(obj, "date") == date:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen pagos con la fecha ingresada")
                        break
            
            elif option == "3":
                kind = input("Ingrese el tipo de pago: ")
                for obj in self.__payments:
                    if getattr(obj, "kind") == kind:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen pagos con el tipo ingresado")
                        break
            
            elif option == "4":
                coin = input("Ingrese el tipo de moneda del pago: ")
                for obj in self.__payments:
                    if getattr(obj, "coin") == coin:
                        filtered_objects.append(obj)
                    else:
                        print("Error!, no existen pagos con la moneda ingresada")
                        break
            
            else:
                option = input("Error! Seleccione una opción válida")
            
            return print(filtered_objects)

    def register_shipment(self): #Función Incompleta
        """
        Función para registrar un objeto Shipment dentro de la lista de envíos
        """
        code = input("Ingrese el orden de compra: ")
        date = input("Ingrese la fecha del envío: ")
        service = input("Ingrese el tipo de servicio: ")
        delivery = input("Ingrese los datos del motorizado: ") #Crear clase motorizado y añadir el objeto??
        cost = input("Ingrese el costo del envío: ")
        new_shipment = Shipment(code, date, service, delivery, cost)
        self.__shipments.append(new_shipment)
    
    def search_shipment(self):
        """
        Función para filtrar los envíos por Cliente y Fecha. Retorna los envíos filtrados
        """
        filtered_objects = []
        option = input("""
        1. Cliente
        2. Fecha
        Escoja la opción a filtrar: 
        """)
        while True:
            if option == "1":
                client = input("Ingrese el nombre del cliente: ")
                for obj in self.__shipments:
                    if getattr(obj, "client") == client:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen envíos con el cliente ingresado")
                        break

            elif option == "2":
                date= input("Ingrese la fecha del envío: ")
                for obj in self.__shipments:
                    if getattr(obj, "date") == date:
                        filtered_objects.append(obj)
                    else:
                        print("Error! no existen pagos con la fecha ingresada")
                        break
            
            else:
                option = input("Error! Seleccione una opción válida")
            
            return print(filtered_objects)

    def menu(self):
        """
        Función principal Menú que permite navegar por los distintos modulos de la tienda
        """
        self.load_products()
        options = ["Gestión de Productos", "Gestión de ventas", "Gestión de Clientes", "Gestión de Pagos", "Gestión de envíos", "Salir"]
        while True:
            for i in range(len(options)):
                print(f"{i+1}. {options[i]}")
            option = input("Ingrese la opción deseada: ")
            while not option.isnumeric() or (int(option) -1) not in range(len(options)):
                option = input("Error! Ingrese la opción deseada: ")
            if option == "1":
                functions = ["Añadir productos", "Filtrar productos", "Editar productos", "Eliminar productos", "Salir"]
                while True:
                    for i in range(len(functions)):
                        print(f"{i+1}. {functions[i]}")
                    choice = input("Ingrese la opción deseada: ")
                    while not choice.isnumeric() or (int(choice) -1) not in range(len(functions)):
                        choice = input("Error! Ingrese la opción deseada: ")
                    if choice == "1":
                        self.add_product()
                    elif choice == "2":
                        self.search_product()
                    elif choice == "3":
                        self.edit_product()
                    elif choice == "4":
                        self.delete_product()
                    else:
                        break
            if option == "2":
                functions = ["Registrar ventas", "Generar facturas", "Filtrar clientes", "Salir"]
                while True:
                    for i in range(len(functions)):
                        print(f"{i+1}. {functions[i]}")
                    choice = input("Ingrese la opción deseada: ")
                    while not choice.isnumeric() or (int(choice) -1) not in range(len(functions)):
                        choice = input("Error! Ingrese la opción deseada: ")
                    if choice == "1":
                        self.register_sell()
                    elif choice == "2":
                        self.generate_sell()
                    elif choice == "3":
                        self.search_sell()
                    else:
                        break
            if option == "3":
                functions = ["Registrar clientes", "Editar clientes", "Eliminar clientes", "Filtrar clientes", "Salir"]
                while True:
                    for i in range(len(functions)):
                        print(f"{i+1}. {functions[i]}")
                    choice = input("Ingrese la opción deseada: ")
                    while not choice.isnumeric() or (int(choice) -1) not in range(len(functions)):
                        choice = input("Error! Ingrese la opción deseada: ")
                    if choice == "1":
                        self.register_client()
                        break
                    elif choice == "2":
                        self.edit_client()
                    elif choice == "3":
                        self.delete_client()
                    elif choice == "4":
                        self.search_client()
                    else:
                        break
            if option == "4":
                functions = ["Registrar pagos", "Filtrar pagos", "Salir"]
                while True:
                    for i in range(len(functions)):
                        print(f"{i+1}. {functions[i]}")
                    choice = input("Ingrese la opción deseada: ")
                    while not choice.isnumeric() or (int(choice) -1) not in range(len(functions)):
                        choice = input("Error! Ingrese la opción deseada: ")
                    if choice == "1":
                        self.register_payment()
                    elif choice == "2":
                        self.search_payment()
                    else:
                        break
            if option == "5":
                functions = ["Registrar envíos", "Filtrar envíos", "Salir"]
                while True:
                    for i in range(len(functions)):
                        print(f"{i+1}. {functions[i]}")
                    choice = input("Ingrese la opción deseada: ")
                    while not choice.isnumeric() or (int(choice) -1) not in range(len(functions)):
                        choice = input("Error! Ingrese la opción deseada: ")
                    if choice == "1":
                        self.register_shipment()
                    elif choice == "2":
                        self.search_shipment()
                    else:
                        break
            else:
                break

    def load_product(url):
        data = urlopen(url)
        data_json =json.loads(data.read())
        return data_json

    def create_product(url):
        lector = []
        jeison = load_product(url)
        for product in jeison:
            new_product = Product(product["name"], product["description"], product["price"], product["category"], product["quantity"])
            lector.append(new_product)
            return lector
        

