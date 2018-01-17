""" Performance logging for code blocks """

import time
import logging


class PerformanceTimer:
    """ Calculate execution time of certain code blocks  """

    def __init__(self):
        """
        Remember the current time to calculate execution time
        """
        self.start_time = time.time()

    def elapsed_time(self):
        """
        Return the elapsed time since the timer started
        :return: Elapsed time in milliseconds
        """
        return round(((time.time() - self.start_time) * 100), 3)

    def stop(self, action_message):
        """
        Calculate the execution time and write to the log file
        :param action_message: The function that was tested
        :rtype: void
        """
        elapsed_time = self.elapsed_time()
        message = "Performance timer: {} in: {} ms".format(action_message, elapsed_time)
        logging.debug(message)
        print(message)
