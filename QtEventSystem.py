import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLineEdit, QBoxLayout, QGridLayout, QLabel, QWidget


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        widget = QWidget()
        self.setCentralWidget(widget)
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)

        label1 = QLabel('Enter a palindrome')
        label2 = QLabel('<html><img src="icons/bug.png"></html>')
        label1.setContentsMargins(10, 20, 0, 20)
        label2.setContentsMargins(0, 0, 5, 0)

        input_line = QLineEdit(self)
        input_line.textChanged.connect(self.print_text)
        input_line.move(130, 22)
        input_line.setContentsMargins(5, 0, 0, 0)

        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_clicked)

        self.statusBar()

        layout_r = QBoxLayout(0)
        layout_r.addStretch()
        layout_r.addWidget(btn1)
        layout_r.setSpacing(0)
        layout_r.addWidget(btn2)

        layout_b = QBoxLayout(2)
        layout_b.addStretch()

        layout_t = QBoxLayout(2)
        layout_t.addWidget(label1)

        layout_l = QBoxLayout(1)
        layout_l.addWidget(label2)
        layout_l.addWidget(input_line)

        layout_t.addLayout(layout_l)
        layout_b.addLayout(layout_r)
        main_layout.addLayout(layout_b, 1, 0)
        main_layout.addLayout(layout_t, 0, 0)

        widget.setLayout(main_layout)

        self.setGeometry(300, 300, 1000, 500)
        self.setWindowTitle('Event sender')
        self.show()

    def print_text(self):
        sender = self.sender()
        self.statusBar().showMessage("Text Changed To: " + sender.text())

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
