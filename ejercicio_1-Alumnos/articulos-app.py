import sys

from PyQt6.QtWidgets import QWidget, QApplication, QStackedWidget, QLabel, QVBoxLayout, \
    QHBoxLayout, QMainWindow, QStatusBar, QScrollArea

from Xwidgets.components_ui import BotonMenu, LabelItem, EditItem, BotonAction
from Xwidgets.nuevo_articulo_ui import NuevoArticuloUI
from Xwidgets.listado_articulos_ui import ListadoArticulosUI

class ArticulosApp(QWidget):
    def __init__(self):
        super().__init__()
        self.articulos = []
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Menu botones - Entradas")
        self.resize(600, 500)

        # Configuracion layouts
        layout = QVBoxLayout(self)

        self.panelMenu = QWidget(self)
        layout.addWidget(self.panelMenu)
        self.panelMenu.setStyleSheet("background-color: #8B0000;")

        self.panelCentral = QWidget(self)
        layout.addWidget(self.panelCentral)
        self.panelCentral.setStyleSheet("background-color: #00008B;")

        self.panelStatus = QWidget(self)
        layout.addWidget(self.panelStatus)
        self.panelStatus.setStyleSheet("background-color: #008B00;")

        # Configuración Menu

        return
        # Configuración panel Central
        self.panel_central = QStackedWidget()
        self.panel_central.setStyleSheet("background-color: #8B0000;")

        # Configuración panel StatusBar
        self.crear_statusBar()
        self.statusBar().showMessage(f"Número de articulos: {len(self.articulos)}")

        self.crear_widgets()




    def crear_widgets(self):




        self.nuevo_articulo_ui = NuevoArticuloUI(self.panel_central)
        self.listado_articulos_ui = ListadoArticulosUI(self.panel_central)
        # Añadimos el panel al QStackedWidget
        self.panel_central.addWidget(self.nuevo_articulo_ui)
        self.panel_central.addWidget(self.listado_articulos_ui)

        self.setCentralWidget(self.panel_central)

        panel_estado = QStatusBar()
        panel_estado.setStyleSheet("background-color: #c71585;")
        panel_estado.setFixedHeight(50)

        self.setStatusBar(panel_estado)


    def crear_menu(self):
        panel_menu = QWidget()
        panel_menu.setFixedHeight(50)
        panel_menu.setStyleSheet("background-color: #c71585;")
        self.setMenuWidget(panel_menu)

        layout_menu = QHBoxLayout(panel_menu)
        # panel_menu.setLayout(layout_menu)

        self.boton_nueva = BotonMenu("Nueva", panel_menu)
        self.boton_nueva.setCheckable(True)
        self.boton_nueva.setChecked(True)
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = BotonMenu("Listado", panel_menu)
        self.boton_listado.setCheckable(True)
        self.boton_listado.setChecked(False)
        self.boton_listado.clicked.connect(self.listado_entradas)

        self.boton_salir = BotonMenu("Salir", panel_menu)
        self.boton_salir.setCheckable(True)
        self.boton_salir.clicked.connect(self.cerrar_app)

        layout_menu.addWidget(self.boton_nueva)
        layout_menu.addWidget(self.boton_listado)
        layout_menu.addWidget(self.boton_salir)

    def crear_statusBar(self):
        pass

    def nueva_entrada(self):
        self.panel_central.setCurrentIndex(0)
        self.boton_nueva.setChecked(True)
        self.boton_listado.setChecked(False)

    def listado_entradas(self):
        self.panel_central.setCurrentIndex(1)
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(True)
        self.listado_articulos_ui.listar()

    def cerrar_app(self):
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(False)
        self.boton_salir.setChecked(True)
        # sys.exit()
        QApplication.quit()

    def guardar(self):
        entrada = self.edit_entrada.text()
        self.entradas.append(entrada)
        self.edit_entrada.clear()
        self.statusBar().showMessage(f"Número de entradas: {len(self.entradas)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())