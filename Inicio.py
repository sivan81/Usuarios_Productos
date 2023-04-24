import mysql.connector
from Usuario import Usuario
from Producto import Producto
from Factura import Factura

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
                            print("Eres el usuario Administrador, ¿Qué desea realizar? \n")
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
                                print("Nuevo producto agregado. \n")
                            
                            elif opcion == "2": # Modificar producto
                                id_producto=input("Indice que ID del producto que quiere modificar su precio: ")
                                producto=Producto.buscar_producto(id_producto)
                                if producto:
                                    print(f"Producto encontrado: {producto.get_nombre()} - {producto.get_precio()} € \n")
                                    nuevo_precio=input("indique el nuevo precio del producto: ")
                                    Producto.modificar_producto(id_producto,producto.get_nombre(), nuevo_precio)
                                    print("Precio del producto modificado correctamente. \n")
                                else:
                                    print("Producto no encontrado. \n")
                            
                            elif opcion == "3": # Eliminar Usuario
                                id_usuario=input("Indique el ID del Usuario que quiere eliminar: ")
                                if id_usuario == "1":
                                    print("No se puede eliminar el usuario Administrador. \n")
                                else:
                                    usuario=Usuario.eliminar_usuario(id_usuario)
                                    print("El usuario ha sido eliminado. \n")

                            elif opcion == "4": # Obtener la facturación total
                                facturacion_total = Factura.obtener_facturacion_total()
                                print(f"La facturación total de todos los productos vendidos es de: {facturacion_total} \n")
                            
                            elif opcion == "5": # Obtener la facturación total de un usuario específico
                                nombre_usuario = input("Introduzca el nombre del cliente: ")
                                facturacion_total = Factura.obtener_facturacion_total_por_usuario(nombre_usuario)
                                if facturacion_total > 0:
                                    print(f"La facturación total del cliente {nombre_usuario} es de: {facturacion_total} € \n")

                            elif opcion == "6": # Obtener la facturación total de un producto específico
                                nombre_producto = input("Introduzca el nombre del producto: ")
                                facturacion_total = Factura.obtener_facturacion_total_por_producto(nombre_producto)
                                if facturacion_total > 0:
                                    print(f"La facturación total del producto {nombre_producto} es de: {facturacion_total} € \n")

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

                            if opcion=="1": # Muestra los productos que hay al cliente.
                                print("Estos son los productos que hay actualmente. \n")
                                Producto.mostrar_productos()
                            
                            elif opcion=="2": # El cliente compra un producto y se genera una compra/factura
                                id_producto = input("Introduzca el ID del producto que desea comprar: ")
                                producto = Producto.buscar_producto(id_producto)
                                if producto:
                                    nombre_usuario = usuario.get_nombre()
                                    precio = producto.get_precio()
                                    nombre_producto = producto.get_nombre()
                                    Factura.agregar_producto_a_factura(nombre_usuario, nombre_producto, precio)
                                    print("Compra realizada con éxito. \n")
                                else:
                                    print("El ID producto indicado, no existe. \n")
                            
                            elif opcion=="3":
                                nuevo_password=input("Puede modificar su password si lo desea. ¿Cuál sería su nuevo password?: ")
                                Usuario.modificar_dato(usuario.get_id_usuario(),nuevo_password)
                                print("Su password ha sido modificado correctamente. \n")

                            elif opcion=="4":
                                print("Hasta luego!")
                                break
                            else:
                                print("Opción inválida. \n")
                else:
                    print("Usuario no encontrado. \n")
                

            elif opcion == "3":
                print("Hasta luego!")
                break
            else:
                print("Opción inválida. \n")

    
Inicio.menu()
        


