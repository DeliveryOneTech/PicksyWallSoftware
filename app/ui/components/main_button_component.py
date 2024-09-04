from PyQt5.QtWidgets import QVBoxLayout, QLabel, QFrame, QDialog, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from app.styles import Styles
from app.ui.components.ballon_dialog_component import BalloonDialog


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
        # Dialogu oluştur ve göster
        dialog = BalloonDialog(self.tooltip)

        # Pozisyon hesaplama
        x_coord = self.mapToGlobal(self.rect().topLeft()).x()
        y_coord = self.mapToGlobal(self.rect().topLeft()).y()
        dialog_width = self.width() - 40
        dialog.setFixedSize(dialog_width, 150)

        dialog.show_with_position(x_coord + 20, y_coord + 80)

    def remove_shadow_effect(self):
        self.setGraphicsEffect(None)

    def add_shadow_effect(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(60)
        shadow.setXOffset(15)
        shadow.setYOffset(10)
        shadow.setColor(Qt.gray)
        self.setGraphicsEffect(shadow)

    def enterEvent(self, event):
        self.remove_shadow_effect()
        self.setStyleSheet(Styles.btn_main_clicked())

    def leaveEvent(self, event):
        self.add_shadow_effect()
        self.setStyleSheet(Styles.btn_main())
