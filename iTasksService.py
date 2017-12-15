#!/usr/bin/python3

import fcntl
import os
import json
from subprocess import *
from threading import Thread


class ItasksService:
    """Service that starts the iTasks Server in a background thread"""

    process = None
    newSessionCallbacks = {}
    taskInstanceCallbacks = {}
    reqId = 1

    def __init__(self):
        super(ItasksService, self).__init__()

        self.start_server()

    def start_server(self):
        # Start iTasks server
        process = Popen(
            ["/usr/bin/mono", "/home/nick/RiderProjects/iTasksToStdIO/iTasksToStdIO/bin/Debug/iTasksToStdIO.exe"],
            stdout=PIPE, stdin=PIPE, bufsize=0)
        thread = Thread(target=self.background_worker, args=[process.stdout])
        thread.daemon = True
        thread.start()
        self.process = process

    def stop_server(self):
        self.process.kill()

    def background_worker(self, stdout):
        """ needs to be in a thread so we can read the stdout w/o blocking """
        while True:
            output = self.non_block_read(stdout)
            if output:
                self.process_data(output)

    @staticmethod
    def non_block_read(output):
        fd = output.fileno()
        fl = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
        try:
            line = output.readline().decode('utf-8')
            if len(line) > 1:
                return str(line.strip())
        except:
            return

    def process_data(self, data):
        o = json.loads(data)
        if type(o) == list:
            request_id = o[0]
            response = o[1]

            if request_id in self.newSessionCallbacks:
                instance_no = response['instanceNo']
                instance_key = response['instanceKey']
                self.newSessionCallbacks[request_id](instance_no, instance_key)
            else:
                print("Unknown response: " + data)
        else:
            instance_no = o['instance']
            self.taskInstanceCallbacks[instance_no](data)

    def send_data(self, data):
        self.process.stdin.write((data + '\n').encode())

    def new_session(self, callback):
        self.newSessionCallbacks[self.reqId] = callback
        self.send_data(json.dumps([self.reqId, "new"]))
        self.reqId = self.reqId + 1

    def attach_task_instance(self, instance_no, instance_key, callback):
        self.taskInstanceCallbacks[instance_no] = callback
        self.send_data(json.dumps(["attach", instance_no, instance_key]))
