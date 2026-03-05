import logging
import sqlite3

class ArticulosDao:

    def __init__(self, filename="articulos.db"):
        self.conn = sqlite3.connect(filename)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

        self.crear_tablas()
        self.config_log()
        self.logger.info("Conexión realizada con éxito")

    def config_log(self):
        logging.basicConfig(
            filename="articulos.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            encoding="utf-8"
        )
        self.logger = logging.getLogger(__name__)

    def crear_tablas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referencia TEXT UNIQUE NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL,
            observaciones TEXT
        )
        ''')
        self.conn.commit()

    def save(self, articulo: dict):
        sql = """INSERT INTO articulos 
                 (referencia, descripcion, precio, stock, observaciones)
                 VALUES (?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(sql, (
                articulo["referencia"],
                articulo.get("descripcion", None),
                articulo["precio"],
                articulo["stock"],
                articulo.get("observaciones", None)
            ))
            self.conn.commit()
            print("Artículo añadido correctamente")
            return True
        except Exception as e:
            self.logger.error(e)
            print(f"Error al añadir artículo: {e}")
            return False

    def find(self, referencia: str) -> dict:
        try:
            sql = "SELECT * FROM articulos WHERE referencia = ?"
            self.cursor.execute(sql, (referencia,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            self.logger.error(e)
            print(f"Error al obtener artículo: {e}")
            return None
