import mysql.connector
from Usuario import Usuario

class Inicio:
    
    # Conexión a la base de datos de Inicio

    def conectar():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taream6ivan"
        )
        return db
    

    # Busca si existe la tabla antes de crearla
    
    def tabla_existe(nombre_tabla):
        db = Inicio.conectar()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM information_schema.tables WHERE table_schema = 'taream6ivan' AND table_name = '{nombre_tabla}'")
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
    
    # Crea las tablas si no existen

    def crear_tabla():
        db = Inicio.conectar()
        cursor = db.cursor()

        if Inicio.tabla_existe('Usuario'):
            print("La tabla Usuario ya existe")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS Usuario (id_usuario INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), apellido VARCHAR(255), password VARCHAR(255))")
            Usuario.agregar_usuario('Ivan', 'Garrido', '1234') # Crea el usuario Administrador

        if Inicio.tabla_existe('Producto'):
            print("La tabla Producto ya existe")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS Producto (id_producto INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), precio DECIMAL(10,2))")
        
        if Inicio.tabla_existe('Factura'):
            print("La tabla Factura ya existe")
        else:
            cursor.execute("CREATE TABLE IF NOT EXISTS Factura (id_factura INT AUTO_INCREMENT PRIMARY KEY, nombre_usuario VARCHAR(255), nombre_producto VARCHAR(255), precio DECIMAL(10,2))")

        db.commit()
        db.close()



    # Menú de preguntas al usuario
    
    def menu():
        Inicio.crear_tabla()
        while True:
            print("1. Registrarse.")
            print("2. Iniciar Sesión.")
            opcion=input("Seleccione una opcion: ")

            if opcion == "1":
                nombre=input("¿Cuál es su nombre?: ")
                apellido=input("¿Cuál es su apellido?: ")
                password=input("¿Cuál es su password?: ")
                Usuario.agregar_usuario(nombre, apellido, password)
                print("Nuevo usuario registrado.")

            if opcion == "2":
                nombre=input("¿Cuál es su nombre?: ")
                password=input("¿Cuál es su password?: ")
                usuario=Usuario.buscar_usuario(nombre, password)
                if usuario:
                    print(f"ID: {usuario.get_id_usuario()}")
                    print(f"Nombre: {usuario.get_nombre()}")
                    print(f"Apellido: {usuario.get_apellido()}")
                    print(f"Password: {usuario.get_password()}")
                else:
                    print("Usuario no encontrado")

    
Inicio.menu()
        


