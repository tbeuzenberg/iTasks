""" Performance logging for code blocks """

import time
import logging


class PerformanceLogger:
    """ Calculate execution time of certain code blocks  """

    def __init__(self):
        """
        Remember the current time to calculate execution time
        """
        self.start_time = time.time()

    def stop(self, message):
        """
        Calculate the execution time and write to the log file
        :param message: The function being tested
        :rtype: void
        """
        elapsed_time = round(((time.time() - self.start_time) * 100), 3)
        logging.debug("Performance logger: %s in: %s ms", message, elapsed_time)
        print("{} in: {} ms".format(message, elapsed_time))
