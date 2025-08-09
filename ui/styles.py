from PySide6.QtCore import QFile
from PySide6.QtWidgets import QWidget

def apply_styles(widget: QWidget):
    try:
        f = QFile("ui/styles.qss")
        if f.open(QFile.ReadOnly | QFile.Text):
            data = f.readAll().data().decode("utf-8")
            widget.setStyleSheet(data)
    except Exception:
        pass
