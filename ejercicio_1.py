"""Punto de entrada de la aplicación gráfica CRUD de artículos."""

import sys

from PyQt6.QtWidgets import QApplication, QStyleFactory

from ui_articulos_app import ArticulosApp


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Windows"))
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())



