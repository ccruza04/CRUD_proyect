from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QFormLayout, QMessageBox, QStackedWidget

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction
from articulos_dao import ArticulosDao


class UINuevoArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()

    def config_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.addStretch(1)

        layout.addWidget(LabelTitulo("NUEVO ARTÍCULO"))

        widget_form = QFrame()
        form_layout = QFormLayout(widget_form)

        self.referencia = EditItem()
        form_layout.addRow(LabelItem("Referencia:"), self.referencia)

        self.descripcion = EditItem()
        form_layout.addRow(LabelItem("Descripción:"), self.descripcion)

        self.precio = EditItem()
        form_layout.addRow(LabelItem("Precio:"), self.precio)

        self.stock = EditItem()
        form_layout.addRow(LabelItem("Stock:"), self.stock)

        form_layout.addRow(LabelItem("Observaciones:"))
        self.observaciones = TextItem()
        form_layout.addRow(self.observaciones)

        boton_guardar = BotonAction("Guardar")
        boton_guardar.clicked.connect(self.guardar_articulo)
        form_layout.addRow(boton_guardar)

        layout.addWidget(widget_form)
        layout.addStretch(1)

    def guardar_articulo(self) -> None:
        referencia = self.referencia.text().strip()
        descripcion = self.descripcion.text().strip()

        try:
            precio = float(self.precio.text().replace(",", "."))
        except ValueError:
            QMessageBox.critical(self, "Error", "El precio no es numérico.", QMessageBox.StandardButton.Close)
            return

        try:
            stock = int(float(self.stock.text()))
        except ValueError:
            QMessageBox.critical(self, "Error", "El stock no es entero.", QMessageBox.StandardButton.Close)
            return

        if not referencia or not descripcion:
            QMessageBox.critical(self, "Error", "Referencia y descripción son obligatorias.", QMessageBox.StandardButton.Close)
            return

        articulo = {
            "referencia": referencia,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "observaciones": self.observaciones.text()
        }

        if self.articulos_dao.save(articulo):
            QMessageBox.information(self, "OK", "Artículo guardado correctamente.", QMessageBox.StandardButton.Close)
            self.init_form()
        else:
            QMessageBox.critical(self, "Error", "No se ha podido guardar (referencia duplicada).", QMessageBox.StandardButton.Close)

    def init_form(self):
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.setText("")
