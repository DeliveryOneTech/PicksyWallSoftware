from PyQt5 import QtGui


def get_icon(icon):
    return QtGui.QIcon(QtGui.QPixmap(f"{icon}"))


def get_pixmap(pixmap):
    return QtGui.QPixmap(f"{pixmap}")
