#importar sqlite3 y crear la base de datos e inventario
import sqlite3

def crear_conexion():
    return sqlite3.connect("inventario.db")

def crear_tabla():
    conexion = crear_conexion()
    cursor = conexion.cursor()

#ejecutar la creación de la tabla productos si no existe
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

    conexion.commit()
    conexion.close()
