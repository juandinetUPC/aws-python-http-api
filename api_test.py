#API unit test
from decimal import Decimal
from json import JSONEncoder
import json
import unittest
import requests

import create
import read
import update
import delete
import list
import custom_encoder

base_url='https://jkudehd1l6.execute-api.us-east-2.amazonaws.com/dev/'

#Prueba el constructor de la respuesta de la API (HTTP)
class TestBuildResponse(unittest.TestCase):
    def test_buildResponse(self):
        response = custom_encoder.buildResponse(200,{'mensaje':'hola', 'age':Decimal(5)})
        self.assertEqual(response['statusCode'],200)
        self.assertEqual(response['body'],'{"mensaje": "hola", "age": 5}')

#Prueba el método create
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

#Prueba el método read
class TestRead(unittest.TestCase):
    def test_read_user(self):
        userid=111111111
        response = requests.get(f'{base_url}user/{userid}')
        if response.status_code == 200:
            self.assertEqual(response.status_code,200)
            self.assertEqual(response.json(), {'username': 'Pepito Perez', 'userid': userid, 'age': 29})
        elif response.status_code == 404:
            self.assertEqual(response.status_code,404)
            self.assertEqual(response.json(), {'Message': f'userid:{userid} not found'})
       
    def test_read_user_fail(self):
        response = requests.get(f'{base_url}user/99999999')
        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(), {'Message': 'userid:99999999 not found'})