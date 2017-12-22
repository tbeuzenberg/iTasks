""" QtEventSystemExample """
import sys
from PyQt5.QtWidgets import (  # pylint: disable-msg=E0611
    QMainWindow,
    QPushButton,
    QApplication,
    QLineEdit,
    QBoxLayout,
    QGridLayout,
    QLabel,
    QWidget
)


class QtEventSystemExample(QMainWindow):
    """" Initialise Components """
    def __init__(self):
        """ init """
        super().__init__()
        # Initialise Components here so we can access them in the functions
        self.widget = QWidget()
        self.btn1 = QPushButton("Continue", self)
        self.btn2 = QPushButton("Quit", self)
        self.label1 = QLabel('Enter a palindrome')
        self.label2 = QLabel('<html><img src="icons/bug.png"></html>')
        self.main_layout = QGridLayout()
        self.init_ui()

    def init_ui(self):
        """ init_ui """
        # Set actions listeners and layout
        self.setCentralWidget(self.widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.label1.setContentsMargins(10, 20, 0, 20)
        self.label2.setContentsMargins(0, 0, 5, 0)

        input_line = QLineEdit(self)
        input_line.textChanged.connect(self.print_text)
        input_line.move(130, 22)
        input_line.setContentsMargins(5, 0, 0, 0)

        self.btn1.clicked.connect(self.button_clicked)
        self.btn2.clicked.connect(self.button_clicked)
        self.btn1.setEnabled(False)

        self.statusBar()

        # LAYOUT RIGHT-TO-LEFT
        layout_r = QBoxLayout(0)
        layout_r.addStretch()
        layout_r.addWidget(self.btn1)
        layout_r.setSpacing(0)
        layout_r.addWidget(self.btn2)

        # LAYOUT BOTTOM-TO-TOP
        layout_b = QBoxLayout(2)
        layout_b.addStretch()

        # LAYOUT TOP-TO-BOTTOM
        layout_t = QBoxLayout(2)
        layout_t.addWidget(self.label1)

        # LAYOUT LEFT-TO-RIGHT
        layout_l = QBoxLayout(1)
        layout_l.addWidget(self.label2)
        layout_l.addWidget(input_line)

        # LAYOUT MERGING
        layout_t.addLayout(layout_l)
        layout_b.addLayout(layout_r)
        self.main_layout.addLayout(layout_b, 1, 0)
        self.main_layout.addLayout(layout_t, 0, 0)
        self.widget.setLayout(self.main_layout)

        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('Event sender')
        self.show()

    def print_text(self):
        """ Prints whether it is a palindrome or not """
        sender = self.sender()
        text = str(sender.text())
        if text == text[::-1] and text is not None and text != "" and len(text) is not 1:
            self.btn1.setEnabled(True)
            self.statusBar().showMessage(sender.text() + " is a palindrome")
        else:
            self.btn1.setEnabled(False)
            self.statusBar().showMessage(sender.text() + " is not a palindrome")

    @staticmethod
    def button_clicked():
        """ Button clicked event """
        APP.quit()


APP = QApplication(sys.argv)
ex = QtEventSystemExample()
sys.exit(APP.exec_())
