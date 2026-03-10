from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QFormLayout, QMessageBox, QStackedWidget, QHBoxLayout, QCompleter

from funciones_ui.ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction, aplicar_candado
from ejemploFAKER.dao.articulos_dao import ArticulosDao


class UINuevoArticulo(QWidget):
    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()
        self.actualizar_completer()

    def config_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.addStretch(1)
        layout.addWidget(LabelTitulo("NUEVO ARTÍCULO"))

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
        boton_buscar = BotonAction("Buscar")
        boton_buscar.clicked.connect(self.buscar_referencia)
        fila_buscar.addWidget(boton_buscar)
        form_layout.addRow(LabelItem("Referencia a buscar:"), fila_buscar)

        self.referencia = EditItem()
        self.referencia.setReadOnly(True)
        aplicar_candado(self.referencia)
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

    def actualizar_completer(self):
        self.completer.model().setStringList(self.articulos_dao.get_referencias())

    def buscar_referencia(self):
        ref = self.txt_buscar.text().strip()
        if not ref:
            return
        if self.articulos_dao.find(ref):
            QMessageBox.warning(self, "Error", "La referencia ya existe.", QMessageBox.StandardButton.Close)
            self.referencia.clear()
            return
        self.referencia.setText(ref)

    def guardar_articulo(self) -> None:
        referencia = self.referencia.text().strip()
        descripcion = self.descripcion.text().strip()

        if not referencia:
            QMessageBox.warning(self, "Error", "Primero debes buscar una referencia disponible.", QMessageBox.StandardButton.Close)
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

        if self.articulos_dao.save(articulo):
            QMessageBox.information(self, "OK", "Artículo guardado correctamente.", QMessageBox.StandardButton.Close)
            self.limpiar()
            self.actualizar_completer()
        else:
            QMessageBox.critical(self, "Error", "No se ha podido guardar.", QMessageBox.StandardButton.Close)

    def limpiar(self):
        self.txt_buscar.clear()
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.clear()
