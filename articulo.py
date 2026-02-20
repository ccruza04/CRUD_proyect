"""Modelo de datos para un artículo."""


class Articulo:
    """Representa un artículo del inventario."""

    def __init__(self, referencia, descripcion, precio, stock, observaciones):
        self.referencia = referencia
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.observaciones = observaciones

    def a_linea_texto(self):
        """Convierte el artículo en una línea de texto separada por |."""
        return (
            f"{self.referencia}|{self.descripcion}|{self.precio}|"
            f"{self.stock}|{self.observaciones}"
        )

    @staticmethod
    def desde_linea_texto(linea):
        """Crea un artículo a partir de una línea del fichero de texto."""
        partes = linea.strip().split("|")
        if len(partes) != 5:
            return None

        referencia, descripcion, precio_texto, stock_texto, observaciones = partes

        try:
            precio = float(precio_texto)
            stock = int(stock_texto)
        except ValueError:
            return None

        return Articulo(referencia, descripcion, precio, stock, observaciones)
