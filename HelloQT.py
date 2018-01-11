import sys

# pylint: disable-all

from ui_generator import components
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


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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

        MainLayout = QGridLayout()
        MainLayout.setContentsMargins(0, 0, 0, 0)

        # LAYOUT RIGHT-TO-LEFT
        LayoutR = QBoxLayout(0)
        LayoutR.addStretch()
        LayoutR.addWidget(button1)
        LayoutR.setSpacing(0)
        LayoutR.addWidget(button2)

        # LAYOUT BOTTOM-TO-TOP
        LayoutB = QBoxLayout(2)
        LayoutB.addStretch()

        # LAYOUT TOP-TO-BOTTOM
        LayoutT = QBoxLayout(2)
        LayoutT.addWidget(label1)

        # LAYOUT LEFT-TO-RIGHT
        LayoutL = QBoxLayout(1)
        LayoutL.addWidget(label2)
        LayoutL.addWidget(line_edit1)

        lmao = components.Components.icon(iconCls="add")
        LayoutL.addWidget(lmao)
        # LAYOUT MERGING
        LayoutT.addLayout(LayoutL)
        LayoutB.addLayout(LayoutR)
        MainLayout.addLayout(LayoutB, 1, 0)
        MainLayout.addLayout(LayoutT, 0, 0)
        self.setLayout(MainLayout)

        self.setGeometry(0, 30, 800, 800)
        self.setWindowTitle('Hai nick')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
