from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QFormLayout, QMessageBox, QStackedWidget

from ui_components import LabelTitulo, LabelItem, EditItem, BotonAction
from articulos_dao import ArticulosDao


class UIBajaArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()

    def config_ui(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(LabelTitulo("BAJA ARTÍCULO"))

        frame = QFrame()
        form_layout = QFormLayout(frame)
        self.referencia = EditItem()
        form_layout.addRow(LabelItem("Referencia:"), self.referencia)

        boton_borrar = BotonAction("Eliminar")
        boton_borrar.clicked.connect(self.borrar_articulo)
        form_layout.addRow(boton_borrar)

        layout.addWidget(frame)
        layout.addStretch(1)

    def borrar_articulo(self):
        referencia = self.referencia.text().strip()
        if not referencia:
            QMessageBox.warning(self, "Error", "Debes indicar una referencia.", QMessageBox.StandardButton.Close)
            return

        if self.articulos_dao.delete(referencia):
            QMessageBox.information(self, "OK", "Artículo eliminado correctamente.", QMessageBox.StandardButton.Close)
            self.referencia.clear()
        else:
            QMessageBox.warning(self, "Error", "No se encontró la referencia indicada.", QMessageBox.StandardButton.Close)
