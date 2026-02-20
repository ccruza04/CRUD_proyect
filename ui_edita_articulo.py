from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStringListModel
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QFormLayout, QMessageBox, QStackedWidget, QHBoxLayout, QCompleter

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction, aplicar_candado
from articulos_dao import ArticulosDao


class UIEditaArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()
        self.actualizar_completer()
        self.bloquear_edicion(True)

    def config_ui(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(LabelTitulo("EDICIÓN ARTÍCULO"))

        frame = QFrame()
        form = QFormLayout(frame)

        self.txt_buscar = EditItem(placeholder="Buscar referencia...")
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setModel(QStringListModel([]))
        self.txt_buscar.setCompleter(self.completer)

        fila_buscar = QHBoxLayout()
        fila_buscar.addWidget(self.txt_buscar)
        boton_buscar = BotonAction("Buscar")
        boton_buscar.clicked.connect(self.buscar)
        fila_buscar.addWidget(boton_buscar)
        form.addRow(LabelItem("Referencia a buscar:"), fila_buscar)

        self.referencia = EditItem()
        self.referencia.setReadOnly(True)
        aplicar_candado(self.referencia)
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

        boton_reset = BotonAction("Resetear")
        boton_reset.clicked.connect(self.resetear)
        form.addRow(boton_reset)

        layout.addWidget(frame)
        layout.addStretch(1)

    def actualizar_completer(self):
        self.completer.model().setStringList(self.articulos_dao.get_referencias())

    def bloquear_edicion(self, bloquear=True):
        self.descripcion.setDisabled(bloquear)
        self.precio.setDisabled(bloquear)
        self.stock.setDisabled(bloquear)
        self.observaciones.setDisabled(bloquear)

    def buscar(self):
        ref = self.txt_buscar.text().strip()
        if not ref:
            return

        articulo = self.articulos_dao.find(ref)
        if not articulo:
            self.resetear()
            QMessageBox.warning(self, "Error", "No existe la referencia indicada.", QMessageBox.StandardButton.Close)
            return

        self.referencia.setText(articulo.get("referencia"))
        self.descripcion.setText(articulo.get("descripcion"))
        self.precio.setText(str(articulo.get("precio")))
        self.stock.setText(str(articulo.get("stock")))
        self.observaciones.setText(articulo.get("observaciones"))
        self.bloquear_edicion(False)

    def actualizar(self):
        referencia = self.referencia.text().strip()
        descripcion = self.descripcion.text().strip()

        if not referencia:
            QMessageBox.warning(self, "Error", "Primero debes buscar una referencia.", QMessageBox.StandardButton.Close)
            return

        try:
            precio = float(self.precio.text().replace(",", "."))
            stock = int(float(self.stock.text()))
        except ValueError:
            QMessageBox.critical(self, "Error", "Precio o stock no válidos.", QMessageBox.StandardButton.Close)
            return

        if not descripcion:
            QMessageBox.critical(self, "Error", "La descripción es obligatoria.", QMessageBox.StandardButton.Close)
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
            self.resetear()
            self.actualizar_completer()
        else:
            QMessageBox.warning(self, "Error", "No existe la referencia indicada.", QMessageBox.StandardButton.Close)

    def resetear(self):
        self.txt_buscar.clear()
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.clear()
        self.bloquear_edicion(True)
