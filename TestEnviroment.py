import json
import unittest

import JSONParser


# Example Unittest
class TestJSONParser(unittest.TestCase):

    def test_decoder(self):
        result = JSONParser.json_decode('["foo", {"bar":["baz", null, 1.0, 2]}]')
        self.assertEqual(result, json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))


if __name__ == '__main__':
    unittest.main()
