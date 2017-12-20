#!/usr/bin/python3

import sys
import os
import json

from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication
)

from itasks.itasks_service import ItasksService


class Main(QMainWindow):
    temp_start_palindrome = 0

    def __init__(self):
        super(Main, self).__init__()

        # Start a new itasks session
        self.itasksService = ItasksService()
        self.itasksService.start_server()
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
        """
        Callback method for the creation of a new session
        :param instance_no: iTasks instance number
        :param instance_key: iTasks instance key
        :rtype: void
        """
        self.itasksService.attach_task_instance(
            instance_no, instance_key, self.task_callback)

    def task_callback(self, data):
        """
        Task instance callback method
        :param data: iTasks response data
        :rtype: void
        """
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
            self.itasksService.send_data(
                '["event",1,["1-61",null,"Start task"]]')
        if self.temp_start_palindrome is 4:
            obj = json.loads(data)
            global attributes
            if os.name is "nt":
                attributes = obj['change']['children'][0][2]['children'][0][2]
                attributes = attributes['children'][0][2]['children'][1][2]
                attributes = attributes['children'][0]['attributes']
            elif os.name is "posix":
                attributes = obj['change']['children'][0][2]['children']
                attributes = attributes[0][2]['definition']['children'][1]
                attributes = attributes['children'][0]['children']
                attributes = attributes[0]['attributes']
            instance_no = attributes['instanceNo']
            instance_key = attributes['instanceKey']
            self.itasksService.attach_task_instance(
                instance_no, instance_key, self.task_callback)
        self.temp_start_palindrome += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
