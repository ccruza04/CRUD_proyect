"""Menú interactivo para la aplicación CRUD de artículos."""

from operaciones_crud import alta_articulo, baja_articulo, modificar_articulo, listar_articulos


def menu():
    """Muestra el menú principal y ejecuta la opción elegida."""
    while True:
        print("\n=== GESTIÓN DE ARTÍCULOS ===")
        print("1. Alta de artículo")
        print("2. Baja de artículo")
        print("3. Modificar artículo")
        print("4. Listar artículos")
        print("5. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            alta_articulo()
        elif opcion == "2":
            baja_articulo()
        elif opcion == "3":
            modificar_articulo()
        elif opcion == "4":
            listar_articulos()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
