import mysql.connector
from Producto import Producto


class Factura:


    # Creación de Factura y sus atributos

    def __init__(self, id_factura, nombre_usuario, nombre_producto, precio):
        self.__id_factura = id_factura
        self.__nombre_usuario = nombre_usuario
        self.__nombre_producto = nombre_producto
        self.__precio = precio
    
    # Getters
    def get_id_factura(self):
        return self.__id_factura
    
    def get_nombre_usuario(self):
        return self.__nombre_usuario
    
    def get_nombre_producto(self):
        return self.__nombre_producto
    
    def get_precio(self):
        return self.__precio
    
    # Setters
    def set_id_factura(self, id_factura):
        self.__id_factura = id_factura
        
    def set_nombre_usuario(self, nombre_usuario):
        self.__nombre_usuario = nombre_usuario
    
    def set_nombre_producto(self, nombre_producto):
        self.__nombre_producto = nombre_producto
    
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
    

    # Agregar producto a Factura

    def agregar_producto_a_factura(nombre_usuario, nombre_producto, precio):
        # Agregar la factura a la tabla Factura
        db = Producto.conectar()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO Factura (nombre_usuario, nombre_producto, precio) VALUES ('{nombre_usuario}', '{nombre_producto}', {precio})")
        db.commit()
        db.close()

        # Crear una nueva instancia de Factura, quizás lo utilice para obtener la facturación de un usuario específico o un producto.
        # factura = Factura(None, nombre_usuario, nombre_producto, precio)
        # return factura
    

    # Facturacion Total, es decir, suma de los precios de los artículos vendidos

    def obtener_facturacion_total():
        db = Producto.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT SUM(precio) FROM Factura")
        resultado = cursor.fetchone()
        db.close()
        return resultado[0]
    

    # Obtener facturación total de un usuario específico

    def obtener_facturacion_total_por_usuario(nombre_usuario):
        db = Factura.conectar()
        cursor = db.cursor()
        cursor.execute(f"SELECT SUM(precio) FROM Factura WHERE nombre_usuario='{nombre_usuario}'")
        resultado = cursor.fetchone()
        db.close()

        # retornar la suma de precios
        if resultado and resultado[0]:
            return resultado[0] if resultado[0] else 0
        else:
            print(f"No existe ninguna factura para el usuario {nombre_usuario}")
            return 0
