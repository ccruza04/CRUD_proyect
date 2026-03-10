"""Funciones para cargar y guardar artículos en texto plano."""

from articulo import Articulo

ARCHIVO_DATOS = "articulos.dat"


def cargar_articulos():
    """Lee el fichero y devuelve una lista de artículos."""
    articulos = []

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as fichero:
            for linea in fichero:
                if not linea.strip():
                    continue

                articulo = Articulo.desde_linea_texto(linea)
                if articulo is not None:
                    articulos.append(articulo)
    except FileNotFoundError:
        # Si el archivo no existe todavía, devolvemos lista vacía.
        pass

    return articulos


def guardar_articulos(lista_articulos):
    """Sobrescribe completamente el fichero con la lista indicada."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as fichero:
        for articulo in lista_articulos:
            fichero.write(articulo.a_linea_texto() + "\n")
