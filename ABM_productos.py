#importar 
from colorama import Fore
from db import crear_conexion

#Functionality:

#1. agregar un nuevo producto
def agregar_producto():
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    # conexion a db
    conexion = crear_conexion()
    cursor = conexion.cursor()

    #insert en la db tabla productos
    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()
    #impresion en consola al agregar producto
    print(Fore.GREEN + "Producto agregado.")

    input("\nPresione Enter para continuar...")


#2. consulta a la db inventario
def mostrar_productos():
    # conexion a db
    conexion = crear_conexion()
    cursor = conexion.cursor()

    #consulta en la db tabla productos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    #impresion en consola del inventario
    if productos:
        for p in productos:
            print(Fore.GREEN + f"ID: {p[0]}")
            print(f"Nombre: {p[1]}")
            print(f"Descripción: {p[2]}")
            print(f"Cantidad: {p[3]}")
            print(f"Precio: {p[4]}")
            print(f"Categoría: {p[5]}")
            print("-" * 30)  
    
    #impresion en consola si no hay productos
    else:
        print(Fore.RED + "No hay productos cargados.")

    conexion.close()

    input("\nPresione Enter para continuar...")


#3. buscar producto por id
def buscar_por_id():
    id_prod = input("ID del producto: ")

    # conexion a db
    conexion = crear_conexion()
    cursor = conexion.cursor()

    #consulta en la db tabla productos por id
    cursor.execute("SELECT * FROM productos WHERE id=?", (id_prod,))
    prod = cursor.fetchone()

    #impresion en consola de la busqueda por ID
    if prod:
        print(Fore.GREEN + f"ID: {prod[0]}")
        print(f"Nombre: {prod[1]}")
        print(f"Descripción: {prod[2]}")
        print(f"Cantidad: {prod[3]}")
        print(f"Precio: {prod[4]}")
        print(f"Categoría: {prod[5]}")
        
    #impresion en consola si no se encuentra el producto
    else:
        print(Fore.RED + "No existe ese producto en la base de datos.")

    conexion.close()

    input("\nPresione Enter para continuar...")


#4. hacer update a un producto por id
def actualizar_producto():
    id_prod = input("ID del producto a actualizar: ")

    nombre = input("Nuevo nombre: ")
    descripcion = input("Nueva descripción: ")
    cantidad = int(input("Nueva cantidad: "))
    precio = float(input("Nuevo precio: "))
    categoria = input("Nueva categoría: ")

    # conexion a db
    conexion = crear_conexion()
    cursor = conexion.cursor()

   #update en la db tabla productos
    cursor.execute("""
        UPDATE productos SET
            nombre=?, descripcion=?, cantidad=?, precio=?, categoria=?
        WHERE id=?
    """, (nombre, descripcion, cantidad, precio, categoria, id_prod))

    conexion.commit()
    
    #impresion en consola del resultado
    print(Fore.YELLOW + "Producto actualizado." if cursor.rowcount else Fore.RED + "No se encontró el producto.")
    conexion.close()

    input("\nPresione Enter para continuar...")


#5. haciendo un delete a un producto por id
def eliminar_producto():
    id_prod = input("ID del producto a eliminar: ")

    # conexion a db
    conexion = crear_conexion()
    cursor = conexion.cursor()

    #delete en la db tabla productos
    cursor.execute("DELETE FROM productos WHERE id=?", (id_prod,))
    conexion.commit()

    #impresion en consola del resultado
    print(Fore.GREEN + "Producto eliminado." if cursor.rowcount else Fore.RED + "No existe ese producto.")
    conexion.close()

    input("\nPresione Enter para continuar...")


#6. reporte de productos
def reporte_stock():
    limite = int(input("Mostrar productos con cantidad menor o igual a: "))

    # conexion a db
    conexion = crear_conexion()
    cursor = conexion.cursor()

    #consulta en la db tabla productos 
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    #impresion en consola del reporte
    if productos:
        for p in productos:
            print(Fore.GREEN + f"ID: {p[0]}")
            print(f"Nombre: {p[1]}")
            print(f"Descripción: {p[2]}")
            print(Fore.RED + f"Cantidad: {p[3]}")
            print(f"Precio: {p[4]}")
            print(f"Categoría: {p[5]}")
            print("-" * 30)
      #impresion en consola si no hay productos que cumplan el criterio de búsqueda
    else:
        print(Fore.RED + "No hay productos que cumplan el criterio de búsqueda.")

    conexion.close()

    input("\nPresione Enter para continuar...")

