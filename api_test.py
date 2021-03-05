import requests
import unittest


class LoginTest(unittest.TestCase):

    def test_positive(self):
        url = "http://localhost:5000/"
        body_data = {"tel": "13639490306", "pwd": "123456"}
        res = requests.post(url, json=body_data).json()
        self.assertEqual(res.get('code'), 1)