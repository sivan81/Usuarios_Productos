import mysql.connector


class Factura:


    # Creación de Factura y sus atributos

    def __init__(self, usuario, producto, precio):
        self.__usuario = usuario
        self.__producto = producto
        self.__precio = precio
    
    def get_usuario(self):
        return self.__usuario
    
    def set_usuario(self, usuario):
        self.__usuario = usuario
    
    def get_producto(self):
        return self.__producto
    
    def set_producto(self, producto):
        self.__producto = producto
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, precio):
        self.__precio = precio

    

    # Conexión a la base de datos para los usuarios

    def conectar():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taream6ivan"
        )
        return db
