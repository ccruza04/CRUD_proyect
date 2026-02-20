"""Modelo de datos para un artículo."""


class Articulo:
    """Representa un artículo del inventario."""

    def __init__(self, referencia, descripcion, precio, stock, observaciones):
        self.referencia = referencia
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.observaciones = observaciones

    @staticmethod
    def _escapar_campo(campo):
        """Escapa separadores y barras invertidas en un campo de texto."""
        return str(campo).replace("\\", "\\\\").replace("|", "\\|")

    @staticmethod
    def _dividir_campos_escapados(linea):
        """Divide una línea en campos respetando el escape con barra invertida."""
        campos = []
        actual = []
        escapando = False

        for caracter in linea:
            if escapando:
                actual.append(caracter)
                escapando = False
            elif caracter == "\\":
                escapando = True
            elif caracter == "|":
                campos.append("".join(actual))
                actual = []
            else:
                actual.append(caracter)

        if escapando:
            return None

        campos.append("".join(actual))
        return campos

    def a_linea_texto(self):
        """Convierte el artículo en una línea de texto separada por |."""
        return (
            f"{self._escapar_campo(self.referencia)}|"
            f"{self._escapar_campo(self.descripcion)}|"
            f"{self.precio}|"
            f"{self.stock}|"
            f"{self._escapar_campo(self.observaciones)}"
        )

    @staticmethod
    def desde_linea_texto(linea):
        """Crea un artículo a partir de una línea del fichero de texto."""
        partes = Articulo._dividir_campos_escapados(linea.strip())
        if partes is None or len(partes) != 5:
            return None

        referencia, descripcion, precio_texto, stock_texto, observaciones = partes

        try:
            precio = float(precio_texto)
            stock = int(stock_texto)
        except ValueError:
            return None

        return Articulo(referencia, descripcion, precio, stock, observaciones)
