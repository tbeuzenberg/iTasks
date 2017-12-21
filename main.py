#!/usr/bin/python3

""" iTasks Desktop Application Entry point """

import sys
import os
import json

from PyQt5.QtWidgets import (  # pylint: disable-msg=E0611
    QMainWindow,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication
)

from itasks.itasks_service import ItasksService


class Main(QMainWindow):
    """ Main Window for the """

    temp_start_palindrome = 0

    def __init__(self):
        """ Main window constructor """
        super(Main, self).__init__()

        # Start a new itasks session
        self.itasks_service = ItasksService()
        self.itasks_service.start_server()
        self.itasks_service.new_session(self.new_session_callback)

        self.init_ui()

    def init_ui(self):
        """ Initialize basic UI """
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

        self.setGeometry(200, 200, 600, 500)
        self.setWindowTitle('iTasks')
        self.show()

    def closeEvent(self, q_close_event):  # pylint: disable-msg=C0103,W0613
        """ Close window event """
        self.itasks_service.stop_server()

    def button_clicked(self):
        """ Button click handler """
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def new_session_callback(self, instance_no, instance_key):
        """
        Callback method for the creation of a new session
        :param instance_no: iTasks instance number
        :param instance_key: iTasks instance key
        :rtype: void
        """
        self.itasks_service.attach_task_instance(
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
        if self.temp_start_palindrome == 0:
            self.itasks_service.send_data('["event",1,["1-7",null,"Continue"]]')
        if self.temp_start_palindrome == 1:
            self.itasks_service.send_data('["event",1,["1-41",null,"New"]]')
        if self.temp_start_palindrome == 2:
            self.itasks_service.send_data('["event",1,["1-63","v",[17]]]')
        if self.temp_start_palindrome == 3:
            self.itasks_service.send_data(
                '["event",1,["1-61",null,"Start task"]]')
        if self.temp_start_palindrome == 4:
            attributes = json.loads(data)
            if os.name == "nt":
                attributes = attributes['change']['children'][0][2]['children']
                attributes = attributes[0][2]['children'][0][2]['children']
                attributes = attributes[1][2]['children'][0]['attributes']
            elif os.name == "posix":
                attributes = attributes['change']['children'][0][2]['children']
                attributes = attributes[0][2]['definition']['children'][1]
                attributes = attributes['children'][0]['children']
                attributes = attributes[0]['attributes']
            instance_no = attributes['instanceNo']
            instance_key = attributes['instanceKey']
            self.itasks_service.attach_task_instance(
                instance_no, instance_key, self.task_callback)
        self.temp_start_palindrome += 1


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    ex = Main()
    sys.exit(APP.exec_())