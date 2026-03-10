from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QFrame, QVBoxLayout, QWidget


class BotonMenu(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
                        QPushButton {
                            background-color: #00AA00;
                            border: 1px solid #444;
                            padding: 5px;
                            border-radius: 5px;
                        }
                        QPushButton:pressed {
                            background-color: #33CC33;
                            font-weight: bold;
                            border-bottom: 2px solid #000000;
                        }   
                        QPushButton:hover {
                            font-weight: bold;
                            border-color: #20b2aa;
                        }                             
                """)

class BotonAction(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
                        QPushButton {
                            background-color: #ba55d3;
                            border: 1px solid #444;
                            padding: 5px;
                            border-radius: 5px;
                        }
                        QPushButton:hover {
                            color: #c71585;
                            font-weight: bold;
                            border-color: #c71585;
                        }                             
                """)


class LabelItem(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text,parent)
        self.setStyleSheet("font-weight:bold; color:#0000BB;")

class LabelTitulo(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text,parent)
        self.setStyleSheet("font-weight:bold; color:#BB0000; font-size:14px;")



class EditItem(QLineEdit):
    def __init__(self, parent=None, placeholder=""):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #444;
                padding: 5px;
                border-radius: 5px;
            }

            QLineEdit:hover {
                border: 1px solid #20b2aa;
            }

            QLineEdit:focus {
                border: 2px solid #1e90ff;
            }            
        """)

# Los TextEdit requieren una configuracion especial para que se vean los bordes
class TextItem(QWidget):
    """
    QTextEdit con borde personalizado usando QFrame,
    que responde a focus y hover.
    """
    def __init__(self, parent=None, placeholder=""):
        super().__init__(parent)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(placeholder)

        # Frame contenedor
        self.frame = QFrame()
        self.frame.setStyleSheet(self._get_style(normal=True))
        self.frame.setMouseTracking(True)  # Necesario para hover

        # Layout del frame
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setContentsMargins(2, 2, 2, 2)
        frame_layout.addWidget(self.text_edit)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.frame)

        # Eventos focus
        self.text_edit.focusInEvent = self._on_focus_in
        self.text_edit.focusOutEvent = self._on_focus_out

        # Eventos hover
        self.frame.enterEvent = self._on_hover_in
        self.frame.leaveEvent = self._on_hover_out

        # Estado
        self._is_hover = False
        self._is_focus = False

    def _get_style(self, normal=False, hover=False, focus=False):
        """
        Genera el CSS del frame según estado.
        """
        border_color = "#444"
        border_width = "1px"
        if hover:
            border_color = "#20b2aa"
        if focus:
            border_color = "#1e90ff"
            border_width = "2px"

        return f"""
            QFrame {{
                border: {border_width} solid {border_color};
                border-radius: 5px;
                padding: 5px;
                background-color: #ffffff;
            }}
        """

    # -------------------------------
    # Focus Events
    # -------------------------------
    def _on_focus_in(self, event):
        self._is_focus = True
        self._update_style()
        QTextEdit.focusInEvent(self.text_edit, event)

    def _on_focus_out(self, event):
        self._is_focus = False
        self._update_style()
        QTextEdit.focusOutEvent(self.text_edit, event)

    # -------------------------------
    # Hover Events
    # -------------------------------
    def _on_hover_in(self, event):
        self._is_hover = True
        self._update_style()
        QWidget.enterEvent(self.frame, event)

    def _on_hover_out(self, event):
        self._is_hover = False
        self._update_style()
        QWidget.leaveEvent(self.frame, event)

    def _update_style(self):
        """Actualiza el CSS según hover/focus."""
        self.frame.setStyleSheet(self._get_style(hover=self._is_hover, focus=self._is_focus))

    # -------------------------------
    # Métodos útiles
    # -------------------------------
    def text(self):
        return self.text_edit.toPlainText()

    def setText(self, text):
        self.text_edit.setText(text)

    def setPlaceholderText(self, text):
        self.text_edit.setPlaceholderText(text)



