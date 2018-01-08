#!/usr/bin/python3

""" The ItasksService handles the communication with the iTasks Service """

import os
import json
import sys

from subprocess import Popen, PIPE
from threading import Thread

from itasks.exceptions import CouldNotReadStdIOException


class ItasksService(object):
    """Service that starts the iTasks Server in a background thread"""

    __instance = None  # Singleton instance

    process = None  # Popen process
    newSessionCallbacks = {}
    taskInstanceCallbacks = {}
    req_id = 1  # Unique request id

    def __new__(cls):
        """
        Singleton retreive instance by calling constructor
        :return: iTask Service instance
        :rtype: ItasksService
        """
        if ItasksService.__instance is None:
            ItasksService.__instance = object.__new__(cls)
        return ItasksService.__instance

    def start_server(self):
        """
        Start iTasks server in a background thread
        :rtype: void
        """
        if os.name == "nt":
            self.process = Popen(
                ["itasks_server/iTasksToStdIO.exe"],
                stdout=PIPE, stdin=PIPE, bufsize=0)
        elif os.name == "posix":
            self.process = Popen(
                ["/usr/bin/mono", "itasks_server/iTasksToStdIO.exe"],
                stdout=PIPE, stdin=PIPE, bufsize=0)

        # Start a background thread that reads the stdio output from
        # the iTasks Server
        thread = Thread(target=self.background_worker,
                        args=[self.process.stdout])
        thread.daemon = True
        thread.start()

    def stop_server(self):
        """
        Stop the iTasks server that is running in the background
        :rtype: void
        """
        self.process.kill()

    def background_worker(self, stdout):
        """
        Read the standard output without in a thread without blocking
        the main thread
        Call process data when data is read
        :rtype: void
        """
        while True:
            output = self.non_block_read(stdout)
            if output:
                try:
                    self.process_data(output)
                except TypeError:
                    sys.excepthook(*sys.exc_info())

    @staticmethod
    def non_block_read(output):
        """
        Read the stdout from the iTasks Server without blocking the main thread
        :param output: stdout
        :return JSON stream from the iTasks Server
        :rtype: str
        """
        try:
            line = output.readline().decode('utf-8')
            if len(line) > 1:
                return str(line.strip())
        except Exception:
            raise CouldNotReadStdIOException
        return None

    def process_data(self, data):
        """
        Process data from the iTasks Server
        This method finds the correct callback to handle the request
        :param data: Response from the iTasks Server
        :rtype: void
        """
        decoded_response = json.loads(data)
        if isinstance(decoded_response, list):
            request_id = decoded_response[0]
            response = decoded_response[1]

            if request_id in self.newSessionCallbacks:
                instance_no = response['instanceNo']
                instance_key = response['instanceKey']
                self.newSessionCallbacks[request_id](instance_no, instance_key)
            else:
                print("Unknown response: " + data)
        else:
            instance_no = decoded_response['instance']
            if instance_no in self.taskInstanceCallbacks:
                self.taskInstanceCallbacks[instance_no](data)

    def send_data(self, data):
        """
        Send data to the iTasks Server
        :param data: Data to send to the server
        :rtype: void
        """
        self.process.stdin.write((data + '\n').encode())

    def new_session(self, callback):
        """
        Request the creation of a new session
        :param callback: Method to call when a response is received
        :rtype: void
        """
        self.newSessionCallbacks[self.req_id] = callback
        self.send_data(json.dumps([self.req_id, "new"]))
        self.req_id = self.req_id + 1

    def attach_task_instance(self, instance_no, instance_key, callback):
        """
        Attach a view to an task instance
        :param instance_no: iTasks task instance number
        :param instance_key: iTasks task instance number
        :param callback: Method to call when a response is received
        :rtype: void
        """
        self.taskInstanceCallbacks[instance_no] = callback
        self.send_data(json.dumps(["attach", instance_no, instance_key]))
