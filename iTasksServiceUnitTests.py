import unittest
from unittest.mock import patch, Mock
from iTasksService import ItasksService
import json


class TestItasksService(unittest.TestCase):

    @patch('subprocess.Popen')
    def test_new_session(self, mocked_popen):
        # Assign
        itasksservice = ItasksService()
        itasksservice.process = mocked_popen
        callback = Mock()
        request_id = itasksservice.reqId

        # Act
        itasksservice.new_session(callback)

        # Assert
        self.assertEqual(request_id + 1, itasksservice.reqId)
        callback.assert_not_called()
        mocked_popen.stdin.write.assert_called_once_with('[1, "new"]\n'.encode())

    @patch('subprocess.Popen')
    def test_process_data_new_session_callback(self, mocked_popen):
        # Assign
        itasksservice = ItasksService()
        itasksservice.process = mocked_popen
        callback = Mock()
        instance_no = 2
        instance_key = 'zwybytwiucxuukecmubejicucfakxwcj'

        # Act
        itasksservice.new_session(callback)
        itasksservice.process_data(json.dumps([1, {'instanceNo': instance_no, 'instanceKey': instance_key}]))

        # Assert
        callback.assert_called_once_with(instance_no, instance_key)

    @patch('subprocess.Popen')
    def test_process_data_attach_task_instance_callback(self, mocked_popen):
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


if __name__ == '__main__':
    unittest.main()
