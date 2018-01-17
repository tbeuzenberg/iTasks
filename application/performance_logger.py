
import time
import logging


class PerformanceLogger:

    def __init__(self):
        self.start_time = time.time()

    def start(self):
        pass

    def stop(self, message):
        elapsed_time = round(((time.time() - self.start_time) * 100), 3)
        logging.debug("Performance logger: %s in: %s ms", message, elapsed_time)
        print("{} in: {} ms".format(message, elapsed_time))
