from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QFormLayout, QMessageBox, QStackedWidget

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction
from articulos_dao import ArticulosDao


class UIEditaArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()

    def config_ui(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(LabelTitulo("EDICIÓN ARTÍCULO"))

        frame = QFrame()
        form = QFormLayout(frame)

        self.referencia = EditItem()
        form.addRow(LabelItem("Referencia:"), self.referencia)

        self.descripcion = EditItem()
        form.addRow(LabelItem("Descripción:"), self.descripcion)

        self.precio = EditItem()
        form.addRow(LabelItem("Precio:"), self.precio)

        self.stock = EditItem()
        form.addRow(LabelItem("Stock:"), self.stock)

        form.addRow(LabelItem("Observaciones:"))
        self.observaciones = TextItem()
        form.addRow(self.observaciones)

        boton = BotonAction("Actualizar")
        boton.clicked.connect(self.actualizar)
        form.addRow(boton)

        layout.addWidget(frame)
        layout.addStretch(1)

    def actualizar(self):
        referencia = self.referencia.text().strip()
        descripcion = self.descripcion.text().strip()

        try:
            precio = float(self.precio.text().replace(",", "."))
            stock = int(float(self.stock.text()))
        except ValueError:
            QMessageBox.critical(self, "Error", "Precio o stock no válidos.", QMessageBox.StandardButton.Close)
            return

        if not referencia or not descripcion:
            QMessageBox.critical(self, "Error", "Referencia y descripción son obligatorias.", QMessageBox.StandardButton.Close)
            return

        articulo = {
            "referencia": referencia,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "observaciones": self.observaciones.text(),
        }

        if self.articulos_dao.update(articulo):
            QMessageBox.information(self, "OK", "Artículo modificado correctamente.", QMessageBox.StandardButton.Close)
        else:
            QMessageBox.warning(self, "Error", "No existe la referencia indicada.", QMessageBox.StandardButton.Close)
