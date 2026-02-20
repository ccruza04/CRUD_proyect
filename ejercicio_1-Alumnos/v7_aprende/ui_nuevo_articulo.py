from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QStackedWidget, QLabel, QLineEdit, QFrame, QTextEdit, QFormLayout, QMessageBox
)

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction
from articulos_dao import ArticulosDao

class UINuevoArticulo(QWidget):
    """
    """

    def __init__(self, parent: QStackedWidget, articulos_dao: ArticulosDao):
        """
        """
        super().__init__(parent)
        parent.addWidget(self)
        self.articulos_dao = articulos_dao
        self.config_ui()

    # ----------------------------------------------
    #   CONFIGURACIÓN DE LA INTERFAZ
    # ----------------------------------------------

    def config_ui(self) -> None:
        """
        """
        layout = QVBoxLayout(self)

        # Stretch arriba para centrar verticalmente
        layout.addStretch(1)

        # Título centrado
        label = LabelTitulo("NUEVO ARTÍCULO")

        # Contenedor del formulario con borde
        widget_form = QFrame()

        # Formulario con QFormLayout
        form_layout = QFormLayout(widget_form)

        # Campos del formulario
        self.referencia = EditItem()
        form_layout.addRow(LabelItem("Referencia:"), self.referencia)

        self.descripcion = EditItem()
        form_layout.addRow(LabelItem("Descripción:"), self.descripcion)

        self.precio = EditItem()
        form_layout.addRow(LabelItem("Precio:"), self.precio)

        self.stock = EditItem()
        form_layout.addRow(LabelItem("Stock:"), self.stock)

        # Observaciones en línea separada
        label_obs = LabelItem("Observaciones:")
        form_layout.addRow(label_obs)
        self.observaciones = TextItem()
        form_layout.addRow(self.observaciones)

        # Botón Guardar alineado a la derecha
        boton_guardar = BotonAction("Guardar")
        boton_guardar.clicked.connect(self.guardar_articulo)

        form_layout.addRow(boton_guardar)

        layout.addWidget(widget_form)

        # Stretch abajo para centrar verticalmente
        layout.addStretch(1)



    # ----------------------------------------------
    #   FUNCIONALIDADES
    # ----------------------------------------------

    def guardar_articulo(self) -> None:
        """
        Guarda un nuevo artículo a partir de los datos introducidos en el formulario.

        Actualmente solo imprime un mensaje de prueba, pero en una versión
        completa debería validar los datos y añadir el artículo a la lista
        de artículos.
        """
        referencia = self.referencia.text()
        descripcion = self.descripcion.text()
        try:
            precio = float(self.precio.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "No se ha podido guardar el artículo.\nEl precio no es numérico.",
                                QMessageBox.StandardButton.Close)
            return
        try:
            stock = float(self.stock.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "No se ha podido guardar el artículo.\nEl stock no es numérico.",
                                QMessageBox.StandardButton.Close)
            return
        observaciones = self.observaciones.text()

        articulo = {
            "referencia": referencia,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "observaciones": observaciones
        }

        if self.articulos_dao.save(articulo):
            self.init_form()
        else:
            QMessageBox.critical(self, "Error",
                                 "No se ha podido guardar el artículo.",
                                 QMessageBox.StandardButton.Close)

    def init_form(self):
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.setText("")
