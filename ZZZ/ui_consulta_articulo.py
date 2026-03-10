from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget, QFrame, QFormLayout, QMessageBox, QHBoxLayout, QCompleter
)

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction, aplicar_candado
from articulos_dao import ArticulosDao


class UIConsultaArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()
        self.actualizar_completer()

    def config_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(LabelTitulo("CONSULTA ARTÍCULO"))

        widget_form = QFrame()
        form_layout = QFormLayout(widget_form)

        self.txt_buscar = EditItem(placeholder="Buscar referencia...")
        self.completer = QCompleter()
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setModel(QStringListModel([]))
        self.txt_buscar.setCompleter(self.completer)

        fila_buscar = QHBoxLayout()
        fila_buscar.addWidget(self.txt_buscar)
        boton_consultar = BotonAction("Buscar")
        boton_consultar.clicked.connect(self.consultar_articulo)
        fila_buscar.addWidget(boton_consultar)
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

        layout.addWidget(widget_form)
        layout.addStretch(1)

    def actualizar_completer(self):
        self.completer.model().setStringList(self.articulos_dao.get_referencias())

    def consultar_articulo(self) -> None:
        referencia_buscada = self.txt_buscar.text().strip()
        if not referencia_buscada:
            return

        articulo = self.articulos_dao.find(referencia_buscada)
        if articulo:
            self.referencia.setText(articulo.get("referencia"))
            self.descripcion.setText(articulo.get("descripcion"))
            self.precio.setText(str(articulo.get("precio")))
            self.stock.setText(str(articulo.get("stock")))
            self.observaciones.setText(articulo.get("observaciones"))
        else:
            self.limpiar_campos()
            QMessageBox.warning(self, "Error", "No se ha encontrado la referencia indicada.", QMessageBox.StandardButton.Close)

    def limpiar_campos(self):
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.clear()
