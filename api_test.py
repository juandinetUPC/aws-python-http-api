#API unit test
import unittest
import requests

import create
import read
import update
import delete
import list
import custom_encoder

base_url='https://jkudehd1l6.execute-api.us-east-2.amazonaws.com/dev/'

class TestCreate(unittest.TestCase):
    def test_create_user(self):
        payload = {
            "userid": 111111111,
            "username": "Pepito Perez",
            "age": 29
        }
        response = requests.post(f'{base_url}user', json=payload)
        if response.status_code == 201:
            self.assertEqual(response.json(), {'Message': 'Usuario creado', 'User': payload})
        elif response.status_code == 202:
            self.assertEqual(response.json(), {'Message': 'Usuario ya existe', 'User': payload})




