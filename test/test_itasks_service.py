
""" Unit tests for itasks_service.py """

import unittest
import json

from unittest.mock import patch, Mock

from itasks.itasks_service import ItasksService


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
            '[1, "new"]\n'.encode())

    @patch('subprocess.Popen')
    def test_process_data_new_session_callback(self, mocked_popen):
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
            json.dumps([1, {'instanceNo': instance_no,
                            'instanceKey': instance_key}]))

        # Assert
        callback.assert_called_once_with(instance_no, instance_key)

    @patch('subprocess.Popen')
    def test_process_data_attach_task_instance_callback(self, mocked_popen):
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
        data = json.dumps({'instance': instance_no, 'change': 'dummy'})

        # Act
        itasksservice.attach_task_instance(instance_no, instance_key, callback)
        itasksservice.process_data(data)

        # Assert
        callback.assert_called_once_with(data)

    @patch('subprocess.Popen')
    def test_process_data_incorrect_instance_no(self, mocked_popen):
        """
        method: process_data
        state: Response with incorrect instance number
        expected_result: Callback method is not called
        """
        # Assert
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


if __name__ == '__main__':
    unittest.main()
