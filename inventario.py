
import sqlite3

# Conectar con la base de datos
conexion = sqlite3.connect("inventario.db")

# Crear un cursor
cursor = conexion.cursor()

# Crear la tabla productos
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

# Guardar los cambios
conexion.commit()

# Cerrar la conexión
conexion.close()

print("Base de datos y tabla creadas correctamente.")
