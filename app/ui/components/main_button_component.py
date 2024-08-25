from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QDialog, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from app.styles import Styles


class MainButtonComponent(QFrame):
    def __init__(self, title_html, icon_path, tooltip):
        super().__init__()
        self.tooltip = tooltip

        # Set the overall style for the button component
        self.setStyleSheet(Styles.btn_main())

        # Layout for the button component
        layout = QVBoxLayout()

        # Info Icon (top left)
        info_icon = QLabel()
        info_icon.setPixmap(QPixmap(':/icons/assets/info-circle-fill.svg').scaled(48, 48, Qt.KeepAspectRatio))
        info_icon.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        # onclick event
        info_icon.mousePressEvent = lambda event: self.show_dialog()

        # Title (with HTML support)
        title_label = QLabel(title_html)
        title_label.setFont(QFont("Arial", 16))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setTextFormat(Qt.RichText)  # Allows HTML formatting in the text

        # Main Icon
        icon_label = QLabel()
        icon_label.setPixmap(QPixmap(icon_path).scaled(176, 176, Qt.KeepAspectRatio))
        icon_label.setAlignment(Qt.AlignCenter)

        # Add widgets to the layout
        layout.addWidget(info_icon)
        layout.addStretch()
        layout.addWidget(title_label)
        layout.addWidget(icon_label)
        layout.addStretch()

        # add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(60)
        shadow.setXOffset(15)
        shadow.setYOffset(10)
        shadow.setColor(Qt.gray)
        self.setGraphicsEffect(shadow)

        self.setLayout(layout)

    def show_dialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("Info")
        dialog.setWindowFlag(Qt.FramelessWindowHint)
        dialog.setStyleSheet("""
            background-color: white;
            QLabel {
                padding: 5px;
                text-align: center;
            }
        """)

        # butonun üstüne tam oturması
        x_coord = self.mapToGlobal(self.rect().topLeft()).x()
        y_coord = self.mapToGlobal(self.rect().topLeft()).y()
        dialog.move(x_coord + 20, y_coord)
        btn_width = self.width() - 40
        dialog.setFixedSize(btn_width, 100)

        label = QLabel(self.tooltip)
        font = label.font()
        font.setPointSize(12)
        label.setFont(font)
        label.setWordWrap(True)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)
        dialog.setLayout(dialog_layout)

        dialog.show()
        QTimer.singleShot(5000, dialog.close)
        dialog.exec_()
