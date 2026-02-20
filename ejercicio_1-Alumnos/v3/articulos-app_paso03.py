import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel


class ArticulosApp(QWidget):
    """
    Aplicación de gestión de artículos.

    Funcionalidades: Nuevo; Consulta; Baja; Edición; Listado

    Contiene un menú superior con opciones, un panel central
    donde se mostrarán las distintas pantallas de la aplicación
    y una barra para indicar el resultado de las acciones.
    """

    def __init__(self):
        """
        Constructor de la aplicación.
        Inicializa la lista de artículos y configura la interfaz gráfica.
        """
        super().__init__()
        self.articulos = []   #  Para ponerlo más correcto: self.articulos: List[Dict] = []
        self.config_ui()

    # ----------------------------------------------
    #   CONFIGURACIÓN DE LA INTERFAZ
    # ----------------------------------------------

    def config_ui(self) -> None:
        """
        Configura la interfaz principal de la ventana.

        Crea la estructura básica con tres paneles:
        - Menú superior
        - Panel central
        - Barra de estado
        """
        self.setWindowTitle("Gestión de Artículos")
        self.resize(600, 500)

        # Configuracion layouts
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Panel Menu
        self.panel_menu = QWidget(self)
        layout.addWidget(self.panel_menu)
        self.panel_menu.setStyleSheet("background-color: #AA0000;")
        self.panel_menu.setFixedHeight(50)

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
        self.crear_widgets_nuevo()
        self.crear_widgets_consulta()
        self.crear_widgets_baja()
        self.crear_widgets_edita()
        self.crear_widgets_listado()

        # Muestra inicialmente la opción Nuevo
        self.panel_central.setCurrentIndex(0)


    def crear_menu(self) -> None:
        """
        Crea el menú principal con los botones de navegación.
        """
        layout = QHBoxLayout(self.panel_menu)

        # Opción: Nuevo Articulo
        self.boton_nuevo = QPushButton("Nuevo")
        self.boton_nuevo.setStyleSheet("background-color: #00AA00;")
        self.boton_nuevo.clicked.connect(self.opcion_nuevo)
        layout.addWidget(self.boton_nuevo)

        # Opción: Consulta Articulo
        self.boton_consulta = QPushButton("Consulta")
        self.boton_consulta.setStyleSheet("background-color: #00AA00;")
        self.boton_consulta.clicked.connect(self.opcion_consulta)
        layout.addWidget(self.boton_consulta)

        # Opción: Baja Articulo
        self.boton_baja = QPushButton("Baja")
        self.boton_baja.setStyleSheet("background-color: #00AA00;")
        self.boton_baja.clicked.connect(self.opcion_baja)
        layout.addWidget(self.boton_baja)

        # Opción: Edición Articulo
        self.boton_edita = QPushButton("Edicion")
        self.boton_edita.setStyleSheet("background-color: #00AA00;")
        self.boton_edita.clicked.connect(self.opcion_edita)
        layout.addWidget(self.boton_edita)

        # Opción: Listado Articulos
        self.boton_listado = QPushButton("Listado")
        self.boton_listado.setStyleSheet("background-color: #00AA00;")
        self.boton_listado.clicked.connect(self.opcion_listado)
        layout.addWidget(self.boton_listado)

        # Opción: Salir
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.setStyleSheet("background-color: #00AA00;")
        self.boton_salir.clicked.connect(self.opcion_cerrar_app)
        layout.addWidget(self.boton_salir)


    def crear_widgets_nuevo(self) -> None:
        """
        Crea los widgets de la opción 'Nuevo'
        """
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Nuevo"))
        self.panel_central.addWidget(panel)

    def crear_widgets_consulta(self) -> None:
        """
        Crea los widgets de la opción 'Consulta'
        """
        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Consulta"))
        self.panel_central.addWidget(panel)

    def crear_widgets_baja(self) -> None:
        """
        Crea los widgets de la opción 'Baja'
        """
        panel= QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Baja"))
        self.panel_central.addWidget(panel)

    def crear_widgets_edita(self) -> None:
        """
        Crea los widgets de la opción 'Edita'
        """
        panel= QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Edición"))
        self.panel_central.addWidget(panel)

    def crear_widgets_listado(self) -> None:
        """
        Crea los widgets de la opción 'Listado'
        """
        panel= QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Listado"))
        self.panel_central.addWidget(panel)

    def opcion_cerrar_app(self) -> None:
        """ Cierra la aplicación. """
        QApplication.quit()

    # ----------------------------------------------
    #   ACCIONES DEL MENU PRINCIPAL
    # ----------------------------------------------

    def opcion_nuevo(self) -> None:
        """ Acción ejecutada al pulsar el botón 'Nuevo'. """
        self.panel_central.setCurrentIndex(0)

    def opcion_consulta(self) -> None:
        """ Acción ejecutada al pulsar el botón 'Consulta'. """
        self.panel_central.setCurrentIndex(1)

    def opcion_baja(self) -> None:
        """ Acción ejecutada al pulsar el botón 'Baja'. """
        self.panel_central.setCurrentIndex(2)

    def opcion_edita(self) -> None:
        """ Acción ejecutada al pulsar el botón 'Edición'. """
        self.panel_central.setCurrentIndex(3)

    def opcion_listado(self) -> None:
        """ Acción ejecutada al pulsar el botón 'Listado'. """
        self.panel_central.setCurrentIndex(4)

    def opcion_cerrar_app(self) -> None:
        """ Cierra la aplicación. """
        QApplication.quit()


# ----------------------------------------------
#   PROGRAMA PRINCIPAL
# ----------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())