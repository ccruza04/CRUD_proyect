"""Funciones CRUD para gestionar artículos desde consola."""

from articulo import Articulo
from gestion_fichero import cargar_articulos, guardar_articulos
from validaciones import pedir_float, pedir_int


def buscar_articulo_por_referencia(lista_articulos, referencia):
    """Busca un artículo por referencia y devuelve (índice, artículo)."""
    for indice, articulo in enumerate(lista_articulos):
        if articulo.referencia == referencia:
            return indice, articulo
    return None, None


def alta_articulo():
    """Crea un artículo nuevo."""
    articulos = cargar_articulos()

    referencia = input("Referencia (única): ").strip()
    if not referencia:
        print("La referencia no puede estar vacía.")
        return

    _, articulo_existente = buscar_articulo_por_referencia(articulos, referencia)
    if articulo_existente is not None:
        print("Error: ya existe un artículo con esa referencia.")
        return

    descripcion = input("Descripción: ").strip()
    precio = pedir_float("Precio: ")
    stock = pedir_int("Stock: ")
    observaciones = input("Observaciones: ").strip()

    nuevo_articulo = Articulo(referencia, descripcion, precio, stock, observaciones)
    articulos.append(nuevo_articulo)
    guardar_articulos(articulos)
    print("Artículo añadido correctamente.")


def baja_articulo():
    """Elimina un artículo por referencia."""
    articulos = cargar_articulos()
    referencia = input("Referencia del artículo a eliminar: ").strip()

    indice, articulo = buscar_articulo_por_referencia(articulos, referencia)
    if articulo is None:
        print("No se encontró ningún artículo con esa referencia.")
        return

    del articulos[indice]
    guardar_articulos(articulos)
    print("Artículo eliminado correctamente.")


def modificar_articulo():
    """Modifica un artículo existente."""
    articulos = cargar_articulos()
    referencia = input("Referencia del artículo a modificar: ").strip()

    indice, articulo = buscar_articulo_por_referencia(articulos, referencia)
    if articulo is None:
        print("No se encontró ningún artículo con esa referencia.")
        return

    print("Introduce los nuevos datos (deja vacío para mantener el valor actual).")

    nueva_descripcion = input(f"Descripción [{articulo.descripcion}]: ").strip()
    if nueva_descripcion:
        articulo.descripcion = nueva_descripcion

    nuevo_precio = input(f"Precio [{articulo.precio}]: ").strip()
    if nuevo_precio:
        while True:
            try:
                articulo.precio = float(nuevo_precio.replace(",", "."))
                break
            except ValueError:
                nuevo_precio = input("Precio inválido. Introduce un valor numérico: ").strip()

    nuevo_stock = input(f"Stock [{articulo.stock}]: ").strip()
    if nuevo_stock:
        while True:
            try:
                articulo.stock = int(nuevo_stock)
                break
            except ValueError:
                nuevo_stock = input("Stock inválido. Introduce un valor entero: ").strip()

    nuevas_observaciones = input(f"Observaciones [{articulo.observaciones}]: ").strip()
    if nuevas_observaciones:
        articulo.observaciones = nuevas_observaciones

    articulos[indice] = articulo
    guardar_articulos(articulos)
    print("Artículo modificado correctamente.")


def listar_articulos():
    """Lista todos los artículos guardados."""
    articulos = cargar_articulos()

    if not articulos:
        print("No hay artículos registrados.")
        return

    print("\nListado de artículos")
    print("-" * 80)
    for articulo in articulos:
        print(f"Referencia   : {articulo.referencia}")
        print(f"Descripción  : {articulo.descripcion}")
        print(f"Precio       : {articulo.precio:.2f}")
        print(f"Stock        : {articulo.stock}")
        print(f"Observaciones: {articulo.observaciones}")
        print("-" * 80)
