"""Lógica de negocio para el CRUD de artículos."""

from articulo import Articulo
from gestion_fichero import cargar_articulos, guardar_articulos


def buscar_articulo_por_referencia(lista_articulos, referencia):
    """Busca por referencia y devuelve (índice, artículo) o (None, None)."""
    for indice, articulo in enumerate(lista_articulos):
        if articulo.referencia == referencia:
            return indice, articulo
    return None, None


def validar_datos_articulo(referencia, descripcion, precio_texto, stock_texto):
    """Valida datos de entrada básicos y devuelve (ok, resultado)."""
    referencia = referencia.strip()
    descripcion = descripcion.strip()

    if not referencia:
        return False, "La referencia es obligatoria."
    if not descripcion:
        return False, "La descripción es obligatoria."

    try:
        precio = float(str(precio_texto).strip().replace(",", "."))
    except ValueError:
        return False, "El precio debe ser numérico."

    try:
        stock = int(str(stock_texto).strip())
    except ValueError:
        return False, "El stock debe ser un número entero."

    return True, (referencia, descripcion, precio, stock)


def alta_articulo(referencia, descripcion, precio_texto, stock_texto, observaciones):
    """Da de alta un artículo nuevo."""
    ok, datos = validar_datos_articulo(referencia, descripcion, precio_texto, stock_texto)
    if not ok:
        return False, datos

    referencia, descripcion, precio, stock = datos
    observaciones = observaciones.strip()

    articulos = cargar_articulos()
    _, existente = buscar_articulo_por_referencia(articulos, referencia)
    if existente is not None:
        return False, "Ya existe un artículo con esa referencia."

    articulos.append(Articulo(referencia, descripcion, precio, stock, observaciones))
    guardar_articulos(articulos)
    return True, "Artículo añadido correctamente."


def baja_articulo(referencia):
    """Elimina un artículo por referencia."""
    referencia = referencia.strip()
    if not referencia:
        return False, "Debes indicar una referencia."

    articulos = cargar_articulos()
    indice, articulo = buscar_articulo_por_referencia(articulos, referencia)
    if articulo is None:
        return False, "No se encontró ningún artículo con esa referencia."

    del articulos[indice]
    guardar_articulos(articulos)
    return True, "Artículo eliminado correctamente."


def modificar_articulo(referencia, descripcion, precio_texto, stock_texto, observaciones):
    """Modifica un artículo existente."""
    ok, datos = validar_datos_articulo(referencia, descripcion, precio_texto, stock_texto)
    if not ok:
        return False, datos

    referencia, descripcion, precio, stock = datos
    observaciones = observaciones.strip()

    articulos = cargar_articulos()
    indice, articulo = buscar_articulo_por_referencia(articulos, referencia)
    if articulo is None:
        return False, "No se encontró ningún artículo con esa referencia."

    articulo.descripcion = descripcion
    articulo.precio = precio
    articulo.stock = stock
    articulo.observaciones = observaciones
    articulos[indice] = articulo
    guardar_articulos(articulos)
    return True, "Artículo modificado correctamente."


def listar_articulos():
    """Devuelve la lista de artículos desde fichero."""
    return cargar_articulos()
