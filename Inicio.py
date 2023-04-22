import mysql.connector
from Usuario import Usuario
from Producto import Producto

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
        while True: # Registro o Inicio de sesión.
            print("1. Registrarse.")
            print("2. Iniciar Sesión.")
            print("3. Salir.")
            opcion=input("Seleccione una opcion: ")

            if opcion == "1":
                nombre=input("¿Cuál es su nombre?: ")
                apellido=input("¿Cuál es su apellido?: ")
                password=input("¿Cuál es su password?: ")
                Usuario.agregar_usuario(nombre, apellido, password)
                print("Nuevo usuario registrado.")

            elif opcion == "2":
                apellido=input("¿Cuál es su apellido?: ")
                password=input("¿Cuál es su password?: ")
                usuario=Usuario.buscar_usuario(apellido, password)
                if usuario: #Si es Administrador o cliente.
                    print(f"Hola: {usuario.get_nombre()}")
                    if usuario.get_id_usuario()==1:
                        while True: 
                            print("Eres el usuario Administrador, ¿Qué desea realizar?")
                            print("1. Crear productos.")
                            print("2. Modificar producto.")
                            print("3. Eliminar Usuario.")
                            print("4. Sacar facturación total.")
                            print("5. Sacar la facturación por usuario.")
                            print("6. Sacar la facturación por producto.")
                            print("7. Salir.")
                            opcion=input("Seleccione una opción: ")

                            if opcion=="1": # Buscar producto
                                nombre=input("¿Cuál es el nombre del producto?: ")
                                precio=input("¿Cuál es el precio del producto?: ")
                                Producto.agregar_producto(nombre,precio)
                                print("Nuevo producto agregado.")
                            
                            elif opcion == "2": # Modificar producto
                                id_producto=input("Indice que ID del producto que quiere modificar: ")
                                producto=Producto.buscar_producto(id_producto)
                                if producto:
                                    print(f"Producto encontrado: {producto.get_nombre()} - {producto.get_precio()} €")
                                    db = Inicio.conectar()
                                    cursor = db.cursor()
                                    opcion = input("¿Desea modificar el nombre del producto? (S/N)")
                                    if opcion.upper() == "S": # Modificar nombre
                                        nuevo_nombre = input("Introduce el nuevo nombre: ")
                                        cursor.execute(f"UPDATE Producto SET nombre='{nuevo_nombre}' WHERE id_producto='{id_producto}'")
                                        db.commit()
                                        producto.set_nombre(nuevo_nombre)

                                    opcion = input("¿Desea modificar el precio del producto? (S/N)")
                                    if opcion.upper() == "S": # Modificar precio
                                        nuevo_precio = input("Introduce el nuevo precio: ")
                                        cursor.execute(f"UPDATE Producto SET precio='{nuevo_precio}' WHERE id_producto='{id_producto}'")
                                        db.commit()
                                        producto.set_precio(nuevo_precio)
                                    db.close()
                                    print("Producto modificado correctamente.")
                                else:
                                    print("Producto no encontrado.")
                            
                            elif opcion == "3": # Eliminar Usuario
                                id_usuario=input("Indique el ID del Usuario que quiere eliminar: ")
                                if id_usuario == "1":
                                    print("No se puede eliminar el usuario Administrador.")
                                else:
                                    usuario=Usuario.eliminar_usuario(id_usuario)
                                    print("El usuario ha sido eliminado.")
                            
                            elif opcion=="7":
                                print("Hasta luego!")
                                break
                    else:
                        while True:
                            print("¿Qué desea hacer?")
                            print("1. Ver productos.")
                            print("2. Comprar productos.")
                            print("3. Modificar sus datos.")
                            print("4. Salir.")
                            opcion=input("Seleccione una opción: ")

                            if opcion=="1":
                                print("Estos son los productos que hay actualmente.")
                                Producto.mostrar_productos()
                            
                            elif opcion=="2":
                                opcion=input("Introduzca el ID del producto que desea comprar.")

                            elif opcion=="4":
                                print("Hasta luego!")
                                break
                            else:
                                print("Opción inválida.")
                else:
                    print("Usuario no encontrado")
                

            elif opcion == "3":
                print("Hasta luego!")
                break
            else:
                print("Opción inválida.")

    
Inicio.menu()
        


