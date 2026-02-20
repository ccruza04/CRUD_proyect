from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QStackedWidget

from ui_components import LabelTitulo, BotonAction
from articulos_dao import ArticulosDao


class UIListadoArticulos(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()

    def config_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(LabelTitulo("LISTADO DE ARTÍCULOS"))

        self.boton_refrescar = BotonAction("Refrescar")
        self.boton_refrescar.clicked.connect(self.listar)
        layout.addWidget(self.boton_refrescar)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["Referencia", "Descripción", "Precio", "Stock", "Observaciones"])
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tabla.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.tabla)

    def listar(self):
        articulos = self.articulos_dao.get_all()
        self.tabla.setRowCount(len(articulos))

        for fila, articulo in enumerate(articulos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(articulo.get("referencia", ""))))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(articulo.get("descripcion", ""))))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(articulo.get("precio", ""))))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(articulo.get("stock", ""))))
            self.tabla.setItem(fila, 4, QTableWidgetItem(str(articulo.get("observaciones", ""))))
