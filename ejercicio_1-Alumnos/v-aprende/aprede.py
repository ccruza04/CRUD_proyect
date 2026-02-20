import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, \
    QFormLayout, QLineEdit, QTextEdit


class Aprende(QWidget):
    def __init__(self):
        super().__init__()
        self.config_ui()


    def config_ui(self) -> None:
        self.setWindowTitle("Gestión de Artículos")

        # Configuracion layouts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Panel Menu
        self.panelMenu = QWidget(self)
        layout.addWidget(self.panelMenu)
        self.panelMenu.setStyleSheet("background-color: #AA0000;")
        self.panelMenu.setFixedHeight(50)

        # Panel Nuevo
        self.panel_central = QStackedWidget(self)
        layout.addWidget(self.panel_central)
        self.panel_central.setStyleSheet("background-color: #00AAAA;")

        # Panel Status
        self.panel_status = QWidget(self)
        layout.addWidget(self.panel_status)
        self.panel_status.setStyleSheet("background-color: #00AA00;")
        self.panel_status.setFixedHeight(50)

        # Creación de widgets
        self.crear_menu()
        self.crear_widgets_portada()
        self.crear_widgets_nuevo()
        self.crear_widgets_consulta()

        self.panel_central.setCurrentIndex(0)


    def crear_menu(self) -> None:
        layout = QHBoxLayout(self.panelMenu)

        # Opción: Nuevo Articulo
        self.boton_nuevo = QPushButton("Nuevo")
        self.boton_nuevo.clicked.connect(self.opcion_nuevo)
        layout.addWidget(self.boton_nuevo)

        # Opción: Consulta Articulo
        self.boton_consulta = QPushButton("Consulta")
        self.boton_consulta.clicked.connect(self.opcion_consulta)
        layout.addWidget(self.boton_consulta)

        # Opción: Salir
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.clicked.connect(self.opcion_cerrar_app)
        layout.addWidget(self.boton_salir)


    def crear_widgets_portada(self) -> None:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Portada"))
        self.panel_central.addWidget(panel)

    def crear_widgets_nuevo(self) -> None:
        panel = QWidget()
        layout = QVBoxLayout(panel)

        label = QLabel("NUEVO ARTICULO")
        layout.addWidget(label)

        # Formulario con QFormLayout
        form_layout = QFormLayout(panel)

        # Campos
        self.referencia = QLineEdit()
        self.referencia.setMaximumWidth(100)
        form_layout.addRow("Referencia:", self.referencia)

        self.descripcion = QLineEdit()
        self.descripcion.setMaximumWidth(400)
        form_layout.addRow("Descripción:", self.descripcion)

        label_obs = QLabel("Observaciones")
        form_layout.addRow(label_obs)
        self.observaciones = QTextEdit()
        form_layout.addRow(self.observaciones)

        # Botón
        boton_guardar = QPushButton("Guardar")
        boton_guardar.clicked.connect(self.guardar_articulo)
        form_layout.addRow(boton_guardar)

        layout.addLayout(form_layout)

        #  Stretch abajo para centrar verticalmente
        layout.addStretch(1)


        self.panel_central.addWidget(panel)

    def crear_widgets_consulta(self) -> None:
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Consulta"))
        self.panel_central.addWidget(panel)

    # ----------------------------------------------
    #   ACCIONES DEL MENU PRINCIPAL
    # ----------------------------------------------

    def opcion_nuevo(self) -> None:
        self.panel_central.setCurrentIndex(1)

    def opcion_consulta(self) -> None:
        self.panel_central.setCurrentIndex(2)

    def opcion_cerrar_app(self) -> None:
        QApplication.quit()

    # --------------------------------------
    def guardar_articulo(self) -> None:
        print("Guardar articulo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Aprende()
    ventana.show()
    sys.exit(app.exec())