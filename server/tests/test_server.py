from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/get_animal', text='duck')
            m.post('http://animal_api:5000/get_noise', text='quack')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'The duck goes quack', response.data)