import unittest
from unittest.mock import patch, Mock
from iTasksService import ItasksService


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


if __name__ == '__main__':
    unittest.main()
