import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel

from articulos_dao import ArticulosDao
from ui_components import BotonMenu
from ui_nuevo_articulo import UINuevoArticulo
from ui_consulta_articulo import UIConsultaArticulo

class ArticulosApp(QWidget):
    """
    """

    def __init__(self):
        """
        """
        super().__init__()
        self.articulosDao = ArticulosDao()
        self.config_ui()

    # ----------------------------------------------
    #   CONFIGURACIÓN DE LA INTERFAZ
    # ----------------------------------------------

    def config_ui(self) -> None:
        """
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
        self.panel_nuevo = UINuevoArticulo(self.panel_central, self.articulosDao)
        self.panel_consulta= UIConsultaArticulo(self.panel_central, self.articulosDao)
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
        self.boton_nuevo = BotonMenu("Nuevo")
        self.boton_nuevo.clicked.connect(self.opcion_nuevo)
        layout.addWidget(self.boton_nuevo)

        # Opción: Consulta Articulo
        self.boton_consulta = BotonMenu("Consulta")
        self.boton_consulta.clicked.connect(self.opcion_consulta)
        layout.addWidget(self.boton_consulta)

        # Opción: Baja Articulo
        self.boton_baja = BotonMenu("Baja")
        self.boton_baja.clicked.connect(self.opcion_baja)
        layout.addWidget(self.boton_baja)

        # Opción: Edición Articulo
        self.boton_edita = BotonMenu("Edición")
        self.boton_edita.clicked.connect(self.opcion_edita)
        layout.addWidget(self.boton_edita)

        # Opción: Listado Articulos
        self.boton_listado = BotonMenu("Listado")
        self.boton_listado.clicked.connect(self.opcion_listado)
        layout.addWidget(self.boton_listado)

        # Opción: Salir
        self.boton_salir = BotonMenu("Salir")
        self.boton_salir.clicked.connect(self.opcion_cerrar_app)
        layout.addWidget(self.boton_salir)



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
        panel= QWidget(self.panel_central)
        layout = QVBoxLayout(panel)
        layout.addWidget(QLabel("Listado"))
        self.panel_central.addWidget(panel)

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
    #   FUNCIONES CRUD
    # ----------------------------------------------



# ----------------------------------------------
#   PROGRAMA PRINCIPAL
# ----------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())