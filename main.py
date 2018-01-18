#!/usr/bin/python3

""" iTasks Desktop Application Entry point """

import logging
import sys
import traceback

from PyQt5.QtWidgets import (  # pylint: disable-msg=E0611
    QApplication)

from application import Application
from temporary_dir.json_components import get_itasks_layout, get_palindrome, \
    get_icon


def log_uncaught_exceptions(exctype, exception, trace):
    """
    Log uncaught exceptions to errors.log file and to console
    :param exctype: Exception type or class
    :param exception: The original exception
    :param trace: Traceback for the exception
    """
    # Write error to file
    logging.critical(''.join(traceback.format_tb(trace)))
    logging.critical('%s: %s', exctype, exception)

    # Write error to console
    sys.__excepthook__(exctype, exception, trace)
    sys.exit(6)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] %(levelname)s - %(message)s',
        filename='errors.log',
        filemode='a')
    sys.excepthook = log_uncaught_exceptions

    app = Application(application=QApplication(sys.argv))
    # app.handle_instruction(get_palindrome())
    app.main_window.show()

    # app.from_main_thread_nonblocking()

    while True:
        app.qt_application.processEvents()
        app.from_main_thread_nonblocking()

    # sys.exit(app.qt_application.exec_())
