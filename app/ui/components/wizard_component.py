from PyQt5 import QtWidgets, QtCore, QtGui
from app.styles import Styles


class WizardItemViewModel:
    def __init__(self, order: int, title: str):
        self.order = order
        self.title = title


class WizardComponent(QtWidgets.QWidget):
    current_index_changed = QtCore.pyqtSignal(int)

    def __init__(self,
                 wizard_item_name_prefix: str = "step_",
                 item_list: list[WizardItemViewModel] = None,
                 disable_steps: bool = False):
        super().__init__()
        self.item_list = item_list
        self.current_index = 0

        # Create the layout and components
        self.layout = QtWidgets.QHBoxLayout(self)

        self.step_labels = []
        for index, item in enumerate(self.item_list):
            step_label = QtWidgets.QLabel(f"{item.order}. {item.title}", self)
            step_label.setObjectName(f"{wizard_item_name_prefix}{index}")
            step_label.setStyleSheet(Styles.green_box())
            step_label.setDisabled(disable_steps)
            step_label.mousePressEvent = lambda event, idx=index: self.go_to_step(idx)
            spacer = QtWidgets.QSpacerItem(100, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.layout.addItem(spacer)
            self.layout.addWidget(step_label)
            spacer = QtWidgets.QSpacerItem(100, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
            self.layout.addItem(spacer)
            self.step_labels.append(step_label)

        # Center the widget
        self.setLayout(self.layout)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.current_index_changed.connect(self.update_view)

    def paintEvent(self, event):
        """Override paintEvent to draw lines between the step labels."""
        super().paintEvent(event)
        painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtGui.QColor("gray"), 2)
        painter.setPen(pen)

        # Draw lines between each step label
        for i in range(len(self.step_labels) - 1):
            start_label = self.step_labels[i]
            end_label = self.step_labels[i + 1]

            # Get the center bottom of the start label and center top of the end label
            start_pos = start_label.geometry().center()
            end_pos = end_label.geometry().center()

            # Draw a horizontal line between the labels
            painter.drawLine(start_pos.x(), start_pos.y(), end_pos.x(), end_pos.y())

    def update_view(self):
        """Update the view to reflect the current step."""
        for index, step_label in enumerate(self.step_labels):
            step_label.setStyleSheet(Styles.green_box())
            if index == self.current_index:
                step_label.setStyleSheet(Styles.gray_box())

    def emit_current_index_changed(self):
        self.current_index_changed.emit(self.current_index)

    def go_to_step(self, index: int):
        """Go to the specified step."""
        if 0 <= index < len(self.item_list):
            self.current_index = index
            self.emit_current_index_changed()
