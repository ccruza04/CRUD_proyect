from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QFrame, QVBoxLayout, QWidget


class BotonMenu(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #f3f3f3;
                color: #111111;
                border: 1px solid #a0a0a0;
                padding: 6px 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #e8e8e8;
            }
            QPushButton:pressed {
                background-color: #dcdcdc;
                border: 1px solid #7e7e7e;
            }
        """)


class BotonAction(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #e9eef7;
                color: #111111;
                border: 1px solid #8ea9d3;
                padding: 6px 10px;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #dce7f8;
            }
            QPushButton:pressed {
                background-color: #cfdcf3;
                border: 1px solid #7b96c3;
            }
        """)


class LabelItem(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("font-weight:600; color:#111111;")


class LabelTitulo(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("font-weight:700; color:#111111; font-size:14px;")


class EditItem(QLineEdit):
    def __init__(self, parent=None, placeholder=""):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #111111;
                border: 1px solid #9e9e9e;
                padding: 5px;
                border-radius: 2px;
            }
            QLineEdit:focus {
                border: 1px solid #5b9bd5;
            }
        """)


class TextItem(QWidget):
    def __init__(self, parent=None, placeholder=""):
        super().__init__(parent)

        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText(placeholder)
        self.text_edit.setStyleSheet("QTextEdit { color: #111111; background-color: #ffffff; border: none; }")

        self.frame = QFrame()
        self.frame.setStyleSheet(self._get_style())

        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setContentsMargins(2, 2, 2, 2)
        frame_layout.addWidget(self.text_edit)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.frame)

        self.text_edit.focusInEvent = self._on_focus_in
        self.text_edit.focusOutEvent = self._on_focus_out

        self._is_focus = False

    def _get_style(self, focus=False):
        border_color = "#9e9e9e"
        if focus:
            border_color = "#5b9bd5"
        return f"""
            QFrame {{
                border: 1px solid {border_color};
                border-radius: 2px;
                background-color: #ffffff;
            }}
        """

    def _on_focus_in(self, event):
        self._is_focus = True
        self._update_style()
        QTextEdit.focusInEvent(self.text_edit, event)

    def _on_focus_out(self, event):
        self._is_focus = False
        self._update_style()
        QTextEdit.focusOutEvent(self.text_edit, event)

    def _update_style(self):
        self.frame.setStyleSheet(self._get_style(focus=self._is_focus))

    def text(self):
        return self.text_edit.toPlainText()

    def setText(self, text):
        self.text_edit.setText(text)

    def setPlaceholderText(self, text):
        self.text_edit.setPlaceholderText(text)

    def clear(self):
        self.text_edit.clear()

    def setDisabled(self, disabled):
        self.text_edit.setDisabled(disabled)
