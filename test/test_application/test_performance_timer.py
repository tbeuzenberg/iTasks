""" File for testing the performance_timer """
import unittest

from unittest.mock import (
    Mock,
    patch
)

from application import PerformanceTimer


class TestPerformanceTimer(unittest.TestCase):
    """ The class for testing the PerformanceTimer class """

    @patch('time.time', return_value=Mock())
    def test_elapsed_time_calculation(self, time_mock):
        """
        Test if the elapsed time calculation
        :method: elapsed_time
        :state: With one digit to much
        :expect: Result is rounded to 3 digits
        """
        # Assign
        time_mock.return_value = 56.125821
        performance_timer = PerformanceTimer()
        time_mock.return_value = 81.183509
        expected = 2505.769

        # Act
        result = performance_timer.elapsed_time()

        # Assert
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
