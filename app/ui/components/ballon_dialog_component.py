from PyQt5.QtCore import Qt, QTimer, QRect, QPoint
from PyQt5.QtGui import QPainter, QPolygon, QColor
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QApplication


class BalloonDialog(QDialog):
    def __init__(self, tooltip, parent=None):
        super().__init__(parent)
        self.tooltip = tooltip
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.ToolTip)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Şeffaf arka plan
        self.setStyleSheet("background-color: none;")  # Arka planı tamamen şeffaf yap
        self.setModal(False)

        # focus kaçarsa kapat
        QApplication.instance().focusChanged.connect(self.close)

        # Dialog içeriği
        label = QLabel(self.tooltip)
        label.setStyleSheet("padding: 10px; background-color: white; border-radius: 10px; border: 0px;")
        font = label.font()
        font.setPointSize(12)
        label.setFont(font)
        label.setWordWrap(True)

        # Layout ayarı
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.setContentsMargins(15, 35, 15, 15)  # Baloncuk ve ok için alan bırak
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Baloncuk gövdesi (aşağıda)
        rect = QRect(10, 30, self.width() - 20, self.height() - 40)
        painter.setBrush(QColor(255, 255, 255))  # Beyaz arka plan
        painter.setPen(QColor(150, 150, 150))  # Gri kenarlık
        painter.drawRoundedRect(rect, 10, 10)  # Yuvarlatılmış köşeler

        # Ok çizimi (baloncuğun üstündeki üçgen)
        triangle = QPolygon([
            QPoint(80 - 10, 30),  # Sol köşe
            QPoint(80 + 10, 30),  # Sağ köşe
            QPoint(80, 20)  # Alt köşe (ortada)
        ])
        painter.setBrush(QColor(255, 255, 255))  # Üçgenin rengi beyaz
        painter.setPen(Qt.NoPen)
        painter.drawPolygon(triangle)

    def show_with_position(self, x, y):
        self.move(x, y)
        self.show()
        QTimer.singleShot(5000, self.close)  # 5 saniye sonra kapan
        self.exec_()
