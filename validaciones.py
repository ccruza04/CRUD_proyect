"""Funciones auxiliares para validar entradas del usuario."""


def pedir_float(mensaje):
    """Solicita un número decimal al usuario y lo valida."""
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Error: introduce un valor numérico válido.")


def pedir_int(mensaje):
    """Solicita un número entero al usuario y lo valida."""
    while True:
        texto = input(mensaje).strip()
        try:
            return int(texto)
        except ValueError:
            print("Error: introduce un número entero válido.")
