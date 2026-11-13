
import sqlite3

# Conectar con la base de datos
def conectar():
    return sqlite3.connect("inventario.db")


# Mostrar menú principal
def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Modificar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    
def agregar_producto():
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio: "))
    categoria = input("Categoría: ")

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO productos
        (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conexion.commit()
    conexion.close()

    print("¡Producto agregado correctamente!")
    

# Mostrar todos los productos
def mostrar_productos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")

    productos = cursor.fetchall()

    print("\n===== LISTA DE PRODUCTOS =====")

    if productos:
        for producto in productos:
            print("--------------------------")
            print("ID:", producto[0])
            print("Nombre:", producto[1])
            print("Descripción:", producto[2])
            print("Cantidad:", producto[3])
            print("Precio:", producto[4])
            print("Categoría:", producto[5])
    else:
        print("No hay productos registrados.")

    conexion.close()
    

# Programa principal
while True:
    mostrar_menu()

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        print("Buscar producto")

    elif opcion == "4":
        print("Modificar producto")

    elif opcion == "5":
        print("Eliminar producto")

    elif opcion == "6":
        print("¡Hasta pronto!")
        break

    else:
        print("Opción incorrecta. Intentá nuevamente.")
