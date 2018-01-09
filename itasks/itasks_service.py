#!/usr/bin/python3

""" The ItasksService handles the communication with the iTasks Service """

import os
import json
import subprocess
import threading
import time

from itasks.exceptions import (
    CouldNotReadStdIOException,
    UnsupportedOperatingSystemException
)


class ItasksService(object):
    """Service that starts the iTasks Server in a background thread"""

    __instance = None  # Singleton instance

    process = None  # Popen process
    newSessionCallbacks = {}
    taskInstanceCallbacks = {}
    req_id = 0  # Unique request id

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
            self.process = subprocess.Popen(
                ["itasks_server/iTasksToStdIO.exe"],
                stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=0)
        elif os.name == "posix":
            self.process = subprocess.Popen(
                ["/usr/bin/mono", "itasks_server/iTasksToStdIO.exe"],
                stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=0)
        else:
            raise UnsupportedOperatingSystemException

        # Start a background thread that reads the stdio output from
        # the iTasks Server
        thread = threading.Thread(
            target=self.background_worker,
            args=[self.process.stdout])
        thread.daemon = True
        thread.start()

    def stop_server(self):
        """
        Stop the iTasks server that is running in the background
        :rtype: void
        """
        # TODO: Remove when iTasks has support for StdIO
        self.write_data_to_itasks("EXIT_SERVER")
        time.sleep(1)
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
                self.process_data(output)

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
        if isinstance(decoded_response, list) and len(decoded_response) == 3:
            request_id = decoded_response[0]
            request_type = decoded_response[1]
            request_arguments = decoded_response[2]

            # Define handlers for the response types
            handlers = {
                'new': self.process_new,
                'attach': self.process_attach,
                'detach': self.process_detach,
                'ping': self.process_ping,
                'ui-change': self.process_ui_change,
                'exception': self.process_exception
            }

            # Call the handler
            if request_type in handlers:
                handlers[request_type](request_arguments=request_arguments,
                                       request_id=request_id)
            else:
                print("Unknown response from iTasks: " + data)

    def process_new(self, request_arguments, **kwargs):
        """
        Process a "new" response
        :param request_arguments: Response arguments
        :param kwargs: request_id
        :rtype: void
        """
        if kwargs["request_id"] in self.newSessionCallbacks:
            instance_no = request_arguments['instanceNo']
            instance_key = request_arguments['instanceKey']
            self.newSessionCallbacks[kwargs["request_id"]](instance_no,
                                                           instance_key)
            del self.newSessionCallbacks[kwargs["request_id"]]
        else:
            print("Unknown response from iTasks for request_id: " +
                  str(kwargs['request_id']))

    def process_attach(self, request_arguments, **kwargs):
        """
        Process a "attach" response
        :param request_arguments: Response arguments
        :param kwargs: request_id
        :rtype: void
        """
        pass

    def process_detach(self, request_arguments, **kwargs):
        """
        Process a "detach" response
        :param request_arguments: Response arguments
        :param kwargs: request_id
        :rtype: void
        """
        pass

    def process_ping(self, request_arguments, **kwargs):
        """
        Process a "ping" response
        :param request_arguments: Response arguments
        :param kwargs: request_id
        :rtype: void
        """
        pass

    def process_ui_change(self, request_arguments, **kwargs):
        """
        Process a "ui-change" response
        :param request_arguments: Response arguments
        :param kwargs: request_id
        :rtype: void
        """
        kwargs.pop('request_id')
        instance_no = request_arguments['instanceNo']
        if instance_no in self.taskInstanceCallbacks:
            self.taskInstanceCallbacks[instance_no](request_arguments)

    def process_exception(self, request_arguments, **kwargs):
        """
        Process a "exception" response
        :param request_arguments: Response arguments
        :param kwargs: request_id
        :rtype: void
        """
        pass

    def write_data_to_itasks(self, data):
        """
        Write data to the itasks server via StdIO
        :param data: the data to write
        :rtype: void
        """
        self.process.stdin.write((data + '\n').encode())

    def send_data(self, request_type, data):
        """
        Send data to the iTasks Server
        :param request_type: The request type
        :param data: Data to send to the server
        :rtype: void
        """
        self.write_data_to_itasks(
            json.dumps([self.req_id, request_type, data])
        )
        self.req_id += 1

    def send_ui_event(self, data):
        """
        Send ui-event to the iTasks Server
        :param data: Request to send
        :rtype: void
        """
        self.send_data("ui-event", data)

    def new_session(self, callback):
        """
        Request the creation of a new session
        :param callback: Method to call when a response is received
        :rtype: void
        """
        self.newSessionCallbacks[self.req_id] = callback
        self.send_data("new", {})

    def attach_task_instance(self, instance_no, instance_key, callback):
        """
        Attach a view to an task instance
        :param instance_no: iTasks task instance number
        :param instance_key: iTasks task instance number
        :param callback: Method to call when a response is received
        :rtype: void
        """
        self.taskInstanceCallbacks[instance_no] = callback
        self.send_data(
            "attach",
            {"instanceNo": instance_no, "instanceKey": instance_key}
        )
