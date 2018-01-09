""" Unit tests for itasks_service.py """

import json
import os
import builtins
import unittest

# pylint: disable=ungrouped-imports
from unittest.mock import (
    patch,
    Mock
)
# pylint: enable=ungrouped-imports

from itasks import (
    ItasksService,
    CouldNotReadStdIOException,
    UnsupportedOperatingSystemException
)


class TestItasksService(unittest.TestCase):
    """ Unit test class """

    @patch('subprocess.Popen')
    def test_new_session_callback(self, mocked_popen):
        """
        method: new_session
        state: with callback
        expected_result: new session request is made
        """
        # Assign
        itasksservice = ItasksService()
        itasksservice.req_id = 1
        itasksservice.process = mocked_popen
        callback = Mock()
        request_id = itasksservice.req_id

        # Act
        itasksservice.new_session(callback)

        # Assert
        self.assertEqual(request_id + 1, itasksservice.req_id)
        self.assertEqual(
            itasksservice.newSessionCallbacks[request_id], callback)
        callback.assert_not_called()
        mocked_popen.stdin.write.assert_called_once_with(
            '[1, "new", {}]\n'.encode())

    @patch('subprocess.Popen')
    def test_process_data_new_session_callback(self, mocked_popen):
        # pylint: disable=R0201, C0103
        """
        method: process_data
        state: with correct callback
        expected_result: callback is called with correct data
        """
        # Assign
        itasksservice = ItasksService()
        itasksservice.req_id = 1
        itasksservice.process = mocked_popen
        callback = Mock()
        instance_no = 2
        instance_key = 'zwybytwiucxuukecmubejicucfakxwcj'

        # Act
        itasksservice.new_session(callback)
        itasksservice.process_data(
            json.dumps([1, "new", {'instanceNo': instance_no,
                                   'instanceKey': instance_key}]))

        # Assert
        callback.assert_called_once_with(instance_no, instance_key)

    def test_process_data_new_session_invalid_response(self):
        # pylint: disable=R0201, C0103
        """
        method: process_data
        state: response with invalid request_id
        expected_result: Unknown response is shown in console
        """
        # Assign
        itasksservice = ItasksService()
        itasksservice.newSessionCallbacks = {}
        builtins.print = Mock()

        # Act
        itasksservice.process_data(
            json.dumps(
                [5, "new",
                 {'instanceNo': 2,
                  'instanceKey': "zwybytwiucxuukecmubejicucfakxwcj"}]))

        # Assign
        builtins.print.assert_called_once()

    @patch('subprocess.Popen')
    def test_process_data_attach_task_instance_callback(self, mocked_popen):
        # pylint: disable=R0201, C0103
        """
        method: attach_task_instance
        state: with correct callback
        expected_result: callback is called with correct data
        """
        # Assign
        itasksservice = ItasksService()
        itasksservice.process = mocked_popen
        callback = Mock()
        instance_no = 2
        instance_key = 'zwybytwiucxuukecmubejicucfakxwcj'
        arguments = {'instanceNo': instance_no, 'change': 'dummy'}
        data = json.dumps([1, "ui-change", arguments])

        # Act
        itasksservice.attach_task_instance(instance_no, instance_key, callback)
        itasksservice.process_data(data)

        # Assert
        callback.assert_called_once_with(arguments)

    @patch('subprocess.Popen')
    def test_process_data_incorrect_instance_no(self, mocked_popen):
        # pylint: disable=R0201, C0103
        """
        method: process_data
        state: Response with incorrect instance number
        expected_result: Callback method is not called
        """
        # Assign
        itasksservice = ItasksService()
        itasksservice.process = mocked_popen
        callback = Mock()
        instance_no = 2
        instance_key = 'zwybytwiucxuukecmubejicucfakxwcj'
        data = json.dumps({'instance': 5, 'change': 'dummy request'})

        # Act
        itasksservice.attach_task_instance(instance_no, instance_key, callback)
        itasksservice.process_data(data)

        # Assert
        callback.assert_not_called()

    @patch('subprocess.Popen')
    @patch('threading.Thread')
    def test_start_server_on_nt(self, mocked_popen, mocked_thread):
        """
        method: start_server
        state: Server started on Windows platform
        expected_result: Server started
        """
        # Assign
        itasksservice = ItasksService()
        os.name = "nt"

        # Act
        itasksservice.start_server()

        # Assert
        mocked_popen.assert_called()
        mocked_thread.assert_called()
        self.assertTrue(mocked_thread.daemon)

    @patch('subprocess.Popen')
    @patch('threading.Thread')
    def test_start_server_on_posix(self, mocked_popen, mocked_thread):
        """
        method: start_server
        state: Server started on Unix platform
        expected_result: Server started
        """
        # Assign
        itasksservice = ItasksService()
        os.name = "posix"

        # Act
        itasksservice.start_server()

        # Assert
        mocked_popen.assert_called()
        mocked_thread.assert_called()
        self.assertTrue(mocked_thread.daemon)

    def test_start_server_on_unsupported_system(self):
        # pylint: disable=R0201, C0103
        """
        method: start_server
        state: Server started on Mac platform
        expected_result: Exception
        """
        # Assign
        itasksservice = ItasksService()
        os.name = "mac"

        # Assert
        self.assertRaises(UnsupportedOperatingSystemException,
                          itasksservice.start_server)

    def test_stop_server(self):  # pylint: disable=R0201, C0103
        """
        method: stop_server
        expected_result: stop method called on process
        """
        # Assign
        itasksservice = ItasksService()
        itasksservice.process = Mock()
        itasksservice.process.pid = 999999
        os.kill = Mock()

        # Act
        itasksservice.stop_server()

        # Assert
        itasksservice.process.kill.assert_called()
        os.kill.assert_called_with(999999, 2)

    def test_non_block_read(self):
        """
        method: non_block_read
        state: Line is available longer than 1 character
        expected_result: String is returned
        """
        # Assign
        itasksservice = ItasksService()
        method_input = Mock()
        method_input.readline = Mock()
        method_input.readline.return_value = "Test string ".encode()
        expected_result = "Test string"

        # Act
        result = itasksservice.non_block_read(method_input)

        # Assert
        self.assertEqual(result, expected_result)

    def test_non_block_read_nothing_to_read(self):
        # pylint: disable=C0103
        """
        method: non_block_read
        state: No data available
        expected_result: String is returned
        """
        # Assign
        itasksservice = ItasksService()
        method_input = Mock()
        method_input.readline = Mock()
        method_input.readline.return_value = "".encode()
        expected_result = None

        # Act
        result = itasksservice.non_block_read(method_input)

        # Assert
        self.assertEqual(result, expected_result)

    def test_non_block_read_failed(self):
        """
        method: non_block_read
        state: Exception is thrown
        expected_result: Exception is thrown
        """
        # Assign
        itasksservice = ItasksService()
        method_input = Mock()
        method_input.readline = Mock(side_effect=Exception)

        # Assert
        self.assertRaises(CouldNotReadStdIOException,
                          itasksservice.non_block_read,
                          method_input)


if __name__ == '__main__':
    unittest.main()
