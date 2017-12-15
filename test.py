#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
from iTasksService import ItasksService
import json


class Example(QMainWindow):

    itasksService = None
    temp_start_palindrome = 0

    def __init__(self, itasks_service):
        super(Example, self).__init__()

        # Start a new itasks session
        self.itasksService = itasks_service
        self.itasksService.new_session(self.new_session_callback)

        self.initUI()

    def initUI(self):
        window = QWidget()

        ok_button = QPushButton("OK", self)
        cancel_button = QPushButton("Cancel", self)
        ok_button.clicked.connect(self.button_clicked)
        cancel_button.clicked.connect(self.button_clicked)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        window.setLayout(vbox)
        self.setCentralWidget(window)

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('iTasks')
        self.show()

    def closeEvent(self, q_close_event):
        self.itasksService.stop_server()

    def button_clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def new_session_callback(self, instance_no, instance_key):
        self.itasksService.attach_task_instance(instance_no, instance_key, self.task_callback)

    def task_callback(self, data):
        self.statusBar().showMessage(data)
        print(data)

        # Start the palindrome task
        if self.temp_start_palindrome is 0:
            self.itasksService.send_data('["event",1,["1-7",null,"Continue"]]')
        if self.temp_start_palindrome is 1:
            self.itasksService.send_data('["event",1,["1-41",null,"New"]]')
        if self.temp_start_palindrome is 2:
            self.itasksService.send_data('["event",1,["1-63","v",[17]]]')
        if self.temp_start_palindrome is 3:
            self.itasksService.send_data('["event",1,["1-61",null,"Start task"]]')
        if self.temp_start_palindrome is 4:
            object = json.loads(data)
            attributes = object['change']['children'][0][2]['children'][0][2]['definition']['children'][1]['children'][0]['children'][0]['attributes']
            instance_no = attributes['instanceNo']
            instance_key = attributes['instanceKey']
            self.itasksService.attach_task_instance(instance_no, instance_key, self.task_callback)
        self.temp_start_palindrome += 1


if __name__ == '__main__':
    service = ItasksService()

    app = QApplication(sys.argv)
    ex = Example(service)
    sys.exit(app.exec_())
