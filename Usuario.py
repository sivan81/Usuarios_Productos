import mysql.connector


class Usuario:
    
    # Creación de Usuario y sus atributos

    def __init__(self, id_usuario, nombre, apellido, password):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__password = password
    
    def get_id_usuario(self):
        return self.__id_usuario
    
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password

        

    # Conexión a la base de datos para los usuarios

    def conectar():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taream6ivan"
        )
        return db
    

    # Agregar Usuarios

    def agregar_usuario(nombre, apellido, password):
        db=Usuario.conectar()
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO Usuario (nombre, apellido, password) VALUES ('{nombre}', '{apellido}', '{password}')")
        db.commit()
        db.close()


    # Buscar Usuarios

    def buscar_usuario(apellido, password):
        db = Usuario.conectar()
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM Usuario WHERE apellido='{apellido}' AND password='{password}'")
        result = cursor.fetchone()
        db.close()
        if result:
            id_usuario, nombre, apellido, password = result
            usuario = Usuario(id_usuario, nombre, apellido, password)
            return usuario
        else:
            return None
        
    
    # Eliminar Usuario

    def eliminar_usuario(id_usuario):
        db = Usuario.conectar()
        cursor = db.cursor()
        cursor.execute(f"DELETE FROM Usuario WHERE id_usuario='{id_usuario}'")
        db.commit()
        db.close()

    
    # Modificar Datos Usuario

    def modificar_dato(id_usuario, password):
        db = Usuario.conectar()
        cursor = db.cursor()
        cursor.execute(f"UPDATE Usuario SET password = '{password}' WHERE id_usuario = '{id_usuario}'")
        db.commit()
        db.close()