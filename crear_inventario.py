
import sqlite3

# Conectar con la base de datos
conexion = sqlite3.connect("inventario.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla productos
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT
)
""")

# Insertar un producto
cursor.execute("""
INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
VALUES (?, ?, ?, ?, ?)
""", ("Teclado", "Teclado inalámbrico", 15, 25000.50, "Informática"))

# Guardar los cambios
conexion.commit()

print("Producto agregado correctamente.")


# Guardar cambios
conexion.commit()

# Consultar las columnas de la tabla
cursor.execute("PRAGMA table_info(productos)")
columnas = cursor.fetchall()

# Mostrar las columnas
print("\nESTRUCTURA DE LA TABLA PRODUCTOS:")

for columna in columnas:
    print(columna)

 
# Consultar todos los productos
cursor.execute("SELECT * FROM productos")

productos = cursor.fetchall()

print("\n===== LISTA DE PRODUCTOS =====")

for producto in productos:
    print(producto)
   

# Cerrar la conexión al finalizar
conexion.close()

print("\nBase de datos creada y verificada correctamente.")

