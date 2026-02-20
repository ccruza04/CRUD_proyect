"""Interfaz gráfica PyQt6 para la gestión de artículos."""

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView,
)

from servicio_articulos import alta_articulo, baja_articulo, modificar_articulo, listar_articulos


class ArticulosApp(QWidget):
    """Ventana principal del CRUD de artículos."""

    def __init__(self):
        super().__init__()
        self._configurar_ui()
        self._cargar_tabla()

    def _configurar_ui(self):
        self.setWindowTitle("CRUD de Artículos - PyQt6")
        self.resize(900, 600)

        layout_principal = QVBoxLayout(self)

        titulo = QLabel("Gestión de Artículos")
        titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout_principal.addWidget(titulo)

        formulario = QVBoxLayout()

        fila_referencia = QHBoxLayout()
        fila_referencia.addWidget(QLabel("Referencia:"))
        self.txt_referencia = QLineEdit()
        self.txt_referencia.setPlaceholderText("Ejemplo: REF001")
        fila_referencia.addWidget(self.txt_referencia)
        formulario.addLayout(fila_referencia)

        fila_descripcion = QHBoxLayout()
        fila_descripcion.addWidget(QLabel("Descripción:"))
        self.txt_descripcion = QLineEdit()
        fila_descripcion.addWidget(self.txt_descripcion)
        formulario.addLayout(fila_descripcion)

        fila_precio = QHBoxLayout()
        fila_precio.addWidget(QLabel("Precio:"))
        self.txt_precio = QLineEdit()
        self.txt_precio.setPlaceholderText("Ejemplo: 59.99")
        fila_precio.addWidget(self.txt_precio)
        formulario.addLayout(fila_precio)

        fila_stock = QHBoxLayout()
        fila_stock.addWidget(QLabel("Stock:"))
        self.txt_stock = QLineEdit()
        self.txt_stock.setPlaceholderText("Ejemplo: 10")
        fila_stock.addWidget(self.txt_stock)
        formulario.addLayout(fila_stock)

        fila_observaciones = QHBoxLayout()
        fila_observaciones.addWidget(QLabel("Observaciones:"))
        self.txt_observaciones = QTextEdit()
        self.txt_observaciones.setFixedHeight(70)
        fila_observaciones.addWidget(self.txt_observaciones)
        formulario.addLayout(fila_observaciones)

        layout_principal.addLayout(formulario)

        fila_botones = QHBoxLayout()
        self.btn_alta = QPushButton("Alta")
        self.btn_baja = QPushButton("Baja")
        self.btn_modificar = QPushButton("Modificar")
        self.btn_listar = QPushButton("Listar")
        self.btn_limpiar = QPushButton("Limpiar")

        fila_botones.addWidget(self.btn_alta)
        fila_botones.addWidget(self.btn_baja)
        fila_botones.addWidget(self.btn_modificar)
        fila_botones.addWidget(self.btn_listar)
        fila_botones.addWidget(self.btn_limpiar)

        layout_principal.addLayout(fila_botones)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["Referencia", "Descripción", "Precio", "Stock", "Observaciones"])
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tabla.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        layout_principal.addWidget(self.tabla)

        self.lbl_estado = QLabel("Listo.")
        self.lbl_estado.setStyleSheet("padding: 6px; background-color: #f0f0f0;")
        layout_principal.addWidget(self.lbl_estado)

        self.btn_alta.clicked.connect(self._accion_alta)
        self.btn_baja.clicked.connect(self._accion_baja)
        self.btn_modificar.clicked.connect(self._accion_modificar)
        self.btn_listar.clicked.connect(self._cargar_tabla)
        self.btn_limpiar.clicked.connect(self._limpiar_campos)
        self.tabla.cellClicked.connect(self._cargar_desde_fila)

    def _datos_formulario(self):
        return (
            self.txt_referencia.text(),
            self.txt_descripcion.text(),
            self.txt_precio.text(),
            self.txt_stock.text(),
            self.txt_observaciones.toPlainText(),
        )

    def _mostrar_mensaje(self, titulo, texto, error=False):
        self.lbl_estado.setText(texto)
        if error:
            QMessageBox.warning(self, titulo, texto)
        else:
            QMessageBox.information(self, titulo, texto)

    def _accion_alta(self):
        ok, mensaje = alta_articulo(*self._datos_formulario())
        self._mostrar_mensaje("Alta de artículo", mensaje, error=not ok)
        if ok:
            self._cargar_tabla()
            self._limpiar_campos()

    def _accion_baja(self):
        referencia = self.txt_referencia.text()
        ok, mensaje = baja_articulo(referencia)
        self._mostrar_mensaje("Baja de artículo", mensaje, error=not ok)
        if ok:
            self._cargar_tabla()
            self._limpiar_campos()

    def _accion_modificar(self):
        ok, mensaje = modificar_articulo(*self._datos_formulario())
        self._mostrar_mensaje("Modificación de artículo", mensaje, error=not ok)
        if ok:
            self._cargar_tabla()

    def _cargar_tabla(self):
        articulos = listar_articulos()
        self.tabla.setRowCount(len(articulos))

        for fila, articulo in enumerate(articulos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(articulo.referencia))
            self.tabla.setItem(fila, 1, QTableWidgetItem(articulo.descripcion))
            self.tabla.setItem(fila, 2, QTableWidgetItem(f"{articulo.precio:.2f}"))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(articulo.stock)))
            self.tabla.setItem(fila, 4, QTableWidgetItem(articulo.observaciones))

        self.lbl_estado.setText(f"Artículos cargados: {len(articulos)}")

    def _cargar_desde_fila(self, fila, _columna):
        self.txt_referencia.setText(self.tabla.item(fila, 0).text())
        self.txt_descripcion.setText(self.tabla.item(fila, 1).text())
        self.txt_precio.setText(self.tabla.item(fila, 2).text())
        self.txt_stock.setText(self.tabla.item(fila, 3).text())
        self.txt_observaciones.setText(self.tabla.item(fila, 4).text())

    def _limpiar_campos(self):
        self.txt_referencia.clear()
        self.txt_descripcion.clear()
        self.txt_precio.clear()
        self.txt_stock.clear()
        self.txt_observaciones.clear()
