import sys
import PyQt5.QtCore
from PyQt5.QtGui import QIcon, QPicture, QPainter

from PyQt5.QtWidgets import (QWidget, QPushButton,
    QBoxLayout, QHBoxLayout, QVBoxLayout, QApplication, QLabel, QLineEdit, QGridLayout)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        b1 = QPushButton("OK")
        b2 = QPushButton("Cancel")
        l1 = QLabel('Enter a palindrome')
        l2 = QLabel('<html><img src="icons/bug.png"></html>')
        q1 = QLineEdit()

        #OPMAAK
        I1 = QIcon("icons/accept.png")
        I2 = QIcon("icons/cancel.png")
        b1.setIcon(I1)
        b1.setEnabled(False)
        b1.setMaximumSize(45,30)
        b2.setIcon(I2)
        b2.setMaximumSize(60,30)
        l1.setContentsMargins(10,20,0,20)
        q1.setContentsMargins(5,0,0,0)
        l2.setContentsMargins(0,0,5,0)

        MainLayout = QGridLayout()
        MainLayout.setContentsMargins(0,0,0,0)

        #LAYOUTR
        LayoutR = QBoxLayout(0)
        LayoutR.addStretch()
        LayoutR.addWidget(b1)
        LayoutR.setSpacing(0)
        LayoutR.addWidget(b2)

        #LAYOUTB
        LayoutB = QBoxLayout(2)
        LayoutB.addStretch()

        #LAYOUTT
        LayoutT = QBoxLayout(2)
        LayoutT.addWidget(l1)

        #LAYOUTR2
        LayoutL = QBoxLayout(1)
        LayoutL.addWidget(l2)
        LayoutL.addWidget(q1)

        #LAYOUTMERGE
        LayoutT.addLayout(LayoutL)
        LayoutB.addLayout(LayoutR)
        MainLayout.addLayout(LayoutB, 1,0)
        MainLayout.addLayout(LayoutT, 0, 0)
        self.setLayout(MainLayout)

        self.setGeometry(0, 30, 800, 800)
        self.setWindowTitle('Hai nick')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())