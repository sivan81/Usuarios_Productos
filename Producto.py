import mysql.connector


class Producto:

    # Creación de Producto y sus atributos.

    def __init__(self, id_producto, nombre, precio):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio

    def get_id_producto(self):
        return self._id_producto

    def set_id_producto(self, id_producto):
        self._id_producto = id_producto

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio


    # Conexión a la base de datos para los usuarios

    def conectar():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taream6ivan"
        )
        return db
    

    # Agregar Producto

    def agregar_producto(nombre, precio):
        db=Producto.conectar()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO Producto (nombre, precio) VALUES ('{nombre}', '{precio}')")
        db.commit()
        db.close()
