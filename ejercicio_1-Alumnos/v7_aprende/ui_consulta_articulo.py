from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QStackedWidget, QLabel, QLineEdit, QFrame, QTextEdit, QFormLayout, QMessageBox, QHBoxLayout
)

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction
from articulos_dao import ArticulosDao


class UIConsultaArticulo(QWidget):
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
        label = LabelTitulo("CONSULTA ARTÍCULO")


        # Contenedor del formulario con borde
        widget_form = QFrame()

        # Formulario con QFormLayout
        form_layout = QFormLayout(widget_form)

        self.referencia_buscada_widget(form_layout)

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

        # Añade el formulario al layout principal
        layout.addWidget(widget_form)

        # Stretch abajo para centrar verticalmente
        layout.addStretch(1)

        self.init_form()

    def referencia_buscada_widget(self, form_layout):
        busqueda_frame = QFrame()

        busqueda_layout = QHBoxLayout(busqueda_frame)

        busqueda_layout.addWidget(LabelItem("Referencia a buscar:"))

        self.referencia_buscada = EditItem()
        busqueda_layout.addWidget( self.referencia_buscada)

        boton_consultar = BotonAction("Buscar")
        boton_consultar.clicked.connect(self.consultar_articulo)
        busqueda_layout.addWidget(boton_consultar)

        # Añade el bloque de búsqueda antes del formulario principal
        form_layout.addRow(busqueda_frame)

    # ----------------------------------------------
    #   FUNCIONALIDADES
    # ----------------------------------------------

    def consultar_articulo(self) -> None:
        """
        """
        referencia_buscada = self.referencia_buscada.text()

        articulo = self.articulos_dao.find(referencia_buscada)
        self.init_form()

        if articulo:
            self.referencia.setText(articulo.get("referencia"))
            self.descripcion.setText(articulo.get("descripcion"))
            self.precio.setText( str(articulo.get("precio")) )
            self.stock.setText( str(articulo.get("stock")) )
            self.observaciones.setText(articulo.get("observaciones"))
        else:
            QMessageBox.warning(self, "Error", "No se ha encontrado la referncia indicada.",
                                QMessageBox.StandardButton.Close)

    def init_form(self):
        self.referencia_buscada.clear()
        self.referencia.clear()
        self.descripcion.clear()
        self.precio.clear()
        self.stock.clear()
        self.observaciones.setText("")

        self.referencia.setDisabled(True)
        self.descripcion.setDisabled(True)
        self.precio.setDisabled(True)
        self.stock.setDisabled(True)
        self.observaciones.setDisabled(True)


