"""Demo code for layouts and other basic PyQT things."""
# pylint: disable-msg=no-name-in-module
# pylint: disable-msg=too-few-public-methods

import sys

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (  # pylint: disable-msg=E0611
    QWidget,
    QPushButton,
    QBoxLayout,
    QApplication,
    QLabel,
    QLineEdit,
    QGridLayout
)

from ui_generator import components


class Example(QWidget):
    """Example class for demonstrating how PyQt works"""

    def __init__(self):
        """
        Initializes the UI by calling init_ui and
        the super.__init__ of the Qwidget
        """

        super().__init__()

        self.init_ui()

    def init_ui(self):
        """Initialises the UI"""

        button1 = QPushButton("OK")
        button2 = QPushButton("Cancel")
        label1 = QLabel('Enter a palindrome')
        label2 = QLabel('<html><img src="icons/bug.png"></html>')
        line_edit1 = QLineEdit()

        # OPMAAK
        icon1 = QIcon("icons/accept.png")
        icon2 = QIcon("icons/cancel.png")
        button1.setIcon(icon1)
        button1.setEnabled(False)
        button1.setMaximumSize(45, 30)
        button2.setIcon(icon2)
        button2.setMaximumSize(60, 30)
        label1.setContentsMargins(10, 20, 0, 20)
        line_edit1.setContentsMargins(5, 0, 0, 0)
        label2.setContentsMargins(0, 0, 5, 0)

        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # LAYOUT RIGHT-TO-LEFT
        layout_r = QBoxLayout(0)
        layout_r.addStretch()
        layout_r.addWidget(button1)
        layout_r.setSpacing(0)
        layout_r.addWidget(button2)

        # LAYOUT BOTTOM-TO-TOP
        layout_b = QBoxLayout(2)
        layout_b.addStretch()

        # LAYOUT TOP-TO-BOTTOM
        layout_t = QBoxLayout(2)
        layout_t.addWidget(label1)

        # LAYOUT LEFT-TO-RIGHT
        layout_l = QGridLayout()
        layout_l.addWidget(label2, 0, 0)
        layout_l.addWidget(line_edit1, 0, 1)

        # LAYOUT MERGING
        layout_t.addLayout(layout_l)
        layout_b.addLayout(layout_r)
        main_layout.addLayout(layout_b, 1, 0)
        main_layout.addLayout(layout_t, 0, 0)
        self.setLayout(main_layout)

        self.setGeometry(0, 30, 800, 800)
        self.setWindowTitle('Hai nick')
        self.show()


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    ex = Example()
    sys.exit(APP.exec_())
