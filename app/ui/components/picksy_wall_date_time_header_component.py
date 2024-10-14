from PyQt5 import QtCore, QtWidgets
from app.ui.utils.styles import Styles


class PicksyWallDateTimeHeaderComponent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.setupUi(self)

    def setupUi(self, picksy_wall_header_widget):
        picksy_wall_header_widget.setObjectName("picksy_wall_header_widget")
        picksy_wall_header_widget.setStyleSheet(Styles.label())
        self.gridLayout = QtWidgets.QGridLayout(picksy_wall_header_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.picksy_wall_header_hlayout = QtWidgets.QHBoxLayout()
        self.picksy_wall_header_hlayout.setObjectName("picksy_wall_header_hlayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.picksy_wall_header_hlayout.addItem(spacerItem)
        self.picksy_wall_header_date_label = QtWidgets.QLabel(picksy_wall_header_widget)
        self.picksy_wall_header_date_label.setObjectName("picksy_wall_header_date_label")
        self.picksy_wall_header_hlayout.addWidget(self.picksy_wall_header_date_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.picksy_wall_header_hlayout.addItem(spacerItem1)
        self.picksy_wall_header_device_name_label = QtWidgets.QLabel(picksy_wall_header_widget)
        self.picksy_wall_header_device_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.picksy_wall_header_device_name_label.setObjectName("picksy_wall_header_device_name_label")
        self.picksy_wall_header_hlayout.addWidget(self.picksy_wall_header_device_name_label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.picksy_wall_header_hlayout.addItem(spacerItem2)
        self.picksy_wall_header_time_label = QtWidgets.QLabel(picksy_wall_header_widget)
        self.picksy_wall_header_time_label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.picksy_wall_header_time_label.setObjectName("picksy_wall_header_location_label")
        self.picksy_wall_header_hlayout.addWidget(self.picksy_wall_header_time_label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.picksy_wall_header_hlayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.picksy_wall_header_hlayout, 0, 0, 1, 1)
        self.picksy_wall_header_hr_label = QtWidgets.QLabel(picksy_wall_header_widget)
        self.picksy_wall_header_hr_label.setObjectName("picksy_wall_header_hr_label")
        self.gridLayout.addWidget(self.picksy_wall_header_hr_label, 1, 0, 1, 1)

        self.retranslateUi(picksy_wall_header_widget)

        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def retranslateUi(self, picksy_wall_header_widget):
        self.picksy_wall_header_device_name_label.setText("Picksy Wall #0001")
        self.picksy_wall_header_hr_label.setText("<html><body><hr/></body></html>")
        self.update_time()

    def update_time(self):
        current_time = QtCore.QTime.currentTime()
        self.picksy_wall_header_time_label.setText(current_time.toString("hh:mm"))
        current_date = QtCore.QDate.currentDate()
        self.picksy_wall_header_date_label.setText(current_date.toString("dd MMM yyyy"))
