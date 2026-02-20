from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStringListModel
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QFormLayout, QMessageBox, QStackedWidget, QHBoxLayout, QCompleter

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction, aplicar_candado
from articulos_dao import ArticulosDao


class UIBajaArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()
        self.actualizar_completer()

    def config_ui(self):
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(LabelTitulo("BAJA ARTÍCULO"))

        frame = QFrame()
        form_layout = QFormLayout(frame)

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
        form_layout.addRow(LabelItem("Referencia a buscar:"), fila_buscar)

        self.referencia = EditItem()
        self.descripcion = EditItem()
        self.precio = EditItem()
        self.stock = EditItem()
        self.observaciones = TextItem()

        for campo in (self.referencia, self.descripcion, self.precio, self.stock):
            campo.setReadOnly(True)
            aplicar_candado(campo)
        self.observaciones.setReadOnly(True)

        form_layout.addRow(LabelItem("Referencia:"), self.referencia)
        form_layout.addRow(LabelItem("Descripción:"), self.descripcion)
        form_layout.addRow(LabelItem("Precio:"), self.precio)
        form_layout.addRow(LabelItem("Stock:"), self.stock)
        form_layout.addRow(LabelItem("Observaciones:"))
        form_layout.addRow(self.observaciones)

        boton_borrar = BotonAction("Eliminar")
        boton_borrar.clicked.connect(self.borrar_articulo)
        form_layout.addRow(boton_borrar)

        layout.addWidget(frame)
        layout.addStretch(1)

    def actualizar_completer(self):
        self.completer.model().setStringList(self.articulos_dao.get_referencias())

    def buscar(self):
        ref = self.txt_buscar.text().strip()
        if not ref:
            return

        articulo = self.articulos_dao.find(ref)
        if not articulo:
            self.limpiar_campos()
            QMessageBox.warning(self, "Error", "No se encontró la referencia indicada.", QMessageBox.StandardButton.Close)
            return

        self.referencia.setText(articulo.get("referencia"))
        self.descripcion.setText(articulo.get("descripcion"))
        self.precio.setText(str(articulo.get("precio")))
        self.stock.setText(str(articulo.get("stock")))
        self.observaciones.setText(articulo.get("observaciones"))

    def borrar_articulo(self):
        referencia = self.referencia.text().strip()
        if not referencia:
            QMessageBox.warning(self, "Error", "Primero debes buscar una referencia.", QMessageBox.StandardButton.Close)
            return

        res = QMessageBox.question(self, "Confirmar baja", f"¿Eliminar la referencia {referencia}?")
        if res != QMessageBox.StandardButton.Yes:
            return

        if self.articulos_dao.delete(referencia):
            QMessageBox.information(self, "OK", "Artículo eliminado correctamente.", QMessageBox.StandardButton.Close)
            self.limpiar_todo()
            self.actualizar_completer()
        else:
            QMessageBox.warning(self, "Error", "No se encontró la referencia indicada.", QMessageBox.StandardButton.Close)

    def limpiar_campos(self):
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.clear()

    def limpiar_todo(self):
        self.txt_buscar.clear()
        self.limpiar_campos()
