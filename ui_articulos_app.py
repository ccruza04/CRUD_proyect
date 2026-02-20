import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel, QStyleFactory

from articulos_dao import ArticulosDao
from ui_components import BotonMenu
from ui_nuevo_articulo import UINuevoArticulo
from ui_consulta_articulo import UIConsultaArticulo
from ui_baja_articulo import UIBajaArticulo
from ui_edita_articulo import UIEditaArticulo
from ui_listado_articulos import UIListadoArticulos


class ArticulosApp(QWidget):
    def __init__(self):
        super().__init__()
        self.articulos_dao = ArticulosDao()
        self.config_ui()

    def config_ui(self) -> None:
        self.setWindowTitle("Gestión de Artículos")
        self.resize(800, 550)
        self.setStyleSheet("""
            QWidget {
                color: #111111;
                background-color: #f0f0f0;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.panel_menu = QWidget(self)
        layout.addWidget(self.panel_menu)
        self.panel_menu.setStyleSheet("background-color: #e1e1e1;")
        self.panel_menu.setFixedHeight(50)

        self.panel_central = QStackedWidget(self)
        layout.addWidget(self.panel_central)
        self.panel_central.setStyleSheet("background-color: #f7f7f7; color: #111111;")

        self.panel_status = QLabel("Aplicación iniciada")
        layout.addWidget(self.panel_status)
        self.panel_status.setStyleSheet("background-color: #d6e3f3; color: #111111; padding: 8px;")

        self.crear_menu()

        self.panel_nuevo = UINuevoArticulo(self.panel_central, self.articulos_dao)
        self.panel_consulta = UIConsultaArticulo(self.panel_central, self.articulos_dao)
        self.panel_baja = UIBajaArticulo(self.panel_central, self.articulos_dao)
        self.panel_edita = UIEditaArticulo(self.panel_central, self.articulos_dao)
        self.panel_listado = UIListadoArticulos(self.panel_central, self.articulos_dao)

        self.panel_central.setCurrentIndex(0)

    def crear_menu(self) -> None:
        layout = QHBoxLayout(self.panel_menu)

        self.boton_nuevo = BotonMenu("Nuevo")
        self.boton_nuevo.clicked.connect(self.opcion_nuevo)
        layout.addWidget(self.boton_nuevo)

        self.boton_consulta = BotonMenu("Consulta")
        self.boton_consulta.clicked.connect(self.opcion_consulta)
        layout.addWidget(self.boton_consulta)

        self.boton_baja = BotonMenu("Baja")
        self.boton_baja.clicked.connect(self.opcion_baja)
        layout.addWidget(self.boton_baja)

        self.boton_edita = BotonMenu("Edición")
        self.boton_edita.clicked.connect(self.opcion_edita)
        layout.addWidget(self.boton_edita)

        self.boton_listado = BotonMenu("Listado")
        self.boton_listado.clicked.connect(self.opcion_listado)
        layout.addWidget(self.boton_listado)

        self.boton_salir = BotonMenu("Salir")
        self.boton_salir.clicked.connect(self.opcion_cerrar_app)
        layout.addWidget(self.boton_salir)

    def opcion_nuevo(self) -> None:
        self.panel_status.setText("Pestaña: Nuevo")
        self.panel_central.setCurrentIndex(0)

    def opcion_consulta(self) -> None:
        self.panel_status.setText("Pestaña: Consulta")
        self.panel_central.setCurrentIndex(1)

    def opcion_baja(self) -> None:
        self.panel_status.setText("Pestaña: Baja")
        self.panel_central.setCurrentIndex(2)

    def opcion_edita(self) -> None:
        self.panel_status.setText("Pestaña: Edición")
        self.panel_central.setCurrentIndex(3)

    def opcion_listado(self) -> None:
        self.panel_status.setText("Pestaña: Listado")
        self.panel_listado.listar()
        self.panel_central.setCurrentIndex(4)

    def opcion_cerrar_app(self) -> None:
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Windows"))
    ventana = ArticulosApp()
    ventana.show()
    sys.exit(app.exec())
