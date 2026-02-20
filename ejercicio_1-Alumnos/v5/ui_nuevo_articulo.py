from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QStackedWidget, QLabel, QLineEdit, QFrame, QTextEdit, QFormLayout
)

from ui_components import LabelTitulo, LabelItem, EditItem, TextItem, BotonAction


class UINuevoArticulo(QWidget):
    """
    Panel de la interfaz para crear un nuevo artículo.

    Esta clase representa la pantalla "Nuevo Artículo" de la aplicación.
    Campos: Referencia; Descripción; Precio; Stock; Observaciones
    Botones: Botón para guardar el artículo.

    Atributos:
        referencia (QLineEdit): Campo de texto para la referencia del artículo.
        descripcion (QLineEdit): Campo de texto para la descripción.
        precio (QLineEdit): Campo de texto para el precio.
        stock (QLineEdit): Campo de texto para el stock.
        observaciones (QTextEdit): Área de texto para observaciones adicionales.
    """

    def __init__(self, parent: QStackedWidget):
        """
        Inicializa el panel "Nuevo Artículo".

        Args:
            parent (QStackedWidget): Widget principal donde se añadirá este panel.
        """
        super().__init__(parent)
        parent.addWidget(self)
        self.config_ui()

    # ----------------------------------------------
    #   CONFIGURACIÓN DE LA INTERFAZ
    # ----------------------------------------------

    def config_ui(self) -> None:
        """
        Configura la interfaz gráfica del panel "Nuevo Artículo".

        Crea un formulario dentro de un QFrame con borde, centrado
        verticalmente en el panel, con los campos necesarios para
        introducir los datos del artículo y un botón "Guardar".
        """
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Stretch arriba para centrar verticalmente
        layout.addStretch(1)

        # Título centrado
        label = LabelTitulo("NUEVO ARTÍCULO")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Contenedor del formulario con borde
        widget_form = QFrame()
        widget_form.setMaximumWidth(500)
        widget_form.setFrameShape(QFrame.Shape.Box)
        widget_form.setFrameShadow(QFrame.Shadow.Raised)
        widget_form.setLineWidth(2)
        widget_form.setStyleSheet("background-color: white;")

        # Formulario con QFormLayout
        form_layout = QFormLayout(widget_form)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_layout.setHorizontalSpacing(10)
        form_layout.setVerticalSpacing(15)

        # Campos del formulario
        self.referencia = EditItem()
        self.referencia.setMaximumWidth(100)
        form_layout.addRow(LabelItem("Referencia:"), self.referencia)

        self.descripcion = EditItem()
        self.descripcion.setMaximumWidth(400)
        form_layout.addRow(LabelItem("Descripción:"), self.descripcion)

        self.precio = EditItem()
        self.precio.setMaximumWidth(70)
        form_layout.addRow(LabelItem("Precio:"), self.precio)

        self.stock = EditItem()
        self.stock.setMaximumWidth(70)
        form_layout.addRow(LabelItem("Stock:"), self.stock)

        # Observaciones en línea separada
        label_obs = LabelItem("Observaciones:")
        form_layout.addRow(label_obs)
        self.observaciones = TextItem()
        self.observaciones.setMaximumWidth(500)
        self.observaciones.setFixedHeight(80)
        form_layout.addRow(self.observaciones)

        # Botón Guardar alineado a la derecha
        boton_guardar = BotonAction("Guardar")
        boton_guardar.setFixedWidth(75)
        boton_guardar.clicked.connect(self.guardar_articulo)

        boton_layout = QVBoxLayout()
        boton_layout.addWidget(boton_guardar, alignment=Qt.AlignmentFlag.AlignRight)
        form_layout.addRow(boton_layout)

        # Añade el formulario al layout principal
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
        print("Guardar articulo")
