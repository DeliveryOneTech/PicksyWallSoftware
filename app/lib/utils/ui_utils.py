from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget


def get_icon(icon):
    return QtGui.QIcon(QtGui.QPixmap(f"{icon}"))


def get_pixmap(pixmap):
    return QtGui.QPixmap(f"{pixmap}")


def lock_ui(widget: QWidget):
    widget.setEnabled(False)
    widget.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))


def unlock_ui(widget: QWidget):
    widget.setEnabled(True)
    widget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
