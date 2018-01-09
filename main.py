#!/usr/bin/python3

""" iTasks Desktop Application Entry point """

import sys
import os
import json
import logging
import traceback

from PyQt5.QtWidgets import (  # pylint: disable-msg=E0611
    QMainWindow,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QApplication
)

from itasks import ItasksService


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
        1/0
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
        self.statusBar().showMessage("Response received from iTasks")
        print(data)

        # Start the palindrome task
        if self.temp_start_palindrome == 0:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 7, "action": "Continue"})
        if self.temp_start_palindrome == 1:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 41, "action": "New"})
        if self.temp_start_palindrome == 2:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 63, "edit": "v", "value": [17]})
        if self.temp_start_palindrome == 3:
            self.itasks_service.send_ui_event(
                {"instanceNo": 1, "taskNo": 61, "action": "Start task"})
        if self.temp_start_palindrome == 4:
            attributes = data['change']['children'][0][2]['children']
            attributes = attributes[0][2]['children'][0][2]['children']
            attributes = attributes[1][2]['children'][0]['attributes']
            instance_no = attributes['instanceNo']
            instance_key = attributes['instanceKey']
            self.itasks_service.attach_task_instance(
                instance_no, instance_key, self.task_callback)
        self.temp_start_palindrome += 1


def log_uncaught_exceptions(exctype, exception, trace):
    """
    Log uncaught exceptions to errors.log file and to console
    :param exctype: Exception type or class
    :param exception: The original exception
    :param trace: Traceback for the exception
    """
    # Write error to file
    logging.critical(''.join(traceback.format_tb(trace)))
    logging.critical('{0}: {1}'.format(exctype, exception))

    # Write error to console
    sys.__excepthook__(exctype, exception, trace)
    return


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        filename='errors.log',
        filemode='a')
    sys.excepthook = log_uncaught_exceptions
    APP = QApplication(sys.argv)
    ex = Main()
    sys.exit(APP.exec_())
