from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from app.styles import Styles


class StatusCircle(QWidget):
    def __init__(self, status='gray'):
        super().__init__()
        self.status = status
        self.setFixedSize(50, 50)  # Only circle size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Set color based on status
        if self.status == 'yellow':
            painter.setBrush(QColor(255, 255, 0))  # Yellow
        elif self.status == 'green':
            painter.setBrush(QColor(0, 255, 0))  # Green
        elif self.status == 'red':
            painter.setBrush(QColor(255, 0, 0))  # Red
        else:
            painter.setBrush(QColor(128, 128, 128))  # Gray

        # Draw the circle without any border
        radius = 20
        painter.drawEllipse(self.width() // 2 - radius, self.height() // 2 - radius, radius * 2, radius * 2)


class StatusCircleComponent(QWidget):
    def __init__(self, status_name: str, status: str = 'yellow'):
        super().__init__()
        self.status_name = status_name
        self.status_circle = StatusCircle(status)
        self.status_label = QLabel(self.status_name)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet(Styles.label())

        layout = QHBoxLayout()
        layout.addWidget(self.status_circle)
        layout.addWidget(self.status_label)

        self.setLayout(layout)
