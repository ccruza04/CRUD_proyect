import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QStackedWidget


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

    def config_ui(self):
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


# ----------------------------------------------
#   PROGRAMA PRINCIPAL
# ----------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())